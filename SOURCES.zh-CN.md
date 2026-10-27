# 来源与阅读边界

[English](SOURCES.md)

每项材料的用途、作者与实现说明。实验数字保留原作者的设置；文件版本记录在详情中。

## weight-tying

[输入输出权重共享：早期实验](https://aclanthology.org/E17-2025/) — Ofir Press; Lior Wolf

Press 与 Wolf 分析输入输出嵌入的权重共享，并报告神经语言模型和机器翻译实验。

实验涵盖循环神经语言模型与神经机器翻译。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`EACL 2017, E17-2025`。

- [tie](https://github.com/ofirpress/UsingTheOutputEmbedding/blob/master/README.md) · `cc3c7d2750dd396463d8bda0af58d75f82e5c956` · 2026-10-27T01:51:31Z

</details>

## tying-hypothesis

[权重共享与分布假设](https://proceedings.mlr.press/v235/bertolotti24a.html) — Francesco Bertolotti; Walter Cazzola

将权重共享与分布假说联系起来，研究输入和输出表示在什么条件下适合共用矩阵。

共享权重的论证取决于数据中语义相似性与上下文相似性的关系。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`ICML 2024, PMLR235:3584–3610`。


</details>

## gemma3n

[Gemma 3n：PLE 缓存](https://ai.google.dev/gemma/docs/gemma-3n) — Google

Gemma 3n 官方文档，介绍 PLE 缓存、加速器驻留参数，以及模态参数的选择性加载。

PLE 缓存、MatFormer 与模态参数跳过分别改变资源预算的不同部分。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`English footer: 2025-11-01; Chinese page may differ`。


</details>

## gemma4

[Gemma 4 嵌入与 block 源码](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) — Google DeepMind

官方嵌入模块与解码器 block 源码，包含 token 查表、逐层投影、门控、权重共享和模态投影。

模块定义查表、投影、门控与模态输入；存储位置由运行时安排。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`fa50f0358d92302cfd02451cc45ab9f44336c438`。

- [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z
- [gemma-gate](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z

</details>

## scone

[SCONE：语言模型嵌入层扩展](https://arxiv.org/html/2502.01637v3) — Da Yu et al.

用频繁 n-gram 扩展输入表示；独立模型生成上下文向量，推理时从预计算表读取。

训练包含 f-gram 学习器；推理使用预计算向量，仍需计入索引存储和传输。

<details>
<summary>版本与文件</summary>

首次公开：2025-02-03

读取于 2026-10-27；版本：`arXiv:2502.01637v3, 2025-10-23`。


</details>

## engram

[Engram 官方架构演示](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) — DeepSeek-AI

架构演示代码，展示 n-gram 哈希、多头查表和依赖隐藏状态的门控；attention 与 MoE 使用简化占位实现。

架构演示省略或模拟了 attention、MoE 和超连接组件。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`f3ce993dee7c6b2e89c102f367f777926dba016e`。

- [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z
- [engram-gate](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z

</details>

## albert

[ALBERT 分解式嵌入源码](https://github.com/google-research/albert/blob/master/modeling.py) — Google Research

将词表嵌入矩阵分解为低维查表与隐藏维度投影，分开设置嵌入宽度和 Transformer 宽度。

编码器实现参照：嵌入维度与隐藏维度不同时，使用投影映射。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`be7d9412536c4d751e4fe687e82abc998ec54f46`。

- [embedding_lookup and transformer_model embedding_hidden_mapping_in (lines 1040–1100)](https://github.com/google-research/albert/blob/master/modeling.py) · `be7d9412536c4d751e4fe687e82abc998ec54f46` · 2026-10-27T01:51:31Z

</details>

## tensorgpt

[TensorGPT：张量列嵌入压缩](https://arxiv.org/html/2307.00526v2) — Mingxue Xu; Yao Lei Xu; Danilo P. Mandic

用张量列（Tensor Train）因子压缩各个 token 向量，并在查表时重构所需向量。

逐个分解 token 行；代价取决于因子形状、秩和重建内核。

<details>
<summary>版本与文件</summary>

首次公开：2023-07-02

读取于 2026-10-27；版本：`arXiv:2307.00526v2, 2024-10-03`。


</details>

## optic

[OPTIC：共享 token 编码的 PLE 压缩](https://github.com/VILA-Lab/optic) — Jiacheng Liu et al.; VILA Lab

用跨层共享的紧凑 token 编码和每层仿射解码器压缩 PLE。

保存跨层共享的 token 编码、码本与每层解码器；压缩存储需计入三者。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`894852b95d2604c4edd9ebd92e017346481f2e74`。

- [optic](https://github.com/VILA-Lab/optic/blob/main/README.md) · `894852b95d2604c4edd9ebd92e017346481f2e74` · 2026-10-27T01:51:31Z
- [optic-decoder](https://github.com/VILA-Lab/optic/blob/main/src/ple_eval/compact_adapter.py) · `1e2798e0fcc1b79e5a0ae6d3afc6b22c9774b3e6` · 2026-10-27T01:51:31Z

</details>

## quantization

[llm-compressor：输入嵌入量化](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) — vLLM Project contributors

输入嵌入量化配方，采用对称 INT4 权重和 64 的组大小，附 Pythia-1.4B 评测结果。

示例为仅权重 INT4 量化，组大小 64；存储包含打包值与量化缩放因子。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`96227ba7a336a8067aad5b6882092fdc0335a841`。

- [quant](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) · `96227ba7a336a8067aad5b6882092fdc0335a841` · 2026-10-27T01:51:31Z
- [quant-code](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/llama3_example.py) · `c66f70db7cf784ec9ac7e063d1091e94d7e0c717` · 2026-10-27T01:51:31Z

</details>

## raschka-ple

[每层嵌入架构解读](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/) — Sebastian Raschka

Raschka 解释 PLE 的残差路径，并讨论如何用对照实验区分结构作用与新增参数容量的作用。

解释残差路径，并提出用于区分 PLE 贡献的受控基线。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`Live page; no immutable revision exposed`。


</details>

## scratch

[从零实现语言模型：GPT 代码](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) — Sebastian Raschka

《从零构建大语言模型》配套的简洁 GPT 实现，包含 token 与位置嵌入、Transformer block 和输出头。

第 4 章用紧凑的 GPT 实现展示 token 查表、Transformer 主干与输出头。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`85e37361e911bc98624f0c02f360617bde68b91b`。

- [scratch-code](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) · `85e37361e911bc98624f0c02f360617bde68b91b` · 2026-10-27T01:51:31Z

</details>

## tinyengram

[TinyEngram 系统实验课](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) — TinyEngram contributors

围绕 n-gram 记忆的系统教程，介绍访问行、预取、缓存与卸载模拟。

系统课包含练习、参考解答和卸载模拟；使用估算时需查看假设。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`c4fca97a629ae57afb8f21661fd09e9b093b0906`。

- [tiny](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) · `c4fca97a629ae57afb8f21661fd09e9b093b0906` · 2026-10-27T01:51:31Z

</details>

## siglip2

[SigLIP 2 图像块投影与位置嵌入](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) — Hugging Face contributors

SigLIP 2 视觉编码器中的图像块投影与可学习位置嵌入实现。

连续图像块投影与离散位置查表是不同操作。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`02f5f9629293632ea50587ac1a74afd4871abcd6`。

- [siglip](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) · `02f5f9629293632ea50587ac1a74afd4871abcd6` · 2026-10-27T01:51:31Z

</details>

## moshi

[Mimi codec 与 Moshi token 嵌入](https://github.com/kyutai-labs/moshi) — Kyutai contributors

Mimi 音频 codec 与 Moshi 语言模型实现，可对照 codec 码本和独立的音频 token 嵌入表。

codec 的 EMA 状态与下游 token 表承担不同的存储与训练职责。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`746036e1d100e397936a629da012d00b87dfc619`。

- [mimi](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/quantization/core_vq.py) · `746036e1d100e397936a629da012d00b87dfc619` · 2026-10-27T01:51:31Z
- [moshi-lm](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/models/lm.py) · `209b7a59c9c086810a81a7d8b99c5233a0ad87ff` · 2026-10-27T01:51:31Z

</details>

## cosmos-fsq

[Cosmos Tokenizer：有限标量量化](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) — NVIDIA contributors

有限标量量化（FSQ）实现，包含固定标量级别、可选的可学习投影和物化码本缓冲区。

归档实现采用固定标量级别，可选学习投影，并分配非持久码本缓冲区。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`38042e989f236d97736052c4a619619b636db19d`。

- [fsq](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) · `38042e989f236d97736052c4a619619b636db19d` · 2026-10-27T01:51:31Z

</details>

## adaptive-input

[自适应输入表示](https://arxiv.org/abs/1809.10853v3) — Alexei Baevski; Michael Auli; fairseq contributors

按词频为不同词表组分配不同嵌入维度，再投影到统一的模型宽度。

不同词频分组使用不同维度；自适应输入输出共享要求分界、因子与维度匹配。

<details>
<summary>版本与文件</summary>

首次公开：2018-09-28

读取于 2026-10-27；版本：`arXiv:1809.10853v3 (2019-02-22); file SHAs below`。

- [AdaptiveInput.__init__, weights_for_band, forward](https://github.com/facebookresearch/fairseq/blob/main/fairseq/modules/adaptive_input.py) · `01ac4accaccc3e4625ee2ca6a17cf88df1db0ca1` · 2026-10-27T02:03:11Z
- [build_model tie_adaptive_weights assertions](https://github.com/facebookresearch/fairseq/blob/main/fairseq/models/transformer_lm.py) · `1e3aa72d38a9970916f3677bb3b7871aceaeafce` · 2026-10-27T02:03:11Z
- [Sections 1–3, frequency bands and weight sharing](https://arxiv.org/pdf/1809.10853) · `arXiv:1809.10853v3` · 2026-10-27T02:03:11Z

</details>

## minbpe

[Andrej Karpathy：分词与嵌入查表](https://github.com/karpathy/minbpe/blob/master/lecture.md) — Andrej Karpathy

Karpathy 的 BPE 分词器实现与讲义，串联文本、token ID、词表大小和嵌入表行。

文字讲义尚未完稿，已覆盖分词器与嵌入表的衔接；后续 BPE 内容可沿视频与仓库学习。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`file blob ebe169f837d5b0113b7545fcda1db6dd040a1f7d`。

- [Character-level tokenization; trainable table rows; BPE introduction](https://github.com/karpathy/minbpe/blob/master/lecture.md) · `ebe169f837d5b0113b7545fcda1db6dd040a1f7d` · 2026-10-27T05:26:45.040244Z

</details>

## gemma3n-guide

[Google：Gemma 3n 开发者指南](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/) — Omar Sanseviero; Ian Ballantyne

模型团队介绍 PLE 的端侧部署动机，以及 Gemma 3n 总参数量与加速器驻留参数量的区别。

作为技术文档的入门补充；PLE 一节解释了端侧模型设计中的 CPU 存储与计算安排。

<details>
<summary>版本与文件</summary>

首次公开：2025-06-26

读取于 2026-10-27；版本：`Developer blog, 2025-06-26; live page`。

- [Per-Layer Embeddings (PLE): Unlocking more memory efficiency](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/) · `Developer blog, 2025-06-26; live page` · 2026-10-27T05:26:45.040244Z

</details>

## longcat

[LongCat：嵌入容量与专家容量的扩展比较](https://arxiv.org/html/2601.21204v2) — Hong Liu et al.

比较嵌入与 MoE 专家的容量分配，并介绍 LongCat-Flash-Lite 的系统设计。

论文报告的优势对应其所研究的设置；应结合参数预算、模型宽度与系统优化阅读。

<details>
<summary>版本与文件</summary>

首次公开：2026-01-29

读取于 2026-10-27；版本：`arXiv:2601.21204v2, 2026-02-11`。

- [Architecture, embedding/expert allocation experiments, and systems optimizations](https://arxiv.org/html/2601.21204v2) · `arXiv:2601.21204v2, 2026-02-11` · 2026-10-27T05:26:45.040244Z

</details>

## qwen-ngram

[Qwen3.8-Next：n-gram 注入位置与词表消融](https://arxiv.org/html/2608.30320v1) — Qwen Team

报告 n-gram 注入位置与词表预算的消融实验，并介绍主机内存预取设计。

第 2.3 节比较注入位置与词表预算；在增加容量的实验中，损失下降，但部分下游指标趋于饱和或波动。

<details>
<summary>版本与文件</summary>

首次公开：2026-08-31

读取于 2026-10-27；版本：`arXiv:2608.30320v1`。

- [Section 2.3; Tables 7–9; host prefetch at Layer 2](https://arxiv.org/html/2608.30320v1) · `arXiv:2608.30320v1` · 2026-10-27T05:26:45.040244Z

</details>

## staple

[STAPLE：为预训练检查点加入嵌入记忆](https://github.com/Infini-AI-Lab/STAPLE) — Ranajoy Sadhukhan et al.

为预训练检查点加入 token 查表残差记忆，并提供预热和主机卸载设计。

保留预训练 FFN 上投影，加入按 token ID 查表的残差路径。论文列出缓存与推理设置；README 给出八 GPU 训练流程。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`arXiv:2610.12599v1; README blob 7e3384be54f7bb02771e9cbd0df14f0870faf68f`。

- [README quick start; paper Sections 2, 8–9](https://arxiv.org/html/2610.12599v1) · `arXiv:2610.12599v1` · 2026-10-27T05:26:45.040244Z
- [Quick start and model variants](https://github.com/Infini-AI-Lab/STAPLE/blob/main/README.md) · `7e3384be54f7bb02771e9cbd0df14f0870faf68f` · 2026-10-27T05:26:45.040244Z

</details>

## count

[COUNT：用语料统计构造 n-gram 嵌入](https://arxiv.org/html/2610.20456v1) — Ian Magnusson; Noah A. Smith; Pang Wei Koh

用固定语料统计和模型已有输出向量构造 n-gram 嵌入，为学习表行提供另一种方案。

COUNT 在主机端保存统计，组合模型已有的输出嵌入；论文还研究了推理时切换领域统计表。

<details>
<summary>版本与文件</summary>

首次公开：2026-10-14

读取于 2026-10-27；版本：`arXiv:2610.20456v1`。

- [Sections 2.2–2.3 and 5–6](https://arxiv.org/html/2610.20456v1) · `arXiv:2610.20456v1` · 2026-10-27T05:26:45.040244Z

</details>

## memory-layers

[Meta：大规模记忆层](https://github.com/facebookresearch/memory) — Vincent-Pierre Berges; Barlas Oğuz et al.

作为 token ID 与 n-gram 查表的对照，介绍由隐藏状态查询的可训练乘积键记忆。

作为相邻机制对照：查询依赖隐状态。论文与参考实现讨论了稀疏查表、内存带宽和分布式值表。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`arXiv:2412.09764v1; README blob 4e142638886df2901996d7d77eabd914e8c963ae`。

- [Paper Sections 1, 3, 6; README project overview](https://arxiv.org/html/2412.09764v1) · `arXiv:2412.09764v1` · 2026-10-27T05:26:45.040244Z
- [Project overview and configuration](https://github.com/facebookresearch/memory/blob/main/README.md) · `4e142638886df2901996d7d77eabd914e8c963ae` · 2026-10-27T05:26:45.040244Z

</details>

## groupreduce

[GroupReduce：按词频分组的低秩压缩](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html) — Patrick H. Chen; Si Si; Yang Li; Ciprian Chelba; Cho-Jui Hsieh

按词频对词表分块，使用加权低秩近似压缩各块。

先按词频对词表分组，再迭代优化各块的加权低秩近似；实验使用当时的神经语言模型和翻译模型。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`NeurIPS 2018 proceedings`。

- [Introduction and Section 3, GroupReduce](https://proceedings.neurips.cc/paper_files/paper/2018/file/a2b8a85a29b2d64ad6f47275bf1360c6-Paper.pdf) · `NeurIPS 2018 proceedings` · 2026-10-27T05:26:45.040244Z

</details>

## tt-embedding

[张量化嵌入层](https://aclanthology.org/2020.findings-emnlp.436/) — Oleksii Hrinchuk; Valentin Khrulkov; Leyla Mirvakhabova; Elena Orlova; Ivan Oseledets

用共享张量列因子参数化整张嵌入表，并研究端到端训练。

用共享 TT 因子表示词表轴与特征轴，并重构所请求的表行；论文研究了紧凑嵌入层的端到端训练。

<details>
<summary>版本与文件</summary>

首次公开：2019-01-30

读取于 2026-10-27；版本：`Findings of EMNLP 2020, pp. 4847–4860; earlier preprint arXiv:1901.10787`。

- [Introduction; TT-matrix and TT-embedding construction](https://aclanthology.org/2020.findings-emnlp.436.pdf) · `Findings of EMNLP 2020, pp. 4847–4860; earlier preprint arXiv:1901.10787` · 2026-10-27T05:26:45.040244Z

</details>

## megatron-embedding

[Megatron-LM：词表并行嵌入查表](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) — NVIDIA; Megatron-LM contributors

词表并行查表实现，包含行分片、token ID 掩码、本地查表和跨设备集合通信。

沿词表行对嵌入表分片；前向路径屏蔽非本地 ID 并合并结果。分片与压缩解决的存储问题不同。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`commit 3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08`。

- [VocabParallelEmbedding, lines 351 onward](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) · `commit 3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08` · 2026-10-27T05:26:45.040244Z

</details>

## tying-bias

[权重共享如何使 token 嵌入偏向输出空间](https://arxiv.org/html/2603.26663v1) — Antonio Lopardo; Avyukth Harish; Catherine Arnett; Akshat Gupta

研究共享嵌入中的输入输出梯度不平衡，以及改变其输出空间对齐程度的干预。

作者重调输入梯度后，嵌入对齐发生变化，下游表现却没有一致提升。部分共享与非共享模型对照也存在训练数据差异。

<details>
<summary>版本与文件</summary>

首次公开：2026-03-27

读取于 2026-10-27；版本：`arXiv:2603.26663v1`。

- [Sections 3, 4–6; OLMo model/data comparison](https://arxiv.org/html/2603.26663v1) · `arXiv:2603.26663v1` · 2026-10-27T05:26:45.040244Z

</details>

