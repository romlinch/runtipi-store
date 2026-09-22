# stable-diffusion.cpp

`sd-server` from [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp):
image generation and editing in pure C/C++ on top of ggml, the same engine as
llama.cpp. Loads GGUF or safetensors weights, runs on the CPU.

## Features

- OpenAI-compatible `POST /v1/images/generations` and `POST /v1/images/edits`
  on port `8087` (host) / `8080` (internal) — plug it into LiteLLM or OpenWebUI
- Built-in web UI at the root URL
- CPU only (`--backend cpu`): the image ships a Vulkan build, but the GPU is
  left alone so it stays free for llama.cpp
- One model loaded at start and kept in RAM

## Default model: FLUX.2 klein 4B (Apache 2.0)

Download the three files into the models directory:

| File | Source | Size |
|---|---|---|
| `flux-2-klein-4b-Q8_0.gguf` | [leejet/FLUX.2-klein-4B-GGUF](https://huggingface.co/leejet/FLUX.2-klein-4B-GGUF) | 4.3 GB |
| `Qwen3-4B-Q8_0.gguf` | [unsloth/Qwen3-4B-GGUF](https://huggingface.co/unsloth/Qwen3-4B-GGUF) | 4.3 GB |
| `flux2-vae.safetensors` | [Comfy-Org/flux2-klein](https://huggingface.co/Comfy-Org/flux2-klein/tree/main/split_files/vae) | 0.34 GB |

Resident RAM is about 8.5 GB. Keep 4 steps and CFG 1.0: klein is distilled.

Other models (Qwen-Image, Z-Image, SDXL...) work by changing the file names,
steps and CFG in the app settings; see the
[model docs](https://github.com/leejet/stable-diffusion.cpp/tree/master/docs).

## Security

No authentication: the port is published on the LAN only and the app is not
exposable. Put LiteLLM in front for keys and budgets.
