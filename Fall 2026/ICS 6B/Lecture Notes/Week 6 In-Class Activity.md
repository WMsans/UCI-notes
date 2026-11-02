Group Members:
1. Jeremy Zhao
2. Vincent Chen
3. Armando Martinez

# Problem 1
## Solution
The last product contains $\overline{w}\cdot w=0$, so that whole term is always $0$.

Thus:
$$g=\overline{x}\overline{y}z t w q+\overline{x}y z t w\overline{q}$$
Each product term is true for exactly one assignment:

- $\overline{x}\overline{y}z t w q=1$: 1 row
- $\overline{x}y z t w\overline{q}=1$: 1 row

So $g=1$ for $2$ rows. With $6$ variables, there are $2^6=64$ total rows.

Therefore, the answer is $64 -2 = 2$

# Problem 2
## Solution
A, B, and C.
Let $M = Monkey$ and $D = Dolphin$

**A**: gives pure $M,D$ formulas for $xy$ and $\bar x$. Since ${AND, NOT}$ is functionally complete, ${M,D}$ is complete.

**B**: gives pure $M,D$ formulas for $x+y$ and $\bar x$. Since ${OR, NOT}$ is functionally complete, ${M,D}$ is complete.

**C**: gives a pure $M,D$ formula for $x↑y$ (NAND). Since ${NAND}$ alone is functionally complete, ${M,D}$ is complete.

**D**: gives only $AND$ and $OR$, and ${AND, OR}$ is not functionally complete.

**E**: expresses $M,D$ in terms of NAND, which is the reverse direction. That does not prove NAND can be built from $M,D$.

**F**: expresses $M,D$ using standard gates, also the reverse direction.

**G**: the second line gives $\bar x$, but the first line   $$xy=(xMy)(xDy)$$ 
still uses ordinary $AND$ on the right side, so it is circular and does not give a pure $M,D$ expression for $AND$.

# Problem 3
## Solution
The rows with output $0$ are:

$(x,y,z)=(0,1,1)$ gives clause $(x \lor \bar y \lor \bar z)$
$(x,y,z)=(1,0,1)$ gives clause $(\bar x \lor y \lor \bar z)$
$(x,y,z)=(1,1,0)$ gives clause $(\bar x \lor \bar y \lor z)$

Therefore the CNF form is:

$f(x,y,z)=(x \lor \bar y \lor \bar z)(\bar x \lor y \lor \bar z)(\bar x \lor \bar y \lor z)$

# Problem 4
## Solution
A Boolean expression for the rules is:

$$E =
(F_1+F_2+F_3)(\overline{F_1}+\overline{F_2})(\overline{F_1}+\overline{F_3})(\overline{F_2}+\overline{F_3})
\cdot
(A_1+A_2+A_3)(\overline{A_1}+\overline{A_2})(\overline{A_1}+\overline{A_3})(\overline{A_2}+\overline{A_3})
\cdot
(G_1+G_2+G_3)(\overline{G_1}+\overline{G_2})(\overline{G_1}+\overline{G_3})(\overline{G_2}+\overline{G_3})
\cdot
(W_1+W_2+W_3)(\overline{W_1}+\overline{W_2})(\overline{W_1}+\overline{W_3})(\overline{W_2}+\overline{W_3})
\cdot
(\overline{F_1}+\overline{A_1})(\overline{F_2}+\overline{A_2})(\overline{F_3}+\overline{A_3})
\cdot
(\overline{G_1}+\overline{W_1})(\overline{G_2}+\overline{W_2})(\overline{G_3}+\overline{W_3})$$

