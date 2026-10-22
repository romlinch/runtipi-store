# Pi Pocket

[Pi Pocket](https://github.com/TannerMidd/pi-pocket) is a self-hosted web app for the [Pi coding agent](https://pi.dev),
built on Pi Durable: every model call and tool call is checkpointed in SQLite, so a restarted server resumes its work.

## First start

- The container clones the pinned Pi Pocket tag into the data volume and runs `npm ci` (a few minutes).
- The owner's sign-in link is printed in the container logs. It is the key to the server: open it once per browser,
  never share it. A new one: run the app with `--rotate-token`.
- Models: put Pi's `models.json` (and optionally `settings.json`) in `data/home/.pi/agent/`, then **Refresh models**
  in the app. Any OpenAI-compatible endpoint works (LiteLLM, llama.cpp, Ollama).

## Data

| Host path (`app-data`) | Content |
|---|---|
| `data/home/.pi-pocket` | `pocket.sqlite`, people, settings, uploads, push keys, extensions |
| `data/home/.pi/agent` | Pi's models, sign-ins, settings, prompt templates, skills |
| `data/home/.ssh` | SSH keys the agent may use |
| `data/workspace` | default folder of new sessions |

## Security

Anyone who can steer a session runs commands in this container as uid 1000, with every key and file it holds.
Keep the app on your LAN (or a VPN), use HTTPS for push notifications and the PWA, and give its SSH keys only the
access you would give the agent.
