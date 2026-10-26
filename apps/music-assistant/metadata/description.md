# Music Assistant

Music Assistant is a free, open source media library manager that connects your streaming
services and local music to a wide range of speakers: AirPlay, Chromecast, Sonos, DLNA,
Squeezebox, Snapcast and Home Assistant media players.

## Notes

- The container runs with **host networking**: players are discovered by mDNS/SSDP and
  audio is streamed over UDP, which does not work behind a Docker bridge. The web UI listens
  on port 8095 and the stream server on 8097; both must be free on the host.
- Runtipi does not add Traefik labels to host-network apps: reach the UI at
  `http://<host>:8095` or route it from your own reverse proxy.
- Home Assistant: add the Music Assistant integration and point it at `http://<host>:8095`.
- Only run one Music Assistant server per network (players would be controlled twice).
