# llama.cpp Router

`llama-server` in **router mode**: several models declared in a preset file, one
loaded at a time, on demand, unloaded again after `--sleep-idle-seconds`.

Built for a small-VRAM box: the GPU is only busy while a request is in flight,
so it stays free for gaming or transcoding the rest of the time.

## Features

- OpenAI-compatible endpoint on port `8085` (host) / `8080` (internal)
- Models load on first request, unload after idle — no permanent VRAM reservation
- `--models-max 1` by default: one resident model, the router swaps as needed
- NVIDIA CUDA build, Flash Attention and quantized KV cache
- Sits behind LiteLLM on the Runtipi shared network

## Shipped models

Both are **abliterated** builds of Qwen — the refusal direction is removed from
the activations, the model is otherwise unchanged.

| Alias | Model | Size | Placement | Throughput |
|---|---|---|---|---|
| `qwen` | Huihui-Qwen3.6-35B-A3B-abliterated Q4_K_S | 19.9 GB | experts in RAM, attention on GPU | ~15-25 tok/s |
| `qwen-fast` | Huihui-Qwen3.5-4B-abliterated Q5_K_M | 3.1 GB | fully GPU-resident | ~45-60 tok/s |

`qwen` keeps thinking mode on — that is what makes the wait worth it.
`qwen-fast` has it off; a 4B that reasons for 800 tokens is no longer fast.

Both are hybrid-attention models: only one layer in four uses full attention, so
the KV cache is small and 64k of context costs well under a gigabyte. Both accept
262144 tokens natively if you have the VRAM for it.

## Install

**1. Fetch the GGUFs** into the host directory you pass as `LLAMA_MODELS_DIR`:

```bash
hf download mradermacher/Huihui-Qwen3.5-4B-abliterated-GGUF \
  Huihui-Qwen3.5-4B-abliterated.Q5_K_M.gguf \
  --local-dir $LLAMA_MODELS_DIR/qwen3.5-4b-abliterated

hf download Abiray/Huihui-Qwen3.6-35B-A3B-abliterated-GGUF \
  Huihui-Qwen3.6-35B-A3B-abliterated-Q4_K_S.gguf \
  --local-dir $LLAMA_MODELS_DIR/qwen3.6-35b-a3b-abliterated
```

Expected layout:

```
$LLAMA_MODELS_DIR/
├── qwen3.5-4b-abliterated/Huihui-Qwen3.5-4B-abliterated.Q5_K_M.gguf
└── qwen3.6-35b-a3b-abliterated/Huihui-Qwen3.6-35B-A3B-abliterated-Q4_K_S.gguf
```

**2. Drop the preset** — the container will not start without it:

```bash
cp models-preset.ini <runtipi>/app-data/custom/llama-cpp/config/models-preset.ini
```

The template lives at the root of this app directory. Runtipi creates the
`app-data` folder on the first install attempt, so do this after installing once.

## Consumption via LiteLLM

```yaml
- model_name: qwen
  litellm_params:
    model: openai/qwen          # must match the [section] in models-preset.ini
    api_base: http://llama-cpp:8080/v1
    api_key: "dummy"
    timeout: 900                # covers a cold load
```

Do not give these two a cloud fallback. If a request asks for `qwen`, it is
because it must not leave the machine — an error is better than a silent
reroute to a hosted model.

## Tuning

- **`n-cpu-moe`** (per model, in the INI) decides how many layers keep their MoE
  experts in RAM. `99` means all of them. Each step down moves one layer's
  experts onto the GPU, worth a few percent of throughput until VRAM runs out.
- **Prefill is the real cost** with experts in RAM — ingesting 32k of fresh
  context takes a minute or two. `cache-reuse` and `slot-save-path` are set in
  the preset precisely to avoid paying it twice.
- **Reload after idle is fast**: the GGUF stays in the Linux page cache, so the
  second load takes seconds rather than the initial 30-40 s.

## Requirements

- NVIDIA GPU with `nvidia-container-toolkit` configured on the host
- Enough RAM for the biggest declared model (MoE experts live in RAM, not VRAM)
- `models-preset.ini` present in `${APP_DATA_DIR}/config/`
