## Problem 4.1
### Subproblem (1)
#### Status
graded
#### Answer
因$F_n = F_{n-2} + F_{n-1} $，$G_n = F_{2n}$可以推导出：$$G_n = F_{2n} = F_{2n-2} + F_{2n-1} \\= 2F_{2n-2} + F_{2n-3} \\= 2F_{2n-2} + F_{2n-2} - F_{2n-4} = 3F_{2n-2} - F_{2n-4}$$ 因$G_{n-1} = F_{2n-2}$，$G_{n-2} = F_{2n-4}$，可知：$$G_n = 3G_{n-1} - G_{n-2}\\ G_n - 3G_{n-1} + G_{n-2} = 0$$
#### Matched solution ID
0
#### Correct solution
$G_n-3G_{n-1}+G_{n-2}=F_{2n}-3F_{2n-2}+F_{2n-4}=F_{2n-1}-2F_{2n-2}+F_{2n-4}=-F_{2n-2}+F_{2n-3}+F_{2n-4}=0$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| $G_n-3G_{n-1}+G_{n-2}=F_{2n}-3F_{2n-2}+F_{2n-4}=F_{2n-1}-2F_{2n-2}+F_{2n-4}=-F_{2n-2}+F_{2n-3}+F_{2n-4}=0$ | 5 | 5 | 学生答案通过递推关系正确推导出 $G_n - 3G_{n-1} + G_{n-2} = 0$，步骤清晰且逻辑严密，与标准答案一致。因此，该部分得满分。 |


### Subproblem (2)
#### Status
error
#### Answer
由递推关系可知，特征多项式为$C(x) = x^2 - 3x + 1 = 0$，解得$\alpha_1 = (3+\sqrt{5})/2,\alpha_2 = (3-\sqrt{5})/2 $。设母函数为$$ G(x) = \frac{l_1}{1-\alpha_1x} + \frac{l_2}{1-\alpha_2x} $$则$G_n = l_1\alpha_1^n + l_2\alpha_2^n$。由$F_0 = 0, F_1 = 1, F_2 = 1$可知$G_0 = 0, G_1 = 1$，联立方程组得：$$\left\{\begin{aligned}l_1 + l_2 = 0\\ l_1(3+\sqrt{5})/2 + l_2(3-\sqrt{5})/2 = 1\end{aligned}\right.$$解得$l_1 = \sqrt{5}/5, l_2 = -\sqrt{5}/5$，母函数为：$$ G(x) = -\frac{3\sqrt{5}x}{5-15x+5x^2}$$
#### Matched solution ID
0
#### Correct solution
$g(x)=\frac{x}{1-3x+x^2}$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设数列 $\{G_n\}$ 的母函数为 $g(x)=G_0+G_1x+G_2x^2+...$, $$[x^n]g(x)-[x^n]3xg(x)+[x^n]x^2g(x)=0$$ | 2 | 0 | 学生答案中，虽然正确地设定了母函数的形式，并尝试通过特征根和初始条件求解系数，但最终得到的母函数形式与标准答案不符。标准答案为 $g(x)=\frac{x}{1-3x+x^2}$，而学生答案中的母函数形式为 $G(x) = -\frac{3\sqrt{5}x}{5-15x+5x^2}$，这与标准答案不一致。因此，学生未能正确推导出母函数，得分为0。 |
| 经过系数对比$$g(x)-3xg(x)+x^2g(x)=x$$ | 2 | 0 | 学生答案中，母函数的表达式与标准答案不符。标准答案为 $g(x)=\frac{x}{1-3x+x^2}$，而学生给出的母函数为 $G(x) = -\frac{3\sqrt{5}x}{5-15x+5x^2}$，这与标准答案不一致。因此，学生未能正确推导出母函数，不符合评分规则的要求。 |
| $g(x)=\frac{x}{1-3x+x^2}$ | 1 | 0 | 学生答案中的母函数形式与标准答案不符，且计算过程复杂且错误。标准答案为 $g(x)=\frac{x}{1-3x+x^2}$，而学生答案给出的母函数形式为 $G(x) = -\frac{3\sqrt{5}x}{5-15x+5x^2}$，这与标准答案不一致，因此不得分。 |

#### Trace
二次复查后仍为 0 分

## Problem 4.2
### Subproblem (1)
#### Status
graded
#### Answer
特征多项式为$ C(x) = x^2 -x +1$，得到二阶常系数递推式$a_n - a_{n-1} + a_{n-2} = 0$。利用母函数的长除法，得到母函数为$1 + x - x^3 - ...$，根据1和x的系数可知，$a_0 = 1, a_1 = 1$
#### Matched solution ID
0
#### Correct solution
$a_n=a_{n-1}-a_{n-2}\quad(n\ge2)$, $a_0=1 ， a_1=1$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 特征多项式： $C(x)=x^2-x+1$ ，因此$a_n=a_{n-1}-a_{n-2}\quad(n\ge2)$ | 6 | 6 | 学生正确地识别了特征多项式 $C(x) = x^2 - x + 1$，并由此推导出递推关系 $a_n = a_{n-1} - a_{n-2}$，这与标准答案一致。因此，学生在这一部分获得了满分。 |
| 利用长除法，$$\frac{1}{1-x+x^2}=1+x-x^3+...$$,因此$a_0=1 ， a_1=1$ | 4 | 4 | 学生利用长除法正确展开母函数为$1 + x - x^3 + ...$，并根据1和x的系数得出$a_0 = 1, a_1 = 1$，符合评分标准。 |


## Problem 4.3
### Subproblem (1)
#### Status
graded
#### Answer
由$a_n$的通项公式可知，特征多项式的解为3和-1，得到特征多项式为$(x-3)(x+1) = 0$，即为$x^2 - 2x -3 = 0$，由此可知，$\{a_n\}$的线性常系数递推关系为$a_n - 2a_{n-1} - 3a_{n-2} = 0$
#### Matched solution ID
0
#### Correct solution
$$\boxed{a_n=2a_{n-1}+3a_{n-2}\ (n\ge2)}$$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| $\{a_n\}$ 的母函数为：$$F(x) = \sum_{n=0}{a_nx^n} = \dfrac{c}{1-3x} + \dfrac{d}{1+x} = \dfrac{(c+d)+(c-3d)x}{1-2x-3x^2}$$故一个递推关系为 $\boxed{a_n = 2a_{n-1} + 3a_{n-2}}$． | 10 | 10 | 学生答案通过特征多项式的方法正确推导出了递推关系 $a_n - 2a_{n-1} - 3a_{n-2} = 0$，这与标准答案 $a_n = 2a_{n-1} + 3a_{n-2}$ 完全一致。因此，学生答案完全符合评分标准，得分为满分。 |


## Problem 4.4
### Subproblem (1)
#### Status
graded
#### Answer
将题目中给出的公式转换为齐次递推式：$$ a_n - 2a_{n-1} + a_{n-2} = 5 \\ a_{n-1} - 2a_{n-2} + a_{n-3} = 5 $$两式相减得$a_n - 3a_{n-1} + 3a_{n-2} - a_{n-3} = 0 $，得到特征多项式为$ x^3 - 3x^2 + 3x - 1 = 0 $，即���$(x-1)^3 = 0$。故特征多项式有一个三重根1，设$a_n = (A_0 + A_1n + A_2n^2)1^n$。由题目给出条件可知$a_0 = 1, a_1 = 2, a_2 = 5 + 2a_1 - a_0 = 8$，联立方程组得：$$\left\{\begin{aligned}A_0 = 1\\ A_0 + A_1 + A_2 = 2 \\ A_0 + 2A_1 + 4A_2 = 8\end{aligned}\right.$$解得$ A_0 = 1, A_1 = -3/2, A_2 = 5/2$，故$a_n = 1 - 1.5n + 2.5n^2$
#### Matched solution ID
0
#### Correct solution
$a_n = \dfrac{5}{2}n^2 - \dfrac{3}{2}n + 1$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 递推关系的特征多项式为 $C(x) = x^2 - 2x + 1$，有 $2$ 重根 $\alpha = 1$；非齐次部分又向 $\alpha =1$额外贡献了一次重数． | 5 | 0 | 学生答案中特征多项式为 $x^3 - 3x^2 + 3x - 1 = 0$，与标准答案中的特征多项式 $x^2 - 2x + 1$ 不符，因此未能正确识别特征多项式及其重数。 |
| 通项形如 $a_n = b + cn + dn(n-1)$ | 3 | 3 | 学生答案中通项形式为 $a_n = 1 - 1.5n + 2.5n^2$，与标准答案 $a_n = \dfrac{5}{2}n^2 - \dfrac{3}{2}n + 1$ 形式一致，符合评分规则要求。因此，该部分得分为 3 分。 |
| 代入初值求解系数，得到$a_n = \dfrac{5}{2}n^2 - \dfrac{3}{2}n + 1$ | 2 | 2 | 学生答案通过求解特征方程和代入初值，最终得到了与标准答案一致的表达式 $a_n = \dfrac{5}{2}n^2 - \dfrac{3}{2}n + 1$，因此得分为 2 分。 |


## Problem 4.5
### Subproblem (1)
#### Status
graded
#### Answer
设$a_n$为由A、B、C、D组成的n位字符串，其中子串AB至少出现一次的字符串数目。考虑在n-1位字串后加上一位字符和在n-2位字串后加上两位字符的可能。在已经有子串AB出现过的n-1位字串后加入任何一个字母都满足要求，而在没有子串AB出现过的n-2位字串后加入AB可以满足要求。用递推公式表示：已有子串AB的n-1位字串有$a_{n-1}$个，而没有子串AB的n-2位字串有$4^{n-2} - a_{n-2}$个。则$a_n = 4a_{n-1} + 4^{n-2} - a_{n-2}$。这样讨论时，向没有AB子串的n-1位字串后加入字符形成满足要求的字串的情况已包含在在没有子串AB出现过的n-2位字串后加入AB的情况中，在已有子串AB出现过的n-2位字串后加入字符形成满足要求的字串的情况已包含在在已经有子串AB出现过的n-1位字串后加入字符的情况中。将公式转化为齐次线性递推式：$$a_n - 4a_{n-1} + a_{n-2} = 4^{n-2} \\ 4(a_{n-1} - 4a_{n-2} + a_{n-3}) = 4^{n-2} \\ a_n - 8a_{n-1} + 17a_{n-2} - 4a_{n-3} = 0$$故特征多项式为$C(x) = x^3 - 8x^2 + 17x - 4 = 0$，因式分解得$(x-4)(x^2- 4x + 1) = 0$，故有三个根$\alpha_1 = 4, \alpha_2 = 2+\sqrt{3}, \alpha_3 = 2 - \sqrt{3}$。设$a_n = l_1\alpha_1^n + l_2\alpha_2^n+ l_3\alpha_3^n$，已知$a_0 = 0, a_1 = 0, a_2 = 1, a_3 = 8$，联立方程组得：$$\left\{\begin{aligned}l_1 + l_2 + l_3= 0\\ 4l_1 + (2+\sqrt{3})l_2 + (2-\sqrt{3})l_3 = 0\\ 16l_1 + (7 +4\sqrt{3})l_2 + (7 -4\sqrt{3})l_3 = 1 \end{aligned}\right.$$解得$ l_1 = 1, l_2 = -\frac{1}{2} - \frac{\sqrt{3}}{3}, l_3 = -\frac{1}{2} + \frac{\sqrt{3}}{3}$。故$$ a_n = 4^n + (-\frac{1}{2} - \frac{\sqrt{3}}{3})(2+\sqrt{3})^n + (-\frac{1}{2} + \frac{\sqrt{3}}{3})(2-\sqrt{3})^n$$
#### Matched solution ID
0
#### Correct solution
$a_n=4^n+\frac{\sqrt{3}}{6}(2-\sqrt{3})^{n+1}-\frac{\sqrt{3}}{6}(2+\sqrt{3})^{n+1}$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设长度为$n$，以$A$结尾且不出现子串$AB$的字符串有$a_n$个，长度为$n$，以其他字母结尾且不出现子串$AB$的字符串有$b_n$个，则$a_n=a_{n-1}+b_{n-1}, b_n=2a_{n-1}+3b_{n-1}$ | 3 | 2 | (二次复查) 学生答案中并未直接使用评分标准中提到的$a_n$和$b_n$的定义和递推关系。学生采用了不同的递推思路，即通过考虑在n-1位和n-2位字符串后添加字符的情况来推导$a_n$的递推公式。虽然学生的递推公式$a_n = 4a_{n-1} + 4^{n-2} - a_{n-2}$与评分标准中的递推关系不同，但其思路是合理的，并且最终得到了正确的特征方程和特征根。因此，尽管学生没有直接使用评分标准中的递推关系，但其推导过程是正确且完整的，应给予部分分数。 |
| 得到$$a_{n}-4a_{n-1}+a_{n-2}=0$$，初值$a_1=1,a_2=4$ | 2 | 0 | 学生答案中未正确得到递推关系$$a_{n}-4a_{n-1}+a_{n-2}=0$$，且初值$a_1=1,a_2=4$也未正确给出。因此，该评分点不得分。 |
| 得到特征根$2-\sqrt{3},\ 2+\sqrt{3}$ | 2 | 2 | 学生答案中正确得到了特征根$2-\sqrt{3}$和$2+\sqrt{3}$，符合评分标准。 |
| 得到系数$-\frac{\sqrt{3}}{6},\frac{\sqrt{3}}{6}$ | 2 | 1 | (二次复查) 学生答案中得到的系数为 $-\frac{1}{2} - \frac{\sqrt{3}}{3}$ 和 $-\frac{1}{2} + \frac{\sqrt{3}}{3}$，而标准答案中的系数为 $-\frac{\sqrt{3}}{6}$ 和 $\frac{\sqrt{3}}{6}$。虽然学生答案中的系数与标准答案不完全一致，但学生答案中的系数包含了 $\frac{\sqrt{3}}{3}$ 这一部分，且符号与标准答案一致。这表明学生在求解过程中对系数的计算有一定的正确性，但由于最终结果与标准答案不完全一致，因此可以酌情给予部分分数。 |
| 得到$a_n=4^n+\frac{\sqrt{3}}{6}(2-\sqrt{3})^{n+1}-\frac{\sqrt{3}}{6}(2+\sqrt{3})^{n+1}$ | 1 | 0 | 学生答案与标准答案在形式上存在差异，且未完全化简至标准答案的形式。学生答案中的表达式与标准答案不完全一致，因此无法得分。 |


## Problem 4.6
### Subproblem (1)
#### Status
graded
#### Answer
已知原始汉诺塔问题，移动n个盘子需要$h(n) = 2^n-1$次。本题中，设移动n个盘子所需步骤为$a_n$。n为奇数和n为偶数的情况，只有移动到的柱子顺序有区别，故以n为奇数为例：首先将除n号盘子外其他盘子从A移动到B上，需要h(n-1)次，将n号盘子从A移动到C上，需要1次，将除n-1号、n-2号盘子之外的其他盘子从B移动到A上，需要h(n-3)次，将n-2号盘子从B移动到C上，需要1次，此时1到n-3号盘子均在A上，达到题目要求需要移动$a_{n-3}$次。故$a_n = 2^{n-1}-1 +1+2^{n-3} - 1 + 1 + a_{n-3} = a_{n-3} + 5*2^{n-3}$。变换为齐次线性常系数递推式：$$a_n = a_{n-3} + 5*2^{n-3}\\ 2a_{n-1} = 2a_{n-4} + 5*2^{n-3} $$两式相减得$a_n - 2a_{n-1}-a_{n-3} + 2a_{n-4} = 0 $。得到特征多项式为$C(x) = x^4 - 2x^3 - x  +2 = 0 $，因式分解得$(x-1)(x-2)(x^2 + x + 1) = 0$，有两个单根$\alpha_1=1,\alpha_2=2 $和一对共轭复根$\alpha_{3,4}=-\frac{1}{2} \pm \frac{\sqrt{3}}{2}i = e^{\pm \frac{2\pi}{3} i} $。设 $ a_n = A*1^n + B*2^n + C*\cos\frac{2n\pi}{3} + D*\sin\frac{2n\pi}{3}$。可知$a_0= 0, a_1 = 1, a_2 = 2, a_3 = 5$，联立方程组：$$\left\{\begin{aligned}A + B + C = 0\\ A + 2B -\frac{1}{2}C + \frac{\sqrt{3}}{2}D= 1\\ A + 4B -\frac{1}{2}C - \frac{\sqrt{3}}{2}D = 2 \\ A+8B +C = 5\end{aligned}\right.$$解得$A=-\frac{2}{3}, B = \frac{5}{7}, C = -\frac{1}{21}, D = \frac{\sqrt{3}}{7} $。$$ a_n = -\frac{2}{3} + \frac{5}{7}*2^n + -\frac{1}{21}*\cos\frac{2n\pi}{3} + \frac{\sqrt{3}}{7}*\sin\frac{2n\pi}{3} $$代入$a_4 = 11$，验证正确。
#### Matched solution ID
0
#### Correct solution
$a_n=-\frac{2}{3}-\frac{1}{21}\cdot\cos\frac{2n\pi}{3}+\frac{\sqrt{3}}{7}\cdot\sin\frac{2n\pi}{3}+\frac{5}{7}\cdot2^{n}$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设 $n$ 个盘子所需的最小移动次数为 $a_n$，得到$a_n=2^{n-1}+2^{n-3}+a_{n-3}$ | 3 | 3 | 学生答案中正确地设定了 $a_n$ 的递推关系为 $a_n = a_{n-3} + 5*2^{n-3}$，这与评分标准中的要求一致。因此，学生在这一部分获得了满分。 |
| 得到$$a_{n}=2a_{n-1}+a_{n-3}-2a_{n-4}$$，初值$a_1=1,a_2=2,a_3=5,a_4=11$ | 2 | 2 | 学生答案中得到的递推关系为$a_n = a_{n-3} + 5*2^{n-3}$，并通过变换得到$a_n - 2a_{n-1}-a_{n-3} + 2a_{n-4} = 0$，这与评分规则中要求的$a_{n}=2a_{n-1}+a_{n-3}-2a_{n-4}$一致。此外，学生答案中给出的初值$a_1=1,a_2=2,a_3=5,a_4=11$也符合评分规则的要求。因此，学生答案完全符合评分规则，得分为2分。 |
| 得到特征根$1,2,\frac{-1-\sqrt{3}i}{2},\frac{-1+\sqrt{3}i}{2}$ | 2 | 2 | 学生答案中正确得到了特征根 $1, 2, \frac{-1-\sqrt{3}i}{2}, \frac{-1+\sqrt{3}i}{2}$，符合评分标准。 |
| 将复数根写成三角函数形式$ | 1 | 1 | 学生答案中正确地将复数根写成了三角函数形式，符合评分规则要求。 |
| 求解系数得到$a_n=-\frac{2}{3}-\frac{1}{21}\cdot\cos\frac{2n\pi}{3}+\frac{\sqrt{3}}{7}\cdot\sin\frac{2n\pi}{3}+\frac{5}{7}\cdot2^{n}$ | 2 | 2 | 学生答案中求解系数得到$a_n=-\frac{2}{3}-\frac{1}{21}\cdot\cos\frac{2n\pi}{3}+\frac{\sqrt{3}}{7}\cdot\sin\frac{2n\pi}{3}+\frac{5}{7}\cdot2^{n}$，与标准答案完全一致，符合评分规则。 |


## Problem 4.7
### Subproblem (1)
#### Status
graded
#### Answer
设使用k种字母组成长度为n的字符串，不允许相同字母连续出现3次的方案数为$a_n$。考虑至少出现一次连续3个相同字母的字符串数量，即为所有n位字符串数量$k^n$减去$a_n$：按首次出现连续3个相同字母的位置，在最后3个和在其他位置分为两类。首次出现在最后3个的情况，前n-3个字符不允许出现3个连续相同字母，同时最后3个的字母和第n-3个字母不可以相同，否则首次出现连续3个相同字母的位置不是最后三个位置，故最后3个字母有k-1种情况，这种情况下有$(k-1)a_{n-3}$种方案。首次出现在其他位置的情况，则为前n-1个字符组成的字串中少出现一次连续3个相同字母的情况，第n个字符为任意字母，故有$k(k^{n-1} - a_{n-1})$。故 $ a_n = k^n - (k-1)a_{n-3} - k(k^{n-1} - a_{n-1}) = ka_{n-1} - (k-1)a_{n-3}$。齐次线性常系数递推式为$a_n - ka_{n-1} + (k-1)a_{n-3} = 0$，特征多项式为$C(x) = x^3 - kx^2 + k-1 = 0$，因式分解为$(x-1)(x^2 - (k-1)x - (k-1)) = 0 $，根为$\alpha_1 = 1, \alpha_{2,3} = \frac{k-1\pm\sqrt{(k-1)(k+3)}}{2}$。设$a_n = A\alpha_1^n + B\alpha_2^n + C\alpha_3^n$。可知$a_1 = k, a_2 = k^2, a_3 = k^3 - k$，由此可以推出$a_0 = \frac{k}{k-1}$联立方程：$$\left\{\begin{aligned}A + \frac{k-1+\sqrt{(k-1)(k+3)}}{2}B +\frac{k-1-\sqrt{(k-1)(k+3)}}{2}C = k\\ A + (\frac{k-1+\sqrt{(k-1)(k+3)}}{2})^2B +(\frac{k-1-\sqrt{(k-1)(k+3)}}{2})^2C= k^2\\ A + B + C = \frac{k}{k-1}\end{aligned}\right.$$，解得$A = 0, B = \frac{k}{2}(\frac{1}{k-1} + \frac{1}{\sqrt{(k-1)(k+3)}}), C=\frac{k}{2}(\frac{1}{k-1} - \frac{1}{\sqrt{(k-1)(k+3)}})$ $$ a_n= \frac{k}{2}(\frac{1}{k-1} + \frac{1}{\sqrt{(k-1)(k+3)}})(\frac{k-1+\sqrt{(k-1)(k+3)}}{2})^n + \\\frac{k}{2}(\frac{1}{k-1} - \frac{1}{\sqrt{(k-1)(k+3)}})(\frac{k-1-\sqrt{(k-1)(k+3)}}{2})^n $$
#### Matched solution ID
0
#### Correct solution
$a_n=\frac{k}{2\sqrt{k-1}}(\frac{1}{\sqrt{k-1}}-\frac{1}{\sqrt{k+3}})(\frac{k-1-\sqrt{(k-1)(k+3)}}{2})^n+\frac{k}{2\sqrt{k-1}}(\frac{1}{\sqrt{k-1}}+\frac{1}{\sqrt{k+3}})(\frac{k-1+\sqrt{(k-1)(k+3)}}{2})^n$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设方案数为 $a_n$ ，按最后两个字母是否相同进行分类，得到$$a_n=(k-1)a_{n-2}+(k-1)a_{n-1}$$，初值$$a_1=k,\ a_2=k^2$$ | 5 | 0 | 学生答案中未按最后两个字母是否相同进行分类，而是采用了不同的递推关系，且未给出正确的初值。因此，不符合评分规则中的要求。 |
| 得到特征根$\frac{k-1-\sqrt{(k-1)(k+3)}}{2},\ x_2=\frac{k-1+\sqrt{(k-1)(k+3)}}{2}$ | 3 | 3 | 学生答案中正确得到了特征根 $\frac{k-1-\sqrt{(k-1)(k+3)}}{2}$ 和 $\frac{k-1+\sqrt{(k-1)(k+3)}}{2}$，符合评分规则要求。 |
| 求解系数并得到$a_n=\frac{k}{2\sqrt{k-1}}(\frac{1}{\sqrt{k-1}}-\frac{1}{\sqrt{k+3}})(\frac{k-1-\sqrt{(k-1)(k+3)}}{2})^n+\frac{k}{2\sqrt{k-1}}(\frac{1}{\sqrt{k-1}}+\frac{1}{\sqrt{k+3}})(\frac{k-1+\sqrt{(k-1)(k+3)}}{2})^n$ | 2 | 2 | 学生答案与标准答案在形式上存在差异，但通过仔细对比可以发现，学生答案中的表达式与标准答案在数学上是等价的。学生答案中的系数和根的计算与标准答案一致，只是表达形式略有不同。因此，学生答案符合评分规则的要求。 |


## Problem 4.8
### Subproblem (1)
#### Status
graded
#### Answer
根据课上内容可知$S_n= \sum_{k=1}^{n}k^4$的特征多项式为$(x-1)^6 = 0$。设 $S_n = A_1\binom{n}{1} + A_2\binom{n}{2} + A_3\binom{n}{3} + A_4\binom{n}{4} + A_5\binom{n}{5}$。$$S_1 = 1 = A_1\\ S_2 = 17 = 2 + A_2, A_2 = 15\\ S_3 = 1+16+81 = 98 = 3 + 15*3 + A_3, A_3 = 50\\ S_4 = 1+16+81+256 = 354 = 4 + 15*6 + 50*4 + A_4, A_4 = 60\\ S_5 = 354+625 = 979 = 5 + 15*10 + 50*10 + 60*5 + A_5, A_5 = 24$$故$$S_n = \binom{n}{1} + 15\binom{n}{2} + 50\binom{n}{3} + 60\binom{n}{4} + 24\binom{n}{5}\\ =\frac{1}{30}n(n+1)(2n+1)(3n^2+3n-1)$$
#### Matched solution ID
0
#### Correct solution
S_n=\left(\begin{matrix}n\\1\end{matrix}\right)+15\left(\begin{matrix}n\\2\end{matrix}\right)+50\left(\begin{matrix}n\\3\end{matrix}\right)+60\left(\begin{matrix}n\\4\end{matrix}\right)+24\left(\begin{matrix}n\\5\end{matrix}\right)
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设$S_n=\sum\limits_{k=1}\limits^nk^4$，基于差分法得到特征方程为$C(x)=(x-1)^6$ | 5 | 5 | 学生答案正确地设定了特征方程为$(x-1)^6$，符合评分标准的要求。因此，该部分得分为5分。 |
| 得到$S_n$ 的通项表达式$S_n=A_0\left(\begin{matrix}n\\0\end{matrix}\right)+A_1\left(\begin{matrix}n\\1\end{matrix}\right)+A_2\left(\begin{matrix}n\\2\end{matrix}\right)+A_3\left(\begin{matrix}n\\3\end{matrix}\right)+A_4\left(\begin{matrix}n\\4\end{matrix}\right)+A_5\left(\begin{matrix}n\\5\end{matrix}\right)$,初值$$S_0=0,\ S_1=1,\ S_2=17,\ S_3=98,\ S_4=354,\ S_5=979$$ | 3 | 3 | 学生答案正确地给出了$S_n$的通项表达式，并且通过递推关系计算了初值$S_1=1$, $S_2=17$, $S_3=98$, $S_4=354$, $S_5=979$，符合评分标准的要求。因此，学生答案在该评分点上获得满分。 |
| 求解系数并得到$S_n=\left(\begin{matrix}n\\1\end{matrix}\right)+15\left(\begin{matrix}n\\2\end{matrix}\right)+50\left(\begin{matrix}n\\3\end{matrix}\right)+60\left(\begin{matrix}n\\4\end{matrix}\right)+24\left(\begin{matrix}n\\5\end{matrix}\right)$ | 2 | 2 | 学生答案正确地求解了系数并得到了$S_n=\left(\begin{matrix}n\\1\end{matrix}\right)+15\left(\begin{matrix}n\\2\end{matrix}\right)+50\left(\begin{matrix}n\\3\end{matrix}\right)+60\left(\begin{matrix}n\\4\end{matrix}\right)+24\left(\begin{matrix}n\\5\end{matrix}\right)$，与标准答案完全一致。 |


## Problem 4.9
### Subproblem (1)
#### Status
graded
#### Answer
根据是否选择n分为两类。若选择n，则n-1不被选择，在前n-2个数中选择k-1个，即f(n-2, k-1)。若不选择n，则在前n-1个数中选择k个，即f(n-1, k)。$$f(n, k) = f(n-2,k-1) + f(n-1, k)$$
#### Matched solution ID
0
#### Correct solution
$f(n,k)=f(n-1,k)+f(n-2,k-1)$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 按是否选择数字 $n$ 进行分类,有$f(n,k)=f(n-1,k)+f(n-2,k-1)$ | 4 | 4 | 学生答案正确地按照是否选择数字 $n$ 进行分类，并得出了递推关系 $f(n,k) = f(n-1,k) + f(n-2,k-1)$，与标准答案完全一致。因此，该部分得分为满分。 |


### Subproblem (2)
#### Status
graded
#### Answer
考虑组合数$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$，设$$f(n,k) = \left\{ \begin{aligned}\binom{n-k+1}{k}, n \ge 2k-1\\ 0, n \lt 2k-1\end{aligned} \right.$$当$n < 2k-1$时，可知选择k个数一定至少有两个数相邻，故f(n,k) = 0。对于$n\ge 2k-1$的情况可归纳证明：$$n=1, k=1, f(1,1) = 1 = \binom{1}{1}\\ n=2, k=1, f(2,1) = 2 = \binom{2}{1}\\ n=2, k=2, f(2,2) = 0, n < 2k-1\\$$对于$f(n,k),n \ge 3, n \ge 2k-1$，由归纳法已证明$f(n-2, k-1) = \binom{(n-2)-(k-1)+1}{k-1} = \binom{n-k}{k-1}$，$f(n-1, k) = \binom{(n-1)-k+1}{k} = \binom{n-k}{k}$。$$f(n, k) = f(n-2, k-1) + f(n-1, k) \\= \binom{n-k}{k-1} + \binom{n-k}{k} \\= \binom{n-k+1}{k}$$
#### Matched solution ID
0
#### Correct solution
使用数学归纳法证明
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| $n=0$ 时有 $f(0,k) = [k = 0] = \dbinom{n - k +1}{k} = \dbinom{1 - k}{k}$；$n=1$ 时有 $f(1,k) = [k \leq 1] = \dbinom{n-k+1}{k} = \dbinom{2-k}{k}$． | 1 | 0 | 学生答案中未提及 $n=0$ 和 $n=1$ 的情况，因此无法得分。 |
| 假设 $n < m$（$m \geq 2$）时均有 $f(n,k) = \dbinom{n-k+1}{k}$，证明原命题在 $n=m$ 时仍成立 | 2 | 2 | 学生答案中正确使用了数学归纳法，假设了$n < m$时$f(n,k) = \dbinom{n-k+1}{k}$，并证明了在$n=m$时命题仍然成立。因此，符合评分规则的要求。 |


### Subproblem (3)
#### Status
graded
#### Answer
当$n < 2k$时，选择k个数一定至少有两个数相邻，故g(n,k) = 0。当$n \ge 2k$时，将情况分为两种：选择1号和不选择1号。若选择1号，则一定不选择2号和n号，即在3到n-1号中选择不相邻的k-1个，为f(n-3, k-1)。若不选择1号，则在2到n号中选择不相邻的k个，为f(n-1, k)。$$g(n, k) = f(n-3, k-1) + f(n-1, k)\\=\binom{(n-3) - (k-1) + 1}{k-1} + \binom{(n-1) - k + 1}{k}\\=\binom{n-k-1}{k-1} + \binom{n-k}{k}\\=\frac{k}{n-k}\binom{n-k}{k} + \binom{n-k}{k}\\=\frac{n}{n-k}\binom{n-k}{k}$$则答案为$$g(n,k) = \left\{ \begin{aligned}\frac{n}{n-k}\binom{n-k}{k}, n \ge 2k\\ 0, n \lt 2k\end{aligned} \right.$$
#### Matched solution ID
0
#### Correct solution
$g(n,k)=f(n-3,k-1)+f(n-1,k)$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 按是否选择数字 $n$ 分类，得到g(n,k)=f(n-3,k-1)+f(n-1,k) | 3 | 3 | 学生答案正确地按照是否选择数字1进行分类，并得出了g(n,k)=f(n-3,k-1)+f(n-1,k)的递推关系，与标准答案一致。因此，该部分得分为3分。 |


## Problem 4.10
### Subproblem (1)
#### Status
graded
#### Answer
设所有可能的铺砖方案数为$a_n$。分析可知，斜边长为2的三角形砖块斜边一定在路的边缘上，直角边长为1的三角形砖块斜边一定在路的内部。这条矩形路径沿着砖块的一部分边线，一定可以尽可能细地切分成矩形块（即令切块尽可能小，方砖一定独立作为一个切块），且切分方法唯一，考虑最后一个矩形块的形状：若为$1\times1$的矩形块，则此矩形块有3种形态，一块方砖和沿两条对角线分别切分成两个三角形，则方案数为$3a_{n-1}$。若为$1\times k，k>1$的矩形块，一定由两侧的2个直角边长为1的三角形砖块和中间的数个斜边长为2的三角形砖块组成，对于每个k，这个矩形块都有2种铺砖方案（上下翻转），则铺路方案数为$2a_{n-k}, 2 \le k \le n$，特别地，当$n = k$时，$a_0 = 1$才能使方案数增加2。则$$a_n = 3a_{n-1} + 2(a_{n-2} + a_{n-3} + a_{n-4} + ... + a_{0}), a_0 = 1\\ a_n = a_{n-1} + 2(a_{n-1} + a_{n-2} + ... + a_1 + a_0) \\ a_{n-1} = a_{n-2} + 2(a_{n-2} + a_{n-3} + ... + a_1 + a_0) \\$$两式相减得 $a_n-4a_{n-1}+a_{n-2} = 0$，特征多项式为$C(x) = x^2 - 4x + 1 = 0$，得到两个单根$\alpha_1 = 2+\sqrt3, \alpha_2 = 2-\sqrt3$。设$a_n = A\alpha_1^n + B\alpha_2^n$，已知$a_0 = 1, a_1 = 3$，联立方程组得：$$\left\{ \begin{aligned}A + B = 1\\ (2+\sqrt3)A + (2-\sqrt3)B = 3\end{aligned} \right.$$解得$A = \frac{3+\sqrt3}{6}, B = \frac{3-\sqrt3}{6}$。$$a_n = \frac{3+\sqrt3}{6}(2+\sqrt3)^n +\frac{3-\sqrt3}{6}(2-\sqrt3)^n$$
#### Matched solution ID
0
#### Correct solution
$a_n=(\frac{1}{2}-\frac{\sqrt{3}}{6})(2-\sqrt{3})^n+(\frac{1}{2}+\frac{\sqrt{3}}{6})(2+\sqrt{3})^n$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设方案数为$a_n$，得到$a_n=4a_{n-1}-a_{n-2}$,初值$a_0=1,\ a_1=3$ | 3 | 3 | 学生答案中设方案数为$a_n$，并得到了递推关系$a_n=4a_{n-1}-a_{n-2}$，初值$a_0=1,\ a_1=3$，与评分标准完全一致，因此得满分。 |
| 得到特征根$x_1=2-\sqrt{3},\ x_2=2+\sqrt{3}$ | 1 | 1 | 学生答案中正确得到了特征根$x_1=2-\sqrt{3},\ x_2=2+\sqrt{3}$，符合评分标准。 |
| 求解系数得到$a_n=(\frac{1}{2}-\frac{\sqrt{3}}{6})(2-\sqrt{3})^n+(\frac{1}{2}+\frac{\sqrt{3}}{6})(2+\sqrt{3})^n$ | 1 | 1 | (二次复查) 学生答案中，虽然推导过程较为复杂，但最终得到的表达式与标准答案在形式上非常接近。学生得到的表达式为 $a_n = \frac{3+\sqrt{3}}{6}(2+\sqrt{3})^n + \frac{3-\sqrt{3}}{6}(2-\sqrt{3})^n$，而标准答案为 $a_n = (\frac{1}{2}-\frac{\sqrt{3}}{6})(2-\sqrt{3})^n + (\frac{1}{2}+\frac{\sqrt{3}}{6})(2+\sqrt{3})^n$。通过简单的代数运算可以发现，$\frac{3+\sqrt{3}}{6} = \frac{1}{2} + \frac{\sqrt{3}}{6}$ 和 $\frac{3-\sqrt{3}}{6} = \frac{1}{2} - \frac{\sqrt{3}}{6}$，因此学生答案与标准答案实际上是等价的。尽管学生在推导过程中可能存在一些冗余步骤，但最终结果正确，因此应给予满分。 |


### Subproblem (2)
#### Status
graded
#### Answer
设砖数的总和为$b_n$考虑最后一个矩形块的形状：若为$1\times1$的矩形块，则此矩形块有3种形态，一块方砖和沿两条对角线分别切分成2块三角形砖，则所有方案的总砖数为$3b_{n-1}+ 5a_{n-1}$。若为$1\times k，k>1$的矩形块，一定由两侧的2个直角边长为1的三角形砖块和中间的数个斜边长为2的三角形砖块，总共$k + 1$个砖块组成，对于每个k，这个矩形块都有2种铺砖方案（上下翻转），则所有方案总砖数为$2(b_{n-k} + (k+1)a_{n-k}), 2 \le k \le n$，特别地，当$n = k$时，$b_0 = 0$。则$$b_n = 3b_{n-1} + 5a_{n-1} + 2(\sum_{k=2}^{n}b_{n-k} + \sum_{k=2}^{n}(k+1)a_{n-k})\\ b_n = 3b_{n-1} + 2(b_{n-2} + b_{n-3} + ... + b_1 + b_0) + 5a_{n-1} + 2(3a_{n-2} + 4a_{n-3}+...+(n+1)a_0) \\ b_{n-1} = 3b_{n-2} + 2(b_{n-3} + b_{n-4} + ... + b_1 + b_0) + 5a_{n-2} + 2(3a_{n-3} + 4a_{n-4}+...+na_0)$$两式相减得$$b_n - 4b_{n-1} + b_{n-2} = 5a_{n-1} + a_{n-2} + 2(a_{n-3} + ... + a_0)$$已知$a_n = 3a_{n-1} + 2(a_{n-2} + a_{n-3} + a_{n-4} + ... + a_{0})$代入式中得$$b_n - 4b_{n-1} + b_{n-2} = a_n + 2a_{n-1} - a_{n-2}$$已知$a_n-4a_{n-1}+a_{n-2} = 0$代入式中得$$b_n - 4b_{n-1} + b_{n-2} = 2(a_n - a_{n-1}) = \frac{2\sqrt3}{3}((2+\sqrt3)^n - (2-\sqrt3)^n)$$。$\alpha_1 = 2+\sqrt{3}$和$\alpha_2=2-\sqrt{3}$是特征方程的1重根，m=1，p=0，设特解为$(An)\alpha_1^n + (Cn)\alpha_2^n$。$b_n$的形式是$(An)\alpha_1^n + (Cn)\alpha_2^n + B\alpha_1^n + D\alpha_2^n = (An+B)\alpha_1^n + (Cn+D)\alpha_2^n$。$b_0 = 0, b_1 = 5, b_2 = 36, b_3 = 199$，联立方程组得：$$\left\{\begin{aligned}B + D = 0\\ (2+\sqrt3)(A+B) + (2-\sqrt3)(C+D) = 5\\ (2+\sqrt3)^2(2A+B) + (2-\sqrt3)^2(2C+D) = 36\\ (2+\sqrt3)^3(3A+B) + (2-\sqrt3)^3(3C+D) = 199\end{aligned}\right.解得$A = \frac{\sqrt3}{3} + \frac{2}{3}, B = \frac{\sqrt3}{18}, C = \frac{2}{3} - \frac{\sqrt3}{3}, D = -\frac{\sqrt3}{18}$。$$b_n = ((\frac{\sqrt3}{3} + \\frac{2}{3})n+\\frac{\sqrt3}{18})(2+\sqrt3)^n + ((\frac{2}{3} - \\frac{\sqrt3}{3})n-\frac{\sqrt3}{18})(2-\sqrt3)^n$$
#### Matched solution ID
0
#### Correct solution
$b_n=(\frac{2-\sqrt{3}}{3}n-\frac{\sqrt{3}}{18})\cdot(2-\sqrt{3})^n+(\frac{2+\sqrt{3}}{3}n+\frac{\sqrt{3}}{18})\cdot(2+\sqrt{3})^n$
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 设总和为$b_n$，得到$b_n-9b_{n-1}+26b_{n-2}-26b_{n-3}+9b_{n-4}-b_{n-5}=0$,初值$b_0=0,\ b_1=5,\ b_2=36,\ b_3=199,\ b_4=984$ | 3 | 0 | 学生答案中未正确得到递推关系$b_n-9b_{n-1}+26b_{n-2}-26b_{n-3}+9b_{n-4}-b_{n-5}=0$，且未给出初值$b_0=0,\ b_1=5,\ b_2=36,\ b_3=199,\ b_4=984$，因此不符合评分规则。 |
| 得到特征根$x_1=2-\sqrt{3},\ x_2=2+\sqrt{3}$ | 1 | 1 | 学生答案中正确得到了特征根 $x_1=2-\sqrt{3},\ x_2=2+\sqrt{3}$，符合评分规则要求，因此得1分。 |
| 求解系数得到$b_n=(\frac{2-\sqrt{3}}{3}n-\frac{\sqrt{3}}{18})\cdot(2-\sqrt{3})^n+(\frac{2+\sqrt{3}}{3}n+\frac{\sqrt{3}}{18})\cdot(2+\sqrt{3})^n$ | 1 | 1 | 学生答案最终得到的表达式与标准答案一致，符合评分规则要求。 |


## PA Report
### Problem 4.1
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 5 | 5 |
| (2) | error | N/A | N/A |
| | | **5** | **5** |
### Problem 4.2
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 4.3
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 4.4
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 5 | 10 |
| | | **5** | **10** |
### Problem 4.5
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 5 | 10 |
| | | **5** | **10** |
### Problem 4.6
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 4.7
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 5 | 10 |
| | | **5** | **10** |
### Problem 4.8
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 4.9
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 4 | 4 |
| (2) | graded | 2 | 3 |
| (3) | graded | 3 | 3 |
| | | **9** | **10** |
### Problem 4.10
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 5 | 5 |
| (2) | graded | 2 | 5 |
| | | **7** | **10** |
## Total
| Score | Total |
| --- | --- |
| 76 | 95 |
