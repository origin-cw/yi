### 基础语法
**\命令行{}**

**\textbf{P}**  加粗P

**textcolor{red}{文本内容}**  设置字体颜色

**_{内容}** 下标
**\hat T**  就是在T这个字母头上添加一个小箭头
**\rm**  使得斜体变直体，或直体变斜体
**{x}^{2}**  书写X的平方
**\in**  数学符号“属于”
**\times 3**  把前面的公式或者符号“*3”
**\over**  表示几分之几，分子在前，分母在后


**\textit{文本}**  设置斜体
**\underline{文本}**  设置下划线
**两个换行符**是另起一个新的段落

**\section{设置章节}
\subsection{设置二级子章节}
\subsubsection{设置三级子章节}**
比section大的是chapter和part


### 超链接与引用  
**\ref{}** 是让某些字体成为超链接
**\label{}** 是标记要跳转的位置

**\cite{参考文献1，参考文献2}** 用来引用参考文献   
但是所有的参考文献是放在 **.bib** 文件下的    
引用要填写的参考信息可以在网上搜论文，点击引用，选择BibTex，获取相关内容
**\bibliography{参考文献的bib文件名}**，会自动生成参考文献

### 图片
如果要添加图片，需要先引用graphicx包  \usepackage{graphicx}
> \begin{figure}[h]%
> \centering
\includegraphics[width=1\textwidth]{Fig1.eps}
\caption{图片注释}\label(fig1)
\end{figure}

### 公式
* 文本内插入公式用两个$,公式放在里面
* 行外公式语法如下
> \begin{equation}
(公式)
\label{eq2}
\end{equation}

> 公式的具体语法，可以现在mathtype里面打出来，然后在预置里面设置一下复制成tex语法，之后直接在overleaf里面复制就可以了

### 表格

可以使用**tabular环境**创建一个表格
> \begin{table}
\center
\begin{tabular}{c p{2cm} c}
单元格1 & 单元格2 & 单元格3 \\
\hline\hline
单元格2 &  单元格2 & 单元格2 \\
\hline
单元格2 & 单元格2 & 单元格2
\end{tabular}
\caption{表格的标题}
\end{table}

**ccc**代表有三列，其中每一列都代表居中对齐，可以替换成r l,
在ccc中间添加 | 可以为表格添加竖直的直线，如**c|c|c**
水平直线则可以使用 **\hline**,两次\hline可以生成双横线的效果
**p{2cm}** 可以设置列宽，行宽呢？
**\center** 将表格居中显示





### 列表
列表要先进入**环境**
* 无序列表可以使用itemize的环境
>\begin{itemize}
\item  列表项1
\item  列表项2
\item  列表项3
\end{itemize}
* 有序列表可以使用enumerate环境
>\begin{enumerate}
\item  列表项1
\item  列表项2
\item  列表项3
\end{enumerate}


