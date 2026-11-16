# Pocket ID

Simple OpenID Connect provider: users sign in with passkeys only, no passwords.

- Expose the app on a domain and keep it stable: passkeys are bound to that domain.
- `APP_URL` is built from the exposed domain; `TRUST_PROXY` is on because Traefik sits in front.
- The encryption key is generated at install time. Keep `app.env` in your backups: without it the stored keys are unreadable.
- First start: open `https://<domain>/signup/setup` to create the admin account and its passkey.

To protect apps without OIDC support, pair it with a forward-auth proxy such as Tinyauth (generic OAuth provider pointing at Pocket ID).
