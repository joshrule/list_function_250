# List Routines DSL

- [Overview](#overview)
- [Types](#type-system)
- [Symbols](#symbols)
- [Lambdas](#lambdas)
- [Ideas for the Future](#ideas-for-the-future)

## Overview

This is a Domain-specific language (DSL) for list routines. It applies to integers between 0 and 99 (inclusive), and lists of lengths between 0 and 10 (inclusive). All list indices are 0-based (i.e. index 0 indicates first item in list, 1 indicates second, *N* indicates *N-1*th). This DSL follows a Lisp-like syntax. It aims for inclusivity, capturing a large number of fundamental primitives that people may use when processing lists, and does not exclude certain primitives simply because they can be formulated using other primitives. This DSL is based on one originally prepared by Luc Cary in August 2019.

## Type System

This DSL uses a [Hindley-Milner type system](https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system).

<table>
<thead>
<tr class="header">
<th><strong>Symbol</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>t1,t2,...</code></td>
<td>Universally quantified type variables.</td>
</tr>
<tr>
<td><code>int</code></td>
<td>Integer value.</td>
</tr>
<tr>
<td><code>bool</code></td>
<td>Boolean value.</td>
</tr>
<tr>
<td><code>[&lt;type&gt;]</code></td>
<td>List where each value is of type &lt;type&gt;. E.g.:
<ul style="margin-bottom: 0;">
<li><code>[t1]</code> - List of values of type <code>t1</code>.</li>
<li><code>[int]</code> - List of integers.</li>
<li><code>[[int]]</code> - List of lists of integers.</li></ul></td>
</tr>
<tr>
<td><code>→</code></td>
<td>Arrow type. Left hand side of arrow represents input types, right represents output type. Chaining of arrows represents multiple function arguments, e.g. a function that takes two <code>int</code>s and returns an <code>int</code> would be <code>int → int → int</code>.</td>
</tr>
</tbody>
</table>

*Table 1.0 - Type Definitions*

## Symbols

This section contains a table of symbols in the DSL, along with their type signatures and a brief description.

<table>
  <col>
  <col width="275">
  <col>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>Type Signature</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>lambda</code></td>
<td></td>
<td>Opens a lambda expression.</td>
</tr>
<tr>
<td><code>0..99</code></td>
<td><code>int</code></td>
<td>Constant: integers between 0 and 99, inclusive.</td>
</tr>
<tr>
<td><code>empty</code></td>
<td><code>[t1]</code></td>
<td>Constant: an empty list.</td>
</tr>
<tr>
<td><code>true false</code></td>
<td><code>bool</code></td>
<td>Constant: Boolean literals.</td>
</tr>
<tr>
<td><code>%</code></td>
<td><code>int → int → int</code></td>
<td>Binary remainder operator. Might be low in people's prior.</td>
</tr>
<tr>
<td><code>*</code></td>
<td><code>int → int → int</code></td>
<td>Binary multiplication operator.</td>
</tr>
<tr>
<td><code>+</code></td>
<td><code>int → int → int</code></td>
<td>Binary addition operator.</td>
</tr>
<tr>
<td><code>-</code></td>
<td><code>int → int → int</code></td>
<td>Binary subtraction operator.</td>
</tr>
<tr>
<td><code>/</code></td>
<td><code>int → int → int</code></td>
<td>Binary quotient operator.</td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td><code>int → int → bool</code></td>
<td>Binary less than predicate.</td>
</tr>
<tr>
<td><code>==</code></td>
<td><code>int → int → bool</code></td>
<td>Binary equality predicate.</td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td><code>int → int → bool</code></td>
<td>Binary greater than predicate.</td>
</tr>
<tr>
<tr>
<td><code>abs</code></td>
<td><code>int → int</code></td>
<td>Returns the absolute value of an integer.</td>
</tr>
<tr>
<td><code>and</code></td>
<td><code>bool → bool → bool</code></td>
<td>Boolean AND operator.</td>
</tr>
<tr>
<td><code>append</code></td>
<td><code>[t1] → t1 → [t1]</code></td>
<td>Appends a given item at the end of a list, returning a single list.</td>
</tr>
<tr>
<td><code>concat</code></td>
<td><code>[t1] → [t1] → [t1]</code></td>
<td>Concatenates two lists, returning a single list.</td>
</tr>
<tr>
<td><code><a href="https://en.wikipedia.org/wiki/Cons"><span>cons</span></a></code></td>
<td><code>t1 → [t1] → [t1]</code></td>
<td>Prepends a given item to the beginning of a list.</td>
</tr>
<tr>
<td><code>count</code></td>
<td><code>(t1 → bool) → [t1] → int</code></td>
<td>Counts the number of values in an input list matching a function of type (t1 → bool). Essentially, (length (filter f xs)).</td>
</tr>
<tr>
<td><code>cut_idx</code></td>
<td><code>int → [t1] → [t1]</code></td>
<td>Removes a value at a given index in a given list.</td>
</tr>
<tr>
<td><code>cut_slice</code></td>
<td><code>int → int → [t1] → [t1]</code></td>
<td>Removes all values (inclusive) between a given index (first argument) and another index (second argument) in a given list (third argument).</td>
</tr>
<tr>
<td><code>cut_val</code></td>
<td><code>t1 → [t1] → [t1]</code></td>
<td>Removes the first instance of a given value (first argument) in the input list (second argument).</td>
</tr>
<tr>
<td><code>cut_vals</code></td>
<td><code>t1 → [t1] → [t1]</code></td>
<td>Removes all values matching a given value (first argument) in the input list (second argument).</td>
</tr>
<tr>
<td><code>drop</code></td>
<td><code>int → [t1] → [t1]</code></td>
<td>Drops the first N values in an input list, returning the rest.</td>
</tr>
<tr>
<td><code>droplast</code></td>
<td><code>int → [t1] → [t1]</code></td>
<td>Drops the last N values in an input list, returning the rest.</td>
</tr>
<tr>
<td><code>filter</code></td>
<td><code>(t1 → bool) → [t1] → [t1]</code></td>
<td>Higher-order function that returns a filtered list of values from a list, filtering by an input function.</td>
</tr>
<tr>
<td><code>filteri</code></td>
<td><code>(int → t1 → bool) → [t1] → [t1]</code></td>
<td>Same as filter except the input function is passed the index and value for each element in the list.</td>
</tr>
<tr>
<td><code>find</code></td>
<td><code>(t1 → bool) → [t1] → [int]</code></td>
<td>Returns the indices of the elements that pass the predicate.</td>
</tr>
<tr>
<td><code>flatten</code></td>
<td><code>[[t1]] → [t1]</code></td>
<td>Returns a list flattened into a single dimension.</td>
</tr>
<tr>
<td><code>fold</code></td>
<td><code>(t2 → t1 → t2) → t2 → [t1] → t2</code></td>
<td>Higher-order function that returns a single value after repeatedly applying a function to an input list [t1] and accumulating results in a value of type t2 (initialized in main second argument). Return value could be a list (e.g. in the case of dedupe) or an int (e.g. in the case of cumulative sum). The first input value to the input function is the value of type t1 at a given index in the list, and the second value is the accumulator of type t2. The accumulator t2 is returned after processing all elements in the input list [t1].</td>
</tr>
<tr>
<td><code>foldi</code></td>
<td><code>(int → t2 → t1 → t2) → t2 → [t1] → t2</code></td>
<td>Same as fold except the input function is passed the index, item, and accumulator for each value in the list. The first input value to the input function is the index, the second is the value at a given index in the list, and the last value is the accumulator.</td>
</tr>
<tr>
<td><code>group</code></td>
<td><code>(t1 → t2) → [t1] → [[t1]]</code></td>
<td>Higher-order function that takes an input list and returns a list of lists grouped by an input function of type (t1 → t2).</td>
</tr>
<tr>
<td><code>first</code></td>
<td><code>[t1] → t1</code></td>
<td>Returns the first element (head) of a list.</td>
</tr>
<tr>
<td><code>if</code></td>
<td><code>bool → t2 → t2 → t2</code></td>
<td>standard conditional</td>
</tr>
<tr>
<td><code>insert</code></td>
<td><code>t1 → int → [t1] → [t1]</code></td>
<td>Insert a value (first argument) into a list (third argument) at a given index (second argument), returning the list with the inserted value.</td>
</tr>
<tr>
<td><code>is_even</code></td>
<td><code>int → bool</code></td>
<td>Predicate that checks if an integer is even.</td>
</tr>
<tr>
<td><code>is_in</code></td>
<td><code>t1 → [t1] → bool</code></td>
<td>Returns whether or not the integer exists in a list.</td>
</tr>
<tr>
<td><code>is_odd</code></td>
<td><code>int → bool</code></td>
<td>Predicate that checks if an integer is odd.</td>
</tr>
<tr>
<td><code>last</code></td>
<td><code>[t1] → t1</code></td>
<td>Returns the last element of a list.</td>
</tr>
<tr>
<td><code>length</code></td>
<td><code>[t1] → int</code></td>
<td>Returns the length of a list.</td>
</tr>
<tr>
<td><code>map</code></td>
<td><code>(t1 → t2) → [t1] → [t2]</code></td>
<td>Higher-order function that applies an input function (t1 → t2) to each value of type t1 in a list [t1], e.g. (map is_even [0,1,2]).</td>
</tr>
<tr>
<td><code>mapi</code></td>
<td><code>(int → t1 → t2) → [t1] → [t2]</code></td>
<td>Same as map except the input function is also passed the index in addition to the value for each value in the input list of type [t1].</td>
</tr>
<td><code>max</code></td>
<td><code>[int] → int</code></td>
<td>Returns the maximum value of the list.</td>
</tr>
<tr>
<td><code>min</code></td>
<td><code>[int] → int</code></td>
<td>Returns the minimum value of the list.</td>
</tr>
<tr>
<td><code>not</code></td>
<td><code>bool → bool</code></td>
<td>Boolean NOT operator.</td>
</tr>
<tr>
<td><code>nth</code></td>
<td><code>int → [t1] → t1</code></td>
<td>Returns the nth value in a list.</td>
</tr>
<tr>
<td><code>or</code></td>
<td><code>bool → bool → bool</code></td>
<td>Boolean OR operator.</td>
</tr>
<tr>
<td><code>product</code></td>
<td><code>[int] → int</code></td>
<td>Returns the product of all integers in a list.</td>
</tr>
<tr>
<td><code>range</code></td>
<td><code>int → int → int → [int]</code></td>
<td>Range takes a start position, end position, and step value. The returned range is inclusive with respect to the start and end position, and each value in the returned list differs by the step value.</td>
</tr>
<tr>
<td><code>repeat</code></td>
<td><code>t1 → int → [t1]</code></td>
<td>Returns a list of an input value repeated N times. First argument is the input value to repeat, and second argument is number of times to repeat.</td>
</tr>
<tr>
<td><code>replace</code></td>
<td><code>int → t1 → [t1] → [t1]</code></td>
<td>Replace a value in an input list, returning the list with replacements. First argument is the index of the value to replace, and the second argument is the value to replace it with.</td>
</tr>
<tr>
<td><code>reverse</code></td>
<td><code>[t1] → [t1]</code></td>
<td>Reverses the list.</td>
</tr>
<tr>
<td><code>second</code></td>
<td><code>[t1] → t1</code></td>
<td>Returns the second element of a list.</td>
</tr>
<tr>
<td><code>singleton</code></td>
<td><code>t1 → [t1]</code></td>
<td>Returns the input argument as a list. (e.g. 7 → [7], 3 → [3]). This is useful in cases where a function would otherwise return a single value instead of a list, because the sampled concepts need to have type [int] → [int].</td>
</tr>
<tr>
<td><code>slice</code></td>
<td><code>int → int → [t1] → [t1]</code></td>
<td><p>Returns all values between two indices (values for indices above or equal to first index and below second index) within a list as a new list.</p>
<p>slice([1,2,3,4], 1, 3) = [2,3]</p></td>
</tr>
<tr>
<td><code>sort</code></td>
<td><code>[int] → [int]</code></td>
<td>Sorts a list of integers in ascending order.</td>
</tr>
<tr>
<td><code>splice</code></td>
<td><code>[t1] → int → [t1] → [t1]</code></td>
<td>Insert a list (first argument) into another list (third argument) at a given index (second argument).</td>
</tr>
<tr>
<td><code>sum</code></td>
<td><code>[int] → int</code></td>
<td>Returns the sum of all integers in a list.</td>
</tr>
<tr>
<td><code>swap</code></td>
<td><code>int → int → [t1] → [t1]</code></td>
<td>Given two indices and a list, return the list with the elements at those two indices swapped.</td>
</tr>
<tr>
<td><code>take</code></td>
<td><code>int → [t1] → [t1]</code></td>
<td>Takes the first N values in an input list, dropping the rest.</td>
</tr>
<tr>
<td><code>takelast</code></td>
<td><code>int → [t1] → [t1]</code></td>
<td>Takes the last N values in an input list, dropping the rest.</td>
</tr>
<tr>
<td><code>third</code></td>
<td><code>[t1] → t1</code></td>
<td>Returns the third element of a list.</td>
</tr>
<tr>
<td><code>unique</code></td>
<td><code>[t1] → [t1]</code></td>
<td>Removes duplicates in the list, returning a list of unique values in the same order.</td>
</tr>
<tr>
<td><code>zip</code></td>
<td><code>[t1] → [t1] → [[t1]]</code></td>
<td>Returns a list of pairs (list of lists of values) where an element at index N of the returned list is the pair of each element at index N of two input lists.</td>
</tr>
</tbody>
</table>

*Table 1.1 - Function Definitions*

## Lambdas

lambda returns an anonymous function that runs an input expression when called. For example, lambda functions can be passed as input functions to count, map, filter, and fold. The $-prefixed integers (e.g. `$0`, `$1`, … `$n`) represent [De Bruijn indices](https://en.wikipedia.org/wiki/De_Bruijn_index), where the index then refers to how many variable bindings you are from the variable you're referring to. For instance, `K x y = x` would be written as `(lambda (lambda $1))`.

Some more examples of Lambda functions can be seen below:

| **Example**                     | **Type Signature**  | **Description**                                                 |
| ------------------------------- | ------------------- | --------------------------------------------------------------- |
| `(lambda 5)`                     | `(t1 → int)`         | Returns 5.                                                      |
| `(lambda (+ $0 1))`              | `(int → int)`        | Increments an input value by 1.                                 |
| `(lambda (\> $0 0))`             | `(int → int)`        | Returns whether or not the input value is greater than 0.       |
| `(lambda (index 5 $0))`          | `(\[t1\] → t1)`      | Returns the 6th value (due to 0-indexing) in an input list.     |
| `(lambda (lambda (index $1 $0)))` | `(int → \[t1\] → t1)` | Returns the *N-1*th value of an input list for input value *N*. |

*Table 1.2 - Lambda Examples*

## Ideas for the Future

- more sophisticated `replace` (`(int -> t1 -> bool) -> [t1] -> [t1] -> [t1]`)
- add `windows` and `chunks`
- add `tail` (i.e. `(drop 1 xs)`) and `init` (i.e. `(droplast 1 xs)`)
- add `is_empty`, `any`, and `all`
- add `unfold`
- review existing list libraries for ideas
    - [`dash.el`](https://github.com/magnars/dash.el)
    - [`rnrs lists`](https://www.gnu.org/software/guile/docs/master/guile.html/rnrs-lists.html)
    - [`rnrs base`](https://www.gnu.org/software/guile/docs/master/guile.html/rnrs-base.html#rnrs-base)
    - [Racket pairs & lists](https://docs.racket-lang.org/reference/pairs.html)
    - [`underscore.js`](http://underscorejs.org/)
    - [`underscore-contrib`](http://documentcloud.github.io/underscore-contrib/)
    - [`std::Vec`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html)
    - [`std::iter::Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html)
    - [`itertools::Itertool`](https://docs.rs/itertools/0.8.0/itertools/trait.Itertools.html)
    - [`Data.List`](http://hackage.haskell.org/package/base-4.9.0.0/docs/Data-List.html)
