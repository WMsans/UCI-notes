# Problem 1

## Solution

Let
$E(x)$ = $x$ exercises regularly
$M(x)$ = $x$ has good muscle strength
$L(x)$ = $x$ has low blood pressure

So the argument is

$$\forall x (E(x) \to M(x))$$
$$\forall x (E(x) \to L(x))$$
$$E(j)$$
---
$\exists x (M(x) \land L(x))$

### With (C) = "Juanita exercises regularly"

**It is valid.**

Use the inference rules from Table 1.13.1 to eliminate the quantifiers.

Let $c$ be Juanita, a particular element: $E(c)$

Hypothesis: $\forall x (E(x) \to M(x))$
Universal instantiation: $E(c) \to M(c)$
Hypothesis: $E(c)$
Modus ponens: $M(c)$
Modus ponens: $M(c) \land L(c)$
There Exists rule: $\exists x (M(x) \land L(x))$

So the conclusion follows, and the inference is **valid**.

### With (C') = "Juanita has low blood pressure"

**It is invalid.** Here is a counter-example.

Let the universe be exactly two people: Juanita and Sam, with

|      | $E$ | $M$ | $L$ |
|------|-----|-----|-----|
| Juanita | F | F | T |
| Sam | F | F | F |

Check the three hypotheses:

- (A) $\forall x (E(x) \to M(x))$: $E$ is false for everyone, so every implication $E(x) \to M(x)$ is vacuously **true**.
- (B) $\forall x (E(x) \to L(x))$: same reason, **true**.
- (C') $L(j)$: Juanita has low blood pressure, **true**.

Check the conclusion:

- $\exists x (M(x) \land L(x))$: Juanita is the only one with $L$ true, and she has $M$ false. Sam has $M$ false. So no one has both good muscle strength and low blood pressure. The conclusion is **false**.

All three hypotheses true while the conclusion is false, so the inference is **invalid**.

# Problem 2
## Solution

In the last sentence, we did not prove that 1 is the largest positive integer. What we proved is:

> *If* a largest positive integer $x$ exists, *then* $x = 1$.

But the hypothesis is contradictory, so there is no $x$ to identify. Take $y = 2$ in the very first sentence: $\forall y\;(y \leq x)$ says $2 \leq x = 1$, which is false. So the assumption that a largest positive integer $x$ exists leads to a contradiction.

This is a proof by contradiction, and its correct conclusion is the negation of the hypothesis:

Therefore, there is no largest positive integer. $\blacksquare$

# Problem 3
## Solution

Given $x$ is a positive rational number. We will show that $\frac{6}{1 + 1/x}$ is a rational number.

Since $x$ is rational, by the definition of a rational number there exist integers $a$ and $b$ with $b \neq 0$ such that $x = \frac{a}{b}$.

Since $x > 0$, $a$ and $b$ have the same sign, so neither is zero. Replacing $(a, b)$ with $(-a, -b)$ if necessary, we may assume $a > 0$ and $b > 0$.

1. Since $\frac{a}{b}\cdot\frac{b}{a} = 1$: $\frac{1}{x} = \frac{b}{a}$ (allowed because $a \neq 0$)
2. Since $a \neq 0$: $1 + \frac{1}{x} = 1 + \frac{b}{a} = \frac{a + b}{a}$
3. Since $a > 0$ and $b > 0$, $a + b > 0$, so $a + b \neq 0$
4. Since $a \neq 0$ and $a + b \neq 0$:

$$\frac{6}{1 + 1/x} = \frac{6}{\frac{a+b}{a}} = 6 \cdot \frac{a}{a+b} = \frac{6a}{a+b}$$

5. Since $6a$ is an integer and $a + b$ is a nonzero integer, $\frac{6a}{a+b}$ is a rational number.

Therefore $\frac{6}{1 + 1/x}$ is rational. $\blacksquare$

# Problem 4
## Solution

Statement: $\forall x \forall y \big((x \in \mathbb{Z} \land y \in \mathbb{Z} \land 7 \nmid xy) \to (7 \nmid x \land 7 \nmid y)\big)$

The contrapositive is

$$\forall x \forall y \big((x \in \mathbb{Z} \land y \in \mathbb{Z} \land (7 \mid x \lor 7 \mid y)) \to 7 \mid xy\big)$$

Given $x$, $y$ are integers, and either $7 \mid x$ or $7 \mid y$. We will show $7 \mid xy$.

Case 1: $7 \mid x$

Then $x = 7k$ for some integer $k$.
$$xy = (7k)y = 7(ky)$$
Since $k$ and $y$ are integers, $ky$ is an integer.
Therefore $xy = 7 \cdot (\text{an integer})$, so $7 \mid xy$.

Case 2: $7 \mid y$

Then $y = 7m$ for some integer $m$.
$$xy = x(7m) = 7(xm)$$
Since $x$ and $m$ are integers, $xm$ is an integer.
Therefore $xy = 7 \cdot (\text{an integer})$, so $7 \mid xy$.

Either case gives $7 \mid xy$. Since our hypothesis was $7 \mid x \lor 7 \mid y$, this proves the contrapositive.

Therefore the contrapositive is true, so the original statement is true. $\blacksquare$

# Problem 5
## Solution

Given $a$, $b$ are positive integers. We will show: the last digit of $9^a + 9^b$ is never 6.

First, the last digit of a power of 9 depends only on the parity of the exponent:

- $9^1 = 9$, last digit $9$ (odd exponent)
- $9^2 = 81$, last digit $1$ (even exponent)
- $9^3 = 729$, last digit $9$ (odd exponent)
- $9^4 = 6561$, last digit $1$ (even exponent)

The pattern repeats because each power of 9 is 9 times the previous one, and multiplying a number ending in 9 by 9 gives a number ending in $81$, i.e. ending in 1, while multiplying a number ending in 1 by 9 gives a number ending in 9. So

$$9^n \equiv 9 \pmod{10} \text{ if } n \text{ is odd}, \qquad 9^n \equiv 1 \pmod{10} \text{ if } n \text{ is even}$$

Case 1: $a$ odd and $b$ odd

$$9^a + 9^b \equiv 9 + 9 = 18 \equiv 8 \pmod{10}$$
Last digit is $8$.

Case 2: $a$ odd and $b$ even (or $a$ even and $b$ odd)

$$9^a + 9^b \equiv 9 + 1 = 10 \equiv 0 \pmod{10}$$
Last digit is $0$.

Case 3: $a$ even and $b$ even

$$9^a + 9^b \equiv 1 + 1 = 2 \pmod{10}$$
Last digit is $2$.

In all three cases the last digit is $8$, $0$, or $2$, never $6$. Therefore the sum of two positive powers of 9 cannot have 6 as its last digit. $\blacksquare$