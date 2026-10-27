<!-- topic: reading -->
<!-- sources: gemma4,raschka-ple,scone,engram,quantization,tinyengram,adaptive-input -->

# 阅读路径

[English](READING.md)

选一个问题，沿来源阅读，再检查对应实现。

## 前置知识

了解 token ID 如何索引表、Transformer block 如何更新残差流，以及参数存储与前向计算的区别。阅读压缩路径时，最好熟悉量化、每值位数，以及主机和设备内存。

## 1. PLE 怎样工作？

先读 [PLE 指南](wiki/ple.zh-CN.md)与 Raschka 的[架构解读](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/)，再沿 [Gemma 4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) 中的 `encode_per_layer_input` 和 `Block.__call__` 检查实现。

从 token ID 出发，追踪查表与模型投影两条分支，再看到每层的门控残差更新。分别记录表参数量、驻留内存和每个 token 的计算量。

## 2. PLE、SCONE 与 Engram 有何区别？

对照阅读[上下文 n-gram 查表](wiki/ngram-memory.zh-CN.md)与[机制比较](COMPARISON.zh-CN.md)，再查看 [SCONE 算法](https://arxiv.org/html/2502.01637v3)和 [Engram 演示](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py)。

比较查表键、向量构造、注入位置及训练／推理路径。SCONE 用预计算上下文向量替换命中的输入嵌入；Engram 演示在选定内部 block 加入门控记忆；PLE 按 token ID 为各层提供独立向量。

## 3. 压缩或卸载到底节省了什么？

依次阅读[压缩指南](wiki/compression.zh-CN.md)、[输入表量化示例](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md)和 [TinyEngram 系统课](https://github.com/colorful-lollipop/tinyengram/blob/cf811bef6454dd7a9959b5854af13a52d7ba79f5/docs/lab7-systems.md)，再用[成本矩阵](COMPARISON.zh-CN.md#成本矩阵)整理结果。

先写清压缩对象，再将缩放因子、码本、解码器和缓冲区计入存储。讨论卸载时，记录传输量、缓存行为、带宽和硬件；这些因素决定存储节省能否转化为设备内存或延迟收益。

还可以沿[压缩指南](wiki/compression.zh-CN.md)，比较自适应输入按词频分配的不同维度与 ALBERT 的统一维度分解。

## 让自己的 Agent 协助阅读

可以从这个提示开始：

> 请根据本仓库及其引用来源解释 PLE，并与 SCONE、Engram 比较。沿每种查表键追踪到注入位置，区分参数存储、设备内存和计算量，指出缺少哪些实验对照。每项技术主张请附对应代码或论文章节。
