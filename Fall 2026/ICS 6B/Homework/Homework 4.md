# 3.1.2
(a)
False. A subset must be a set, and $15$ is an integer, not a set. So the statement is not even well formed.

(b) 
True. Since $15$ is an integer multiple of $3$ ($15 = 3 * 5$), $15 \in A$, therefore $\{15\} \subseteq A$. Since $A$ has many other elements, such as $3$, the subset is proper.

(c) 
True. The empty set is a subset of every set, and $C \neq \emptyset$, so the subset is proper.

(d) 
True. A set is a subset of itself, by reflexivity of $\subseteq$.

(e) 
False. $B$ only contains integers, and $\emptyset$ is not an integer. Note that $0 \in B$ instead, since $0 = 0^2$.

(f) 
True. For every $n \in \mathbb{Z}$, $3n$ is a multiple of $3$, so $3n \in A$, which gives infinitely many elements.

(g) 
False. $B = \{\ldots, -4, -1, 0, 1, 4, 9, 16, 25, \ldots\}$, so $B$ is infinite.

(h) 
True. $E = \{3, 6, 9\}$ has the three elements $3$, $6$ and $9$.

(i) 
True. $|F| = 3$ because $F = \{4, 6, 16\}$, and $|E| = 3$ from (h).

# 3.1.5
(a) 

$$\{x \in \mathbb{Z} : -2 \leq x \leq 2\}$$

The set is finite.  $|S| = 5$.

(c) 

$$\{x \in \mathbb{Z} : -3 \leq x \leq 9 \land x \text{ is odd}\}$$

The set is finite. $|S| = 7$.

# 3.2.1
(d) $3 \in X$
False. 

(f) $\{1, 2\} \subseteq X$
True. 

(i) $\{2, 3\} \subseteq X$
False. 

# 3.3.4
(c) 

$$\{\emptyset, \{b\}\}$$

Only $\emptyset$ and $\{b\}$ are subsets of both $A$ and $B$.

(d) 

$$\{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{b, c\}\}$$ 

# 3.4.4
(e)
True. $A \cap B = \emptyset$, so the symmetric difference $A \oplus B = (A \cup B) - (A \cap B) = A \cup B$.

(h)
True. Since $0 \in C$, $\{0\} \in P(C)$, so $\{0\}$ is an element of $P(C)$.

# 3.5.2
(a)

$$(\overline{A} \cap C) \cup (A \cap C)$$

$$(\overline{A} \cup A) \cap C \quad \text{(Distributive Law)}$$

$$U \cap C \quad \text{(Complement Law)}$$

$$C \quad \text{(Identity Law)}$$ 

# 3.6.7
(e)

$$C \times B = \{ab, cb, db\}$$ and $$B \times C = \{ba, bb, bc\}$$
No element appears in both.

$$\{\}$$

(f)

$$A \times B = \{ab, cb\}$$

A set with two elements has $2^2 = 4$ subsets

$$\{\emptyset, \{ab\}, \{cb\}, \{ab, cb\}\}$$ 

# 3.7.3
(b)
Yes. $A$, $B$ and $D$ partition $\mathbb{R}$. Since $$A \cup B \cup D = \mathbb{R}$$ and $$A \cap B = A \cap D = B \cap D = \emptyset$$
both conditions of a partition are satisfied. 

# 3.7.4
(a)
Yes. Let $S$ be the set of currently enrolled students. Every student has a unique ID number, so each student is in exactly one $A_i$:  $$A_i \cap A_j = \emptyset \quad \text{for } i \neq j$$
Also every student's ID begins with one of the digits 0 through 9: $$A_0 \cup A_1 \cup \cdots \cup A_9 = S$$
Both conditions of a partition are satisfied. 

