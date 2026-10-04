# 1.7.3
(a) 
$$\exists x \lnot B(x)$$
(b) 
$$\forall x B(x)$$
(c)
$$T(\text{Sam}) \land \lnot B(\text{Sam})$$
(d)
$$\exists x (\lnot T(x) \land B(x))$$
(e)
$$\forall x (T(x) \to B(x))$$

# 1.7.7
(b)
$$\forall x((x \neq \text{Nima}) \to N(x))$$
Everyone other than Nima is a new employee.
This is **True**

(c)
$$\exists x(\lnot D(x) \land N(x))$$
Someone is a new employee who did not miss the deadline (Dana or Bert).
This is **True**

(i)
$$\forall x(D(x) \leftrightarrow N(x))$$
Everyone missed the deadline if and only if they are a new employee. (Nima breaks it)
This is **False**

# 1.8.3
(d)
$$\exists x (P(x) \land C(x))$$
Negation: $$\lnot \exists x (P(x) \land C(x))$$
Applying De Morgan's law: $$\forall x \lnot(P(x) \land C(x)) \equiv \forall x (\lnot P(x) \lor \lnot C(x))$$
English: Every student showed up without a pencil or without a calculator. 

(e)
$$\exists x (P(x) \lor C(x))$$
Negation: $$\lnot \exists x (P(x) \lor C(x))$$
Applying De Morgan's law: $$\forall x \lnot(P(x) \lor C(x)) \equiv \forall x (\lnot P(x) \land \lnot C(x))$$
English: Every student showed up without a pencil and without a calculator.

(f)
$$\forall x (P(x) \land C(x))$$
Negation: $$\lnot \forall x (P(x) \land C(x))$$
Applying De Morgan's law: $$\exists x \lnot(P(x) \land C(x)) \equiv \exists x (\lnot P(x) \lor \lnot C(x))$$
English: Some student showed up without a pencil or without a calculator.

# 1.8.4
(b)
$$\lnot\forall x(\lnot P(x) \to Q(x))$$
$$\exists x \lnot(\lnot P(x) \to Q(x))$$  Quantifier negation law
$$\exists x \lnot(\lnot(\lnot P(x)) \lor Q(x))$$  Implication law
$$\exists x (\lnot\lnot(\lnot P(x)) \land \lnot Q(x))$$  De Morgan's law
$$\exists x (\lnot P(x) \land \lnot Q(x))$$  Double negation law

Thus, $$\lnot\forall x(\lnot P(x) \to Q(x)) \equiv \exists x(\lnot P(x) \land \lnot Q(x))$$

# 1.9.4
(d)
$$\exists x \forall y (P(x,y) \leftrightarrow P(y,x))$$
$$\forall x \lnot \forall y (P(x,y) \leftrightarrow P(y,x))$$  Quantifier negation law
$$\forall x \exists y \lnot (P(x,y) \leftrightarrow P(y,x))$$  Quantifier negation law
$$\forall x \exists y \lnot ((\lnot P(x,y) \lor P(y,x)) \land (\lnot P(y,x) \lor P(x,y)))$$  Biconditional law
$$\forall x \exists y ((\lnot(\lnot P(x,y) \lor P(y,x)) \land \lnot(\lnot P(y,x) \lor P(x,y))))$$  De Morgan's law
$$\forall x \exists y ((P(x,y) \land \lnot P(y,x)) \land (\lnot P(x,y) \land P(y,x)))$$  Double negation and De Morgan's law
$$\forall x \exists y ((P(x,y) \land \lnot P(y,x)) \lor (\lnot P(x,y) \land P(y,x)))$$  Commutative law

# 1.10.3
(a)

| $P$ | $a$ | $b$ | $c$ |
| --- | --- | --- | --- |
| $a$ | T   | T   | T   |
| $b$ | F   | F   | F   |
| $c$ | T   | T   | F   |

For $\forall x\exists y P(x,y)$, each value of $x$ needs at least one true entry in its row. For $x = b$ we have $P(b,a) = P(b,b) = P(b,c) = F$, so the statement is false.

For $\exists x\forall y P(x,y)$, one value of $x$ needs every entry in its row true. Taking $x = a$, we have $P(a,a) = P(a,b) = P(a,c) = T$, so the statement is true.

Since one statement is false and the other is true for these values of $P$, the two are not logically equivalent.

# 1.10.4
(e)
$$\forall x \left((0 < x \land x < 1) \to \left(\frac{1}{x} > 1\right)\right)$$

(f)
$$\lnot \exists x \forall y (y < x)$$
$$\exists x \forall y (y \ge x)$$

(g)
$$\forall x \left(x \neq 0 \to \exists y (xy = 1)\right)$$

# 1.10.7
(c)
$$\exists x (N(x) \land D(x))$$

(d)
$$\forall y (D(y) \to P(\text{Sam}, y))$$

(e)
$$\exists x (N(x) \land \forall y P(x, y))$$

(f)
$$\exists x (N(x) \land D(x)) \land \lnot \exists y (N(y) \land D(y) \land y \neq x)$$

# 1.10.10
(c)
$$\forall x \exists y \left(y \neq \text{Math 101} \land T(x, y)\right)$$

(d)
$$\exists x \forall y \left(y \neq \text{Math 101} \to T(x, y)\right)$$

(f)
$$\exists y \exists z \left(T(\text{Sam}, y) \land T(\text{Sam}, z) \land y \neq z \land \forall w (T(\text{Sam}, w) \to (w = y \lor w = z))\right)$$

# 1.11.3
(b)
Form: $$((p \lor q) \land \lnot q) \to p$$  (disjunctive syllogism)

| $p$ | $q$ | $p \lor q$ | $\lnot q$ | $((p \lor q) \land \lnot q) \to p$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | T | T | T |
| F | T | T | F | T |
| F | F | F | T | T |

Every row gives $T$, so the argument is valid. When $q$ is false the first premise forces $p$, and when $q$ is true the second premise is false so the argument's hypotheses cannot both hold.

(c)
Form: $$((p \to q) \land q)\to p$$

| $p$ | $q$ | $p \to q$ | $((p \to q) \land q) \to p$ |
|---|---|---|---|
| T | T | T | T |
| T | F | F | T |
| F | T | T | F |
| F | F | T | T |

The third row gives $F$, so the argument is invalid (affirming the consequent). When $\sqrt{2}$ is rational and $2\sqrt{2}$ is still irrational, both premises are true while the conclusion is false, so the form has a counterexample.


# 1.11.4
(a)
Argument: $4$ or $5$ is prime. $5$ is not prime. $\therefore\ 4$ is prime.
Form: $$((p \lor q) \land \lnot q) \to p$$

| $p$ | $q$ | $p \lor q$ | $\lnot q$ | $((p \lor q) \land \lnot q) \to p$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | T | T | T |
| F | T | T | F | T |
| F | F | F | T | T |

Every row is T, so the argument is valid even though its conclusion $p$ (4 is prime) is false. In this situation the second premise $\lnot q$ (5 is not prime) is false, so the hypotheses cannot both be true and the false conclusion is never forced.

(b)
Argument: $5$ is prime. If $4$ is prime then $5$ is prime. $\therefore\ 4$ is not prime.
Form: $$(q \land p \to q) \to \lnot p$$

| $p$ | $q$ | $q$ | $p \to q$ | $q \land (p \to q)$ | $\lnot p$ |
|---|---|---|---|---|---|
| T | T | T | T | T | F |
| T | F | F | T | F | F |
| F | T | T | T | T | T |
| F | F | F | T | F | T |

In the first row both hypotheses are T while the conclusion $\lnot p$ is F, so the form is invalid. Here $p$ is F and $q$ is T, so both hypotheses are true and the conclusion 4 is not prime is true, giving an invalid argument with a true conclusion.
