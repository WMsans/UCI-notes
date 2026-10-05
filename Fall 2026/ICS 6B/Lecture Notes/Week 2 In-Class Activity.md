Group Members: 
1. Vincent Chen
2. Armando Martinez
3. Jeremy Zhao

# Problem 1
1. $$\forall x (Seal(x) \to Swim(x)$$
2. $$\forall x (Fish(x) \to \lnot Fly(x))$$
3. $$\forall x \exists y(Fish(y) \land Fly(y) \land (Fish(x) \land (x \neq y) \to \lnot Fly(x)))$$
4. $$∃x∃y∀z(x \neq y∧Fish(x)∧Fly(x)∧Fish(y)∧Fly(y)∧((Fish(z)∧z \neq x∧z \neq y)→\lnot Fly(z)))$$

# Problem 2
Given $$\forall x ([(x < 0) \land D(x)] \to P(x))$$
Since x is positive integer, $(x<0)$ is false: $$\forall x ([F \land D(x)] \to P(x))$$
Complement law:
$$\forall x (F \to P(x))$$
Thus: $$\forall x (T)$$
Thus: $$T$$
It is true.

# Problem 3
$$\forall x \forall y (G(x, y) \to C(x))$$

# Problem 4
The original statement is $$\forall g \exists w (B(g, w) \ge 5)$$
The negation is $$\exists g \forall w (\lnot B(g, w) < 5)$$
