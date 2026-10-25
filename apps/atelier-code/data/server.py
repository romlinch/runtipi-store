# /// script
# requires-python = ">=3.12"
# ///
"""Atelier de code : sert index.html, garde le projet de chaque enfant et relaie le chat vers LiteLLM.

La clé LiteLLM reste ici, jamais dans le navigateur. Le modèle est imposé côté serveur.
"""

import base64
import hmac
import json
import os
import re
import unicodedata
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ICI = Path(__file__).parent
PROJETS = Path(os.environ.get("PROJETS_DIR", ICI / "projets"))
LITELLM_URL = os.environ.get("LITELLM_URL", "https://litellm.romlinch.fr/v1/chat/completions")
LITELLM_KEY = os.environ["LITELLM_KEY"]
MODELE = os.environ.get("MODELE", "qwen-nothink")
STT_URL = LITELLM_URL.replace("/chat/completions", "/audio/transcriptions")
MOT_DE_PASSE = os.environ.get("MOT_DE_PASSE", "")  # vide = pas de protection
PORT = int(os.environ.get("PORT", "8000"))
TAILLE_MAX = 300_000  # octets, largement assez pour le code d'un enfant
AUDIO_MAX = 5_000_000  # quelques minutes de voix en opus
ID = re.compile(r"[a-z0-9-]{1,30}")


class Handler(BaseHTTPRequestHandler):
    def autorise(self):
        """Basic auth, n'importe quel identifiant : le navigateur la redemande une fois puis la renvoie sur chaque fetch."""
        _, _, b64 = (self.headers.get("Authorization") or "").partition("Basic ")
        try:
            mot = base64.b64decode(b64).decode().partition(":")[2]
        except ValueError:
            mot = ""
        if not MOT_DE_PASSE or hmac.compare_digest(mot.encode(), MOT_DE_PASSE.encode()):
            return True
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Atelier de code", charset="UTF-8"')
        self.send_header("Content-Length", "0")
        self.end_headers()
        return False

    def do_GET(self):
        if not self.autorise():
            return
        if self.path == "/":
            self.repondre(200, (ICI / "index.html").read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/projets":
            projets = [json.loads(p.read_text()) | {"id": p.stem} for p in sorted(PROJETS.glob("*.json"))]
            self.repondre(200, json.dumps(projets).encode(), "application/json")
        else:
            self.repondre(404, b"introuvable")

    def do_PUT(self):
        if not self.autorise():
            return
        id_ = self.path.removeprefix("/api/projets/")
        corps = self.lire_json()
        if not ID.fullmatch(id_) or not isinstance(corps, dict):
            return self.repondre(400, b"projet invalide")
        PROJETS.mkdir(parents=True, exist_ok=True)
        tmp = PROJETS / f".{id_}.tmp"
        tmp.write_text(json.dumps(corps, ensure_ascii=False))
        tmp.replace(PROJETS / f"{id_}.json")  # atomique : jamais de projet à moitié écrit
        self.repondre(204, b"")

    def do_POST(self):
        if not self.autorise():
            return
        if self.path == "/api/stt":
            return self.transcrire()
        corps = self.lire_json()
        if self.path != "/api/chat" or not isinstance(corps, dict) or not isinstance(corps.get("messages"), list):
            return self.repondre(400, b"requete invalide")
        requete = urllib.request.Request(
            LITELLM_URL,
            data=json.dumps({"model": MODELE, "messages": corps["messages"], "stream": True, "max_tokens": 32768}
                            | ({"tools": corps["tools"]} if isinstance(corps.get("tools"), list) else {})).encode(),
            headers={"Authorization": f"Bearer {LITELLM_KEY}", "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(requete, timeout=300) as r:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                while bloc := r.read1(4096):
                    self.wfile.write(bloc)
                    self.wfile.flush()
        except (urllib.error.URLError, TimeoutError) as e:
            self.repondre(502, f"LiteLLM injoignable : {e}".encode())

    def transcrire(self):
        """Audio du micro → texte, via la route stt de LiteLLM (multipart OpenAI)."""
        taille = int(self.headers.get("Content-Length") or 0)
        type_ = self.headers.get("Content-Type", "audio/webm")
        if not 0 < taille <= AUDIO_MAX:
            return self.repondre(400, b"audio invalide")
        audio = self.rfile.read(taille)
        ext = "mp4" if "mp4" in type_ else "ogg" if "ogg" in type_ else "webm"
        limite = "atelier" + os.urandom(8).hex()
        corps = b"".join(f'--{limite}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in {"model": "stt", "language": "fr"}.items())
        corps += f'--{limite}\r\nContent-Disposition: form-data; name="file"; filename="voix.{ext}"\r\nContent-Type: {type_}\r\n\r\n'.encode() + audio + f"\r\n--{limite}--\r\n".encode()
        requete = urllib.request.Request(
            STT_URL, data=corps,
            headers={"Authorization": f"Bearer {LITELLM_KEY}", "Content-Type": f"multipart/form-data; boundary={limite}"},
        )
        try:
            with urllib.request.urlopen(requete, timeout=60) as r:
                texte = json.loads(r.read())["text"]
        except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as e:
            return self.repondre(502, f"transcription impossible : {e}".encode())
        self.repondre(200, json.dumps({"texte": texte.strip()}, ensure_ascii=False).encode(), "application/json")

    def lire_json(self):
        taille = int(self.headers.get("Content-Length") or 0)
        if not 0 < taille <= TAILLE_MAX:
            return None
        try:
            return json.loads(self.rfile.read(taille))
        except ValueError:
            return None

    def repondre(self, code, corps, type_="text/plain; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", type_)
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)


def creer_profils(prenoms):
    """Crée les profils manquants (sans âge : la page le demande à la première ouverture)."""
    PROJETS.mkdir(parents=True, exist_ok=True)
    for nom in filter(None, (n.strip() for n in prenoms.split(","))):
        # même identifiant que la page : sans accents, minuscules, tirets
        id_ = re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode().lower()).strip("-")[:30]
        if id_ and not (PROJETS / f"{id_}.json").exists():
            (PROJETS / f"{id_}.json").write_text(json.dumps({"nom": nom}, ensure_ascii=False))


if __name__ == "__main__":
    creer_profils(os.environ.get("PRENOMS", ""))
    print(f"Atelier de code sur :{PORT}, projets dans {PROJETS}, modèle {MODELE}", flush=True)
    ThreadingHTTPServer(("", PORT), Handler).serve_forever()
