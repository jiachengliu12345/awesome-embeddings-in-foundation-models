<!-- topic: insight-capacity -->
<!-- sources: gemma4,raschka-ple -->

# PLE: table capacity and compute cost

[简体中文](capacity-and-compute.zh-CN.md) · [README](../README.md) · [PLE](../wiki/ple.md) · [Comparison](../COMPARISON.md)

Per-Layer Embeddings (PLE) is best read as a way to add token-specific learned state at every transformer layer while keeping the repeated transformer computation closer to a smaller model. It changes where parameters live and how they enter the forward pass. Its costs include the added table, row access, and gate/projection path.

In Gemma 4 E2B and E4B, the official implementation defines a table named `per_layer_embeddings` with shape `[vocab_size, num_layers, per_layer_input_dim]`. It also defines `per_layer_model_projection`, which maps the ordinary token representation into that per-layer space. The model combines the projected representation with the token-indexed table row, then supplies one slice per layer. In each block, the output after the attention and feed-forward residual updates is mapped through a gate; a GELU-gated per-layer vector is projected back to the model width, normalized, and added as a residual update. These are separate parameters and operations from the usual input embedding and attention/MLP paths. [Gemma 4 implementation](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)

This structure creates two different capacity questions. Table storage grows with vocabulary size, layer count, and per-layer width: its parameter count is `V × L × P`. The repeated transformer stack still performs its attention and feed-forward work, with an additional gate and projection for the PLE path. Therefore, a model card’s “effective” parameter count, which can emphasize the main stack’s compute, should not be mistaken for total stored parameters or a complete serving-cost measure. Actual memory use also depends on precision, sharding, and runtime implementation; latency depends on kernels, batch size, and sequence length.

Sebastian Raschka’s architecture note explains this distinction and reports the E2B/E4B effective-versus-total counts from the model documentation. He also points out the missing controlled comparisons: a regular model at the smaller effective count and one at the larger total count would help isolate PLE’s contribution. Without such controls, a quality result cannot tell us whether PLE’s structure helps, whether the extra parameters help, or both. His note also cautions that a larger model may already have enough capacity, making additional PLE tables less useful. [Raschka’s PLE explainer](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/)

## What to compare

A token-indexed table may be attractive when dense computation is the bottleneck and model-specific information is useful at many layers. But it can increase checkpoint size and memory traffic, and the layer-wise gate/projection still costs computation. The decisive test is a controlled quality–compute–memory comparison with matched training data, tokenization, training budget, and hardware. Include total parameters, active parameters under the stated definition, peak accelerator memory, throughput, and latency. Controlled baselines would show which model sizes and data benefit from the added PLE capacity.
