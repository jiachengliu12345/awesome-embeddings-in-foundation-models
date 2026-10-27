<!-- topic: insight-tying -->
<!-- sources: weight-tying,tying-hypothesis,gemma4,tying-bias -->

# Weight tying: storage savings and representation constraints

[简体中文](weight-tying.zh-CN.md) · [README](../README.md) · [Token embeddings](../wiki/token-embeddings.md) · [Comparison](../COMPARISON.md)

Weight tying reuses one matrix for input embeddings and output projection. In a standard language model, the input embedding maps token IDs to vectors, while the output projection maps hidden states to vocabulary logits. When their dimensions align, a model can use the same matrix for both paths. This removes a second vocabulary-sized matrix, but it also requires one representation to serve two roles.

## Early experiments

Press and Wolf’s 2017 study argued for tying in neural language models. They analyzed how the shared matrix updates and reported lower perplexity across several language-model settings. For neural machine translation, they reported reducing model size to less than half without harming performance. The paper evaluates recurrent language models and neural machine translation. [Press and Wolf, EACL 2017](https://aclanthology.org/E17-2025/)

## Input and output representations

Bertolotti and Cazzola’s 2024 analysis examines when input and output representations support a shared matrix. Their theoretical and empirical work connects tying to the distributional hypothesis: similar meanings tend to yield similar input embeddings, while symbols appearing in similar contexts tend to have similar output embeddings. Tying is encouraged by their analysis when the data satisfy this relationship. The condition is central. Input vectors encode how a symbol is represented when read; output vectors encode how the model scores it when predicted. Those roles may align in some settings and diverge in others. [Bertolotti and Cazzola, ICML 2024](https://proceedings.mlr.press/v235/bertolotti24a.html)

## Gemma 4 implementation

In Gemma 4, its `Embedder.decode` uses the transpose of `input_embedding_table` to produce vocabulary scores. This ordinary input/output path uses one shared table; the PLE table is a separate parameter object. [Gemma 4 implementation](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)

## Comparison dimensions

Untied tables use more parameters, yet they allow input and output roles to specialize independently. Tied tables reduce parameter storage; they do not automatically reduce the cost of computing full-vocabulary logits, and their runtime benefit depends on the implementation and serving bottleneck. A useful evaluation should compare tied and untied models with the same architecture, data, tokenizer, optimization budget, and inference setup. Report quality as well as parameter count, checkpoint size, peak memory, and token-generation latency. Where vocabularies, dimensions, or token-frequency patterns differ, state those conditions. For each model and dataset, weigh the saved parameter storage against the constraint on input/output representations.

## Input and output gradient balance

[Lopardo et al., 2026](https://arxiv.org/html/2603.26663v1) study why tied tables align more closely with output space in selected models. Rescaling input gradients changes alignment without consistent downstream gains. Some tied/untied comparisons also use different training data, and single training runs limit generalization. This adds a mechanism to examine alongside controlled quality evaluations.
