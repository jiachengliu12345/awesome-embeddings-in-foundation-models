# Glossary

[简体中文](GLOSSARY.zh-CN.md)

| English | 中文 | Usage |
| --- | --- | --- |
| embedding | 嵌入 | Name the object: table, continuous representation, or projection. |
| Per-Layer Embeddings (PLE) | 每层嵌入 | Use Google's Chinese term; not positional embeddings. |
| weight tying | 权重共享 | Input and output can use the same matrix; not sharing with every table. |
| token | token | Retain the standard community term. |
| n-gram | n-gram | A sequence of n consecutive tokens. |
| codebook | 码本 | State whether codec centroids, compression dictionary, fixed grid, or LM table. |
| offloading | 卸载 | Specify host/device placement, transfer and cache. |
| compression ratio | 压缩率 | Original bytes / compressed bytes, with metadata accounting. |
| FLOPs | 浮点运算次数 | Separate from FLOPS (operations per second). |
| accelerator memory footprint | 加速器内存占用 | Distinguish resident weights, activations, buffers and cache. |
