# 来源与阅读边界

[English](SOURCES.md)

每项材料的用途、作者与实现说明。实验数字保留原作者的设置；文件版本记录在详情中。

## weight-tying

[输入输出权重共享：早期实验](https://aclanthology.org/E17-2025/) — Ofir Press; Lior Wolf

理解输入输出共用的参数对象及早期评测。

实验涵盖循环神经语言模型与神经机器翻译。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`EACL 2017, E17-2025`。

- [tie](https://github.com/ofirpress/UsingTheOutputEmbedding/blob/master/README.md) · `cc3c7d2750dd396463d8bda0af58d75f82e5c956` · 2026-10-27T01:51:31Z

</details>

## tying-hypothesis

[权重共享与分布假设](https://proceedings.mlr.press/v235/bertolotti24a.html) — Francesco Bertolotti; Walter Cazzola

阅读带适用条件的权重共享论证。

共享权重的论证取决于数据中语义相似性与上下文相似性的关系。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`ICML 2024, PMLR235:3584–3610`。


</details>

## gemma3n

[Gemma 3n：PLE 缓存](https://ai.google.dev/gemma/docs/gemma-3n) — Google

区分有效参数载入量、PLE 缓存和模态参数跳过。

PLE 缓存、MatFormer 与模态参数跳过分别改变资源预算的不同部分。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`English footer: 2025-11-01; Chinese page may differ`。


</details>

## gemma4

[Gemma 4 嵌入与 block 源码](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) — Google DeepMind

追踪查表、模型投影、门控、权重共享和模态投影。

模块定义查表、投影、门控与模态输入；存储位置由运行时安排。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`fa50f0358d92302cfd02451cc45ab9f44336c438`。

- [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z
- [gemma-gate](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z

</details>

## scone

[SCONE：语言模型嵌入层扩展](https://arxiv.org/html/2502.01637v3) — Da Yu et al.

比较预计算上下文 n-gram 输入与模型内部每层表。

训练包含 f-gram 学习器；推理使用预计算向量，仍需计入索引存储和传输。

<details>
<summary>版本与文件</summary>

首次公开：2025-02-03

读取于 2026-10-27；版本：`arXiv:2502.01637v3, 2025-10-23`。


</details>

## engram

[Engram 官方架构演示](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) — DeepSeek-AI

检查 n-gram 哈希、多头查表与依赖隐藏状态的融合。

架构演示省略或模拟了 attention、MoE 和超连接组件。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`f3ce993dee7c6b2e89c102f367f777926dba016e`。

- [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z
- [engram-gate](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z

</details>

## albert

[ALBERT 分解式嵌入源码](https://github.com/google-research/albert/blob/master/modeling.py) — Google Research

在分解设计中区分词表嵌入维度与模型隐藏维度。

编码器实现参照：嵌入维度与隐藏维度不同时，使用投影映射。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`be7d9412536c4d751e4fe687e82abc998ec54f46`。

- [embedding_lookup and transformer_model embedding_hidden_mapping_in (lines 1040–1100)](https://github.com/google-research/albert/blob/master/modeling.py) · `be7d9412536c4d751e4fe687e82abc998ec54f46` · 2026-10-27T01:51:31Z

</details>

## tensorgpt

[TensorGPT：张量列嵌入压缩](https://arxiv.org/html/2307.00526v2) — Mingxue Xu; Yao Lei Xu; Danilo P. Mandic

比较张量列重建与表值量化。

逐个分解 token 行；代价取决于因子形状、秩和重建内核。

<details>
<summary>版本与文件</summary>

首次公开：2023-07-02

读取于 2026-10-27；版本：`arXiv:2307.00526v2, 2024-10-03`。


</details>

## optic

[OPTIC：共享 token 编码的 PLE 压缩](https://github.com/VILA-Lab/optic) — Jiacheng Liu et al.; VILA Lab

检查面向 PLE 的压缩：token 共享编码和每层仿射解码器。

保存跨层共享的 token 编码、码本与每层解码器；压缩存储需计入三者。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`894852b95d2604c4edd9ebd92e017346481f2e74`。

- [optic](https://github.com/VILA-Lab/optic/blob/main/README.md) · `894852b95d2604c4edd9ebd92e017346481f2e74` · 2026-10-27T01:51:31Z
- [optic-decoder](https://github.com/VILA-Lab/optic/blob/main/src/ple_eval/compact_adapter.py) · `1e2798e0fcc1b79e5a0ae6d3afc6b22c9774b3e6` · 2026-10-27T01:51:31Z

</details>

## quantization

[llm-compressor：输入嵌入量化](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) — vLLM Project contributors

找到针对 nn.Embedding 的 INT4、组大小 64 配方及计量边界。

示例为仅权重 INT4 量化，组大小 64；存储包含打包值与量化缩放因子。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`96227ba7a336a8067aad5b6882092fdc0335a841`。

- [quant](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) · `96227ba7a336a8067aad5b6882092fdc0335a841` · 2026-10-27T01:51:31Z
- [quant-code](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/llama3_example.py) · `c66f70db7cf784ec9ac7e063d1091e94d7e0c717` · 2026-10-27T01:51:31Z

</details>

## raschka-ple

[每层嵌入架构解读](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/) — Sebastian Raschka

理解 PLE 残差路径与作者提出的受控基线问题。

解释残差路径，并提出用于区分 PLE 贡献的受控基线。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`Live page; no immutable revision exposed`。


</details>

## scratch

[从零实现语言模型：GPT 代码](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) — Sebastian Raschka

先理解 token 查表与输出头形状，再读额外记忆路径。

第 4 章用紧凑的 GPT 实现展示 token 查表、Transformer 主干与输出头。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`85e37361e911bc98624f0c02f360617bde68b91b`。

- [scratch-code](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) · `85e37361e911bc98624f0c02f360617bde68b91b` · 2026-10-27T01:51:31Z

</details>

## tinyengram

[TinyEngram 系统实验课](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) — TinyEngram contributors

分析访问行、预取、缓存与卸载模拟。

系统课包含练习、参考解答和卸载模拟；使用估算时需查看假设。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`c4fca97a629ae57afb8f21661fd09e9b093b0906`。

- [tiny](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) · `c4fca97a629ae57afb8f21661fd09e9b093b0906` · 2026-10-27T01:51:31Z

</details>

## siglip2

[SigLIP 2 图像块投影与位置嵌入](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) — Hugging Face contributors

区分连续图像块投影与离散位置嵌入表。

连续图像块投影与离散位置查表是不同操作。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`02f5f9629293632ea50587ac1a74afd4871abcd6`。

- [siglip](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) · `02f5f9629293632ea50587ac1a74afd4871abcd6` · 2026-10-27T01:51:31Z

</details>

## moshi

[Mimi codec 与 Moshi token 嵌入](https://github.com/kyutai-labs/moshi) — Kyutai contributors

区分 codec 码本中心与下游音频 token 嵌入表。

codec 的 EMA 状态与下游 token 表承担不同的存储与训练职责。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`746036e1d100e397936a629da012d00b87dfc619`。

- [mimi](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/quantization/core_vq.py) · `746036e1d100e397936a629da012d00b87dfc619` · 2026-10-27T01:51:31Z
- [moshi-lm](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/models/lm.py) · `209b7a59c9c086810a81a7d8b99c5233a0ad87ff` · 2026-10-27T01:51:31Z

</details>

## cosmos-fsq

[Cosmos Tokenizer：有限标量量化](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) — NVIDIA contributors

理解固定标量网格、可选学习投影与运行时码本缓冲区。

归档实现采用固定标量级别，可选学习投影，并分配非持久码本缓冲区。

<details>
<summary>版本与文件</summary>

读取于 2026-10-27；版本：`38042e989f236d97736052c4a619619b636db19d`。

- [fsq](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) · `38042e989f236d97736052c4a619619b636db19d` · 2026-10-27T01:51:31Z

</details>

## adaptive-input

[自适应输入表示](https://arxiv.org/abs/1809.10853v3) — Alexei Baevski; Michael Auli; fairseq contributors

比较不同维度的词表分组，并检查自适应输入输出权重共享的条件。

不同词频分组使用不同维度；自适应输入输出共享要求分界、因子与维度匹配。

<details>
<summary>版本与文件</summary>

首次公开：2018-09-28

读取于 2026-10-27；版本：`arXiv:1809.10853v3 (2019-02-22); file SHAs below`。

- [AdaptiveInput.__init__, weights_for_band, forward](https://github.com/facebookresearch/fairseq/blob/main/fairseq/modules/adaptive_input.py) · `01ac4accaccc3e4625ee2ca6a17cf88df1db0ca1` · 2026-10-27T02:03:11Z
- [build_model tie_adaptive_weights assertions](https://github.com/facebookresearch/fairseq/blob/main/fairseq/models/transformer_lm.py) · `1e3aa72d38a9970916f3677bb3b7871aceaeafce` · 2026-10-27T02:03:11Z
- [Sections 1–3, frequency bands and weight sharing](https://arxiv.org/pdf/1809.10853) · `arXiv:1809.10853v3` · 2026-10-27T02:03:11Z

</details>

