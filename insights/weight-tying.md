<!-- topic: insight-tying -->
<!-- sources: weight-tying,tying-hypothesis,gemma4 -->

# Weight tying saves parameters by making input and output share one table

[简体中文](weight-tying.zh-CN.md) · [README](../README.md) · [Token embeddings](../wiki/token-embeddings.md) · [Comparison](../COMPARISON.md)

Weight tying is a parameter-sharing choice with a useful but conditional trade-off. In a standard language model, the input embedding maps token IDs to vectors, while the output projection maps hidden states to vocabulary logits. When their dimensions align, a model can use the same matrix for both paths. This removes a second vocabulary-sized matrix, but it also requires one representation to serve two roles.

Press and Wolf’s 2017 study argued for tying in neural language models. They analyzed how the shared matrix updates and reported lower perplexity across several language-model settings. For neural machine translation, they reported reducing model size to less than half without harming performance. The paper evaluates recurrent language models and neural machine translation. [Press and Wolf, EACL 2017](https://aclanthology.org/E17-2025/)

Bertolotti and Cazzola’s 2024 analysis gives a reason to treat tying as an assumption rather than a universal default. Their theoretical and empirical work connects tying to the distributional hypothesis: similar meanings tend to yield similar input embeddings, while symbols appearing in similar contexts tend to have similar output embeddings. Tying is encouraged by their analysis when the data satisfy this relationship. The condition is central. Input vectors encode how a symbol is represented when read; output vectors encode how the model scores it when predicted. Those roles may align in some settings and diverge in others. [Bertolotti and Cazzola, ICML 2024](https://proceedings.mlr.press/v235/bertolotti24a.html)

The current Gemma 4 implementation shows why readers should verify a model rather than infer its parameterization from convention: its `Embedder.decode` uses the transpose of `input_embedding_table` to produce vocabulary scores. This ordinary input/output path uses one shared table; the PLE table is a separate parameter object. [Gemma 4 implementation](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)

## What to compare

Untied tables use more parameters, yet they allow input and output roles to specialize independently. Tied tables reduce parameter storage; they do not automatically reduce the cost of computing full-vocabulary logits, and their runtime benefit depends on the implementation and serving bottleneck. A useful evaluation should compare tied and untied models with the same architecture, data, tokenizer, optimization budget, and inference setup. Report quality as well as parameter count, checkpoint size, peak memory, and token-generation latency. Where vocabularies, dimensions, or token-frequency patterns differ, state those conditions. For each model and dataset, weigh the saved parameter storage against the constraint on input/output representations.
