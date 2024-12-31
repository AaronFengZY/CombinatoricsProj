## Problem 6.1
### Subproblem (1)
#### Status
graded
#### Answer
\paragraph{(1)} 考虑如下问题：从 $1,2,\ldots,n$ 中选择 $n-k$ 个元素，且 $1,2,\ldots,m$ 不能被选取，共有多少种方案？由于 $1,2,\ldots,m$ 不能被选取，相当于从剩下 $n-m$ 个中选取 $n-k$ 个，共 $\binom{n-m}{n-k}$ 种方案。 另一方面，将“选取”与“不选取”反转，原问题等价于，从 $1,2,\ldots,n$ 中选择 $k$ 个元素，且 $1,2,\ldots,m$ 必须被选取。考虑 $1,2,\ldots,m$ 中的特定 $j$ 个元素 $a_1,a_2,\ldots,a_j$，它们\textbf{没有}被选取的方案数为 $\binom{n-j}{k}$。而 $a_1,a_2,\ldots,a_j$ 的选取共有 $\binom{m}{j}$ 种。使用容斥原理， $1,2,\ldots,m$ 均被选取的方案数为 \begin{equation} \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k}. \end{equation} 于是我们证明了 \begin{equation} \binom{n-m}{n-k}=\sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k}. \end{equation}
#### Matched solution ID
0
#### Correct solution
定义全集${U}$表示从$1,2,\dots,n$中选出$k$个数字的种数，再定义$A_i(i=1,2,\dots, m)$表示$\mathbb{U}$中必须包含$i$的种数，显然有: \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \binom{n-m}{k-m} = \binom{n-m}{n-k} \end{equation} \par 由容斥原理可得： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = |U| - \sum_i|\complement_UA_i|+\sum_{i<j}|\complement_UA_i \cap \complement_UA_j| - \dots \end{equation} 我们很容易得知： \begin{equation} \sum_{i_1 < i_2 < \dots < i_j}|\complement_UA_{i_1} \cap \complement_UA_{i_2} \cap \dots \cap \complement_UA_{i_j}| = \binom{m}{j}\binom{n-j}{k} \end{equation} 从而我们可以得到： \begin{equation} |A_1 \cap A_2 \cap \dots \cap A_m| = \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k} \end{equation} 综合(1)(4)我们的恒等式得证
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中正确地解释了左侧组合数的意义，即从 $1,2,\ldots,n$ 中选择 $n-k$ 个元素，且 $1,2,\ldots,m$ 不能被选取的方案数为 $\binom{n-m}{n-k}$。这与标准答案中的定义一致，因此根据评分规则，该部分得分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案中正确解释了右侧组合数的组合意义，即从 $1,2,\ldots,n$ 中选择 $k$ 个元素，且 $1,2,\ldots,m$ 必须被选取的方案数。这一解释与标准答案中的容斥原理应用一致，符合评分规则的要求。因此，该部分得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案中正确应用了容斥原理，解释了从 $1,2,\ldots,n$ 中选择 $k$ 个元素且 $1,2,\ldots,m$ 必须被选取的方案数，并通过容斥原理推导出 $\sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n-j}{k}$。这一过程与标准答案中的容斥原理应用一致，因此得分。 |


### Subproblem (2)
#### Status
graded
#### Answer
\paragraph{(2)} 这一问的思路与上一问类似，考虑如下问题：从 $1,2,\ldots,n+m-1$ 中选取 $m-1$ 个元素，且 $1,2,\ldots,m$ 不能被选取，共有多少种方案？由于 $1,2,\ldots,m$ 不能被选取，相当于从剩下 $n-1$ 个中选取 $m-1$ 个，共 $\binom{n-1}{m-1}$ 种方案。 另一方面，将“选取”与“不选取”反转，原问题等价于，从 $1,2,\ldots,n+m-1$ 中选择 $n$ 个元素，且 $1,2,\ldots,m$ 必须被选取。同样考虑 $1,2,\ldots,m$ 中的特定 $j$ 个元素 $a_1,a_2,\ldots,a_j$，它们\textbf{没有}被选取的方案数为 $\binom{n+m-j-1}{n}$。而 $a_1,a_2,\ldots,a_j$ 的选取共有 $\binom{m}{j}$ 种。使用容斥原理， $1,2,\ldots,m$ 均被选取的方案数为 \begin{equation} \sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n+m-j-1}{n}. \end{equation} 于是我们证明了 \begin{equation} \binom{n-1}{m-1}=\sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n+m-j-1}{n}. \end{equation}
#### Matched solution ID
0
#### Correct solution
设 $U$ 是从 $\{1,2,\cdots,n,\cdots,n+m-1\}$ 中选 $m-1$ 个数的方案，$A_i(1\le i\le m)$ 是选择数 $i$ 后的方案，则 $|\bar A_1\cap\cdots\cap \bar A_m|$ 为从剩下 $n-1$ 个数中选 $m-1$ 个数的方案数，为 $\dbinom{n-1}{m-1}$，而 $|A_i|=\dbinom{n+m-2}{m-2},|A_{i_1}\cap\cdots\cap A_{i_j}|=\dbinom{n+m-j-1}{m-j-1}$，从而有 $|\bar A_1\cap\cdots\cap \bar A_m|=|U|-\sum|A_i|+\sum|A_i\cap A_j|+\cdots+(-1)^j\sum |A_{i_1}\cap\cdots\cap A_{i_j}|$ 即 $\dbinom{n-1}{m-1}=\displaystyle\sum_{j=0}^m(-1)^j\dbinom{m}{j}\dbinom{n+m-j-1}{n}$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中正确地描述了从 $1,2,\ldots,n+m-1$ 中选取 $m-1$ 个元素且 $1,2,\ldots,m$ 不能被选取的组合意义，即从剩下 $n-1$ 个中选取 $m-1$ 个，共 $\binom{n-1}{m-1}$ 种方案。这与标准答案中的组合意义一致，因此根据评分规则，该部分得分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案中正确地解释了右侧组合数的组合意义，即从 $1,2,\ldots,n+m-1$ 中选择 $n$ 个元素，且 $1,2,\ldots,m$ 必须被选取的方案数。这一解释与标准答案中的容斥原理应用一致，符合评分规则的要求。因此，该部分得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案正确地应用了容斥原理，解释了从 $1,2,\ldots,n+m-1$ 中选取 $m-1$ 个元素且 $1,2,\ldots,m$ 不能被选取的方案数，并通过反转问题的方式，使用容斥原理推导出了等式 $\binom{n-1}{m-1}=\sum_{j=0}^m(-1)^j\binom{m}{j}\binom{n+m-j-1}{n}$。因此，根据评分规则，该部分得分。 |


### Subproblem (3)
#### Status
graded
#### Answer
\paragraph{(3)} 考虑如下问题，从 $1,2,\ldots,n+m$ 中选取 $n$ 个元素，且必须选取 1，共有多少种方案？这相当于从余下 $n+m-1$ 个元素中 选取 $n-1$ 个，故总方案数为 $\binom{n+m-1}{n-1}$。另一方面，我们可以先不考虑“必须选取1”这个限制，再减去没有选取 1 的方案数，故总方案数为 \begin{equation} \binom{n+m}{n}-\binom{n+m-1}{n}. \end{equation} 于是我们有 \begin{equation} \binom{n+m-1}{n-1}=\binom{n+m}{n}-\binom{n+m-1}{n}. \end{equation} 另一方面，$\binom{n+m-1}{n}$ 这一项，可以看作从 $1,2,\ldots,n+m$ 中选取 $n+1$ 个元素，且必须选取 1 的方案数，再次运用上述的方法，可以得到 \begin{equation} \binom{n+m-1}{n}=\binom{n+m}{n+1}-\binom{n+m-1}{n+1}. \end{equation} 同理我们可以得到，对 $j=0,1,2,\ldots,m$ \begin{equation} \binom{n+m-1}{n+j-1}=\binom{n+m}{n+j}-\binom{n+m-1}{n+j}. \end{equation} 反复代入，可以得到 \begin{equation} \binom{n+m-1}{n-1}=\sum_{j=0}^m(-1)^j\binom{n+m}{n+j}. \end{equation}
#### Matched solution ID
0
#### Correct solution
考虑n+m-1个球，从中选m个的方案数是$C_{n+m-1}^m = C_{n + m - 1}^{n - 1}$ 从另外一种角度考虑，增加一个0号球，那么选m个的方案数是$C_{n+m}^m$，但这可能会选到0号球。于是减去“选0号球，然后所有球里面选m-1个”的方案数$C_{n+m}^{m-1}$，但这可能会再次选到0号球，因此加上选了两次0号球的方案数$C_{n+m}^{m-2}$... 因此总方案数是$\sum_{j=0}^m (-1)^j C_{n + m}^{m-j}$ 故 $$ C_{n + m - 1}^{n - 1} = C_{n+m-1}^m= \sum_{j=0}^m (-1)^j C_{n + m}^{m-j}=\sum_{j=0}^m (-1)^j C_{n + m}^{n + j} $$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得出左侧组合意义 | 1 | 1 | 学生答案中正确解释了左侧组合数 $\binom{n+m-1}{n-1}$ 的组合意义，即从 $1,2,\ldots,n+m$ 中选取 $n$ 个元素且必须选取 1 的方案数。这与标准答案中的解释一致，因此根据评分规则，该部分得分。 |
| 右侧组合数的组合意义 | 1 | 1 | 学生答案中解释了右侧组合数的组合意义，通过反复代入的方法推导出了恒等式，与标准答案的思路基本一致。因此，根据评分规则，该部分得分。 |
| 应用容斥原理 | 1 | 1 | 学生答案通过容斥原理解释了恒等式的组合意义，虽然具体步骤与标准答案有所不同，但整体思路和应用容斥原理的方法是正确的。因此，根据评分规则，该部分得分。 |
| 能说明清楚为什么容斥没有组合数系数 | 1 | 0 | 学生答案中未能说明清楚为什么容斥没有组合数系数，因此根据评分规则，该部分不得分。 |


## Problem 6.2
### Subproblem (1)
#### Status
graded
#### Answer
\paragraph{(1)} 如果有连续3个元素相同，那一定是连续三个 a，三个 b，或三个 c。将三个 a 看成一个整体，三个 a 连续出现的方案数为 \begin{equation} \frac{(1+3+3)!}{1!3!3!}=\frac{7!}{3!3!}=140. \end{equation} 三个 a 同时出现，且三个 b 同时出现的方案数为 \begin{equation} \frac{(1+1+3)!}{1!1!3!}=\frac{5!}{3!}=20. \end{equation} 三个 a，三个 b，三个 c 均同时出现的方案数为 $3!=6$。由容斥原理，任何连续三个元素不能全相同的方案数为 \begin{equation} \frac{(3+3+3)!}{3!3!3!}-3\times 140+3\times 20-6=1314. \end{equation} % \paragraph{(2)} 考虑“出现了相邻的 a”的总方案数。将两个 a 视作一个整体，共 % \begin{equation} % \frac{(2+3+3)!}{2!3!3!}=560. % \end{equation} % 但是在上述的计算中，三个 a 相邻的排列会被计算两次，故总方案数为 % \begin{equation} % 560-140=420. % \end{equation} % 同理，出现了相邻的 a，也出现了相邻的 b，方案数为 % \begin{equation} % \frac{(2+2+3)!}{2!2!3!}-2\times\frac{(2+1+3)!}{2!1!3!}+20=110 % \end{equation} % 类似地，abc 均相邻地出现过，方案数为 % \begin{equation} % \frac{(2+2+2)!}{2!2!2!}-3\times\frac{(1+2+2)!}{1!2!2!}+3\times\frac{(1+1+2)!}{1!1!2!}-6=30. % \end{equation} % 由容斥原理，任何相邻两数不能相同的总方案数为 % \begin{equation} % \frac{(3+3+3)!}{3!3!3!}-3\times 420+3\times 110-30=720. % \end{equation} % \paragraph{(2)} 考虑“出现了相邻的 a”的总方案数。暂时将三个 a 视为不同的 $a_1,a_2,a_3$。$a_1,a_2$ 相邻的方案数为 % \begin{equation} % 2\times \frac{(2+3+3)!}{3!3!}=2240. % \end{equation} % 同理 $a_1,a_3$ 相邻，或 $a_2,a_3$ 相邻的方案数为 2240。$a_1,a_2,a_3$ 均相邻的方案数为 % \begin{equation} % 3!\frac{(1+3+3)!}{3!3!}=840. % \end{equation} % 而三者均相邻的方案，在两者相邻的方案中会被计算两次，故出现相邻的 a 的总方案数为 % \begin{equation} % 2240\times 3 - 840 = 5880. % \end{equation} % 现在去除三个 a 的顺序，即 $5880/3!=980$。 类似地，出现相邻的 b，出现相邻的 c，方案数也为 980。 % 现在考虑出现了相邻的 a，也出现了相邻的 b 的总方案数。暂时将三个 a 和三个 b 都视为不同的。
#### Matched solution ID
0
#### Correct solution
首先不考虑限制的情况：${9! \over 3!3!3!}$ 设$A_3$表示存在连续3个a的方案集合，$B_3$表示存在连续3个b的方案集合，$C_3$表示存在连续3个c的方案集合 对$|A_3|, |B_3|, |C_3|$： 将aaa看成一个字母，故$|A_3|= {7! \over 1!3!3!}= 140 $ 对$|A_3\bigcap B_3|, |A_3\bigcap C_3|, |C_3\bigcap B_3|$ ： 将aaa bbb分别看成一个字母，故$|A_3\bigcap B_3| = {5! \over 1!1!3!}=20$ 对$|A_3\bigcap B_3\bigcap C_3|$ ： 将aaa bbb ccc分别看成一个字母，故$|A_3\bigcap B_3\bigcap C_3| = {3! \over 1!1!1!}=6$ 总方案数为 $$ {9! \over 3!3!3!} - 3*140+20*3-6= 1680 - 420 + 60 - 6 = 1314 $$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 定义集合 | 1 | 0 | 学生答案中未明确定义集合$A_3, B_3, C_3$，因此根据评分规则，该部分不得分。 |
| 容斥原理 | 2 | 2 | 学生答案正确地应用了容斥原理来计算满足条件的排列数目。首先，学生计算了不考虑限制的总排列数，然后分别计算了存在连续三个a、b、c的情况，以及它们两两交集和三重交集的情况，并最终通过容斥原理得到了正确的总方案数1314。因此，根据评分规则，该部分得分。 |
| 答案正确 | 1 | 1 | 学生答案正确地应用了容斥原理，计算了任何连续3个元素不能全相同的排列数目。具体步骤包括：1) 计算不考虑限制的总排列数；2) 计算存在连续3个相同元素的排列数；3) 计算存在两组连续3个相同元素的排列数；4) 计算存在三组连续3个相同元素的排列数；5) 应用容斥原理得到最终结果。学生答案与标准答案完全一致，因此得分为1。 |


### Subproblem (2)
#### Status
graded
#### Answer
\paragraph{(2)} 暂时将每个元素均视为不同的，考虑以下九个条件： \begin{itemize} \item $A_1$: $a_2,a_3$ 相邻； \item $A_2$: $a_3,a_1$ 相邻； \item $A_3$: $a_1,a_2$ 相邻； \item $B_1$: $b_2,b_3$ 相邻； \item \ldots \end{itemize} 我们把 $A_1,A_2,A_3$ 称为一组，$B_1,B_2,B_3$ 称为一组，$C_1,C_2,C_3$ 称为一组。注意到同一组中的三个条件，如 $A_1,A_2,A_3$ 不可能同时满足，即 $a_1,a_2,a_3$ 不可能两两相邻。我们需要通过容斥原理，求出九个条件均不满足的方案数。 首先考虑满足一个条件的方案数。我们可以将相邻的那两个元素视为一个整体，这个“整体”内部有两种顺序，故方案数为 $9\times 2\times (2+3+3)!=18\times8!$。 接下来考虑满足两个条件的方案数。如果两个条件处于同一组，即形如 $A_1,A_2$，那么对应的三个元素连续出现。以 $A_1,A_2$ 为例，那么三个 a 会连续出现，且顺序为 $a_2,a_3,a_1$ 或 $a_1,a_3,a_2$。故总方案数为 $3\times\binom{3}{2}\times2\times(1+3+3)!=18\times 7!$。如果两个条件不处于同一组，方案数为 $\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times (2+2+3)!=108\times 7!$。 接下来考虑满足三个条件的方案数。由于同一组中的三个条件（形如 $A_1,A_2,A_3$）不可能同时满足，所以这三个条件一定分布在两组或三组中。如果是两组，根据前文的做法，我们可以计算出总方案数为 \begin{equation} 3\times 2\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times(1+2+3)!=216\times 6!. \end{equation} 如果是三组，方案数为 \begin{equation} \binom{3}{1}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(2+2+2)!=216\times 6!. \end{equation} 接下来考虑满足四个条件的方案数，同理，这四个条件应该形如 $A_i,A_j,B_u,B_v$ 或 $A_i,A_j,B_u,C_v$。如果是前者，方案数为 \begin{equation} \binom{3}{2}\times\binom{3}{2}\times\binom{3}{2}\times2\times 2\times(1+1+3)!=108\times 5!. \end{equation} 如果是后者，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(1+2+2)!=648\times 5!. \end{equation} 接下来考虑满足五个条件的方案数，此时这五个条件一定形如 $A_i,A_j,B_u,B_v,C_w$，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times 2\times(1+1+2)!=648\times 4!. \end{equation} 满足六个条件时，方案数为 \begin{equation} \binom{3}{2}\times \binom{3}{2}\times \binom{3}{2}\times 2\times 2\times 2\times(1+1+1)!=216\times 3!. \end{equation} 由容斥原理，可得没有条件被满足时，总方案数为 \begin{align} &\quad 9!-18\times 8!+18\times 7!+108\times 7!-216\times 6!-216\times 6! \\ &\quad+108\times 5!+648\times 5!-648\times 4!+216\times 3! \\ &=37584. \end{align} 现在去除相同字母内部的顺序，可得总方案数为 \begin{equation} \frac{37584}{3!3!3!}=174. \end{equation}
#### Matched solution ID
0
#### Correct solution
暂时将每个元素均视为不同的，考虑以下九个条件： \begin{itemize} \item $A_1$: $a_2,a_3$ 相邻； \item $A_2$: $a_3,a_1$ 相邻； \item $A_3$: $a_1,a_2$ 相邻； \item $B_1$: $b_2,b_3$ 相邻； \item \ldots \end{itemize} 我们把 $A_1,A_2,A_3$ 称为一组，$B_1,B_2,B_3$ 称为一组，$C_1,C_2,C_3$ 称为一组。注意到同一组中的三个条件，如 $A_1,A_2,A_3$ 不可能同时满足，即 $a_1,a_2,a_3$ 不可能两两相邻。我们需要通过容斥原理，求出九个条件均不满足的方案数。 首先考虑满足一个条件的方案数。我们可以将相邻的那两个元素视为一个整体，这个“整体”内部有两种顺序，故方案数为 $9\times 2\times (2+3+3)!=18\times8!$。 接下来考虑满足两个条件的方案数。如果两个条件处于同一组，即形如 $A_1,A_2$，那么对应的三个元素连续出现。以 $A_1,A_2$ 为例，那么三个 a 会连续出现，且顺序为 $a_2,a_3,a_1$ 或 $a_1,a_3,a_2$。故总方案数为 $3\times\binom{3}{2}\times2\times(1+3+3)!=18\times 7!$。如果两个条件不处于同一组，方案数为 $\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times (2+2+3)!=108\times 7!$。 接下来考虑满足三个条件的方案数。由于同一组中的三个条件（形如 $A_1,A_2,A_3$）不可能同时满足，所以这三个条件一定分布在两组或三组中。如果是两组，根据前文的做法，我们可以计算出总方案数为 \begin{equation} 3\times 2\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times(1+2+3)!=216\times 6!. \end{equation} 如果是三组，方案数为 \begin{equation} \binom{3}{1}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(2+2+2)!=216\times 6!. \end{equation} 接下来考虑满足四个条件的方案数，同理，这四个条件应该形如 $A_i,A_j,B_u,B_v$ 或 $A_i,A_j,B_u,C_v$。如果是前者，方案数为 \begin{equation} \binom{3}{2}\times\binom{3}{2}\times\binom{3}{2}\times2\times 2\times(1+1+3)!=108\times 5!. \end{equation} 如果是后者，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{1}\times\binom{3}{1}\times 2\times 2\times 2\times(1+2+2)!=648\times 5!. \end{equation} 接下来考虑满足五个条件的方案数，此时这五个条件一定形如 $A_i,A_j,B_u,B_v,C_w$，方案数为 \begin{equation} 3\times\binom{3}{2}\times\binom{3}{2}\times\binom{3}{1}\times 2\times 2\times 2\times(1+1+2)!=648\times 4!. \end{equation} 满足六个条件时，方案数为 \begin{equation} \binom{3}{2}\times \binom{3}{2}\times \binom{3}{2}\times 2\times 2\times 2\times(1+1+1)!=216\times 3!. \end{equation} 由容斥原理，可得没有条件被满足时，总方案数为 \begin{align} &\quad 9!-18\times 8!+18\times 7!+108\times 7!-216\times 6!-216\times 6! \\ &\quad+108\times 5!+648\times 5!-648\times 4!+216\times 3! \\ &=37584. \end{align} 现在去除相同字母内部的顺序，可得总方案数为 \begin{equation} \frac{37584}{3!3!3!}=174. \end{equation}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 捆绑aa,bb,cc并容斥 | 2 | 2 | 学生答案完整地复制了标准答案的内容，包括捆绑aa,bb,cc并容斥的过程，以及最终的计算结果。因此，根据评分规则，该部分得分。 |
| 考虑到aaa,bbb,ccc的情况并容斥 | 2 | 2 | 学生答案完整地考虑了aaa, bbb, ccc的情况，并正确应用了容斥原理，计算过程与标准答案完全一致。因此，根据评分规则，该部分得分。 |
| 答案正确 | 2 | 2 | 学生答案与标准答案完全一致，包括所有步骤和最终结果。因此，根据评分规则，答案正确，得分为2。 |


## Problem 6.3
### Subproblem (1)
#### Status
graded
#### Answer
记 $x_1=y_1+5,x_2=y_2+4,x_3=y_3+9$，则 \begin{equation} 40=x_1+x_2+x_3=y_1+y_2+y_3+5+4+9=y_1+y_2+y_3+18. \end{equation} 故 $y_1+y_2+y_3=22$，且 $1\le y_1\le 10,1\le y_2\le 16,1\le y_3\le 16$。 不考虑上界时，解共有 \begin{equation} \binom{22-1}{3-1}=\binom{21}{2}=210. \end{equation} 若 $y_1\gt 10$，记 $y_1=z_1+10$，则 $z_1\ge 1$ 且 $z_1+y_2+y_3=12$，此时解的个数共有 \begin{equation} \binom{12-1}{3-1}=\binom{11}{2}=55. \end{equation} 同理，若 $y_2\gt 16$，解共有 \begin{equation} \binom{22-16-1}{3-1}=\binom{5}{2}=10. \end{equation} 同理，若 $y_3\gt 16$，解共有 10 个。 由于$y_1+y_2+y_3=22\lt (10+1)+(16+1)$，不可能有至少两个变量超出上界。故原问题的整数解数目为 \begin{equation} 210-55-10-10=135. \end{equation}
#### Matched solution ID
0
#### Correct solution
记 $x_1=y_1+5,x_2=y_2+4,x_3=y_3+9$，则 \begin{equation} 40=x_1+x_2+x_3=y_1+y_2+y_3+5+4+9=y_1+y_2+y_3+18. \end{equation} 故 $y_1+y_2+y_3=22$，且 $1\le y_1\le 10,1\le y_2\le 16,1\le y_3\le 16$。 不考虑上界时，解共有 \begin{equation} \binom{22-1}{3-1}=\binom{21}{2}=210. \end{equation} 若 $y_1\gt 10$，记 $y_1=z_1+10$，则 $z_1\ge 1$ 且 $z_1+y_2+y_3=12$，此时解的个数共有 \begin{equation} \binom{12-1}{3-1}=\binom{11}{2}=55. \end{equation} 同理，若 $y_2\gt 16$，解共有 \begin{equation} \binom{22-16-1}{3-1}=\binom{5}{2}=10. \end{equation} 同理，若 $y_3\gt 16$，解共有 10 个。 由于$y_1+y_2+y_3=22\lt (10+1)+(16+1)$，不可能有至少两个变量超出上界。故原问题的整数解数目为 \begin{equation} 210-55-10-10=135. \end{equation}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 换元正确 | 1 | 1 | 学生答案在换元步骤中完全正确，与标准答案一致。具体表现为：1. 正确地将 $x_1$, $x_2$, $x_3$ 分别换元为 $y_1+5$, $y_2+4$, $y_3+9$；2. 正确推导出 $y_1 + y_2 + y_3 = 22$；3. 正确设定 $y_1$, $y_2$, $y_3$ 的取值范围。因此，根据评分规则，该部分得分。 |
| 计算总情况数 | 2 | 2 | 学生答案与标准答案完全一致，正确计算了总情况数为210，并正确扣除了超出上界的情况，最终得到135。因此，根据评分规则，该部分得分。 |
| 计算一个超出上界的情况 | 2 | 2 | 学生答案中详细计算了一个超出上界的情况，即当 $y_1 > 10$ 时，解的个数为 $\binom{11}{2} = 55$。这一计算与标准答案完全一致，符合评分规则的要求。因此，该部分得分。 |
| 计算两个超出上界的情况 | 2 | 2 | 学生答案中正确计算了两个超出上界的情况，即当 $y_1 > 10$ 和 $y_2 > 16$ 时，分别给出了正确的组合数计算。因此，根据评分规则，该部分得分。 |
| 计算三个超出上界的情况 | 2 | 2 | 学生答案中正确计算了三个超出上界的情况，包括$y_1>10$、$y_2>16$和$y_3>16$的情况，并分别给出了正确的组合数计算。因此，根据评分规则，该部分得分。 |
| 容斥原理得到答案 | 1 | 1 | 学生答案与标准答案完全一致，正确应用了容斥原理，并得出了正确的整数解数目135。因此，根据评分规则，该部分得分。 |


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
| (1) | graded | 3 | 4 |
| (2) | graded | 6 | 6 |
| | | **9** | **10** |
### Problem 6.3
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
## Total
| Score | Total |
| --- | --- |
| 28 | 30 |
