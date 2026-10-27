<!-- topic: maintenance -->
<!-- sources:  -->

# Contributing and updates

[简体中文](MAINTENANCE.zh-CN.md)

Papers, implementation notes, tutorials, and corrections are welcome. Open an issue or pull request with the source and the question it helps answer.

## Suggest a resource

Include the title, author, original link, and a short explanation of its contribution. For code, point to the relevant module or commit. For experimental results, include the model, data, metric, and hardware needed to interpret them.

The collection covers embedding mechanisms inside foundation models: token and per-layer tables, contextual lookup, compression, modality projections, and codec codebooks. Retrieval embedding services belong to a different topic.

## Improve an explanation

Keep the English and Chinese pages together. Use the shared [glossary](GLOSSARY.md), preserve equations and units, and update affected comparisons and captions. For a factual correction, show the source passage or code path that supports it.

## Follow updates

New sources are reviewed weekly. Updates focus on useful explanations, implementations, and changes to existing comparisons. Older papers stay when they remain useful references. See the [update notes](UPDATES.md).

## Check a change

The repository checker uses Python's standard library:

```sh
python3 scripts/check.py
```

It checks local links, paired language pages, source references, and SVG structure. Open `explorer.html` in a browser to check changes to the calculator.
