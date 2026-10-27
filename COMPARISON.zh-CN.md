# 机制与成本比较

[English](COMPARISON.md)

按查表键、参数对象和注入位置比较设计，再分别计算存储、访问与计算代价。延迟需结合对应实现、批大小和硬件阅读。GB = 10⁹ Bytes；GiB = 2³⁰ Bytes。

| 设计 | 键／输入 | 对象 | 注入位置 | 训练 |
| --- | --- | --- | --- | --- |
| token 表／共享输出头 | token ID | E ∈ R^(V×d)；可同时用于 logits | block 前输入；共享 Eᵀ 用于输出 | 联合训练；共享约束输入输出使用同一矩阵 |
| 每层嵌入（Gemma 4） | token ID × 层切片 | P ∈ R^(V×L×dₚ)，另有投影／门控 | block 外准备；启用的 block 在 attention＋FFN 后加入门控更新 | 随模型学习表及融合路径 |
| SCONE | 高频上下文 n-gram 匹配 | 上下文输入向量；输出词表不变 | 主干前的输入嵌入扩展 | 训练独立 f-gram 学习器，再预计算向量 |
| Engram 演示 | 规范化 n-gram 的多头哈希 | 哈希表、键值投影和卷积 | 所选内部 block；演示中位于 attention 前 | 学习记忆与主干；公开演示模拟了部分主干 |
| 分解式嵌入（ALBERT） | token ID 后接线性映射 | V×e 表与 e×d 投影 | 编码器输入 | 训练时学习分解参数化 |
| 自适应输入 | 按频率排序并分组的 token ID | 分组表 V_g×d_g 与投影 d_g×d | 将选中输入行投影到统一模型维度 | 训练变容量输入；可与兼容自适应输出共享权重 |
| TensorGPT | token ID | 每个 token 的张量列核心 | 重建所请求的嵌入向量 | 论文在训练后分解，不用额外训练数据 |
| 用于 PLE 的 OPTIC | 跨层解码器共享 token ID | token 编码元组、共享码本和每层仿射解码器 | 重建 PLE 行，再进入已有融合路径 | 针对 PLE 输出路径拟合压缩表示 |
| 输入表量化 | token ID | 打包 Embedding 权重与分组 scale | 输入侧查表／反量化 | 示例为无需校准数据的仅权重量化：INT4，组大小 64 |
| 图像块／模态投影 | 连续图像块或编码特征；位置表用 ID | 线性映射／卷积；位置表另列 | 图像块编码器输入，或映射到 LM 维度 | 学习投影；训练配方依模型而定 |
| codec 码本／下游音频表 | codec 特征→索引；索引→LM 向量 | codec 中心（Mimi EMA 缓冲区）与 LM 嵌入参数 | 音频 codec 量化器与下游 LM 输入 | codec 更新与 LM 训练承担不同职责 |
| FSQ 对照 | 量化标量坐标↔编码 ID | 固定 levels；可选学习投影及隐式码本缓冲区 | 图像／视频 codec 量化器 | 训练外围模型；不逐项学习码本中心 |

[计算路径图：token 嵌入、PLE、SCONE 与 Engram](assets/injection.zh-CN.svg)对照各自的输入、查表和向量使用位置。

## 成本矩阵

| 设计 | 参数／理论存储 | 加速器内存 | 访问与传输 | FLOPs | 延迟 |
| --- | --- | --- | --- | --- | --- |
| token 表／共享输出头 | 共享时 Vd 个独立值；b 位时 Vdb/8 Bytes，不含其他项 | 依赖放置方式；共享输出头可能需要广泛访问 E | 输入只读取所选行；通常全词表 logits 使用全部行 | 查表主要为内存访问；全输出投影每个隐藏向量按 Vd 扩展 | 未测量 |
| 每层嵌入（Gemma 4） | 表：VLdₚ 个值；VLdₚb/8 Bytes；未计投影 | 取决于表放置和层输入的物化 | token 寻址可预知；仍需执行投影与门控 | 增加模型投影和每层门控／投影 | 未测量 |
| SCONE | 缓存向量数×维度×精度，另有索引；训练学习器另计 | 论文将缓存置于加速器外；固定推理资源结论有实验条件 | 需要匹配、查询和传输；依赖缓存与带宽 | 学习器不在推理路径；训练和预计算仍有计算代价 | 论文报告了指定设置下的查询延迟 |
| Engram 演示 | 各头表值总数×b/8，另计门控／投影；不是 V×L×dₚ | 地址可预知，适合设计预取；演示不是主机卸载基准 | 读取多行；哈希碰撞与融合需分别分析 | 哈希、投影、依赖隐藏状态的门控及卷积 | 未测量 |
| 分解式嵌入（ALBERT） | e≠d 时查表与投影权重 Ve＋ed，不含 bias 和其他表；减少权重需满足 Ve＋ed＜Vd。 | 依赖表与投影的放置 | 读取 e 维行后投影 | 增加 e→d 投影；节省的是存储，计算仍有代价 | 未测量 |
| 自适应输入 | 权重数 Σ_g(V_g d_g＋d_g d)，未计输出共享与其他状态 | 依赖放置方式及分组／投影临时张量 | 选择分组、查表、投影及恢复输出顺序 | 投影依赖所属分组；自适应输出另行计算 | 未测量 |
| TensorGPT | 存储张量列核心；大小取决于分解及秩 | 核心与重建临时内存依赖实现 | 读取核心并重建 | 张量收缩替代直接读取稠密行 | 见论文的特定设备测量 |
| 用于 PLE 的 OPTIC | 编码＋码本＋层解码器；分母必须完整计入 | 紧凑数组驻留，按需解码行 | 读取编码和码本，再做仿射解码 | 增加重建；不移除已有 PLE 门控／投影 | 见仓库指定推理设置下的测量 |
| 输入表量化 | Vdb/8 打包值＋scale、对齐和元数据 | 依赖推理 kernel；README 称表保持打包形式 | 读取所选行并反量化 | 增加反量化；融合行为取决于实现 | 未测量 |
| 图像块／模态投影 | 投影 m×d（使用 bias 时另计）；位置表另计 | 特征激活与图像分辨率会影响内存 | 读取连续特征并矩阵乘 | 稠密投影；不是 ID 查表 | 未测量 |
| codec 码本／下游音频表 | codec 每级 K×c；下游每流 K×d；分别计量 | codec 状态、LM 表和流式缓冲区分别计量 | codec 编解码不同于 LM token 查表 | codec 搜索／解码与 LM 查表／投影不同 | 未测量 |
| FSQ 对照 | 固定网格描述不等于码本缓冲区分配为零 | Cosmos 实现物化 implicit_codebook 缓冲区 | 标量量化与索引转换 | 可包含学习投影；依赖配置 | 未测量 |

## 组合证据

- 已有实现：Gemma 4 模块共存普通共享嵌入、PLE 和模态投影。 [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)
- 已有实现：OPTIC 重建 Gemma 4 PLE 行。 [optic](https://github.com/VILA-Lab/optic)
- 实现文档：输入 Embedding 量化可与 Linear 量化组合；仍需核对具体 checkpoint 与共享输出头。 [quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md)
- 仅有结构上的可能：PLE＋Engram 或 SCONE＋PLE。首版没有检查到条件匹配的组合实验。 [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py), [scone](https://arxiv.org/html/2502.01637v3)
- 有条件的已有实现：fairseq 共享自适应输入输出权重时要求分组分界、因子和输入输出维度匹配。投影共享另有配置。 [adaptive-input](https://arxiv.org/abs/1809.10853v3)

## 逐项依据

- token 表／共享输出头: [weight-tying](https://aclanthology.org/E17-2025/), [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)
- 每层嵌入（Gemma 4）: [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), [gemma3n](https://ai.google.dev/gemma/docs/gemma-3n)
- SCONE: [scone](https://arxiv.org/html/2502.01637v3)
- Engram 演示: [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py), [tinyengram](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md)
- 分解式嵌入（ALBERT）: [albert](https://github.com/google-research/albert/blob/master/modeling.py)
- 自适应输入: [adaptive-input](https://arxiv.org/abs/1809.10853v3)
- TensorGPT: [tensorgpt](https://arxiv.org/html/2307.00526v2)
- 用于 PLE 的 OPTIC: [optic](https://github.com/VILA-Lab/optic)
- 输入表量化: [quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md)
- 图像块／模态投影: [siglip2](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py), [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)
- codec 码本／下游音频表: [moshi](https://github.com/kyutai-labs/moshi)
- FSQ 对照: [cosmos-fsq](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py)

[返回入口](README.zh-CN.md)
