# 4.1.4
(a)
Domain = $$\{(0, 0), (0, 1), (1, 0), (1, 1)\}$$

(b)
![[Pasted image 20261019160242.png]]

(c)
Range = $$\{(0,0),(0,1),(1,0),(1,1)\}$$

# 4.2.1
(a)
$$f(2.2) = \lfloor 2.2 + 1/2 \rfloor = 2 $$
$$f(2.9) = \lfloor 2.9 + 1/2 \rfloor = 3 $$
$$f(2.5) = \lfloor 2.5 + 1/2 \rfloor = 3 $$
$$f(2) = \lfloor 2 + 1/2 \rfloor = 2 $$
$$f(3) = \lfloor 3 + 1/2 \rfloor = 3 $$

(b)
f(x) rounds x to the nearest integer, and rounds a tie (x ending in .5) up.

(c)
Both round to the nearest integer, but $g(x) = \lfloor x - 1/2 \rfloor$ rounds a tie down instead of up, so f and g differ only when x is a half-integer (f(x) = g(x) + 1 there).
# 4.2.2
(a)
$$f(x) = \lceil \frac{5x}{24} \rceil $$
(b)
$$g(y) = \lfloor \frac{y}{8} \rfloor$$
# 4.2.4
(b)
Given $n$ is an odd integer. We will show that $\lfloor \frac{n}{2} \rfloor = \frac{n-1}{2}$.

Recall the defining property of the floor: for any real $x$ and any integer $m$,
$$m = \lfloor x \rfloor \iff m \le x < m + 1.$$
So it suffices to find an integer $m$ with $m \le \frac{n}{2} < m + 1$.

Since $n$ is an odd integer, so $n = 2k + 1$ for some integer $k$. Then
$$\frac{n}{2} = \frac{2k + 1}{2} = k + \frac{1}{2}$$
and our candidate value is
$$\frac{n-1}{2} = \frac{2k}{2} = k,$$
which is an integer because $k$ is. Since $\frac{1}{2} > 0$ we have $k < k + \frac{1}{2}$, and since $\frac{1}{2} < 1$ we have $k + \frac{1}{2} < k + 1$. Putting these together,
$$k \le \frac{n}{2} < k + 1.$$
Since $k$ is an integer satisfying both bounds, the defining property of the floor gives
$$\lfloor \frac{n}{2} \rfloor = k = \frac{n-1}{2}. \qquad \blacksquare$$

# 4.3.2 
(i)
Neither.

Not one-to-one: $$f(0,0) = (0, -2) = f(1,0)$$ yet $(0,0) \neq (1,0)$.

Not onto: for every $y \in \mathbb{Z}$, $5y - 2 \equiv 3 \pmod 5$, so the second coordinate can never be $0$. Thus $$(0,0) \in \mathbb{Z} \times \mathbb{Z}$$ has no preimage.

(k)
Neither.

Not onto: the smallest value is $$f(1,1) = 2 + 1 = 3,$$ so $1 \in \mathbb{Z}^+$ (and also $2$) is never produced.

Not one-to-one: $$f(1,3) = 2 + 3 = 5 = 4 + 1 = f(2,1)$$ yet $(1,3) \neq (2,1)$.

# 4.3.6 

(b)
True. 

Let $f$ be a bijection and $c \neq 0$ a real number. We show that $cf$ is both one-to-one and onto.

One-to-one: suppose $(cf)(x_1) = (cf)(x_2)$ for some $x_1, x_2 \in \mathbb{R}$. Then $c \cdot f(x_1) = c \cdot f(x_2)$. Since $c \neq 0$, we may divide both sides by $c$, giving $f(x_1) = f(x_2)$. Because $f$ is one-to-one, this implies $x_1 = x_2$. Hence $cf$ is one-to-one.

Onto: let $y \in \mathbb{R}$ be arbitrary. Since $c \neq 0$, the number $y/c$ is a real number. Because $f$ is onto, there is some $x \in \mathbb{R}$ with $f(x) = y/c$. Then
$$(cf)(x) = c \cdot f(x) = c \cdot \frac{y}{c} = y.$$
So every $y \in \mathbb{R}$ has a preimage under $cf$, meaning $cf$ is onto.

Since $cf$ is both one-to-one and onto, $cf$ is a bijection. $\qquad \blacksquare$

# 4.4.1
(a)
No. 
$w$ has multiple output.

(b)
Yes.
![[Pasted image 20261019164343.png]]

(c)
Yes.
![[Pasted image 20261019164501.png]]
# 4.5.2 
(b)
$$(f \circ h)(52) = f(h(52)) = f(\lceil 52/5 \rceil) = f(11) = 11^2 = 121$$

(d)
$$(h \circ f)(x) = h(f(x)) = h(x^2) = \lceil \frac{x^2}{5} \rceil$$

# 4.3.4
(d)
One-to-one but not onto.

One-to-one: every input $x_1x_2x_3$ maps to $x_1x_2x_3x_1$, so the first three bits of an output recover its input. If $f(s) = f(t)$, then $s$ and $t$ agree in their first three bits, so $s = t$.

Not onto: in any output the fourth bit equals the first bit. So $0001 \in \{0,1\}^4$ has no preimage, since its preimage would have to be $000$, but $f(000) = 0000 \neq 0001$.

(g)
Neither.

Not one-to-one: $$f(\{1\}) = \{1\} - \{1\} = \varnothing = \varnothing - \{1\} = f(\varnothing)$$ Since, $\{1\} \neq \varnothing$, not one to one. 

Not onto: for every $X \subseteq A$, $1 \notin X - B$, so $\{1\} \in P(A)$ has no preimage.

# 4.4.2
(e)
Yes.

$f$ is its own inverse. For every $X \subseteq A$,
$$f(f(X)) = A - (A - X) = X,$$
so $f$ is a bijection and
$$f^{-1}(X) = A - X.$$

(b)
No.

$f$ is not onto: $$f(x) = 2x + 34 = 2(x + 17)$$ is even for every $x \in \mathbb{Z}$, so $1 \in \mathbb{Z}$ has no preimage. Hence $f$ is not a bijection and has no well-defined inverse.

# 4.5.6
(b)
$$(g \circ h)(010) = g(h(010)) = g(010) = 010$$
($h$ leaves $010$ unchanged because its first bit is already the same as its last bit, and reversing $010$ gives $010$ back.)

(e)
$$\{001, 011, 101, 111\}$$
The range of $f$ is $\{100, 101, 110, 111\}$, so the range of $g \circ f$ is obtained by reversing each of these. Equivalently, $(g \circ f)(b_1b_2b_3) = g(1b_2b_3) = b_3b_21$, which is exactly every string whose last bit is $1$.

