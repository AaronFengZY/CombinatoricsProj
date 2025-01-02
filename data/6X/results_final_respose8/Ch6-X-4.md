## Problem 6.1
### Subproblem (1)
#### Status
graded
#### Answer
\subsubsection{(a)} \textbf{Proof}: \par 我们定义全集${U}$表示从$1,2,\dots,n$中选出$k$个数字的种数，再定义$A_i(i=1,2,\dots, m)$表示$\mathbb{U}$中必须包含$i$的种数，显然我们有: \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \binom{n-m}{k-m} = \binom{n-m}{n-k} \end{equation} \par 由容斥原理可得： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = |U| - \sum_i|\complement_UA_i|+\sum_{i<j}|\complement_UA_i \cap \complement_UA_j| - \dots \end{equation} 我们很容易得知： \begin{equation} \sum_{i_1 < i_2 < \dots < i_j}|\complement_UA_{i_1} \cap \complement_UA_{i_2} \cap \dots \cap \complement_UA_{i_j}| = \binom{m}{j}\binom{n-j}{k} \end{equation} 从而我们可以得到： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k} \end{equation} 综合(1)(4)我们的恒等式得证！
#### Matched solution ID
0
#### Correct solution
定义全集${U}$表示从$1,2,\dots,n$中选出$k$个数字的种数，再定义$A_i(i=1,2,\dots, m)$表示$\mathbb{U}$中必须包含$i$的种数，显然有: \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \binom{n-m}{k-m} = \binom{n-m}{n-k} \end{equation} \par 由容斥原理可得： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = |U| - \sum_i|\complement_UA_i|+\sum_{i<j}|\complement_UA_i \cap \complement_UA_j| - \dots \end{equation} 我们很容易得知： \begin{equation} \sum_{i_1 < i_2 < \dots < i_j}|\complement_UA_{i_1} \cap \complement_UA_{i_2} \cap \dots \cap \complement_UA_{i_j}| = \binom{m}{j}\binom{n-j}{k} \end{equation} 从而我们可以得到： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k} \end{equation} 综合(1)(4)我们的恒等式得证
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中，左侧组合意义的解释与标准答案一致，得1分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案与标准答案在定义全集、应用容斥原理以及推导恒等式方面完全一致，因此得分为1。 |
| 应用容斥原理 | 1 | 1 | 学生答案与标准答案在应用容斥原理的部分完全一致，正确地使用了容斥原理来推导恒等式。因此，根据评分规则，学生在这一部分得分。 |


### Subproblem (2)
#### Status
graded
#### Answer
\subsubsection{(b)} \textbf{Proof}: \par 定义全集${U}=\{(x_1,x_2,\dots,x_n)|x_1+x_2+\dots+x_m=n,x_i\geq 0,i=1,2,\dots,n\}$。然后我们定义全集$\mathbb{U}$的子集族$A_i=\{(x_1,x_2,\dots,x_n)|x_1+x_2+\dots+x_m=n,x_j\geq 0,j=1,2,\dots,i-1, i+1, \dots, n, x_i\geq 1\}, i = 1, 2, \dots m$，首先我们容易得到： \begin{equation} |A_1\cap A_2\cap \dots \cap A_m| = \binom{n-1}{m-1} \end{equation} 由容斥原理可知： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = |U| - \sum_i|\complement_UA_i|+\sum_{i<j}|\complement_UA_i \cap \complement_UA_j| - \dots \end{equation} 我们可以通过不定方程的非负解的数量得到下述结论： \begin{equation} \sum_{i_1 < i_2 < \dots < i_j}|\complement_UA_{i_1} \cap \complement_UA_{i_2} \cap \dots \cap \complement_UA_{i_j}| = \binom{m}{j}\binom{n+m-j-1}{n} \end{equation} 从而我们可以得到： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n+m-j-1}{n} \end{equation} 综合(5)和(8)我们可知结论恒等式成立！
#### Matched solution ID
0
#### Correct solution
设 $U$ 是从 $\{1,2,\cdots,n,\cdots,n+m-1\}$ 中选 $m-1$ 个数的方案，$A_i(1\le i\le m)$ 是选择数 $i$ 后的方案，则 $|\bar A_1\cap\cdots\cap \bar A_m|$ 为从剩下 $n-1$ 个数中选 $m-1$ 个数的方案数，为 $\dbinom{n-1}{m-1}$，而 $|A_i|=\dbinom{n+m-2}{m-2},|A_{i_1}\cap\cdots\cap A_{i_j}|=\dbinom{n+m-j-1}{m-j-1}$，从而有 $|\bar A_1\cap\cdots\cap \bar A_m|=|U|-\sum|A_i|+\sum|A_i\cap A_j|+\cdots+(-1)^j\sum |A_{i_1}\cap\cdots\cap A_{i_j}|$ 即 $\dbinom{n-1}{m-1}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{m}{j}\dbinom{n+m-j-1}{n}$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中，左侧组合意义的部分与标准答案一致，得1分。 |
| 右侧组合数的组合意义 | 1 | 0 | 学生答案中，右侧组合数的组合意义部分与标准答案不符。标准答案中明确解释了从全集$U$中选$m-1$个数的方案，并通过容斥原理推导出右侧的组合数表达式。而学生答案中虽然提到了容斥原理，但对右侧组合数的组合意义的解释不够清晰，且未完全符合标准答案的推导过程。因此，该部分不得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案中应用了容斥原理，但定义的全集和子集族与标准答案不符，且推导过程不够严谨。虽然最终得出了正确的结论，但缺乏对组合场景的清晰解释和严格的逻辑推理。因此，根据评分标准，学生答案在应用容斥原理方面得分。 |


### Subproblem (3)
#### Status
error
#### Answer
\subsubsection{(c)} \textbf{Proof}: \par 我们用数学归纳法证明结论，对$m$归纳，$m=0$时结论显然成立，下面我们假设结论对$m-1$成立，那么： \begin{equation} \binom{n+m-1}{n-1}=\binom{n+m}{n} - \binom{n+m-1}{n}=\binom{n+m}{n}-\binom{(n+1)+(m-1)-1}{(n+1)-1} \end{equation} 利用$m-1$的结论，我们可以继续化简: \begin{equation} \begin{split} \binom{n+m}{n}-\binom{(n+1)+(m-1)-1}{(n+1)-1} &= \binom{n+m}{n} - \sum_{j=0}^{m-1}(-1)^j\binom{n+1+m-1}{n+1+j} \\ &= \binom{n+m}{n} + \sum_{j=0}^{m-1}(-1)^{j+1}\binom{n+m}{n+(j+1)} \\ &= \sum_{j=0}^m(-1)^j\binom{n+m}{n+j} \end{split} \end{equation}
#### Matched solution ID
0
#### Correct solution
考虑n+m-1个球，从中选m个的方案数是$C_{n+m-1}^m = C_{n + m - 1}^{n - 1}$ 从另外一种角度考虑，增加一个0号球，那么选m个的方案数是$C_{n+m}^m$，但这可能会选到0号球。于是减去“选0号球，然后所有球里面选m-1个”的方案数$C_{n+m}^{m-1}$，但这可能会再次选到0号球，因此加上选了两次0号球的方案数$C_{n+m}^{m-2}$... 因此总方案数是$\sum_{j=0}^m (-1)^j C_{n + m}^{m-j}$ 故 $$ C_{n + m - 1}^{n - 1} = C_{n+m-1}^m= \sum_{j=0}^m (-1)^j C_{n + m}^{m-j}=\sum_{j=0}^m (-1)^j C_{n + m}^{n + j} $$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 0 | 学生答案中使用了数学归纳法来证明恒等式，但并未直接解释左侧组合数的组合意义。标准答案中明确解释了左侧组合数的组合意义，即从n+m-1个球中选m个的方案数。学生答案未直接提及这一点，因此无法得分。 |
| 右侧组合数的组合意义 | 1 | 0 | 学生答案中未明确解释右侧组合数的组合意义，而是使用了数学归纳法进行证明，这与评分规则中要求解释组合意义的要求不符。因此，无法获得该评分点的分数。 |
| 应用容斥原理 | 1 | 0 | 学生答案中使用了数学归纳法来证明恒等式，但并未明确应用容斥原理。标准答案中通过容斥原理解释了恒等式的组合意义，而学生答案中并未体现这一关键步骤。因此，学生答案未能满足评分规则中关于应用容斥原理的要求。 |
| 能说明清楚为什么容斥没有组合数系数 | 1 | 0 | 学生答案中使用了数学归纳法来证明恒等式，但并未说明清楚为什么容斥没有组合数系数。标准答案中通过增加一个0号球并应用容斥原理，清晰地解释了为什么容斥没有组合数系数。因此，学生答案未能满足评分规则中的要求。 |

#### Trace
二次复查后仍为 0 分

## Problem 6.2
### Subproblem (1)
#### Status
graded
#### Answer
我们定义我们定义集合$A$表示没有连续的三个a的所有可能多重排列，同理定义集合$B$和$C$分别表示没有连续三个b和没有连续三个c的所有可能的多重排列，那么$|A\cap B \cap C|$即为结果。我们定义$U$为全集，即所有多重排列。根据容斥原理： \begin{equation} \begin{split} |A\cap B \cap C| &= |U| - |\complement_UA| - |\complement_UB| - |\complement_UC| + |\complement_UA\cap\complement_UB| + |\complement_UA\cap\complement_UC| + |\complement_UB\cap\complement_UC| \\ &- |\complement_UA\cap\complement_UB\complement_UC| \\ &=\frac{9!}{3!3!3!}-3\times 7\times \frac{6!}{3!3!} + 3\times 2\times(4+3+2+1) - 3! \\ &= 1314 \end{split} \end{equation}
#### Matched solution ID
0
#### Correct solution
首先不考虑限制的情况：${9! \over 3!3!3!}$ 设$A_3$表示存在连续3个a的方案集合，$B_3$表示存在连续3个b的方案集合，$C_3$表示存在连续3个c的方案集合 对$|A_3|, |B_3|, |C_3|$： 将aaa看成一个字母，故$|A_3|= {7! \over 1!3!3!}= 140 $ 对$|A_3\bigcap B_3|, |A_3\bigcap C_3|, |C_3\bigcap B_3|$ ： 将aaa bbb分别看成一个字母，故$|A_3\bigcap B_3| = {5! \over 1!1!3!}=20$ 对$|A_3\bigcap B_3\bigcap C_3|$ ： 将aaa bbb ccc分别看成一个字母，故$|A_3\bigcap B_3\bigcap C_3| = {3! \over 1!1!1!}=6$ 总方案数为 $$ {9! \over 3!3!3!} - 3*140+20*3-6= 1680 - 420 + 60 - 6 = 1314 $$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 定义集合 | 1 | 1 | 学生答案中定义了集合$A$、$B$、$C$，并正确应用了容斥原理来计算$|A\cap B \cap C|$。虽然计算过程中有些步骤的表达式不够清晰，但最终结果与标准答案一致，得分为1分。 |
| 容斥原理 | 2 | 2 | 学生答案中正确应用了容斥原理，并得出了与标准答案一致的最终结果1314。虽然表达方式与标准答案略有不同，但逻辑推理和计算过程均正确。因此，根据评分规则，学生答案在容斥原理的应用上得分。 |
| 答案正确 | 1 | 1 | 学生答案中使用了容斥原理，并正确计算了总排列数减去不满足条件的排列数，最终得到了与标准答案一致的结果1314。因此，答案正确。 |


### Subproblem (2)
#### Status
error
#### Answer

#### Matched solution ID
0
#### Correct solution
暂时将每个元素均视为不同的，考虑以下九个条件： \begin{itemize} \item $A_1$: $a_2,a_3$ 相邻； \item $A_2$: $a_3,a_1$ 相邻； \item $A_3$: $a_1,a_2$ 相邻； \item $B_1$: $b_2,b_3$ 相邻； \item \ldots \end{itemize} 我们把 $A_1,A_2,A_3$ 称为一组，$B_1,B_2,B_3$ 称为一组，$C_1,C_2,C_3$ 称为一组。注意到同一组中的三个条件，如 $A_1,A_2,A_3$ 不可能同时满足，即 $a_1,a_2,a_3$ 不可能两两相邻。我们需要通过容斥原理，求出九个条件均不满足的方案数。 首先考虑满足一个条件的方案数。我们可以将相邻的那两个元素视为一个整体，这个“整体”内部有两种顺序，故方案数为 $9\times 2\times (2+3+3)!=18\times8!$。 接下来考虑满足两个条件的方案数。如果两个条件处于同一组，即形如 $A_1,A_2$，那么对应的三个元素连续出现。以 $A_1,A_2$ 为例，那么三个 a 会连续出现，且顺序为 $a_2,a_3,a_1$ 或 $a_1,a_3,a_2$。故总方案数为 $3\times\binom{3}{2}\times2\times(1+3+3)!=18\times 7!$。如果两个条件不处于同一组，方案数为 $\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times (2+2+3)!=108\times 7!$。 接下来考虑满足三个条件的方案数。由于同一组中的三个条件（形如 $A_1,A_2,A_3$）不可能同时满足，所以这三个条件一定分布在两组或三组中。如果是两组，根据前文的做法，我们可以计算出总方案数为 \begin{equation} 3\times 2\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times(1+2+3)!=216\times 6!. \end{equation} 如果是三组，方案数为 \begin{equation} \binom{3}{1}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(2+2+2)!=216\times 6!. \end{equation} 接下来考虑满足四个条件的方案数，同理，这四个条件应该形如 $A_i,A_j,B_u,B_v$ 或 $A_i,A_j,B_u,C_v$。如果是前者，方案数为 \begin{equation} \binom{3}{2}\times\binom{3}{2}\times\binom{3}{2}\times2\times 2\times(1+1+3)!=108\times 5!. \end{equation} 如果是后者，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(1+2+2)!=648\times 5!. \end{equation} 接下来考虑满足五个条件的方案数，此时这五个条件一定形如 $A_i,A_j,B_u,B_v,C_w$，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times 2\times(1+1+2)!=648\times 4!. \end{equation} 满足六个条件时，方案数为 \begin{equation} \binom{3}{2}\times \binom{3}{2}\times \binom{3}{2}\times 2\times 2\times 2\times(1+1+1)!=216\times 3!. \end{equation} 由容斥原理，可得没有条件被满足时，总方案数为 \begin{align} &\quad 9!-18\times 8!+18\times 7!+108\times 7!-216\times 6!-216\times 6! \\ &\quad+108\times 5!+648\times 5!-648\times 4!+216\times 3! \\ &=37584. \end{align} 现在去除相同字母内部的顺序，可得总方案数为 \begin{equation} \frac{37584}{3!3!3!}=174. \end{equation}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 捆绑aa,bb,cc并容斥 | 2 | 0 | 学生答案空白，未提供任何解答内容，因此无法获得任何分值。 |
| 考虑到aaa,bbb,ccc的情况并容斥 | 2 | 0 | 学生答案空白，未提供任何解答内容，因此无法得分。 |
| 答案正确 | 2 | 0 | 学生答案为空，未提供任何解答内容，因此无法得分。 |

#### Trace
二次复查后仍为 0 分

## Problem 6.3
### Subproblem (1)
#### Status
graded
#### Answer
定义集合$A=\{(x_1,x_2,x_3)\in\mathbb{Z}^3|x_1+x_2+x_3=19, 0\leq x_1\leq 9\}$, $B=\{(x_1,x_2,x_3)\in\mathbb{Z}^3|x_1+x_2+x_3=19, 0\leq x_2\leq 15\}$, $C=\{(x_1,x_2,x_3)\in\mathbb{Z}^3|x_1+x_2+x_3=19, 0\leq x_3\leq 15\}$(这里我们都减掉了偏置项）。从而$|A\cap B\cap C|$是我们待求结果。我们通过容斥原理计算: \begin{equation} \begin{split} |A\cap B \cap C| &= |U| - |\complement_UA| - |\complement_UB| - |\complement_UC| + |\complement_UA\cap\complement_UB| + |\complement_UA\cap\complement_UC| + |\complement_UB\cap\complement_UC| \\ &- |\complement_UA\cap\complement_UB\complement_UC| \\ &= \binom{21}{2} - \binom{11}{2} - \binom{5}{2} - \binom{5}{2} + 0 + 0 + 0 - 0 \\ &= 135 \end{split} \end{equation}
#### Matched solution ID
0
#### Correct solution
记 $x_1=y_1+5,x_2=y_2+4,x_3=y_3+9$，则 \begin{equation} 40=x_1+x_2+x_3=y_1+y_2+y_3+5+4+9=y_1+y_2+y_3+18. \end{equation} 故 $y_1+y_2+y_3=22$，且 $1\le y_1\le 10,1\le y_2\le 16,1\le y_3\le 16$。 不考虑上界时，解共有 \begin{equation} \binom{22-1}{3-1}=\binom{21}{2}=210. \end{equation} 若 $y_1\gt 10$，记 $y_1=z_1+10$，则 $z_1\ge 1$ 且 $z_1+y_2+y_3=12$，此时解的个数共有 \begin{equation} \binom{12-1}{3-1}=\binom{11}{2}=55. \end{equation} 同理，若 $y_2\gt 16$，解共有 \begin{equation} \binom{22-16-1}{3-1}=\binom{5}{2}=10. \end{equation} 同理，若 $y_3\gt 16$，解共有 10 个。 由于$y_1+y_2+y_3=22\lt (10+1)+(16+1)$，不可能有至少两个变量超出上界。故原问题的整数解数目为 \begin{equation} 210-55-10-10=135. \end{equation}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 换元正确 | 1 | 0 | 学生答案中未进行换元操作，而是直接使用了容斥原理进行计算。虽然最终结果正确，但未按照题目要求进行换元，因此无法获得换元正确的分值。 |
| 计算总情况数 | 2 | 2 | 学生答案通过定义集合和容斥原理计算了整数解的数目，最终得到了正确的结果135。虽然表达方式与标准答案不同，但逻辑正确且结果一致。因此，根据评分规则，学生答案在计算总情况数这一评分点上得分。 |
| 计算一个超出上界的情况 | 2 | 2 | 学生答案中正确地计算了一个超出上界的情况，即当 $y_1 > 10$ 时，解的个数为 55。这一步骤与标准答案一致，符合评分规则的要求。 |
| 计算两个超出上界的情况 | 2 | 2 | 学生答案中正确地计算了两个超出上界的情况，即$y_1>10$和$y_2>16$，分别得到了55和10的解数，与标准答案一致。因此，学生在这一评分点上获得了满分。 |
| 计算三个超出上界的情况 | 2 | 2 | 学生答案中正确计算了三个超出上界的情况，分别对应y1>10、y2>16和y3>16的情况，并正确应用了容斥原理进行求解。因此，符合评分规则的要求。 |
| 容斥原理得到答案 | 1 | 1 | 学生答案通过容斥原理正确计算了整数解的数目，得出了与标准答案一致的结果135。因此，根据评分规则，学生答案符合要求，得1分。 |


## PA Report
### Problem 6.1
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 3 | 3 |
| (2) | graded | 2 | 3 |
| (3) | error | N/A | N/A |
| | | **5** | **6** |
### Problem 6.2
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 4 | 4 |
| (2) | error | N/A | N/A |
| | | **4** | **4** |
### Problem 6.3
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 9 | 10 |
| | | **9** | **10** |
## Total
| Score | Total |
| --- | --- |
| 18 | 20 |