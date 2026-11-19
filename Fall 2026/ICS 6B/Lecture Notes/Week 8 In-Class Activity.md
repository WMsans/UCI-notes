Group Members:
1. Jeremy Zhao
2. Vincent Chen
3. Armando Martinez

# Problem 1
## Solution
a)
Reflective: True
Anti-symmetric: False
Thus not partial order

b)
Reflective: True
Anti-symmetric: True
Transitive: True
Thus partial order.

c)
Reflective: True
Anti-symmetric: True
Transitive: True
Thus partial order.

d)
Reflective: True
Anti-symmetric: True
Transitive: False
Thus not partial order.

# Problem 2
## Solution
I would first construct a relationship by multiplying the matrices to find the adjacency matrix  $R = G^3 \circ G^4 \circ G^4$, then see if $A_1$ and $A_7$ has relationship in $R$ by seeing row 1, column 7 of the resulting matrix. 

# Problem 3
## Solution
Prerequisite edges (prerequisite $\to$ course):

$F\to B,\ F\to H,\ G\to E,\ H\to E,\ E\to D,\ B\to C,\ D\to C,\ C\to A$

The longest chain is $F\to H\to E\to D\to C\to A$, which has $6$ courses, so no schedule can finish in fewer than $6$ quarters.

The schedule:

- Quarter 1: $F, G$ (no prerequisites)
- Quarter 2: $B, H$ (need only $F$)
- Quarter 3: $E$ (needs $G, H$)
- Quarter 4: $D$ (needs $E$)
- Quarter 5: $C$ (needs $B, D$)
- Quarter 6: $A$ (needs $C$)

Additional requirement: $A$ is a prerequisite for $E$

Now the requirements force $E \to D \to C \to A$ and also $A \to E$, so there is a cycle $E \to D \to C \to A \to E$.

A cycle in the prerequisite graph means the DAG no longer exists, so there is no schedule at all under the additional requirement.

# Problem 4
## Solution
Let $(a,b)R(c,d)$ mean $a\equiv c \pmod 3$ and $b\equiv d \pmod 3$.

Reflexive: for any $(a,b)$, $a\equiv a$ and $b\equiv b \pmod 3$, so $(a,b)R(a,b)$.

Symmetric: if $a\equiv c$ and $b\equiv d \pmod 3$, then $c\equiv a$ and $d\equiv b \pmod 3$, so $(c,d)R(a,b)$.

Transitive: if $a\equiv c$, $c\equiv e$, $b\equiv d$, $d\equiv f \pmod 3$, then $a\equiv e$ and $b\equiv f \pmod 3$ by transitivity of congruence, so $(a,b)R(e,f)$.

Thus $R$ is an equivalence relation.

An equivalence class is fixed by the pair of remainders $(r_1,r_2)$ of $(a,b) \bmod 3$, with $r_1,r_2 \in \{0,1,2\}$. There are $3\cdot 3=9$ such pairs, so there are $9$ classes:

- $[0,0] = \{(a,b) : a\equiv 0,\ b\equiv 0 \pmod 3\}$
- $[0,1]$: $a\equiv 0$, $b\equiv 1$
- $[0,2]$: $a\equiv 0$, $b\equiv 2$
- $[1,0]$: $a\equiv 1$, $b\equiv 0$
- $[1,1]$: $a\equiv 1$, $b\equiv 1$
- $[1,2]$: $a\equiv 1$, $b\equiv 2$
- $[2,0]$: $a\equiv 2$, $b\equiv 0$
- $[2,1]$: $a\equiv 2$, $b\equiv 1$
- $[2,2]$: $a\equiv 2$, $b\equiv 2$

Thus $9$ classes.
