# List Function 250

This repository contains a benchmark set of [250 list functions](functions.md), functions over lists of natural numbers.

The benchmark was first described and evaluated in (Rule, 2020).

The problems were designed using a [human-scale domain-specific language](dsl.md) (DSL), though the first 100 problems are somewhat simpler and designed to be learnable for artificial intelligence agents and computational cognitive science models.

JSON files for each function can be found in [`json/`](json/). They are named according to problem and trial ordering, e.g. `c007_4.json` contains trials for function 7, trial ordering 4. Each file contains the function's `id`, a string describing the function as a `program` in [the DSL](dsl.md), and the training `data`. Each training datum is a pair containing an `i`nput, and an `o`utput. You can convert from JSON to CSV or TXT with [`json2.py`](json2.py).
