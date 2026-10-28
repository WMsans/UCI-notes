Group Members:
1. Jeremy Zhao
2. Vincent Chen
3. Armando Martinez

# Problem 1
## Solution

$$(f \circ g)(x) = f(g(x)) = 2(3x + 2) + 3 = 6x + 7$$

$$(g \circ f)(x) = g(f(x)) = 3(2x + 3) + 2 = 6x + 11$$

These are different functions so $f \circ g \neq g \circ f$. **Composition is not commutative.**

# Problem 2
## Solution

Note $|B \times B| = 6 \cdot 6 = 36$ and $|A \times A| = 10 \cdot 10 = 100$.

### a) Onto?

**No.**

A function is onto only if every element of the range is the image of at least one element of the domain, which requires $|B \times B| \ge |A \times A|$. Here $36 < 100$, so at least $64$ elements are missed. So no function $B \times B \to A \times A$ is onto.

### b) 1-1?

**Yes.**

*Example:* list the $36$ elements of $B \times B$ as $p_1, p_2, \dots, p_{36}$, and list $A \times A$ in lexicographic order:

$$(1,1), (1,2), \dots, (1,10), (2,1), \dots, (2,10), (3,1), \dots, (3,10), (4,1), \dots, (4,6).$$

Define $f(p_k) = (m_k, n_k)$ = the $k$-th pair in that list. Since the list has $36$ distinct pairs and each $p_k$ gets its own pair, distinct inputs always have distinct images.

# Problem 3
## Solution

### A. The function that assigns to each bit string a number equal to twice the number of zeros in that string

**Domain:** all bit strings

**Range:** the even nonnegative integer: $\{0, 2, 4, 6, \dots\}$ 

### B. The function that assigns the number of bits left over when a bit string is split into bytes (blocks of 8 bits)

**Domain:** all bit strings

**Range:** $\{0, 1, 2, 3, 4, 5, 6, 7\}$

### C. The function that assigns to each positive integer the largest perfect square not exceeding this integer

**Domain:** $\mathbb{Z}^+$

**Range:** the perfect squares $\{1, 4, 9, 16, 25, \dots\} = \{n^2 : n \in \mathbb{Z}^+\}$

# Problem 4
## Solution

### A. $f(S)$ is the position of a $0$ bit in a string

**Not a function.**

The rule produce multiple outputs. For $S = 001$ there is a $0$ at position $1$ and at position $2$, so $f(S)$ is not determined.

### B. $f(S)$ is the number of $1$ bits in a string

**It is a function.**

### C. $f(S)$ is the smallest integer $i$ such that the $i$-th bit of $S$ is $1$

**Not a function.**

It fails to be defined for any string with no $1$ bits.

# Problem 5
## Solution

### What is $v(xyz)$?

$$v(xyz) = r(q(xyz)) = r(xyz) = yxz$$

### What is $v^{-1}(xyz)$?

$$v^{-1}(xyz) = yxz$$

### What is $q^{-1}(xyz)$?

$$q^{-1}(xyz) = xyz$$

### What is $p^{-1}(xyz)$?

$p^{-1}$ is not a function: $p$ is not injective, since $p(xyz) = p(xy'z)$ for any $y, y'$. The middle character is discarded.