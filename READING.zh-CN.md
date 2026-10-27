<!-- topic: reading -->
<!-- sources: gemma4,raschka-ple,scone,engram,quantization,tinyengram,adaptive-input,minbpe,gemma3n-guide,longcat,qwen-ngram,staple,count,memory-layers,groupreduce,tt-embedding,megatron-embedding,tying-bias -->

# 阅读指南

[English](READING.md)

本专题从语言模型的输入输出表示讲起，依次介绍逐层容量扩展、上下文查表、压缩与系统成本。熟悉 token 嵌入的读者可以直接阅读 PLE 或 n-gram 章节；视觉与音频部分提供跨模态对照。

## 预备知识

基础部分需要了解 token ID、矩阵乘法和 Transformer block。压缩与系统部分会用到低秩分解、量化位宽、设备内存和主机内存。

## 1. token 嵌入与权重共享

[Karpathy 的分词讲义与 minbpe](https://github.com/karpathy/minbpe/blob/master/lecture.md)介绍文本如何转换为 token ID；仓库也链接了配套视频。[token 嵌入指南](wiki/token-embeddings.zh-CN.md)接着说明 ID 如何选择嵌入表行，以及同一矩阵如何参与输出预测。

[权重共享解读](insights/weight-tying.zh-CN.md)串联早期实验、分布假说与近期梯度分析。[输入输出梯度研究](https://arxiv.org/html/2603.26663v1)进一步讨论共享表示为何更接近输出空间。

## 2. 每层嵌入（PLE）

[Gemma 3n 开发者指南](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/)介绍端侧部署动机。[PLE 指南](wiki/ple.zh-CN.md)解释逐层查表、模型投影和门控残差路径；[Gemma 4 源码](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)中的 `encode_per_layer_input` 与 `Block.__call__` 对应这些计算。

[Raschka 的架构解读](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/)讨论有效参数量、总参数量和实验对照。[容量与计算专题](insights/capacity-and-compute.zh-CN.md)将这些观点与公式、实现联系起来。

## 3. n-gram 查表与记忆层

[SCONE 与 Engram 指南](wiki/ngram-memory.zh-CN.md)介绍两种局部上下文寻址方法。[SCONE](https://arxiv.org/html/2502.01637v3)在推理时读取预计算输入向量；[Engram 演示](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py)展示内部 block 中的门控记忆。[机制比较](COMPARISON.zh-CN.md)并列整理 PLE、SCONE 和 Engram 的查表键与注入位置。

相关扩展各自回答不同的设计问题：

- [LongCat](https://arxiv.org/html/2601.21204v2)：嵌入与 MoE 专家之间的容量分配。
- [Qwen3.8-Next](https://arxiv.org/html/2608.30320v1#S2.SS3)：n-gram 注入位置、词表预算与主机预取。
- [STAPLE](https://github.com/Infini-AI-Lab/STAPLE)：为预训练检查点加入查表残差记忆。
- [COUNT](https://arxiv.org/html/2610.20456v1)：用语料统计和已有输出向量构造 n-gram 嵌入。
- [Memory Layers at Scale](https://github.com/facebookresearch/memory)：由隐藏状态查询的乘积键记忆。

## 4. 压缩与系统实现

[嵌入压缩指南](wiki/compression.zh-CN.md)从存储公式出发，介绍低秩分解、自适应维度、张量列分解和量化。[自适应输入](https://arxiv.org/abs/1809.10853v3)与 [GroupReduce](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html)都利用词频分组，但参数化与训练方式不同。[张量化嵌入层](https://aclanthology.org/2020.findings-emnlp.436/)用共享 TT 因子表示整张表，可与 TensorGPT 的逐行压缩对照。

[LLM Compressor 示例](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md)提供输入表 INT4 量化配方。[TinyEngram 系统课](https://github.com/colorful-lollipop/tinyengram/blob/cf811bef6454dd7a9959b5854af13a52d7ba79f5/docs/lab7-systems.md)介绍预取、缓存和卸载模拟；[Megatron-LM](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351)展示跨设备词表分片。

[成本矩阵](COMPARISON.zh-CN.md#成本矩阵)分别列出参数存储、设备内存、访问传输和计算。卸载的收益取决于访问模式、带宽与缓存；分片则改变单设备负担，保留表的总参数量。[离线计算器](explorer.html)可估算不同形状和精度下的原始表存储量。

## 5. 视觉与音频对照

[视觉投影](wiki/visual-projections.zh-CN.md)介绍从图像块到视觉表示、再到语言模型宽度的变换。[音频码本](wiki/audio-codebooks.zh-CN.md)介绍 codec 量化重建与下游语言模型查表。这两个主题说明，embedding 相关组件也可以通过投影或量化生成表示。

## Agent 辅助阅读（可选）

以下提示可用于已有的 coding agent：

> 请根据本仓库及引用来源，解释 PLE 的计算路径，并与 SCONE、Engram 比较。说明各自的查表键、存储对象、注入位置和计算成本，附相应的代码位置或论文章节。
