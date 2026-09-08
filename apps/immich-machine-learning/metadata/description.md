# Immich Machine Learning

Standalone build of Immich's machine-learning service: face recognition,
CLIP-based smart search, and other ML backends used by Immich's photo/video
library. Not a full Immich install — no gallery, no database, no upload UI.

## Why run this separately

The primary Immich instance stays where it already lives (e.g. a Synology
NAS). NAS CPUs are underpowered for ML inference; this app offloads that one
piece to a machine with more headroom, over the LAN.

## Setup

1. Install this app.
2. On the primary Immich instance: **Administration > Settings > Machine
   Learning > URL**, set `http://<this-host>:3003`.
3. Save. Immich now sends inference requests here instead of running them
   locally.

## Build

CPU image (`ghcr.io/immich-app/immich-machine-learning:v3.0.2`, no `-cuda`
suffix) — 4 workers, 300s worker timeout, 10 inter/intra-op threads. A CUDA
build exists upstream if the host has a spare NVIDIA GPU; this app ships the
CPU variant.

## Requirements

- Reachable on port `3003` from the machine running the primary Immich
  instance
- Immich version compatible with `v3.0.2` on both ends (mismatched ML/server
  versions can break inference)
