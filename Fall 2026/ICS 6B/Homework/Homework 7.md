# 6.1.1 
(c)
![[Pasted image 20261102172647.png]]

# 6.1.2 
(e)
$$\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{bmatrix}$$
Pairs:
$${(1,1), (1,4), (2,2), (3,3), (4,1), (4,4)}$$

# 6.2.1 
(c)
1. reflective
	1. For any positive integer $x$, we can choose $n = 1$ (which is a positive integer), and we get $x^1 = x$. Therefore, $xPx$ holds for all $x$ in the domain.
2. anti-symmetric
	1. $2P4$ because $2^2 = 4$, but $4P2$ is false because there is no positive integer $n$ such that $4^n = 2$
3. transitive
	1. Suppose $xPy$ and $yPz$. Then there exist positive integers $n$ and $m$ such that $y = x^n$ and $z = y^m$. Substituting the first equation into the second gives $z = (x^n)^m = x^{nm}$. Since $n$ and $m$ are positive integers, their product $nm$ is also a positive integer. Thus, there exists a positive integer $k = nm$ such that $z = x^k$, which means $xPz$.

(i) 
1. neither reflexive or anti-reflexive
	1. For $xTx$ to hold, we need $x + x = 0$, which simplifies to $2x = 0$ or $x = 0$. This is only true for $x = 0$, not for all real numbers
	2. For $x = 0$, we have $0 + 0 = 0$, so $0T0$ is true.
2. symmetric
	1. If $xTy$, then $x + y = 0$. By the commutative property of addition, $y + x = 0$, which means $yTx$.
3. not transitive
	1. Consider $x = 1$, $y = -1$, and $z = 1$. We have $xTy$ (since $1 + (-1) = 0$) and $yTz$ (since $-1 + 1 = 0$). However, $xTz$ is false because $1 + 1 = 2 neq 0$.

# 6.2.2
(a)
1. Reflexive
	1. $(m(x)ge m(x))$ for every player $(x)$.
2. Anti-symmetric
	1. If $(xRy)$ and $(yRx)$, then $(m(x)ge m(y))$ and $(m(y)ge m(x))$, so $(m(x)=m(y))$. Since no two distinct players have the same measured weight, this forces $(x=y)$.
3. Transitive
	1. if $(m(x)ge m(y))$ and $(m(y)ge m(z))$, then $(m(x)ge m(z))$.

(b)
1. Reflexive
	1. $(m(x)ge m(x))$ for every player $(x)$.
2. Neither symmetric or anti-symmetric
	1. $(m(x)>m(y))$, we have $(xRy)$ but not $(yRx)$.
	2. There are distinct players $(xne y)$ with $(m(x)=m(y))$, so $(xRy)$ and $(yRx)$
3. Transitive
	1. if $(m(x)ge m(y))$ and $(m(y)ge m(z))$, then $(m(x)ge m(z))$.

# 6.2.4 
(c)  
1. anti-reflexive
	1. $(a,a),(b,b),(c,c),(d,d)\notin R.$
2. symmetric
	1. $\text{every pair in } R\text{ has its reverse in }R.$
3. not transitive
	1. $(a,b),(b,a)\in R\text{ but }(a,a)\notin R.$

# 6.3.3
(a) Largest in-degree vertex: $(e)$; in-degree: $(3)$.

(b) Largest out-degree vertex: $(a)$; out-degree: $(4)$.

(c) Self-loops: $(\langle a, a\rangle, \langle b,b\rangle, \langle e,e\rangle)$.

(d) Yes, $(\langle b,d,e,e\rangle)$ is a walk. It is an open walk because it starts at $(b)$ and ends at $(e)$.

(e) No, $(\langle a,c,f,g\rangle)$ is not a walk because there is no directed edge $(cto f)$.

(f) Yes, $(\langle a,a,c,e,e\rangle)$ is a walk. It is an open walk, and it is a trail but not a path, since vertices are repeated. So it is an open trail.

(g) One example is $(\langle b,b,d,e,e\rangle)$. It has length $(4)$, is open, is a trail, and is not a path because $(b)$ and $(e)$ are repeated.

# 6.3.4 
(a)  
A directed trail of length $5$ exists:  
$3\to1\to2\to2\to3\to2$,  
using all five edges exactly once.

For every smaller length we also have examples:

$x=0$: the trivial trail at any vertex
$x=1$: $3\to1$
$x=2$: $3\to1\to2$
$x=3$: $3\to1\to2\to2$
$x=4$: $3\to1\to2\to2\to3$
$x=5$: $3\to1\to2\to2\to3\to2$

Therefore the possible trail lengths are  
$x\in\{0,1,2,3,4,5\}$.  

# 6.4.2 
(a)
For real numbers x, y and z,
$$(x > y) \land (y \leq z)$$
Thus $$\mathbb{R}\times\mathbb{R}$$

(d)
For real numbers x, y and z,
$$(x\leq y) \land (y < z)$$
Thus $$R_3$$

# 6.4.5 
(a)
$True.$ 
Let $x$ be arbitrary. 
Since $R$ is reflexive, $(x,x)\in R$
Since $S$ is reflexive, $(x,x)\in S$. 
Taking $y=x$, we have $xRy$ and $ySx$, so $(x,x)\in S\circ R$. 
Hence $S\circ R$ is reflexive.

(e)
$False.$ 
A counter is that let $A={a,b}$,  $R={(a,a),(a,b),(b,b)}$ and $S={(a,a),(b,a),(b,b)}$.  
Both $R$ and $S$ are antisymmetric. 
$(a,b)\in S\circ R$ because $aRb$ and $bSb$
$(b,a)\in S\circ R$ because $bRb$ and $bSa$
Since $a\ne b$, $S\circ R$ is not antisymmetric.

(i)
$False.$ 
A counter is that let $A={a,b,c,u,v}$,   $R={(a,u),(b,v)}$ and $S={(u,b),(v,c)}$.  
Both $R$ and $S$ are transitive vacuously, since neither has composable pairs.   
$(a,b)\in S\circ R$ because $aRu$ and $uSb$
$(b,c)\in S\circ R$ because $bRv$ and $vSc$
But $(a,c)\notin S\circ R$, since the only $R$-image of $a$ is $u$, and $uSc$ is false. Thus $S\circ R$ is not transitive.

# 6.5.3 
(b)

![[Pasted image 20261104112630.png]]

# 6.5.4
(a) no  
(b) no  
(c) yes  
(d) no  
(e) no  
(f) yes  
(g) vertices 2 and 4  
(h) vertices 1 and 5  
(i) yes, its out-degree in G+G+ is 5