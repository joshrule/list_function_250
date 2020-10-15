# The List Function 250

Below is the list of functions composing the List Function 250 benchmark. Inputs and outputs are assumed to be `[int]` with 0 to 10 elements of values 0 to 9 or 9 to 99 depending on the problem (i.e. each concept is `[int] → [int]`).

For each function, there are 5 unique orderings of a single set of 11 machine-generated examples. In the list below, each function links to a representative ordering. The rest can be found [here](./json).

## Functions ([P1](#p1-11-%C2%B7-12-%C2%B7-13-%C2%B7-14) &middot; [P2](#p2) &middot; [P3](#p3))

The functions can be broken into three subsets, P1, P2, and P3, that provide a total of 250 functions to learn.

### P1 ([1.1](#p11-5-tuples) &middot; [1.2](#p12-4-tuples) &middot; [1.3](#p13-non-recursive-problems) &middot; [1.4](#p14-recursive-problems))

P1 contains 80 problems and can itself be divided into 4 groups of 20 functions.

#### P1.1 5-tuples

P1.1 is organized as 4 5-tuples. Each tuple contains 5 variants of the same problem:
- non-recursive, early in the list
  *return the third item*
- non-recursive, early in the list, with exceptional data
  *return the third item, or the empty list if the input has fewer than 3 elements*
- non-recursive, late in the list
  *return the seventh item*
- non-recursive, late in the list, with exceptional data
  *return the seventh item, or the empty list if the input has fewer than 7 elements*
- recursive, without exceptions
  *return the firsth item in the tail*

001. [`(lambda (singleton (third $0)))`](json/c001_1.json)
002. [`(lambda (if (> 3 (length $0)) empty (singleton (third $0))))`](json/c002_1.json)
003. [`(lambda (singleton (nth 7 $0)))`](json/c003_1.json)
004. [`(lambda (if (> 7 (length $0)) empty (singleton (nth 7 $0))))`](json/c004_1.json)
005. [`(lambda (singleton (nth (first $0) (drop 1 $0))))`](json/c005_1.json)
006. [`(lambda (take 2 $0))`](json/c006_1.json)
007. [`(lambda (take 2 $0))`](json/c007_1.json)
008. [`(lambda (take 6 $0))`](json/c008_1.json)
009. [`(lambda (take 6 $0))`](json/c009_1.json)
010. [`(lambda (take (first $0) (drop 1 $0)))`](json/c010_1.json)
011. [`(lambda (slice 2 4 $0))`](json/c011_1.json)
012. [`(lambda (slice 2 4 $0))`](json/c012_1.json)
013. [`(lambda (slice 3 7 $0))`](json/c013_1.json)
014. [`(lambda (slice 3 7 $0))`](json/c014_1.json)
015. [`(lambda (slice (first $0) (second $0) (drop 2 $0)))`](json/c015_1.json)
016. [`(lambda (replace 2 8 $0))`](json/c016_1.json)
017. [`(lambda (replace 2 8 $0))`](json/c017_1.json)
018. [`(lambda (replace 6 3 $0))`](json/c018_1.json)
019. [`(lambda (replace 6 3 $0))`](json/c019_1.json)
020. [`(lambda (replace 1 (last $0) $0))`](json/c020_1.json)

#### P1.2 4-tuples

P1.2 is organized as 5 4-tuples. Each tuple contains 4 problems:

- 2 simple rules
  *insert 8 as the second element*
  *insert 5 as the second element*
- a conditional form based on the list structure (e.g. length, element equality)
  *insert 8 as the second element if the list length is less than 5, else 5*
- a conditional form based on elements in the list as numbers (e.g. numerical equalities)
  *insert 8 as the second element if the first element is less than 5, else 5*

021. [`(lambda (insert 8 2 $0))`](json/c021_1.json)
022. [`(lambda (insert 5 2 $0))`](json/c022_1.json)
023. [`(lambda (insert (if (> 5 (length $0)) 8 5) 2 $0))`](json/c023_1.json)
024. [`(lambda (insert (if (> 5 (first $0)) 8 5) 2 $0))`](json/c024_1.json)
025. [`(lambda (cut_idx 2 $0))`](json/c025_1.json)
026. [`(lambda (cut_idx 3 $0))`](json/c026_1.json)
027. [`(lambda (cut_idx (if (== (first $0) (second $0)) 2 3) $0))`](json/c027_1.json)
028. [`(lambda (cut_idx (if (> (first $0) (second $0)) 2 3) $0))`](json/c028_1.json)
029. [`(lambda (drop 2 $0))`](json/c029_1.json)
030. [`(lambda (droplast 2 $0))`](json/c030_1.json)
031. [`(lambda ((if (== (first $0) (second $0)) drop droplast) 2 $0))`](json/c031_1.json)
032. [`(lambda ((if (> (first $0) (last $0)) drop droplast) 2 $0))`](json/c032_1.json)
033. [`(lambda (swap 1 4 $0))`](json/c033_1.json)
034. [`(lambda (swap 2 3 $0))`](json/c034_1.json)
035. [`(lambda (if (== (second $0) (third $0)) (swap 1 4 $0) (swap 2 3 $0)))`](json/c035_1.json)
036. [`(lambda (if (> (second $0) (third $0)) (swap 2 3 $0) (swap 1 4 $0)))`](json/c036_1.json)
037. [`(lambda (append $0 3))`](json/c037_1.json)
038. [`(lambda (append $0 9))`](json/c038_1.json)
039. [`(lambda (if (== (length $0) 3) (append $0 3) (if (== (length $0) 9) (append $0 9) $0)))`](json/c039_1.json)
040. [`(lambda (if (is_in $0 3) (append $0 3) (if (is_in $0 9) (append $0 9) $0)))`](json/c040_1.json)

#### P1.3 non-recursive problems

P1.3 contains 20 problems which can all be solved without recursion given the DSL available to the models.

041. [`(lambda (singleton 9))`](json/c041_1.json)
042. [`(lambda (cons 5 (singleton 2)))`](json/c042_1.json)
043. [`(lambda (cons 8 (cons 2 (cons 7 (cons 0 (singleton 3))))))`](json/c043_1.json)
044. [`(lambda (cons 1 (cons 9 (cons 4 (cons 3 (cons 2 (cons 5 (cons 8 (cons 0 (cons 4 (singleton 9)))))))))))`](json/c044_1.json)
045. [`(lambda $0)`](json/c045_1.json)
046. [`(lambda (cons 7 $0))`](json/c046_1.json)
047. [`(lambda (cons 9 (cons 6 (cons 3 (cons 8 (cons 5 $0))))))`](json/c047_1.json)
048. [`(lambda (take 1 $0))`](json/c048_1.json)
049. [`(lambda (drop 1 $0))`](json/c049_1.json)
050. [`(lambda (cons (first $0) $0))`](json/c050_1.json)
051. [`(lambda (concat (repeat (first $0) 5) $0))`](json/c051_1.json)
052. [`(lambda (repeat (first $0) 10))`](json/c052_1.json)
053. [`(lambda (concat (repeat (first $0) 2) (drop 2 $0)))`](json/c053_1.json)
054. [`(lambda (concat (repeat (third $0) 3) (drop 3 $0)))`](json/c054_1.json)
055. [`(lambda (concat (slice 3 4 $0) (concat (take 2 $0) (drop 4 $0))))`](json/c055_1.json)
056. [`(lambda (cut_idx 5 $0))`](json/c056_1.json)
057. [`(lambda (insert 4 7 $0))`](json/c057_1.json)
058. [`(lambda (drop 7 $0))`](json/c058_1.json)
059. [`(lambda (swap 4 8 $0))`](json/c059_1.json)
060. [`(lambda (swap 3 1 (replace 4 4 (cut_idx 6 (take 7 $0)))))`](json/c060_1.json)

#### P1.4 recursive problems

P1.4 contains 20 problems which all require explicit recursion given the DSL available to the models.

061. [`(lambda (singleton (last $0)))`](json/c061_1.json)
062. [`(lambda (droplast 1 $0))`](json/c062_1.json)
063. [`(lambda (drop (first $0) (drop 1 $0)))`](json/c063_1.json)
064. [`(lambda (drop 1 (droplast 1 $0)))`](json/c064_1.json)
065. [`(lambda (cons 9 (append $0 7)))`](json/c065_1.json)
066. [`(lambda (append (drop 1 $0) (first $0)))`](json/c066_1.json)
067. [`(lambda (cons (last $0) (append (drop 1 (droplast 1 $0)) (first $0))))`](json/c067_1.json)
068. [`(lambda (concat $0 (cons 7 (cons 3 (cons 8 (cons 4 (singleton 3)))))))`](json/c068_1.json)
069. [`(lambda (concat (cons 9 (cons 3 (cons 4 (singleton 0)))) (concat $0 (cons 7 (cons 2 (cons 9 (singleton 1)))))))`](json/c069_1.json)
070. [`(lambda (concat $0 $0))`](json/c070_1.json)
071. [`(lambda (map (lambda (+ 2 $0)) $0))`](json/c071_1.json)
072. [`(lambda (flatten (map (lambda (cons $0 (singleton $0))) $0)))`](json/c072_1.json)
073. [`(lambda (mapi + $0))`](json/c073_1.json)
074. [`(lambda (filter (lambda (> $0 7)) $0))`](json/c074_1.json)
075. [`(lambda (filteri (lambda (lambda (is_odd $1))) $0))`](json/c075_1.json)
076. [`(lambda (cons (max $0) (cons (last $0) (cons (length $0) (cons (first $0) (singleton (min $0)))))))`](json/c076_1.json)
077. [`(lambda (singleton (length $0)))`](json/c077_1.json)
078. [`(lambda (singleton (max $0)))`](json/c078_1.json)
079. [`(lambda (singleton (sum $0)))`](json/c079_1.json)
080. [`(lambda (reverse $0))`](json/c080_1.json)

### P2

P2 contains variants of these problems from each subset of P1, modified so that the examples, DSL, and any relevant constants include the numbers 0,1,...,99:

- P1.1: 1&ndash;5
- P1.2: 13&ndash;16
- P1.3: 3, 4, 7, 12, & 15
- P1.4: 4, 5, 9, 13, 14, & 20

081. [`(lambda (singleton (third $0)))`](json/c081_1.json)
082. [`(lambda (if (> 3 (length $0)) empty (singleton (third $0))))`](json/c082_1.json)
083. [`(lambda (singleton (nth 7 $0)))`](json/c083_1.json)
084. [`(lambda (if (> 7 (length $0)) empty (singleton (nth 7 $0))))`](json/c084_1.json)
085. [`(lambda (singleton (nth (first $0) (drop 1 $0))))`](json/c085_1.json)
086. [`(lambda (swap 1 4 $0))`](json/c086_1.json)
087. [`(lambda (swap 2 3 $0))`](json/c087_1.json)
088. [`(lambda (if (== (second $0) (third $0)) (swap 1 4 $0) (swap 2 3 $0)))`](json/c088_1.json)
089. [`(lambda (if (> (second $0) (third $0)) (swap 2 3 $0) (swap 1 4 $0)))`](json/c089_1.json)
090. [`(lambda (cons 18 (cons 42 (cons 77 (cons 20 (singleton 36))))))`](json/c090_1.json)
091. [`(lambda (cons 81 (cons 99 (cons 41 (cons 23 (cons 22 (cons 75 (cons 68 (cons 30 (cons 24 (singleton 69)))))))))))`](json/c091_1.json)
092. [`(lambda (cons 92 (cons 63 (cons 34 (cons 18 (cons 55 $0))))))`](json/c092_1.json)
093. [`(lambda (repeat (first $0) 10))`](json/c093_1.json)
094. [`(lambda (concat (slice 3 4 $0) (concat (take 2 $0) (drop 4 $0))))`](json/c094_1.json)
095. [`(lambda (drop 1 (droplast 1 $0)))`](json/c095_1.json)
096. [`(lambda (cons 98 (append $0 37)))`](json/c096_1.json)
097. [`(lambda (concat (cons 11 (cons 21 (cons 43 (singleton 19)))) (concat $0 (cons 7 (cons 89 (cons 0 (singleton 57)))))))`](json/c097_1.json)
098. [`(lambda (mapi + $0))`](json/c098_1.json)
099. [`(lambda (filter (lambda (> $0 49)) $0))`](json/c099_1.json)
100. [`(lambda (reverse $0))`](json/c100_1.json)

### P3

P3 provides an additional 150 problems where the examples, DSL, and any relevant constants include the numbers 0,1,...,99. These problems are, on average, slightly more difficult than those in P1 or P2:

101. [`(lambda (cons 11 (cons 19 (cons 24 (cons 33 (cons 42 (cons 5 (cons 82 (cons 0 (cons 64 (cons 9 empty)))))))))))`](json/c101_1.json)
102. [`(lambda $0)`](json/c102_1.json)
103. [`(lambda (singleton (length $0)))`](json/c103_1.json)
104. [`(lambda (singleton (max $0)))`](json/c104_1.json)
105. [`(lambda (splice (drop 1 (droplast 1 $0)) 2 $0))`](json/c105_1.json)
106. [`(lambda (sort (lambda $0) $0))`](json/c106_1.json)
107. [`(lambda (unique $0))`](json/c107_1.json)
108. [`(lambda (singleton (sum $0)))`](json/c108_1.json)
109. [`(lambda (singleton (product $0)))`](json/c109_1.json)
110. [`(lambda (takelast 3 (sort (lambda $0) $0)))`](json/c110_1.json)
111. [`(lambda (repeat (max $0) (min $0)))`](json/c111_1.json)
112. [`(lambda (range 1 1 (last $0)))`](json/c112_1.json)
113. [`(lambda (filter (lambda (> (first $1) (% $0 10))) $0))`](json/c113_1.json)
114. [`(lambda (cons (last $0) $0))`](json/c114_1.json)
115. [`(lambda (cons (sum (unique $0)) (append (unique $0) (sum (unique $0)))))`](json/c115_1.json)
116. [`(lambda (concat (reverse (drop 1 $0)) $0))`](json/c116_1.json)
117. [`(lambda (concat (drop 3 $0) (take 3 $0)))`](json/c117_1.json)
118. [`(lambda (concat (drop (last $0) $0) (take (last $0) $0)))`](json/c118_1.json)
119. [`(lambda ((lambda (concat ($0 first) (concat $1 ($0 last)))) (lambda (if (== ($0 $1) 8) empty (singleton 8)))))`](json/c119_1.json)
120. [`(lambda (singleton (first $0)))`](json/c120_1.json)
121. [`(lambda (singleton (last $0)))`](json/c121_1.json)
122. [`(lambda (singleton (second (reverse $0))))`](json/c122_1.json)
123. [`(lambda (singleton (nth (last $0) $0)))`](json/c123_1.json)
124. [`(lambda (singleton (nth (nth (first $0) $0) $0)))`](json/c124_1.json)
125. [`(lambda (filter (lambda (== (/ (first $1) 10) (/ $0 10))) $0))`](json/c125_1.json)
126. [`(lambda (drop 1 $0))`](json/c126_1.json)
127. [`(lambda (droplast 1 $0))`](json/c127_1.json)
128. [`(lambda (sort (lambda $0) (cut_idx 3 (drop 2 $0))))`](json/c128_1.json)
129. [`(lambda (slice (first $0) (second $0) (drop 2 $0)))`](json/c129_1.json)
130. [`(lambda (take (first $0) (drop 1 $0)))`](json/c130_1.json)
131. [`(lambda (filter (lambda (is_even (/ $0 10))) $0))`](json/c131_1.json)
132. [`(lambda (cut_idx 3 $0))`](json/c132_1.json)
133. [`(lambda (cut_slice 2 5 $0))`](json/c133_1.json)
134. [`(lambda (cut_slice (first $0) (second $0) $0))`](json/c134_1.json)
135. [`(lambda (cut_val 7 $0))`](json/c135_1.json)
136. [`(lambda (cut_val (max $0) $0))`](json/c136_1.json)
137. [`(lambda (cut_vals 3 $0))`](json/c137_1.json)
138. [`(lambda (cut_vals (first $0) $0))`](json/c138_1.json)
139. [`(lambda (cut_vals (max $0) (cut_vals (min $0) $0)))`](json/c139_1.json)
140. [`(lambda (replace 2 9 $0))`](json/c140_1.json)
141. [`(lambda (replace (first $0) (second $0) (drop 2 $0)))`](json/c141_1.json)
142. [`(lambda (flatten (map (lambda (cons (/ $0 10) (singleton (% $0 10)))) $0)))`](json/c142_1.json)
143. [`(lambda (map (lambda (if (== $0 (max $1)) (min $1) $0)) $0))`](json/c143_1.json)
144. [`(lambda (map (lambda (if (or (== $0 (max $1)) (== $0 (min $1))) (- (max $1) (min $1)) $0)) $0))`](json/c144_1.json)
145. [`(lambda (map (lambda (first $1)) $0))`](json/c145_1.json)
146. [`(lambda (map (lambda (- (max $0) (min $0))) (zip (droplast 1 $0) (drop 1 $0))))`](json/c146_1.json)
147. [`(lambda (flatten (mapi (lambda (lambda (cons $0 (singleton $1)))) $0)))`](json/c147_1.json)
148. [`(lambda (flatten (map (range 1 1) $0)))`](json/c148_1.json)
149. [`(lambda (map (lambda (* $0 (first $1))) (drop 1 $0)))`](json/c149_1.json)
150. [`(lambda (flatten (map (lambda (if (> $0 (first $1)) (range (first $1) 1 $0) (singleton $0))) $0)))`](json/c150_1.json)
151. [`(lambda (flatten (map (lambda (repeat $0 $0)) $0)))`](json/c151_1.json)
152. [`(lambda (map (lambda (* (/ $0 10) (% $0 10))) $0))`](json/c152_1.json)
153. [`(lambda (flatten (map (lambda (append (take 1 $0) (length $0))) (group (lambda $0) $0))))`](json/c153_1.json)
154. [`(lambda (map (lambda (if (is_even $0) (* 3 $0) $0)) $0))`](json/c154_1.json)
155. [`(lambda (mapi (lambda (lambda (* $0 $1))) $0))`](json/c155_1.json)
156. [`(lambda (mapi (lambda (lambda (+ $0 $1))) (reverse $0)))`](json/c156_1.json)
157. [`(lambda (flatten (map (lambda (cons $0 (singleton (% $0 2)))) $0)))`](json/c157_1.json)
158. [`(lambda (mapi (lambda (lambda (if (== $0 $1) 1 0))) $0))`](json/c158_1.json)
159. [`(lambda (map (lambda (count (lambda (== $1 $0)) $1)) (range 1 1 (max $0))))`](json/c159_1.json)
160. [`(lambda (map (lambda (- 99 $0)) $0))`](json/c160_1.json)
161. [`(lambda (mapi (lambda (lambda (+ $0 (- (length $2) $1)))) $0))`](json/c161_1.json)
162. [`(lambda (map (lambda (+ 7 (* 3 $0))) $0))`](json/c162_1.json)
163. [`(lambda (map (lambda (- (* $0 2) 10)) $0))`](json/c163_1.json)
164. [`(lambda (map (lambda (+ (/ $0 4) 5)) $0))`](json/c164_1.json)
165. [`(lambda (filter is_even (reverse $0)))`](json/c165_1.json)
166. [`(lambda (sort (lambda (+ (% $0 10) (/ $0 10))) (unique $0)))`](json/c166_1.json)
167. [`(lambda (filter (lambda (== (% $0 3) 0)) $0))`](json/c167_1.json)
168. [`(lambda (cut_val (length $0) (range 1 1 10)))`](json/c168_1.json)
169. [`(lambda (singleton (max (cut_vals (max $0) $0))))`](json/c169_1.json)
170. [`(lambda (cons (first $0) (singleton (last $0))))`](json/c170_1.json)
171. [`(lambda (drop 1 (fold (lambda (lambda (append $1 (+ (last $1) $0)))) (singleton 0) $0)))`](json/c171_1.json)
172. [`(lambda (drop 1 (fold (lambda (lambda (append $1 (* (last $1) $0)))) (singleton 1) $0)))`](json/c172_1.json)
173. [`(lambda (mapi (lambda (lambda (max (take $1 $2)))) $0))`](json/c173_1.json)
174. [`(lambda (take (length (unique $0)) $0))`](json/c174_1.json)
175. [`(lambda (fold (lambda (lambda (if (> $0 (last $1)) (append $1 $0) $1))) (take 1 $0) (drop 1 $0)))`](json/c175_1.json)
176. [`(lambda (map (lambda (sum $0)) (zip (droplast 1 $0) (drop 1 $0))))`](json/c176_1.json)
177. [`(lambda (flatten (zip $0 (reverse $0))))`](json/c177_1.json)
178. [`(lambda (map first (filter (lambda (is_even (second $0))) (zip (droplast 1 $0) (drop 1 $0)))))`](json/c178_1.json)
179. [`(lambda (fold (lambda (lambda (append (reverse $1) $0))) empty (reverse (sort (lambda $0) $0))))`](json/c179_1.json)
180. [`(lambda (fold (lambda (lambda (append (reverse $1) $0))) empty (sort (lambda $0) $0)))`](json/c180_1.json)
181. [`(lambda (flatten (zip (filteri (lambda (lambda (is_odd $1))) $0) (reverse (filteri (lambda (lambda (is_even $1))) $0)))))`](json/c181_1.json)
182. [`(lambda (filteri (lambda (lambda (== (% $1 3) 0))) $0))`](json/c182_1.json)
183. [`(lambda (find (== (first $0)) (drop 1 $0)))`](json/c183_1.json)
184. [`(lambda (filteri (lambda (lambda (and (is_even $1) (is_odd $0)))) $0))`](json/c184_1.json)
185. [`(lambda (cons (first $0) (cons (sum (drop 1 (droplast 1 $0))) (takelast 1 $0))))`](json/c185_1.json)
186. [`(lambda (filter (lambda (> $0 (first $1))) $0))`](json/c186_1.json)
187. [`(lambda (concat $0 (cons 0 $0)))`](json/c187_1.json)
188. [`(lambda (map (lambda (if (== (% $0 3) 0) 1 0)) $0))`](json/c188_1.json)
189. [`(lambda (range (min $0) 1 (max $0)))`](json/c189_1.json)
190. [`(lambda (range (first $0) 2 (last $0)))`](json/c190_1.json)
191. [`(lambda (flatten (map (lambda (repeat $0 (/ $0 10))) $0)))`](json/c191_1.json)
192. [`(lambda (map (lambda (/ $0 10)) $0))`](json/c192_1.json)
193. [`(lambda (drop 1 (droplast 1 (sort (lambda $0) $0))))`](json/c193_1.json)
194. [`(lambda (cons (length $0) (append (reverse $0) (length $0))))`](json/c194_1.json)
195. [`(lambda (cons (first $0) (cons 23 (cons 68 (cons 42 (cons 99 (cons 71 (singleton (last $0)))))))))`](json/c195_1.json)
196. [`(lambda (concat (cons 17 (cons 38 (singleton 82))) (concat $0 (cons 1 (cons 55 (singleton 27))))))`](json/c196_1.json)
197. [`(lambda (map (lambda (count (== $0) $1)) $0))`](json/c197_1.json)
198. [`(lambda (reverse (sort (lambda $0) (unique $0))))`](json/c198_1.json)
199. [`(lambda (flatten (zip (range 1 1 (length $0)) (sort (lambda $0) $0))))`](json/c199_1.json)
200. [`(lambda (sort (lambda $0) (map (lambda (/ $0 10)) $0)))`](json/c200_1.json)
201. [`(lambda (concat (filter (lambda (< (first $1) $0)) $0) (filter (lambda (> (first $1) $0)) $0)))`](json/c201_1.json)
202. [`(lambda (find is_even $0))`](json/c202_1.json)
203. [`(lambda (mapi (lambda (lambda (* (min $2) $1))) $0))`](json/c203_1.json)
204. [`(lambda (map first (filter (lambda (== (second $0) 0)) (zip (droplast 1 $0) (drop 1 $0)))))`](json/c204_1.json)
205. [`(lambda (singleton (product (filter (lambda (== (% $0 4) 0)) $0))))`](json/c205_1.json)
206. [`(lambda (filter (lambda (and (> (max (take 2 $1)) $0) (> $0 (min (take 2 $1))))) $0))`](json/c206_1.json)
207. [`(lambda (map sum (zip $0 (reverse $0))))`](json/c207_1.json)
208. [`(lambda (takelast (last $0) $0))`](json/c208_1.json)
209. [`(lambda (insert (+ (max $0) (min $0)) 3 (sort (lambda $0) $0)))`](json/c209_1.json)
210. [`(lambda (insert (last $0) (first $0) (unique $0)))`](json/c210_1.json)
211. [`(lambda (splice (slice 4 5 $0) (- (length $0) 2) (reverse $0)))`](json/c211_1.json)
212. [`(lambda (splice (cons 3 (cons 3 (singleton 3))) 3 $0))`](json/c212_1.json)
213. [`(lambda (take 3 (sort (lambda $0) $0)))`](json/c213_1.json)
214. [`(lambda (cut_idx (first $0) (drop 1 $0)))`](json/c214_1.json)
215. [`(lambda (replace (first $0) (length $0) (drop 1 $0)))`](json/c215_1.json)
216. [`(lambda (sort (lambda (/ $0 10)) $0))`](json/c216_1.json)
217. [`(lambda (sort (lambda (% $0 10)) $0))`](json/c217_1.json)
218. [`(lambda (filter (lambda (== $0 (first $1))) (drop 1 $0)))`](json/c218_1.json)
219. [`(lambda (reverse (filteri (lambda (lambda (is_odd $1))) (reverse $0))))`](json/c219_1.json)
220. [`(lambda (map (lambda (* $0 (if (is_even (length $1)) 2 3))) $0))`](json/c220_1.json)
221. [`(lambda (singleton (sum (filter is_even $0))))`](json/c221_1.json)
222. [`(lambda (map (lambda (length $1)) $0))`](json/c222_1.json)
223. [`(lambda (map (lambda (+ (* (% $0 10) 10) (/ $0 10))) $0))`](json/c223_1.json)
224. [`(lambda (fold (lambda (lambda (cons $0 (reverse $1)))) empty $0))`](json/c224_1.json)
225. [`(lambda (drop 2 (droplast 2 $0)))`](json/c225_1.json)
226. [`(lambda (drop (first $0) (droplast (last $0) $0)))`](json/c226_1.json)
227. [`(lambda (unique (flatten (zip $0 (reverse $0)))))`](json/c227_1.json)
228. [`(lambda (mapi (lambda (lambda (count (== $0) (take $1 $2)))) $0))`](json/c228_1.json)
229. [`(lambda (take (first $0) (reverse $0)))`](json/c229_1.json)
230. [`(lambda (range (min $0) 2 (max $0)))`](json/c230_1.json)
231. [`(lambda (sort (lambda $0) (map length (group (lambda $0) $0))))`](json/c231_1.json)
232. [`(lambda (singleton (/ (sum $0) (length $0))))`](json/c232_1.json)
233. [`(lambda (map length (group (lambda $0) $0)))`](json/c233_1.json)
234. [`(lambda (flatten (map (lambda (drop 1 $0)) (group (lambda $0) $0))))`](json/c234_1.json)
235. [`(lambda (fold (lambda (lambda (concat $1 (drop 1 (range (last $1) (if (> $0 (last $1)) 1 -1) $0))))) (take 1 $0) (drop 1 $0)))`](json/c235_1.json)
236. [`(lambda (map (lambda (/ $0 2)) (filter is_even $0)))`](json/c236_1.json)
237. [`(lambda (fold (lambda (lambda (append $1 (+ (last $1) $0)))) (take 1 (unique $0)) (drop 1 (unique $0))))`](json/c237_1.json)
238. [`(lambda (filter (lambda (== 1 (count (== $0) $1))) $0))`](json/c238_1.json)
239. [`(lambda (singleton (- (length $0) (length (unique $0)))))`](json/c239_1.json)
240. [`(lambda (singleton (count (lambda ((== (length $1)) $0)) $0)))`](json/c240_1.json)
241. [`(lambda (singleton (count is_even $0)))`](json/c241_1.json)
242. [`(lambda (fold (lambda (lambda (append (reverse $1) $0))) empty (reverse (unique (sort (lambda $0) $0)))))`](json/c242_1.json)
243. [`(lambda (singleton (count is_odd $0)))`](json/c243_1.json)
244. [`(lambda (singleton (count (lambda (== 3 $0)) $0)))`](json/c244_1.json)
245. [`(lambda (singleton (count (lambda (== (first $1) $0)) (drop 1 $0))))`](json/c245_1.json)
246. [`(lambda (singleton (length (unique $0))))`](json/c246_1.json)
247. [`(lambda (first (reverse (fold (lambda (lambda (if (== $0 0) (cons empty $1) (cons (append (first $1) $0) (drop 1 $1))))) (singleton empty) $0))))`](json/c247_1.json)
248. [`(lambda (first (fold (lambda (lambda (if (== $0 0) (cons empty $1) (cons (append (first $1) $0) (drop 1 $1))))) (singleton empty) $0)))`](json/c248_1.json)
249. [`(lambda (map first (reverse (fold (lambda (lambda (if (== $0 0) (cons empty $1) (cons (append (first $1) $0) (drop 1 $1))))) (singleton empty) $0))))`](json/c249_1.json)
250. [`(lambda (flatten (map reverse (reverse (fold (lambda (lambda (if (== $0 0) (cons empty $1) (cons (append (first $1) $0) (drop 1 $1))))) (singleton empty) $0)))))`](json/c250_1.json)