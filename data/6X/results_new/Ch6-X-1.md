## Problem 6.1
### Subproblem (1)
#### Status
graded
#### Answer
（1） 设 $U$ 是从 $\{1,2,\cdots,n\}$ 中选 $n-k$ 个数的方案，$A_i(1\le i\le m)$ 是选择数 $i$ 后的方案。 则 $|\bar A_1\cap\cdots\cap \bar A_m|$ 为从剩下 $n-m$ 个数中选 $n-k$ 个数的方案数，$|A_i|=\dbinom{n-1}{n-k-1}$，$|A_{i_1}\cap\cdots\cap A_{i_j}|=\dbinom{n-j}{n-k-j}=\dbinom{n-j}{k}$ 从而有 $|\bar A_1\cap\cdots\cap \bar A_m|=|U|-\sum|A_i|+\sum|A_i\cap A_j|+\cdots+(-1)^j\sum |A_{i_1}\cap\cdots\cap A_{i_j}|$ 即 $\dbinom{n-m}{n-k}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{m}{j}\dbinom{n-j}{k}$
#### Matched solution ID
0
#### Correct solution
定义全集${U}$表示从$1,2,\dots,n$中选出$k$个数字的种数，再定义$A_i(i=1,2,\dots, m)$表示$\mathbb{U}$中必须包含$i$的种数，显然有: \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \binom{n-m}{k-m} = \binom{n-m}{n-k} \end{equation} \par 由容斥原理可得： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = |U| - \sum_i|\complement_UA_i|+\sum_{i<j}|\complement_UA_i \cap \complement_UA_j| - \dots \end{equation} 我们很容易得知： \begin{equation} \sum_{i_1 < i_2 < \dots < i_j}|\complement_UA_{i_1} \cap \complement_UA_{i_2} \cap \dots \cap \complement_UA_{i_j}| = \binom{m}{j}\binom{n-j}{k} \end{equation} 从而我们可以得到： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k} \end{equation} 综合(1)(4)我们的恒等式得证
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中正确地定义了全集 $U$ 和集合 $A_i$，并得出了左侧组合意义 $\dbinom{n-m}{n-k}$。因此，根据评分规则，该部分得分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案正确地定义了全集 $U$ 和集合 $A_i$，并使用了容斥原理来推导恒等式。学生答案中的组合意义与标准答案一致，正确地解释了右侧组合数的组合意义。因此，根据评分规则，该部分得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案正确地应用了容斥原理，通过定义全集$U$和集合$A_i$，并利用容斥原理推导出恒等式$\dbinom{n-m}{n-k}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{m}{j}\dbinom{n-j}{k}$。这一过程与标准答案的思路一致，符合评分规则。 |


### Subproblem (2)
#### Status
graded
#### Answer
（2） 设 $U$ 是从 $\{1,2,\cdots,n,\cdots,n+m-1\}$ 中选 $m-1$ 个数的方案，$A_i(1\le i\le m)$ 是选择数 $i$ 后的方案，则 $|\bar A_1\cap\cdots\cap \bar A_m|$ 为从剩下 $n-1$ 个数中选 $m-1$ 个数的方案数，为 $\dbinom{n-1}{m-1}$，而 $|A_i|=\dbinom{n+m-2}{m-2},|A_{i_1}\cap\cdots\cap A_{i_j}|=\dbinom{n+m-j-1}{m-j-1}$，从而有 $|\bar A_1\cap\cdots\cap \bar A_m|=|U|-\sum|A_i|+\sum|A_i\cap A_j|+\cdots+(-1)^j\sum |A_{i_1}\cap\cdots\cap A_{i_j}|$ 即 $\dbinom{n-1}{m-1}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{m}{j}\dbinom{n+m-j-1}{n}$
#### Matched solution ID
0
#### Correct solution
设 $U$ 是从 $\{1,2,\cdots,n,\cdots,n+m-1\}$ 中选 $m-1$ 个数的方案，$A_i(1\le i\le m)$ 是选择数 $i$ 后的方案，则 $|\bar A_1\cap\cdots\cap \bar A_m|$ 为从剩下 $n-1$ 个数中选 $m-1$ 个数的方案数，为 $\dbinom{n-1}{m-1}$，而 $|A_i|=\dbinom{n+m-2}{m-2},|A_{i_1}\cap\cdots\cap A_{i_j}|=\dbinom{n+m-j-1}{m-j-1}$，从而有 $|\bar A_1\cap\cdots\cap \bar A_m|=|U|-\sum|A_i|+\sum|A_i\cap A_j|+\cdots+(-1)^j\sum |A_{i_1}\cap\cdots\cap A_{i_j}|$ 即 $\dbinom{n-1}{m-1}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{m}{j}\dbinom{n+m-j-1}{n}$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案与标准答案完全一致，正确地描述了左侧组合数的意义，即从剩下的 $n-1$ 个数中选 $m-1$ 个数的方案数为 $\dbinom{n-1}{m-1}$。因此，根据评分规则，该部分得分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案与标准答案完全一致，正确地解释了右侧组合数的组合意义，符合评分规则的要求。因此，该部分得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案完整地应用了容斥原理，正确地描述了从集合中选择元素的方案，并得出了与标准答案一致的结论。因此，根据评分规则，该部分得分。 |


### Subproblem (3)
#### Status
graded
#### Answer
（3） $\dbinom{n+m-1}{n-1}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{n+m}{n+j}$ 左边表示将 $m$ 个相同物品分配给 $n$ 个不同的容器，容器可以为空的方案数。 对于每个 $j$，$\dbinom{n+m}{n+j}$ 计算的是将 $m$ 个球放入 $n$ 个盒子中，但至少有 $j$ 个盒子为空的方法数，用容斥原理得到右侧等于左侧。
#### Matched solution ID
0
#### Correct solution
考虑n+m-1个球，从中选m个的方案数是$C_{n+m-1}^m = C_{n + m - 1}^{n - 1}$ 从另外一种角度考虑，增加一个0号球，那么选m个的方案数是$C_{n+m}^m$，但这可能会选到0号球。于是减去“选0号球，然后所有球里面选m-1个”的方案数$C_{n+m}^{m-1}$，但这可能会再次选到0号球，因此加上选了两次0号球的方案数$C_{n+m}^{m-2}$... 因此总方案数是$\sum_{j=0}^m (-1)^j C_{n + m}^{m-j}$ 故 $$ C_{n + m - 1}^{n - 1} = C_{n+m-1}^m= \sum_{j=0}^m (-1)^j C_{n + m}^{m-j}=\sum_{j=0}^m (-1)^j C_{n + m}^{n + j} $$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中正确解释了左侧的组合意义，即表示将 $m$ 个相同物品分配给 $n$ 个不同的容器，容器可以为空的方案数。这与标准答案中的组合意义一致，因此根据评分规则，该部分得分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案中正确地解释了右侧组合数的组合意义，即使用容斥原理计算将 $m$ 个球放入 $n$ 个盒子中，但至少有 $j$ 个盒子为空的方法数。这与标准答案中的解释一致，因此根据评分规则，该部分得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案正确地应用了容斥原理来解释恒等式，指出左侧表示将 $m$ 个相同物品分配给 $n$ 个不同的容器，容器可以为空的方案数，并通过容斥原理解释了右侧的求和部分。这与标准答案中的思路一致，因此得分为1。 |
| 能说明清楚为什么容斥没有组合数系数 | 1 | 0 | 学生答案中解释了左边表示将 $m$ 个相同物品分配给 $n$ 个不同的容器，容器可以为空的方案数，这与标准答案中的组合意义一致。然而，学生答案没有详细说明为什么容斥没有组合数系数，即为什么右侧的表达式与左侧相等。因此，根据评分规则，未能说明清楚容斥没有组合数系数，扣1分。 |


## Problem 6.2
### Subproblem (1)
#### Status
graded
#### Answer
（1） 设 $A_1$ 为出现 3 个连续的 $a$，$A_2$ 为出现 3 个连续的 $b$，$A_3$ 为出现 3 个连续的 $c$ 的排列情况，$U$ 为不考虑任何约束的排列情况，则答案为 $|\bar A_1\cap\bar A_2\cap\bar A_3|=|U|-\sum_{i=1}^3 |A_i|+\sum_{i<j}|A_i\cap A_j|-|A_1\cap A_2\cap A_3|$。 其中 $|U|=\dfrac{9!}{3!3!3!}=1680,|A_i|=\dfrac{7!}{1!3!3!}=140,|A_i\cap A_j|=\dfrac{5!}{1!1!3!}=20,|A_1\cap A_2\cap A_3|=3!=6$。 从而，答案为 $1680-3*140+3*20-6=1314$。
#### Matched solution ID
0
#### Correct solution
首先不考虑限制的情况：${9! \over 3!3!3!}$ 设$A_3$表示存在连续3个a的方案集合，$B_3$表示存在连续3个b的方案集合，$C_3$表示存在连续3个c的方案集合 对$|A_3|, |B_3|, |C_3|$： 将aaa看成一个字母，故$|A_3|= {7! \over 1!3!3!}= 140 $ 对$|A_3\bigcap B_3|, |A_3\bigcap C_3|, |C_3\bigcap B_3|$ ： 将aaa bbb分别看成一个字母，故$|A_3\bigcap B_3| = {5! \over 1!1!3!}=20$ 对$|A_3\bigcap B_3\bigcap C_3|$ ： 将aaa bbb ccc分别看成一个字母，故$|A_3\bigcap B_3\bigcap C_3| = {3! \over 1!1!1!}=6$ 总方案数为 $$ {9! \over 3!3!3!} - 3*140+20*3-6= 1680 - 420 + 60 - 6 = 1314 $$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 定义集合 | 1 | 1 | 学生答案中正确定义了集合 $A_1$, $A_2$, $A_3$ 和 $U$，并且使用了容斥原理来计算满足条件的排列数目。定义集合的部分与标准答案一致，因此根据评分规则，该部分得分。 |
| 容斥原理 | 2 | 2 | 学生答案正确应用了容斥原理，明确列出了所有相关集合的定义，并正确计算了每个集合的大小以及它们的交集。具体来说，学生答案中正确计算了$|U|$、$|A_i|$、$|A_i \cap A_j|$和$|A_1 \cap A_2 \cap A_3|$，并最终得出了正确的总方案数1314。因此，根据评分规则，该部分得分。 |
| 答案正确 | 1 | 1 | 学生答案正确地应用了容斥原理，计算了不考虑任何约束的排列数 $|U|$，以及存在连续3个相同字母的排列数 $|A_i|$、$|A_i \cap A_j|$ 和 $|A_1 \cap A_2 \cap A_3|$。最终得出的答案 $1314$ 与标准答案一致。因此，根据评分规则，答案正确，得分为1。 |


### Subproblem (2)
#### Status
graded
#### Answer
（2） 设 $B_1$ 为出现 2 个连续的 $a$，$B_2$ 为出现 2 个连续的 $b$，$B_3$ 为出现 2 个连续的 $c$ 的排列情况，$U$ 为不考虑任何约束的排列情况，则答案为 $|\bar B_1\cap\bar B_2\cap\bar B_3|=|U|-\sum_{i=1}^3 |B_i|+\sum_{i<j}|B_i\cap B_j|-|B_1\cap B_2\cap B_3|$。 其中 $|U|=1680,|B_i|=\dfrac{8!}{1!3!3!}=1120,|B_i\cap B_j|=\dfrac{7!}{1!1!3!}=840$ $|B_1\cap B_2\cap B_3|=\dfrac{6!}{1!*1!*1!}=720$ 从而答案为 $1680-3*1120+3*840-720=120$
#### Matched solution ID
0
#### Correct solution
暂时将每个元素均视为不同的，考虑以下九个条件： \begin{itemize} \item $A_1$: $a_2,a_3$ 相邻； \item $A_2$: $a_3,a_1$ 相邻； \item $A_3$: $a_1,a_2$ 相邻； \item $B_1$: $b_2,b_3$ 相邻； \item \ldots \end{itemize} 我们把 $A_1,A_2,A_3$ 称为一组，$B_1,B_2,B_3$ 称为一组，$C_1,C_2,C_3$ 称为一组。注意到同一组中的三个条件，如 $A_1,A_2,A_3$ 不可能同时满足，即 $a_1,a_2,a_3$ 不可能两两相邻。我们需要通过容斥原理，求出九个条件均不满足的方案数。 首先考虑满足一个条件的方案数。我们可以将相邻的那两个元素视为一个整体，这个“整体”内部有两种顺序，故方案数为 $9\times 2\times (2+3+3)!=18\times8!$。 接下来考虑满足两个条件的方案数。如果两个条件处于同一组，即形如 $A_1,A_2$，那么对应的三个元素连续出现。以 $A_1,A_2$ 为例，那么三个 a 会连续出现，且顺序为 $a_2,a_3,a_1$ 或 $a_1,a_3,a_2$。故总方案数为 $3\times\binom{3}{2}\times2\times(1+3+3)!=18\times 7!$。如果两个条件不处于同一组，方案数为 $\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times (2+2+3)!=108\times 7!$。 接下来考虑满足三个条件的方案数。由于同一组中的三个条件（形如 $A_1,A_2,A_3$）不可能同时满足，所以这三个条件一定分布在两组或三组中。如果是两组，根据前文的做法，我们可以计算出总方案数为 \begin{equation} 3\times 2\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times(1+2+3)!=216\times 6!. \end{equation} 如果是三组，方案数为 \begin{equation} \binom{3}{1}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(2+2+2)!=216\times 6!. \end{equation} 接下来考虑满足四个条件的方案数，同理，这四个条件应该形如 $A_i,A_j,B_u,B_v$ 或 $A_i,A_j,B_u,C_v$。如果是前者，方案数为 \begin{equation} \binom{3}{2}\times\binom{3}{2}\times\binom{3}{2}\times2\times 2\times(1+1+3)!=108\times 5!. \end{equation} 如果是后者，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(1+2+2)!=648\times 5!. \end{equation} 接下来考虑满足五个条件的方案数，此时这五个条件一定形如 $A_i,A_j,B_u,B_v,C_w$，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times 2\times(1+1+2)!=648\times 4!. \end{equation} 满足六个条件时，方案数为 \begin{equation} \binom{3}{2}\times \binom{3}{2}\times \binom{3}{2}\times 2\times 2\times 2\times(1+1+1)!=216\times 3!. \end{equation} 由容斥原理，可得没有条件被满足时，总方案数为 \begin{align} &\quad 9!-18\times 8!+18\times 7!+108\times 7!-216\times 6!-216\times 6! \\ &\quad+108\times 5!+648\times 5!-648\times 4!+216\times 3! \\ &=37584. \end{align} 现在去除相同字母内部的顺序，可得总方案数为 \begin{equation} \frac{37584}{3!3!3!}=174. \end{equation}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 捆绑aa,bb,cc并容斥 | 2 | 1 | (二次复查) 学生答案中使用了容斥原理来计算不出现连续相同元素的排列数，这与标准答案的思路一致。然而，学生在计算具体数值时出现了错误。例如，学生计算 $|U|$ 为 1680，而标准答案中 $|U|$ 应为 $9!/(3!3!3!)=1680$，这部分是正确的。但学生在计算 $|B_i|$ 时使用了错误的公式，应为 $8!/(1!3!3!)=1120$，这部分也是正确的。然而，学生在计算 $|B_i\cap B_j|$ 和 $|B_1\cap B_2\cap B_3|$ 时也出现了错误，导致最终答案不正确。尽管学生在思路上与标准答案一致，但由于具体计算错误，最终答案不正确。因此，给予部分分数。 |
| 考虑到aaa,bbb,ccc的情况并容斥 | 2 | 0 | 学生答案中未考虑到aaa,bbb,ccc的情况，并且容斥原理的应用不完整，导致最终答案错误。因此，根据评分规则，该部分不得分。 |
| 答案正确 | 2 | 0 | 学生答案中使用了容斥原理来计算满足条件的排列数目，但计算过程中存在错误。首先，学生计算的总排列数 $|U|$ 为 1680，而标准答案中为 9! = 362880，学生未正确考虑所有元素的排列。其次，学生计算 $|B_i|$ 为 1120，而标准答案中为 $18 \times 8! = 725760$，学生未正确考虑相邻元素的排列。最后，学生计算 $|B_i \cap B_j|$ 为 840，而标准答案中为 $18 \times 7! = 90720$，学生未正确考虑两个相邻对的排列。因此，学生答案与标准答案不符，未能正确计算满足条件的排列数目。 |


## Problem 6.3
### Subproblem (1)
#### Status
graded
#### Answer
解： 做换元，$x_1\rightarrow x_1'+6,x_2\rightarrow x_2'+5,x_3\rightarrow x_3+10$，得到方程 $x_1'+x_2'+x_3'=19\quad\quad (0\le x_1'\le 9,0\le x_2'\le 15,0\le x_3'\le 15)$ 令全集 $U$ 表示不考虑各变量的取值约束时上述方程的全体非负整数解构成的集合，$A$ 表示此方程的全体整数解构成的集合；$A_1,A_2,A_3$ 分别代表变量 $x_1',x_2',x_3'$ 不满足各自的取值约束时的非负整数解构成的集合，即 $A_1=\{x_1'+x_2'+x_3'=19|x_1',x_2',x_3'\in\Z^*,x_1'\ge 10\}$ $A_2=\{x_1'+x_2'+x_3'=19|x_1',x_2',x_3'\in\Z^*,x_2'\ge 16\}$ $A_3=\{x_1'+x_2'+x_3'=19|x_1',x_2',x_3'\in\Z^*,x_3'\ge 16\}$ 则有 $A=\bar A_1\cap \bar A_2\cap \bar A_3$ 考虑集合 $A_1$，其中的解均有 $x_1'\ge 10$，于是做换元 $x_1'\rightarrow y_1+10$，从而将方程化为 $y_1+x_2'+x_3'=19-10=9$，此方程的非负整数解数目为 $|A_1|=\dbinom{9+3-1}{9}=\dbinom{11}{2}$ 同理可得有 $|A_2|=\dbinom{5}{2},|A_3|=\dbinom{5}{2}$ $A_1,A_2,A_3$ 中两个集合的交集代表 $x_1',x_2',x_3'$ 中的某两个变量同时不满足其上界约束，因此同时做换元，同理可得 $|A_1\cap A_2|=0,|A_1\cap A_3|=0,|A_2\cap A_3|=0$，且有 $|A_1\cap A_2\cap A_3|=0$。 从而有 $|A|=|\bar A_1\cap \bar A_2\cap \bar A_3|=\dbinom{21}{2}-\left[\dbinom{11}{2}+\dbinom{5}{2}+\dbinom{5}{2}\right]=135$ 故原方程共有 135 组整数解
#### Matched solution ID
0
#### Correct solution
记 $x_1=y_1+5,x_2=y_2+4,x_3=y_3+9$，则 \begin{equation} 40=x_1+x_2+x_3=y_1+y_2+y_3+5+4+9=y_1+y_2+y_3+18. \end{equation} 故 $y_1+y_2+y_3=22$，且 $1\le y_1\le 10,1\le y_2\le 16,1\le y_3\le 16$。 不考虑上界时，解共有 \begin{equation} \binom{22-1}{3-1}=\binom{21}{2}=210. \end{equation} 若 $y_1\gt 10$，记 $y_1=z_1+10$，则 $z_1\ge 1$ 且 $z_1+y_2+y_3=12$，此时解的个数共有 \begin{equation} \binom{12-1}{3-1}=\binom{11}{2}=55. \end{equation} 同理，若 $y_2\gt 16$，解共有 \begin{equation} \binom{22-16-1}{3-1}=\binom{5}{2}=10. \end{equation} 同理，若 $y_3\gt 16$，解共有 10 个。 由于$y_1+y_2+y_3=22\lt (10+1)+(16+1)$，不可能有至少两个变量超出上界。故原问题的整数解数目为 \begin{equation} 210-55-10-10=135. \end{equation}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 换元正确 | 1 | 1 | 学生答案中的换元步骤与标准答案一致，均正确地将原变量转换为新变量，并调整了取值范围。因此，根据评分规则，该部分得分。 |
| 计算总情况数 | 2 | 2 | 学生答案中正确计算了总情况数，得出了与标准答案一致的135组整数解。因此，根据评分规则，该部分得分。 |
| 计算一个超出上界的情况 | 2 | 2 | 学生答案中详细描述了如何通过换元将原问题转化为一个更简单的方程，并正确地应用了容斥原理来计算满足条件的整数解数目。特别是在计算一个超出上界的情况时，学生正确地使用了组合数公式，并得出了正确的结论。因此，根据评分规则，该部分得分。 |
| 计算两个超出上界的情况 | 2 | 2 | 学生答案中详细计算了两个变量超出上界的情况，即 $y_2 > 16$ 和 $y_3 > 16$，并正确使用了容斥原理进行了计算。因此，根据评分规则，该部分得分。 |
| 计算三个超出上界的情况 | 2 | 2 | 学生答案中详细计算了三个变量超出上界的情况，并正确应用了容斥原理，得出了正确的整数解数目135。因此，根据评分规则，该部分得分。 |
| 容斥原理得到答案 | 1 | 1 | 学生答案正确地应用了容斥原理，通过换元将原问题转化为非负整数解的问题，并详细计算了各集合的大小及其交集，最终得到了正确的答案135。因此，根据评分规则，该部分得分。 |


## PA Report
### Problem 6.1
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 3 | 3 |
| (2) | graded | 3 | 3 |
| (3) | graded | 3 | 4 |
| | | **9** | **10** |
### Problem 6.2
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 4 | 4 |
| (2) | graded | 1 | 6 |
| | | **5** | **10** |
### Problem 6.3
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
## Total
| Score | Total |
| --- | --- |
| 24 | 30 |