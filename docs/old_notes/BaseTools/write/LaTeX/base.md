# LaTeX

## 命令

如果直接输入命令，是xelatex而不是xetex，害我查了好久。

当然也能看到texstudio的命令
```shell
xelatex -synctex=1 -interaction=nonstopmode "main".tex
第一个是pdf同步，第二个是编译不stop。
```

## 对于中文的支持

很多软件都是默认pdftex引擎的，中文一般使用utf8的xetex。

但用了xetex还要搭配xtex宏包，或者使用xtexbook等document格式才能正常显示，否则只是编译通过。

当然pdftex也是可以的，通过ctex，[UTF8] ctexbook等选项，这里我就不验证了。

## 对于emoji的支持
~~感觉latex的配置十分繁琐。~~

貌似luatex支持一点，其他的没查到。总之，貌似用不了，插图片吧。

https://ctan.org/pkg/emotion

## 关于使用
其实就是多抄，这又不用debug。

## begin
readme.zh-cn.html

请记住 texdoc 命令，用于打开宏包帮助文档，使用方法如下

texdoc 宏包/文件名
例如， texdoc amsmath 查看amsmath 宏包的说明文档
另外，推荐入门必读的手册

lshort-zh-zn
install-latex-guide-zh-cn
第一份文档，入门使用，看完它之后，你的一些日常写作应当没有任何问题，强烈推荐

第二份文档，解决你安装过程中遇到的 99% 的问题，请按需仔细阅读

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

## 编译工具
win/linux：texlive下载anzhuang
mac：mactex安装，貌似是个texlive for mac

## 写作工具
texstudio：ui上丑了点，但还是功能还算多。
vscode+tex插件：可能配置比较繁琐。
可以setting.json加上下列配置
```json

    "workbench.editorAssociations": {
        "*.pdf": "latex-workshop-pdf-hook"
    },
    "latex-workshop.latex.autoClean.run": "onBuilt",
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk (xelatex)",
            "tools": [
                "xelatexmk"
            ]
        },
        {
            "name": "xelatex -> bibtex -> xelatex * 2",
            "tools": [
                "xelatex",
                "bibtex",
                "xelatex",
                "xelatex"
            ]
        },
    ],
    "latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk"
    ],
    "latex-workshop.latex.recipe.default": "lastUsed",
```
