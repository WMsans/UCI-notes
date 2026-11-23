Group Members:
1. Jeremy Zhao
2. Vincent Chen
3. Armando Martinez

# Problem 1
## Solution
1. Anti-reflexive
	1. aRa is never true since a set A cannot  $A \subset A$. 
2. Anti-symmetric
	1. Since if $A \subset B$, B cannot be the subset of A due to the extra elements that B has. 
3. Transitive
	1. If $A \subset B$ and $B \subset C$, then every element of $A$ is in $B$, hence in $C$, and $C$ has an element not in $B$, hence not in $A$. So $A \subset C$.

### What if we replace $\subset$ with $\subseteq$?

1. Reflexive
	1. $A \subseteq A$ always holds, so the relation is reflexive (and no longer anti-reflexive, since every set relates to itself).
2. Anti-symmetric
	1. If $A \subseteq B$ and $B \subseteq A$, then $A = B$.
3. Transitive
	1. If $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.

# Problem 2
## Solution

### $S \circ P$

$(a,c) \in S \circ P$ iff there is some $b$ with $(a,b) \in P$ and $(b,c) \in S$

Siblings share parents, so $a$ is a parent of $c$ as well. Conversely, if $a$ is a parent of $c$ and $c$ has a sibling $b$, then $a$ is a parent of $b$ and $b$ is a sibling of $c$. So:

$$S \circ P = P$$

### $P \circ S$

$(a,c) \in P \circ S$ iff there is some $b$ with $(a,b) \in S$ and $(b,c) \in P$, i.e. $a$ is a sibling of $b$ and $b$ is a parent of $c$. So $a$ is a sibling of a parent of $c$:

$$P \circ S = \text{the aunt/uncle relation}$$

# Problem 3
## Solution
$(x,z) \in R_i \circ R_j$ iff there is some $y$ with $(x,y) \in R_j$ and $(y,z) \in R_i$.

### (a) $R_4 \circ R_1$

Need $y$ with $x \le y$ and $y = z$, i.e. $x \le z$.

$$R_4 \circ R_1 = \{(x,y): x \le y\} = R_1$$

### (b) $R_1 \circ R_2$

Need $y$ with $x > y$ and $y \le z$. Taking any $y < \min(x,z)$ works for every pair $(x,z)$, and the choice of $y$ is always possible because $\mathbb{R}$ is unbounded below.

$$R_1 \circ R_2 = \mathbb{R} \times \mathbb{R}$$

# Problem 4
## Solution
The table is a **directed graph**. $A$ knowing $B$'s number says nothing about $B$ knowing $A$'s. Let the vertices be the employees and put an edge $A \to B$ when $A$ knows $B$'s number. Since notification spreads transitively, the group that shows up is the **reachability set**.

$$\mathrm{Reach}(r) = \{r\} \cup \{v : \text{there is a directed path } r \to \cdots \to v\}$$

which is the transitive closure of the edge relation, applied to $r$.

1. Build the adjacency matrix $M$ ($M_{AB} = 1$ iff $A$ knows $B$'s number).
2. Compute reachability from every vertex: run BFS/DFS once per vertex.
3. If some $r$ has $|\mathrm{Reach}(r)| = n$, call $r$; everyone gets notified.
4. Otherwise call the $r$ with $|\mathrm{Reach}(r)|$ as large as possible (break ties arbitrarily). That guarantees the largest possible group.
