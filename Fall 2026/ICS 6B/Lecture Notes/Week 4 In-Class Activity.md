Group Members:
1. Jeremy Zhao
2. Vincent Chen
3. Armando Martinez

# Problem 1

## Solution

$$A \times B = \{(\text{Alex}, \text{Aanya}), (\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Aanya}), (\text{Aanya}, \text{Encong})\}$$

$$
\begin{aligned}
P(A \times B) = \{\, &\varnothing, \\
&\{(\text{Alex}, \text{Aanya})\}, \{(\text{Alex}, \text{Encong})\}, \{(\text{Aanya}, \text{Aanya})\}, \{(\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Alex}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Aanya}, \text{Aanya})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Aanya})\}, \\
&\{(\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Aanya}, \text{Aanya}), (\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Aanya})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Aanya}, \text{Aanya}), (\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Aanya}), (\text{Aanya}, \text{Encong})\}, \\
&\{(\text{Alex}, \text{Aanya}), (\text{Alex}, \text{Encong}), (\text{Aanya}, \text{Aanya}), (\text{Aanya}, \text{Encong})\} \,\}
\end{aligned}
$$

If auditing Nickolas, let $A' = \{\text{Alex}, \text{Aanya}, \text{Nickolas}\}$ and $B' = \{\text{Aanya}, \text{Encong}, \text{Nickolas}\}$.

Thus

$$|P(A' \times B')| = 2^{|A' \times B'|} = 2^{|A'| \, |B'|} = 2^{3 \cdot 3} = 2^9 = 512$$

# Problem 2

## Solution

An ordered pair belongs to both $A \times B$ and $B \times A$ exactly when both of its entries lie in $A \cap B$, so

$$(A \times B) \cap (B \times A) = (A \cap B) \times (A \cap B) \quad\Longrightarrow\quad |(A \times B) \cap (B \times A)| = |A \cap B|^2$$

By inclusion–exclusion, and since $|A \times B| = |A||B| = |B \times A|$,

$$|(A \times B) \cup (B \times A)| = |A||B| + |B||A| - |A \cap B|^2 = 2|A||B| - |A \cap B|^2$$

So the union has the same size as $A \times B$ (which has size $|A||B|$) exactly when

$$2|A||B| - |A \cap B|^2 = |A||B| \quad\Longleftrightarrow\quad |A \cap B|^2 = |A||B|$$

### Situation 1: $A = B$

If $A = B$, then $A \cap B = A$, so $|A \cap B|^2 = |A|^2$ and $|A||B| = |A|^2$. The two sides are equal, so the condition holds. We can also see it directly: $B \times A = A \times B$, so

$$(A \times B) \cup (B \times A) = (A \times B) \cup (A \times B) = A \times B$$

*Example:* $A = B = \{\text{Alex}, \text{Aanya}\}$. Then $A \times B = B \times A$ has $2 \cdot 2 = 4$ elements, and the union also has $4$ elements.

### Situation 2: $A = \varnothing$ (same argument for $B = \varnothing$)

If $A = \varnothing$, then every ordered pair in $A \times B$ would need a first entry from $A$, and there is none, so $A \times B = \varnothing$. Likewise $B \times A = \varnothing$. Hence

$$(A \times B) \cup (B \times A) = \varnothing \cup \varnothing = \varnothing = A \times B$$

so both sides have size $0$. In the formula this is the case $|A| = 0$, where $|A \cap B|^2 = 0 = |A||B|$ as well.

*Example:* $A = \varnothing$ and $B = \{\text{Alex}, \text{Encong}\}$. Then $|A \times B| = 0 \cdot 2 = 0$ and the union has size $0$.

# Problem 3

## Solution

$$(A \oplus B) \setminus C$$

# Problem 4

## Solution

### Statement 1: 

**False.**

Both blocks were defined inside $\mathbb{Z} \times \mathbb{Z}$, so they contain elements that are not in $S$.

- $(0,0)$ satisfies $a = -b$, but $0 \notin \mathbb{Z}^+$ and $0 \notin \mathbb{Z}^-$, so $(0,0) \notin S$.
- $(2,1)$ satisfies $|2| \neq |1|$, but both entries are positive, so $(2,1) \notin S$.

### Statement 2

**True.**

*Contained in $S$:* if $(a,b) \in X_1$ then $a \neq 0$ and $b = -a$, so the entries have opposite signs and $(a,b) \in S$. $X_2 \subseteq \mathbb{Z}^+ \times \mathbb{Z}^-$ and $X_3 \subseteq \mathbb{Z}^- \times \mathbb{Z}^+$, both by definition inside $S$.

*Nonempty:* $(1,-1) \in X_1$, $(1,-2) \in X_2$, $(-1,2) \in X_3$.

*Disjoint:* $X_2$ and $X_3$ have opposite sign patterns, so they cannot share a pair. For $X_1 \cap X_2$: a pair in $X_1$ has $a + b = 0$, while $X_2$ requires $a + b \neq 0$. The same argument gives $X_1 \cap X_3 = \varnothing$.

*Union $= S$:* take any $(a,b) \in S$, so $a$ and $b$ are nonzero with opposite signs.

- If $a + b = 0$, then $a = -b$ and $(a,b) \neq (0,0)$, so $(a,b) \in X_1$.
- If $a + b \neq 0$ and $a \in \mathbb{Z}^+$, then $b \in \mathbb{Z}^-$ and $(a,b) \in X_2$.
- If $a + b \neq 0$ and $a \in \mathbb{Z}^-$, then $b \in \mathbb{Z}^+$ and $(a,b) \in X_3$.

Every element of $S$ lies in exactly one block, so $X_1, X_2, X_3$ form a partition of $S$.

### Statement 3: $\mathbb{Z}^+ \times \mathbb{Z}^-$ and $\mathbb{Z}^- \times \mathbb{Z}^+$

**True.**

The blocks are nonempty ($(1,-1)$ and $(-1,1)$) and disjoint since a first entry cannot be both positive and negative and thus a pair cannot lie in both products.

### Statement 4: $\mathbb{Z}^+ \times \mathbb{Z}^+$ and $\mathbb{Z}^- \times \mathbb{Z}^-$

**False.**

For instance $(1,1)$ is in the first block but not in $S$, and every element of $S$ 

