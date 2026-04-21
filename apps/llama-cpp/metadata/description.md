# llama.cpp Router

`llama-server` in **router mode**: multiple models declared in a preset file, one loaded at a time, automatic unload after `--sleep-idle-seconds`.

## Features

- OpenAI-compatible endpoint on port `8085` (host) / `8080` (internal)
- Hot-swap between declared models on demand
- Frees VRAM + RAM after idle (configurable, default 10 min)
- NVIDIA CUDA build, supports Flash Attention and quantized KV cache
- Designed to sit behind LiteLLM on the Runtipi shared network

## Default models

Pre-declared in `${APP_DATA_DIR}/config/models-preset.ini`:

- **glm-4.7-flash** — 30B-A3B MoE (coding, agentic workflows)
- **gemma4-26b-a4b** — 26B-A4B MoE (generalist, vision, small/fast)

Edit this INI after install to add more models.

## Model files

Drop GGUFs in the host directory you pass as `LLAMA_MODELS_DIR`:

```
$LLAMA_MODELS_DIR/
├── glm-4.7-flash/GLM-4.7-Flash-UD-Q4_K_XL.gguf
└── gemma4-26b/gemma-4-26b-a4b-it-Q4_K_M.gguf
```

Use `huggingface-cli download unsloth/<repo> --local-dir <dir>` to fetch them.

## Consumption via LiteLLM

Add to your LiteLLM `config.yaml`:

```yaml
- model_name: glm-4.7-flash
  litellm_params:
    model: openai/glm-4.7-flash
    api_base: http://llama-cpp:8080/v1
    api_key: "dummy"
    timeout: 600
```

## Post-install

The `models-preset.ini` must exist at `${APP_DATA_DIR}/config/models-preset.ini` before the container can start. Create it from the provided template after the first install attempt (Runtipi will create the `app-data` folder).

## Requirements

- NVIDIA GPU with `nvidia-container-toolkit` configured on the host
- Models directory pre-populated with GGUFs
- Enough RAM for the biggest model you declare (MoE experts are offloaded to CPU/RAM)
