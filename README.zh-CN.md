<a id="top"></a>

# 基础模型中的嵌入

[English](README.md)

本仓库收集基础模型内部嵌入机制的论文、教程与开源实现，面向研究者和进阶实践者。内容以语言模型为主，涵盖 token 嵌入、输入输出权重共享、每层嵌入（PLE）、n-gram 记忆及嵌入压缩，并补充视觉投影与音频码本的对照。

材料按机制组织，从普通 token 嵌入延伸到增加查表容量的设计，再讨论存储与计算成本。[研究 Wiki](#wiki)提供原理说明，[机制比较](COMPARISON.zh-CN.md)并列整理查表键、注入位置和成本，[阅读指南](READING.zh-CN.md)给出推荐顺序。

<a id="directory"></a><a id="start-here"></a>

## 目录

- [token 嵌入与权重共享](#category-token)
- [每层嵌入（PLE）](#category-ple)
- [n-gram 嵌入与记忆层](#category-memory)
- [压缩与系统实现](#category-compression)
- [视觉与音频](#category-modalities)
- [研究 Wiki 与机制比较](#wiki)
- [更新与贡献](#contributing)

<a id="category-token"></a>

## token 嵌入与权重共享

分词器为文本分配 token ID，嵌入表将 ID 映射为向量；输入输出权重共享让同一矩阵也参与下一个 token 的预测。这些材料介绍基本计算，以及嵌入参数的共享和分配。

- [Andrej Karpathy：分词与嵌入查表](https://github.com/karpathy/minbpe/blob/master/lecture.md) [![karpathy/minbpe Stars](https://img.shields.io/github/stars/karpathy/minbpe?style=social&label=Stars)](https://github.com/karpathy/minbpe/stargazers)

  Karpathy 的 BPE 分词器实现与讲义，串联文本、token ID、词表大小和嵌入表行。

- [从零实现语言模型：GPT 代码](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) [![rasbt/LLMs-from-scratch Stars](https://img.shields.io/github/stars/rasbt/LLMs-from-scratch?style=social&label=Stars)](https://github.com/rasbt/LLMs-from-scratch/stargazers)

  《从零构建大语言模型》配套的简洁 GPT 实现，包含 token 与位置嵌入、Transformer block 和输出头。

- [输入输出权重共享：早期实验](https://aclanthology.org/E17-2025/)

  Press 与 Wolf 分析输入输出嵌入的权重共享，并报告神经语言模型和机器翻译实验。

- [权重共享与分布假设](https://proceedings.mlr.press/v235/bertolotti24a.html)

  将权重共享与分布假说联系起来，研究输入和输出表示在什么条件下适合共用矩阵。

- [权重共享如何使 token 嵌入偏向输出空间](https://arxiv.org/html/2603.26663v1)

  研究共享嵌入中的输入输出梯度不平衡，以及改变其输出空间对齐程度的干预。

<a id="category-ple"></a>

## 每层嵌入（PLE）

PLE 为同一 token 在不同解码器层提供各自的可学习向量。官方指南介绍它在 Gemma 中的作用，源码和机制解读说明查表向量如何与投影、门控结合。

- [Google：Gemma 3n 开发者指南](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/)

  模型团队介绍 PLE 的端侧部署动机，以及 Gemma 3n 总参数量与加速器驻留参数量的区别。

- [Gemma 3n：PLE 缓存](https://ai.google.dev/gemma/docs/gemma-3n)

  Gemma 3n 官方文档，介绍 PLE 缓存、加速器驻留参数，以及模态参数的选择性加载。

- [Gemma 4 嵌入与 block 源码](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) [![google-deepmind/gemma Stars](https://img.shields.io/github/stars/google-deepmind/gemma?style=social&label=Stars)](https://github.com/google-deepmind/gemma/stargazers)

  官方嵌入模块与解码器 block 源码，包含 token 查表、逐层投影、门控、权重共享和模态投影。

- [每层嵌入架构解读](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/)

  Raschka 解释 PLE 的残差路径，并讨论如何用对照实验区分结构作用与新增参数容量的作用。

<a id="category-memory"></a>

## n-gram 嵌入与记忆层

查表键可以来自局部 token 序列，也可以由隐藏状态生成。下列设计在寻址方式、存储内容和使用位置上各有选择：SCONE 扩展输入表示，Engram 加入门控内部记忆，乘积键记忆则使用隐藏状态查询。

- [SCONE：语言模型嵌入层扩展](https://arxiv.org/html/2502.01637v3)

  用频繁 n-gram 扩展输入表示；独立模型生成上下文向量，推理时从预计算表读取。

- [Engram 官方架构演示](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) [![deepseek-ai/Engram Stars](https://img.shields.io/github/stars/deepseek-ai/Engram?style=social&label=Stars)](https://github.com/deepseek-ai/Engram/stargazers)

  架构演示代码，展示 n-gram 哈希、多头查表和依赖隐藏状态的门控；attention 与 MoE 使用简化占位实现。

- [LongCat：嵌入容量与专家容量的扩展比较](https://arxiv.org/html/2601.21204v2)

  比较嵌入与 MoE 专家的容量分配，并介绍 LongCat-Flash-Lite 的系统设计。

- [Qwen3.8-Next：n-gram 注入位置与词表消融](https://arxiv.org/html/2608.30320v1)

  报告 n-gram 注入位置与词表预算的消融实验，并介绍主机内存预取设计。

- [STAPLE：为预训练检查点加入嵌入记忆](https://github.com/Infini-AI-Lab/STAPLE) [![Infini-AI-Lab/STAPLE Stars](https://img.shields.io/github/stars/Infini-AI-Lab/STAPLE?style=social&label=Stars)](https://github.com/Infini-AI-Lab/STAPLE/stargazers)

  为预训练检查点加入 token 查表残差记忆，并提供预热和主机卸载设计。

- [COUNT：用语料统计构造 n-gram 嵌入](https://arxiv.org/html/2610.20456v1)

  用固定语料统计和模型已有输出向量构造 n-gram 嵌入，为学习表行提供另一种方案。

- [Meta：大规模记忆层](https://github.com/facebookresearch/memory) [![facebookresearch/memory Stars](https://img.shields.io/github/stars/facebookresearch/memory?style=social&label=Stars)](https://github.com/facebookresearch/memory/stargazers)

  作为 token ID 与 n-gram 查表的对照，介绍由隐藏状态查询的可训练乘积键记忆。

- [TinyEngram 系统实验课](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) [![colorful-lollipop/tinyengram Stars](https://img.shields.io/github/stars/colorful-lollipop/tinyengram?style=social&label=Stars)](https://github.com/colorful-lollipop/tinyengram/stargazers)

  围绕 n-gram 记忆的系统教程，介绍访问行、预取、缓存与卸载模拟。

<a id="category-compression"></a>

## 压缩与系统实现

分解和量化减少嵌入表的表示开销，分片与卸载改变权重的存放和访问方式。本节将这些方法与向量重构、通信和运行时成本联系起来。

- [ALBERT 分解式嵌入源码](https://github.com/google-research/albert/blob/master/modeling.py) [![google-research/albert Stars](https://img.shields.io/github/stars/google-research/albert?style=social&label=Stars)](https://github.com/google-research/albert/stargazers)

  将词表嵌入矩阵分解为低维查表与隐藏维度投影，分开设置嵌入宽度和 Transformer 宽度。

- [自适应输入表示](https://arxiv.org/abs/1809.10853v3)

  按词频为不同词表组分配不同嵌入维度，再投影到统一的模型宽度。

- [GroupReduce：按词频分组的低秩压缩](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html)

  按词频对词表分块，使用加权低秩近似压缩各块。

- [张量化嵌入层](https://aclanthology.org/2020.findings-emnlp.436/)

  用共享张量列因子参数化整张嵌入表，并研究端到端训练。

- [TensorGPT：张量列嵌入压缩](https://arxiv.org/html/2307.00526v2)

  用张量列（Tensor Train）因子压缩各个 token 向量，并在查表时重构所需向量。

- [OPTIC：共享 token 编码的 PLE 压缩](https://github.com/VILA-Lab/optic) [![VILA-Lab/optic Stars](https://img.shields.io/github/stars/VILA-Lab/optic?style=social&label=Stars)](https://github.com/VILA-Lab/optic/stargazers)

  用跨层共享的紧凑 token 编码和每层仿射解码器压缩 PLE。

- [llm-compressor：输入嵌入量化](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) [![vllm-project/llm-compressor Stars](https://img.shields.io/github/stars/vllm-project/llm-compressor?style=social&label=Stars)](https://github.com/vllm-project/llm-compressor/stargazers)

  输入嵌入量化配方，采用对称 INT4 权重和 64 的组大小，附 Pythia-1.4B 评测结果。

- [Megatron-LM：词表并行嵌入查表](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) [![NVIDIA/Megatron-LM Stars](https://img.shields.io/github/stars/NVIDIA/Megatron-LM?style=social&label=Stars)](https://github.com/NVIDIA/Megatron-LM/stargazers)

  词表并行查表实现，包含行分片、token ID 掩码、本地查表和跨设备集合通信。

<a id="category-modalities"></a>

## 视觉与音频

视觉输入常通过可学习投影从图像块生成向量。音频模型中，codec 码本和下游 token 嵌入表分别承担量化重建与模型输入的作用。这些实例补充了查表和投影在不同模态中的用法。

- [SigLIP 2 图像块投影与位置嵌入](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) [![huggingface/transformers Stars](https://img.shields.io/github/stars/huggingface/transformers?style=social&label=Stars)](https://github.com/huggingface/transformers/stargazers)

  SigLIP 2 视觉编码器中的图像块投影与可学习位置嵌入实现。

- [Mimi codec 与 Moshi token 嵌入](https://github.com/kyutai-labs/moshi) [![kyutai-labs/moshi Stars](https://img.shields.io/github/stars/kyutai-labs/moshi?style=social&label=Stars)](https://github.com/kyutai-labs/moshi/stargazers)

  Mimi 音频 codec 与 Moshi 语言模型实现，可对照 codec 码本和独立的音频 token 嵌入表。

- [Cosmos Tokenizer：有限标量量化](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) [![NVIDIA/Cosmos-Tokenizer Stars](https://img.shields.io/github/stars/NVIDIA/Cosmos-Tokenizer?style=social&label=Stars)](https://github.com/NVIDIA/Cosmos-Tokenizer/stargazers)

  有限标量量化（FSQ）实现，包含固定标量级别、可选的可学习投影和物化码本缓冲区。

<a id="wiki"></a>

## 研究 Wiki 与机制比较

| 主题 | 内容 |
| --- | --- |
| [token 嵌入与权重共享](wiki/token-embeddings.zh-CN.md) | token ID、嵌入查表与输入输出权重共享。 |
| [每层嵌入](wiki/ple.zh-CN.md) | 逐层向量、投影与门控残差更新。 |
| [SCONE 与 Engram](wiki/ngram-memory.zh-CN.md) | SCONE 输入扩展与 Engram 内部记忆。 |
| [嵌入压缩](wiki/compression.zh-CN.md) | 分解、量化与嵌入表存储核算。 |
| [视觉输入与模态投影](wiki/visual-projections.zh-CN.md) | 图像块投影与视觉到语言的投影。 |
| [音频码本与语言模型嵌入](wiki/audio-codebooks.zh-CN.md) | codec 量化与下游 token 嵌入表。 |

[机制与成本比较](COMPARISON.zh-CN.md) · [阅读指南](READING.zh-CN.md) · [嵌入表存储计算器](explorer.html)

计算器可下载后离线打开，按词表大小、维度、层数与精度估算表的原始权重存储量。

### 专题解读

- [PLE 的容量与计算代价](insights/capacity-and-compute.zh-CN.md)
- [权重共享：存储收益与表示约束](insights/weight-tying.zh-CN.md)

<a id="contributing"></a>

## 更新与贡献

[更新记录](UPDATES.zh-CN.md) · [完整书目](SOURCES.zh-CN.md) · [社区讨论](DEMAND.zh-CN.md) · [术语表](GLOSSARY.zh-CN.md) · [贡献说明](MAINTENANCE.zh-CN.md)

由 [Jiacheng Liu](https://github.com/jiachengliu12345) 维护。欢迎推荐相关论文、教程和实现，也欢迎指出分类或技术说明中的错误。

[↑ 返回顶部](#top)
