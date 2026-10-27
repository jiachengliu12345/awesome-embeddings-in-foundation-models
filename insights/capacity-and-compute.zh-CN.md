<!-- topic: insight-capacity -->
<!-- sources: gemma4,raschka-ple -->

# PLE 的容量与计算代价

[English](capacity-and-compute.md) · [中文首页](../README.zh-CN.md) · [每层嵌入（PLE）](../wiki/ple.zh-CN.md) · [比较页](../COMPARISON.zh-CN.md)

PLE 为每个 token 在不同 Transformer 层提供各自的可学习向量。额外容量存放在查表参数中，再通过门控与投影参与逐层计算。本篇结合 Gemma 4 实现和 Raschka 的解读，讨论表容量、主干计算量与推理成本之间的关系。

## 参数与计算路径

Gemma 4 E2B 和 E4B 的官方实现定义了名为 `per_layer_embeddings` 的嵌入表，形状为 `[vocab_size, num_layers, per_layer_input_dim]`。实现还定义了 `per_layer_model_projection`，把普通 token 表示映射到每层嵌入空间。模型将投影后的表示与按 token ID 查得的表项结合，再为每层提供一个切片。在每个 Transformer 块中，注意力与前馈残差更新后的输出经过门控映射；经 GELU 门控的每层向量被投影回模型宽度、归一化，最后作为残差更新加入。这些参数和计算路径与常规输入嵌入、注意力及 MLP 路径相互区分。[Gemma 4 官方实现](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)

## 存储与计算

这种结构同时增加参数存储和逐层计算。嵌入表的存储量随词表大小、层数和每层维度增长，其参数量为 `V × L × P`。Transformer 主干仍需执行注意力和前馈计算，此外 PLE 路径还需要门控和投影。因此，模型卡中的“有效”参数量若侧重主干计算，就不能代替总存储参数量，也不能完整表示推理服务成本。实际内存占用还取决于数值精度、分片方式和运行时实现；延迟则受内核、批量大小和序列长度影响。

## Raschka 的观点与实验对照

Sebastian Raschka 的架构说明解释了这一区别，并引用模型文档中的 E2B/E4B 有效参数量与总参数量。他也指出，当前缺少能隔离 PLE 作用的受控对照：分别与较小有效参数量及较大总参数量相当的常规模型比较，才有助于判断 PLE 的独立贡献。缺少这些对照时，质量差异可能来自 PLE 的结构、额外参数，或两者共同作用。他还提醒，较大模型可能已有足够容量，因而未必能从额外的 PLE 表项中获益。[Raschka 的 PLE 说明](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/)

## 比较维度

如果密集计算是瓶颈，而且模型在多个层都需要 token 特定信息，按 token 查表可能有吸引力。但它会增大检查点，并可能增加内存访问；逐层门控和投影也仍需计算。关键实验应在训练数据、分词方式、训练预算和硬件匹配的条件下，同时比较质量、计算与内存，并报告总参数量、按明确定义计算的激活参数量、加速器峰值内存、吞吐量和延迟。受控基线有助于判断哪些模型规模与数据能从新增 PLE 容量中获益。
