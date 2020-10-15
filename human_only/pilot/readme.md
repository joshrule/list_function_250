# Pilot Concepts

This is a list of concepts used to pilot our human experimental paradigm. Inputs and outputs are assumed to be `[int]` with 0 to 10 elements of values 0 to 99 (i.e. each concept is `[int] → [int]`). See [the DSL](../../dsl.md) for details on each symbol. We test one set of 11 machine-generated examples and one set of 11 human-generated examples for each function. For each set, there are 2 unique orderings. In the list below, *h*s link to orderings of the human-generated examples, while *m*s link to orderings of the machine-generated examples.

1. `(lambda (unique $0))`
   [h][1h0] [h][1h1] [m][1m0] [m][1m1]
2. `(lambda (singleton (length $0)))`
   [h][2h0] [h][2h1] [m][2m0] [m][2m1]
3. `(lambda (repeat (max $0) (min $0)))`
   [h][3h0] [h][3h1] [m][3m0] [m][3m1]
4. `(lambda (concat (reverse (drop 1 $0)) $0))`
   [h][4h0] [h][4h1] [m][4m0] [m][4m1]
5. `(lambda (concat (drop (last $0) $0) (take (last $0) $0)))`
   [h][5h0] [h][5h1] [m][5m0] [m][5m1]
6. `(lambda (flatten (map (lambda (cons (first $0) (singleton (length $0)))) (group (lambda $0) $0))))`
   [h][6h0] [h][6h1] [m][6m0] [m][6m1]
7. `(lambda (fold (lambda (lambda (if (> $0 (last $1)) (append $1 $0) $1))) (take 1 $0) (drop 1 $0)))`
   [h][7h0] [h][7h1] [m][7m0] [m][7m1]
8. `(lambda (fold (lambda (lambda (if (is_even (second $0)) (append $1 (first $0)) $1))) empty (zip (droplast 1 $0) (drop 1 $0))))`
   [h][8h0] [h][8h1] [m][8m0] [m][8m1]

[1h0]: json/human/c001_0.json
[1h1]: json/human/c001_1.json
[1m0]: json/machine/c001_0.json
[1m1]: json/machine/c001_1.json
[2h0]: json/human/c002_0.json
[2h1]: json/human/c002_1.json
[2m0]: json/machine/c002_0.json
[2m1]: json/machine/c002_1.json
[3h0]: json/human/c003_0.json
[3h1]: json/human/c003_1.json
[3m0]: json/machine/c003_0.json
[3m1]: json/machine/c003_1.json
[4h0]: json/human/c004_0.json
[4h1]: json/human/c004_1.json
[4m0]: json/machine/c004_0.json
[4m1]: json/machine/c004_1.json
[5h0]: json/human/c005_0.json
[5h1]: json/human/c005_1.json
[5m0]: json/machine/c005_0.json
[5m1]: json/machine/c005_1.json
[6h0]: json/human/c006_0.json
[6h1]: json/human/c006_1.json
[6m0]: json/machine/c006_0.json
[6m1]: json/machine/c006_1.json
[7h0]: json/human/c007_0.json
[7h1]: json/human/c007_1.json
[7m0]: json/machine/c007_0.json
[7m1]: json/machine/c007_1.json
[8h0]: json/human/c008_0.json
[8h1]: json/human/c008_1.json
[8m0]: json/machine/c008_0.json
[8m1]: json/machine/c008_1.json
