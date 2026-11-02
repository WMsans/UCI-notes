# 5.1.2
(d)
$\overline{x\overline{y}+y\overline{z}+\overline{x}z}$
= $(\overline{x\overline{y}})(\overline{y\overline{z}})(\overline{\overline{x}z})$
= $(\overline{x} + y)(\overline{y} + z)(x + \overline{z})$

# 5.3.2 
(a)
DNF

(b)
Both

(c)
CNF

(g)
Neither

# 5.3.3
(d)
$(x + y\overline{z})(\overline{x} + y + \overline{z})$
= $x\overline{x} + xy + x\overline{z} + \overline{x}y\overline{z} + y\overline{z} + y\overline{z}$  (distributive)
= $xy + x\overline{z} + \overline{x}y\overline{z} + y\overline{z}$  (complement, idempotent)
= $xy + x\overline{z} + y\overline{z}$  (distributive, annulment)

# 5.4.1 
(b)
$f = \overline{x}\overline{y}z + xy\overline{z}$  (minterms $m_1 + m_6$)
Only multiplication and complement: $f = \overline{ \overline{\overline{x}\overline{y}z} \cdot \overline{xy\overline{z}} }$ 
Only addition and complement: $f = \overline{x + y + \overline{z}} + \overline{\overline{x} + \overline{y} + z}$ 

# 5.4.2
(a)
$f = x\overline{y} + \overline{x}y$  (XOR, minterms $m_1 + m_2$)
Only NAND: $f = \overline{ \overline{x\cdot\overline{xy}} \cdot \overline{y\cdot\overline{xy}} }$
Only NOR: $f = \overline{ \overline{x+y} + \overline{ \overline{x+x} + \overline{y+y} } }$

# 5.5.1
(a)
**Satisfied** when $x = True$, $y = False$, and $z = False$

(b)
**Satisfied** when $x = True$, $y = False$, and $z = False$

(c)
**Not satisfiable.**

| $x$ | $y$ | $z$ | $f(x,y,z)$ |
|-----|-----|-----|------------|
| False | False | False | False |
| False | False | True | False |
| False | True | False | False |
| False | True | True | False |
| True | False | False | False |
| True | False | True | False |
| True | True | False | False |
| True | True | True | False |

(d)
**Satisfied** when $x = True$, $y = False$, and $z = False$

# 5.6.4
(b)
$f = xy + xz + yz$

![[Pasted image 20261101165949.png]]

# 5.4.5 
(a)
We will construct {$+$, complement} which is functional complete.
Since the complement operation is in both sets, it is sufficient to show that $+$ can be computed using complement and $\rightarrow$. One of the conditional identities from the laws of propositional logic says that $x \rightarrow y$ is equivalent to $\overline{x} + y$. Therefore, $x + y$ is equivalent to $\overline{x} \rightarrow y$. Therefore, {complement, $\rightarrow$} is functional complete. 

# 5.5.5
(a)
$x_{A1} + x_{A2} + x_{A3}$  (1 iff A is in at least one period)

(b)
$\overline{x_{A1}x_{A2} + x_{A1}x_{A3} + x_{A2}x_{A3}}$  (1 iff A is in at most one period)

(c)
$\overline{x_{A1}x_{B1}} \cdot \overline{x_{A2}x_{B2}} \cdot \overline{x_{A3}x_{B3}}$  (1 iff A and B not in same period)

(d)
$4n + 3m$ terms: $n$ at-least-one clauses (1 per class) + $3n$ at-most-one clauses (3 pairwise clauses per class) + $3m$ incompatibility clauses (3 periods per forbidden pair)

# 5.6.3
(d) List the the law you apply. Please don't forget to draw the simplified circuit

$F(x,y) = \overline{\bar{x} \cdot \bar{y}} + \overline{y + \bar{y}}$
= $\overline{\bar{x} \cdot \bar{y}} + \overline{1}$ (Complement Law)
= $\overline{\bar{x} \cdot \bar{y}} + 0$ (Substitution)
= $(\overline{\bar{x}} + \overline{\bar{y}}) + 0$ (De Morgan's Law)
= $(x + y) + 0$ (Double Negation Law)
= $x + y$ (Identity Law)

![[Pasted image 20261101171947.png]]