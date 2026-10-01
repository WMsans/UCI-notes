# 1.1.2
(a) 
$$n \land m$$
(b) 
$$t \land m$$
(c)
$$n \lor m$$
(d)
$$\lnot m$$
(e)
$$t \land n$$
(f)
$$\lnot t$$
# 1.1.4
(d)
Inclusive or: True
Exclusive or: False

# 1.2.4
(d)

| p   | q   | r   | ¬r  | ¬q  | (r∨p) | (¬r∨¬q)(¬r∨¬q | **(r∨p)∧(¬r∨¬q)** |
| --- | --- | --- | --- | --- | ----- | ------------- | ----------------- |
| F   | F   | F   | T   | T   | F     | T             | **F**             |
| F   | F   | T   | F   | T   | T     | T             | **T**             |
| F   | T   | F   | T   | F   | F     | T             | **F**             |
| F   | T   | T   | F   | F   | T     | F             | **F**             |
| T   | F   | F   | T   | T   | T     | T             | **T**             |
| T   | F   | T   | F   | T   | T     | T             | **T**             |
| T   | T   | F   | T   | F   | T     | T             | **T**             |
| T   | T   | T   | F   | F   | T     | F             | **F**             |

# 1.2.7
(c)
$$B \lor (D \land M)$$

# 1.3.3
(b)
1. Converse
	1. Statement: If 5 < 3, then 7 < 5.
	2. False → False.
	3. True
2. Inverse
	1. Statement: If 7 is not less than 5, then 5 is not less than 3
	2. True → True
	3. True
3. Contrapositive
	1. Statement: If 5 is not less than 3, then 7 is not less than 5.
	2. True → True
	3. True

# 1.3.7
(a)
they are a senior and at least 17 years of age = $$s \land y$$
Thus $$p → s \land y$$
(c)
$$p → y$$

# 1.3.10
(b)
$$(T∨r)→r$$
Left side is $$T→r$$
This is **Unknown**

(c)
$$(T∨r)↔(F∧r)$$
Left side is $$T∨r=T$$
Right side is $$F∧r=F$$
Thus $$T↔F$$
This is **False**

(e)
$$T→(r∨F)$$
Right side is $$r∨F=r$$
Thus $$T→r$$
This is **Unknown**

(f)
$$(T∧F)→r$$
Left side is 
$$T∧F=F$$
Thus $$  F→r$$
This is **True**

# 1.4.4
(a)

| p   | q   | ¬q  | p∨¬q | **¬(p∨¬q)** | ¬p  | **¬p∧q** |
| --- | --- | --- | ---- | ----------- | --- | -------- |
| T   | T   | F   | T    | **F**       | F   | **F**    |
| T   | F   | T   | T    | **F**       | F   | **F**    |
| F   | T   | F   | F    | **T**       | T   | **T**    |
| F   | F   | T   | T    | **F**       | T   | **F**    |

The columns for $$¬(p∨¬q)$$ and $$¬p∧q$$ are identical. Therefore, they are logically equivalent.

(c)

| p   | q   | ¬q  | p∨¬q | **¬(p∨¬q)** | ¬p  | ¬q  | **¬p∧¬q** |
| --- | --- | --- | ---- | ----------- | --- | --- | --------- |
| T   | T   | F   | T    | **F**       | F   | F   | **F**     |
| T   | F   | T   | T    | **F**       | F   | T   | **F**     |
| F   | T   | F   | F    | **T**       | T   | F   | **F**     |
| F   | F   | T   | T    | **F**       | T   | T   | **T**     |

The columns for $$p∧(p→q)$$and $$p∧q$$ are identical. Therefore, they are logically equivalent. 

# 1.4.5
(b)
Expression 1 is $$¬j→(l∨¬r)$$
Expression 2 is $$(r∧¬l)→j(r∧¬l)→j$$

| j   | l   | r   | ¬j  | ¬r  | l∨¬r | **Expr 1:** ¬j→(l∨¬r) | ¬l  | r∧¬l | **Expr 2:** (r∧¬l)→j |
| --- | --- | --- | --- | --- | ---- | --------------------- | --- | ---- | -------------------- |
| T   | T   | T   | F   | F   | T    | **T**                 | F   | F    | **T**                |
| T   | T   | F   | F   | T   | T    | **T**                 | F   | F    | **T**                |
| T   | F   | T   | F   | F   | F    | **T**                 | T   | T    | **T**                |
| T   | F   | F   | F   | T   | T    | **T**                 | T   | F    | **T**                |
| F   | T   | T   | T   | F   | T    | **T**                 | F   | F    | **T**                |
| F   | T   | F   | T   | T   | T    | **T**                 | F   | F    | **T**                |
| F   | F   | T   | T   | F   | F    | **F**                 | T   | T    | **F**                |
| F   | F   | F   | T   | T   | T    | **T**                 | T   | F    | **T**                |

Since the result of both expressions are the same, they are equivalent. 

(d)
Expression 1 is $$j→¬l$$
Expression 2 is $$¬j→l$$

| j   | l   | ¬l  | **Expr 1:** j→¬l | ¬j¬j | **Expr 2:** ¬j→l |
| --- | --- | --- | ---------------- | ---- | ---------------- |
| T   | T   | F   | **F**            | F    | **T**            |
| T   | F   | T   | **T**            | F    | **F**            |
| F   | T   | F   | **T**            | T    | **T**            |
| F   | F   | T   | **T**            | T    | **F**            |
Since the result of both expressions are the not same, they are not equivalent. 

# 1.5.1
(c)


1. $$r∨(¬r→p)$$  

2. $$r∨(¬¬r∨p)$$  **Conditional identities**
3. $$r∨(r∨p)$$  **Double Negation Law**
4. $$(r∨r)∨p$$  **Associative Law**    
5. $$r∨p$$  **Idempotent Law**

# 1.5.2
(c)
Given $$(p→q)∧(p→r)$$

Implication law $$(¬p∨q)∧(¬p∨r)$$
Distributive law $$¬p∨(q∧r)$$
Implication law $$p→(q∧r)$$

(f)
Given $$¬(p∨(¬p∧q))$$
De Morgans law $$¬p∧(¬(¬p)∨¬q)$$
Double negative law $$¬p∧(p∨¬q)$$
Distributive law $$(¬p∧p)∨(¬p∧¬q)$$
Negation law $$F∨(¬p∧¬q)$$
Identity law $$¬p∧¬q$$

# 1.5.4
(b)
Let $$p→q$$
The inverse is $$¬p→¬q$$
Condition: 
Implication law $$\neg p \vee q \quad$$
Inverse: 
Implication law
$$\neg(\neg p) \vee \neg q \quad$$
Double negation law $$p∨¬q$$

Thus, they are not logically equivalent.
(c)
Let $$p→q$$
The contrapositive is $$¬q→¬p$$
Condition:
Implications law $$\neg p \vee q$$
Commutative law $$q \vee \neg p$$
Double Negation law $$\neg(\neg q) \vee \neg p$$
Implication Law
$$ \neg q \rightarrow \neg p$$
Thus, conditional statement is logically equivalent to its contrapositive.