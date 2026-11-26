Group Members:
1. Jeremy Zhao
2. Vincent Chen
3. Armando Martinez

# Problem 1
## Solution

| State               | Meaning         | $n$   | $e$         | $s$         | $\Gamma$    |
| ------------------- | --------------- | ----- | ----------- | ----------- | ----------- |
| $q_{start}$         | nothing matched | $q_n$ | $q_{start}$ | $q_{start}$ | $q_{start}$ |
| $q_n$               | ends in `n`     | $q_n$ | $q_{ne}$    | $q_{start}$ | $q_{start}$ |
| $q_{ne}$            | ends in `ne`    | $q_n$ | $q_{start}$ | $q_{nes}$   | $q_{start}$ |
| $q_{nes}$           | ends in `nes`   | $q_n$ | $q_{start}$ | $q_{ness}$  | $q_{start}$ |
| $q_{ness}$ (accept) | ends in `ness`  | $q_n$ | $q_{start}$ | $q_{start}$ | $q_{start}$ |

The single accepting state is $q_{ness}$.

"meanness" ($m,e,a,n,n,e,s,s$):

$$q_{start} \xrightarrow{m} q_{start} \xrightarrow{e} q_{start} \xrightarrow{a} q_{start} \xrightarrow{n} q_n \xrightarrow{n} q_n \xrightarrow{e} q_{ne} \xrightarrow{s} q_{nes} \xrightarrow{s} q_{ness}$$

so the FSA accepts "meanness".

# Problem 2
## Solution
Swap the accepting and non-accepting states of $M$ works.

# Problem 3
## Solution

|       | $0$           | $1$           | $*$               |
| ----- | ------------- | ------------- | ----------------- |
| $q_0$ | $(q_1, 0, R)$ | $(q_0, 1, R)$ | $(q_{rej}, *, R)$ |
| $q_1$ | $(q_1, 0, R)$ | $(q_0, 1, R)$ | $(q_{acc}, *, R)$ |

# Problem 4
## Solution
1. The empty string: $q_0$ reads $*$ and goes to $(q_{rej}, *, R)$. **Rejects**
2. "a": $q_0a \to a\,q_1* \to q_3a \to a\,q_{acc}*$. **Accepts**
3. "ab": $q_0a \to a\,q_1b \to ab\,q_1* \to a\,q_3b \to ab\,q_{rej}*$. **Rejects**
4. "bb": $q_0b \to b\,q_2b \to bb\,q_2* \to b\,q_4b \to bb\,q_{acc}*$. **Accepts**
5. "abb": $q_0a \to a\,q_1bb \to ab\,q_1b \to abb\,q_1* \to ab\,q_3b \to abb\,q_{rej}*$. **Rejects**
6. "bab": $q_0b \to b\,q_2ab \to ba\,q_2b \to bab\,q_2* \to ba\,q_4b \to bab\,q_{acc}*$. **Accepts**

The Turing Machine accepts a string if and only if the string is nonempty and begins and ends with the same symbol.
