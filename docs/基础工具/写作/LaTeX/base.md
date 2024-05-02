# LaTeX
readme.zh-cn.html

请记住 texdoc 命令，用于打开宏包帮助文档，使用方法如下

texdoc 宏包/文件名
例如， texdoc amsmath 查看amsmath 宏包的说明文档
另外，推荐入门必读的手册

lshort-zh-zn
install-latex-guide-zh-cn
第一份文档，入门使用，看完它之后，你的一些日常写作应当没有任何问题，强烈推荐

第二份文档，解决你安装过程中遇到的 99% 的问题，请按需仔细阅读

调出它们的方法很简单，只需要命令行执行

texdoc lshort-zh-zn
texdoc install-latex-guide-zh-cn

texlive
texstduio

```tex
%导言区
\documentclass[UTF8]{ctexart}


%正文区
\begin{document}
	% l 左 c 居中 r 对齐
	% | 竖线 \hline横线 || 双竖线 \hline \hline 双横线
	\begin{tabular}{| l | c | c | c || r |}
		\hline
		名字 & 语文 & 数学 & 英语 & 备注\\
		\hline
		张三 & 87 & 100 & 93 & 优秀 \\
		\hline
		李四 & 75 & 64 & 52 & 补考另行通知\\
		\hline
		\hline
		王五 & 80 & 82 & 78 & 良好\\
		\hline
	\end{tabular}
	
	
	% p{设置宽度},内容超过宽度时，自动换行
	\begin{tabular}{| l | c | c | c || p{1.5cm} |}
		\hline
		名字 & 语文 & 数学 & 英语 & 备注\\
		\hline
		张三 & 87 & 100 & 93 & 优秀 \\
		\hline
		李四 & 75 & 64 & 52 & 补考另行通知\\
		\hline
		\hline
		王五 & 80 & 82 & 78 & 良好\\
		\hline
	\end{tabular}
	
\end{document}
```