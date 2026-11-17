# 6.6.2
(a)
Edges: $1\to6$, $2\to1$, $3\to2$, $3\to4$, $4\to3$, $4\to5$, $5\to5$, $5\to6$, $6\to2$
$$A = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0 & 0 & 0 \end{bmatrix}$$

(b)
$$A^2 = \begin{bmatrix} 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 1 & 1 \\ 0 & 1 & 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$

(c)
$2, 4, 5, 6$
Row 4 of $A^2$ has nonzeros in columns 2, 4, 5, 6:
$4\to3\to2$, $4\to3\to4$, $4\to5\to5$, $4\to5\to6$

(d)
$1, 4, 5$
Column 2 of $A^2$ has nonzeros in rows 1, 4, 5:
$1\to6\to2$, $4\to3\to2$, $5\to6\to2$

# 6.6.3
(a)
$2, 4, 5$

(b)
$5$

(c)
No.
$$A^4 = A^2\cdot A^2 = \begin{bmatrix} 0 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 1 & 0 \\ 1 & 1 & 2 & 0 & 1 \end{bmatrix}$$

(d)
Yes.

(e)
No.

(f)
Yes.

# 6.8.1 
(d)
Strict order. Not total.
Irreflexive: $x=3nx$ would need $n=\tfrac13$, which is not a positive integer, so no $x$ relates to itself.
Transitive: if $y=3nx$ and $z=3my$, then $z=3(3mn)x$ and $3mn$ is a positive integer.
Not total: 1 and 2 are incomparable ($2\ne3n\cdot1$ and $1\ne3n\cdot2$), so not every pair is related.

(j)
Neither. 
Reflexive ($|X|\le|X|$), so it is not a strict order
Not Antisymmetric (e.g. $\{a\}\ne\{b\}$ but $|\{a\}|\le|\{b\}|$ and $|\{b\}|\le|\{a\}|$), so it is not a partial order.

# 6.8.3
(a)
10 quarters:
1. Math 2A
2. Math 6A
3. CS 10
4. CS 11
5. Math 2B
6. CS 12
7. CS 160
8. CS 51
9. CS 181
10. CS 101

(b)
5 quarters:
1. CS 10, Math 2A
2. CS 11, Math 6A
3. CS 12, Math 2B
4. CS 51, CS 160
5. CS 181, CS 101

(c)
5 quarters:
1. CS 10, Math 2A, Math 6A
2. CS 11, Math 2B
3. CS 12
4. CS 101, CS 160, CS 51
5. CS 181

(d)
5 quarters. It is the length of the longest chain, since every course on that chain must be taken in a different quarter. 


# 6.8.4
b, c

(b)
Acyclic.
Transitive closure:
$$\{(d,a),(d,c),(d,f),(d,e),(d,b),(a,c),(a,e),(a,f),(a,b),(c,e),(c,f),(c,b),(f,e),(f,b)\}$$

(c)
Acyclic.
Transitive closure:
$$\{(e,f),(e,c),(e,a),(e,d),(e,b),(f,c),(f,a),(f,d),(f,b),(c,d),(c,a),(c,b),(b,d),(b,a)\}$$

# 6.9.4
(a)
No. It is reflexive (swapping two positions holding the same bit leaves $x$ unchanged) and symmetric (a swap is its own inverse), but not transitive: $100000\,R\,010000$ and $010000\,R\,001000$, yet $100000$ and $001000$ differ in three positions. 

(b)
Yes. It is reflexive (reorder by the identity), symmetric (undo the reordering with the inverse permutation) and transitive (reorder by the composition of the two permutations). The classes are the strings with the same number of 1s: 7 classes, of sizes $1,6,15,20,15,6,1$.


# 6.9.1 
(a)
No, not an equivalence relation. It is reflexive (anyone shares a parent with themself) and symmetric (sharing a parent is mutual), but not transitive. Two people can have the same father and different mothers, and the second can share a mother with a third while their fathers differ, so the first and third share no parent. Thus it is not an equivalence relation.

(d)
Yes, an equivalence relation. 
Reflexive: $x+x=2x$ is even. 
Symmetric: $x+y=y+x$. 
Transitive: if $x+y=2k$ and $y+z=2m$, then $x+z=(2k-y)+(2m-y)=2(k+m-y)$ is even. 

# 6.9.2
(a)
Remainders mod 4: $44,56,4\equiv0$; $13,17\equiv1$; $2,34\equiv2$; $7,99,31\equiv3$.
$$\{\{44,56,4\},\ \{13,17\},\ \{2,34\},\ \{7,99,31\}\}$$
