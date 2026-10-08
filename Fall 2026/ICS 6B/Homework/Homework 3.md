# 1.12.5
(c)
$p = get\ a\ job$
$q = buy\ a\ new\ car$
$r = buy\ a\ new\ house$
The form is: 
$\lnot p \to \lnot (q \land r)$
$\lnot p$
---
$\therefore \lnot q$

Hypothesis: $$\lnot p \to \lnot (q \land r)$$
Implication: $$p \lor \lnot (q \land r)$$
De Morgan's Law: $$p \lor \lnot q \lor \lnot r$$
Hypothesis: $$\lnot p$$
Thus: $$F \lor \lnot q \lor \lnot r$$
Identity Law: $$\lnot q \lor \lnot r$$
Thus its not valid because $\lnot r$ could be true.

(d)
$p = get\ a\ job$
$q = buy\ a\ new\ car$
$r = buy\ a\ new\ house$
The form is:
$\lnot p \to \lnot (q \land r)$
$\lnot p$
$r$
---
$\therefore \lnot q$

Hypothesis: $$\lnot p \to \lnot (q \land r)$$
Identity Law: $$p \lor \lnot (q \land r)$$
De Morgan's Law: $$p \lor \lnot q \lor \lnot r$$
Hypothesis: $$\lnot p$$
Thus: $$F \lor \lnot q \lor \lnot r$$
Identity Law: $$\lnot q \lor \lnot r$$
Hypothesis: $$r$$
Thus: $$\lnot q \lor F$$
Identity Law: $$\lnot q$$
Thus it is valid. 

# 1.13.1
(a)
P(x) = x practices hard
Q(x) = x plays badly

The form is: 
$\forall x (P(x) \lor Q(x)$
$\exists x \lnot P(x)$
---
$\therefore \exists x Q(x)$

Hypothesis: $$\forall x (P(x) \lor Q(x)$$
Let c be an arbitrary argument: $$P(c) \lor Q(c)$$
Hypothesis: $$\exists x \lnot P(x)$$
Let d be an particular element: $$\lnot P(d)$$
Since d is one of c, $P(c)$ is $F$: $$F \lor Q(c)$$
Implication Law: $$Q(c)$$
Universal: $$\exists x Q(x)$$
Thus it is valid. 

# 1.13.4
(a)
Hypothesis: $$\exists x (P(x) \land Q(x))$$
Let c be an particular element: $$P(c) \land Q(c)$$
Existential Generalization: $$\exists x P(x) \land \exists x Q(x)$$
Thus valid. 

(b)
Hypothesis: $$\exists x P(x) \land \exists x Q(x)$$
Let c be an particular element: Existential instantiation $$P(c)$$
Let d be an particular element: Existential instantiation $$Q(d)$$
Thus: $$P(c) \land Q(d)$$
Suppose 

|     | P   | Q   |
| --- | --- | --- |
| c   | T   | F   |
| d   | F   | T   |
which satisfied $P(c) \land Q(d)$. 

Thus, the conclusion $\exists x (P(x) \land Q(x))$ is False. 

# 2.2.1
(a)
False, because there may be miss considered situation that makes the statement false, making it not universal. 

# 2.2.5
(b)
Let c = 3
The sum of all the intergers smaller than c is $$1 + 2 = 3$$
Since $c = 3$, this is a legal statement. 

(d)
7c + 5d = 1
Let c = -2 and d = 3
7 * -2 + 5 * 3 = 1 = 1
This is legal statement. 

# 2.3.2
(a)
Variable reuse of $k$ for $x = kw$ and $z = ky$. 

(b)
> Let m be an integer such that $xz = m * wy$

This is wrong because introducing m from nowhere and assume that it is an integer is invalid. 

(c)
Skipped step that $$(kw)(jy) = (kj)(wy)$$
And proving $(kj)$ is an integer. 

(d)
Not assuming k and w are integers, thus invalid. 

# 2.4.3
(b)
Let x be a real number that $x \leq 3$. We will show that $12 - 7x + x^2 \geq 0$ 

Since $x \leq 3$, $$x - 3 \leq 0$$
Since $x <= 3 < 4$, $$x - 4 \leq 0$$
Since two negative numbers timed together is a positive number, $$(x - 3)(x - 4) \geq 0$$
Simplify the left part: $$12 - 7x + x^2 \geq 0$$
$\blacksquare$

# 2.4.4
(k)
It is true.
Assume we have x, y and z that $xy | z$, we will show that $x|z$ and $y|z$

Since $xy|z$, we assume there exists an integer k that $$k * xy = z$$
while $x \neq 0$ and $y \neq 0$
Thus, $$(k * y) * x = z$$
Since both k and y are integers, $(k * y)$ is an integer. 
Therefore, since z equals x times other integer, and $z \neq 0$, $$x|z$$
Also, $$(k * x) * y = z$$
Since both k and y are integers, $(k * x)$ is an integer. 
Therefore, since z equals x times other integer, and $z \neq 0$, $$y|z$$
$\blacksquare$

(m)
It is false. 
Let x = 2, y = 3 and z = 5. 
Since (y+ z) = 8, and 2* 4 = 8, so that $x|(y+z)$
However, there does not exist integer that allows $2 * k = 3$ or $2 * k = 5$

# 2.5.3
(c)
Assume we have real numbers x and y, y is not irrational and x is rational. We will show that xy is not irrational. 

Since for a real number it can only be irrational or rational, and y is not irrational, y is rational. 

Since x is an real number and y is an real number, xy is an real number. 

Since y is a rational number and x is a rational number, xy is a rational number. 

Therefore xy is not irrational.

$\blacksquare$

# 2.6.6
(d)
Assume there exist a smallest integer x. 

Case 1: x > 0
Therefore, $0 < x$. x is not smallest.

Case 2: x = 0
Therefore, any negative number is smaller than x. x is not smallest.

Case 3: x < 0
Since 2 and x are both integers, 2x is an integer.
Since x < 0, 2x < x. x is not smallest.

There's a contradiction. Therefore, no smallest integer exists. 

# 2.7.3
(d)
Case 1: x is positive not y is positive
x + y = x + y
which satisfied $|x+y| = x+y = |x|+|y|$

Case 2: x is negative and y is negative
$- x - y = - (x + y)$
which satisfied $|x+y| = -(x+y) = -x-y = |x|+|y|$

Case 3: x is positive and y is negative
Since $-y \leq |y|$ and $x \leq |x|$
$$x+y ≤ |x|+|y|$$when $x + y \geq 0$ or $$|x+y| = −x−y ≤ |x|+|y|$$when $x + y < 0$

Which both satisfied $x + y \leq x + y$

Case 4: x is negative and y is positive
Since $y \leq |y|$ and $-x \leq |x|$
$$x+y ≤ |x|+|y|$$when $x + y \geq 0$ or $$|x+y| = −x−y ≤ |x|+|y|$$when $x + y < 0$
Which both satisfied $x + y \leq x + y$

Thus proven. 
$\blacksquare$
