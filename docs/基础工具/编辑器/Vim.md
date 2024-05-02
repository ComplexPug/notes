忘记但常用的快捷键

/key-word\c

%s/str1/str2 替换

ctl+w+方向 切换页面

快速注释多行
ctrl+q（unix下也可以ctrl+v）进入visual block
选中之后大写I插入输入#，再按Esc即可

## 寄存器reg
reg 查看寄存器
剪切板得支持clip+
双引号+加号+y 复制到剪切板 视图模式选中文本后
双引号+加号+p 从剪切板粘贴
```.vimrc
" 支持在Visual模式下，通过C-y复制到系统剪切板
vnoremap <C-y> "+y
" 支持在normal模式下，通过C-p粘贴系统剪切板
nnoremap <C-p> "*p
```

实现ssh远程复制到系统剪切板，此处用到 clipper，下图是其原理，简单来说就是远程通过socket/网络发到本地，本地再设置到系统剪切板。
[link](https://www.cnblogs.com/gmpy/p/11177719.html)
airline

0.配置目录
linux下可以配置.vimrc，也可以在.vim里面创建vimrc

1. 自动补齐括号
   找到vim的配置文件 vimrc 或者 .vimrc 。一般来说，系统配置文件在 /etc/vim/vimrc 。用户配置文件在 ~/.vimrc 。每个人的配置文件位置可能不一样，请自行查看。

# 打开配置文件

在使用vim时，可能会出现系统剪切板和vim剪切板不互通的问题，这个时候请检查vim的clipboard模块是否安装， 输入
vim --version | grep clipboard

1. 若已经安装会显示 +clipboard 。此时只需要更改vim的配置文件就可以实现文件互通。在配置文件中输入
   set clipboard=unnamed
   即可实现系统剪贴板和vim剪贴板互通

若未安装会显示 -clipboard。 此时需要重装vim。使用下面的命令进行vim重装
sudo apt install vim-gtk
重装后回到检查 clipboard 的步骤，查看是否有 +clipboard 出现。
参

vim只能粘贴50行的问题：
在当前用户主目录编辑~/.vimrc（如果不存在，新建这个文件），添加一行
:set viminfo='1000,<500
至于为什么要输入输入’1000,这个其实不重要，最主要的是输入<500,它是设置寄存器保存的行数的。即最大值为 500

        (7) n<Space>：n表示数字，按下数字后再按空格，光标会向右移动这一行的n个字符
        (14) /word：向光标之下寻找第一个值为word的字符串。
        (15) ?word：向光标之上寻找第一个值为word的字符串。
        (16) n：重复前一个查找操作
        (17) N：反向重复前一个查找操作
        (18) :n1,n2s/word1/word2/g：n1与n2为数字，在第n1行与n2行之间寻找word1这个字符串，并将该字符串替换为word2
        (19) :1,$s/word1/word2/g：将全文的word1替换为word2
        (20) :1,$s/word1/word2/gc：将全文的word1替换为word2，且在替换前要求用户确认。
        (29) 大于号 >：将选中的文本整体向右缩进一次
        (30) 小于号 <：将选中的文本整体向左缩进一次
        (36) :set paste 设置成粘贴模式，取消代码自动缩进
        (37) :set nopaste 取消粘贴模式，开启代码自动缩进
        (40) gg=G：将全文代码格式化


## Vision模式
ctrl+v (windows下为ctrl+q) vision block模式，可以选中一个block
v visual 选中
V visual line 选一行

## 进入插入模式的方法
insert --> normal ESC
变为插入模式
i insert
a append
o open a line below

I insert before line
A append after line
O open a line above

i , 表示从光标所在位置开始插入字符
I ，表示从光标所在行开头开始插入字符
a , 表示从光标所在位置后一个开始插入字符
A , 表示从光标所在行行尾插入字符
o , 表示从光标所在行下一行行首开始插入字符
O , 表示从光标所在行上一行行首开始插入字符
s , 表示删除光标所在处的字符然后插入字符
S , 表示删除光标所在行然后插入字符。

## 打开，保存与关闭
打开文件和保存:
1.vim samplex.cpp 2.打开多个:
vim a.cpp b.java c.py
默认是打开第一个文件
可以用b1,b2,b3来切换，即b+number来切换
bn切换到下一个，bp切换到上一个文件(是一个循环，即首尾相连) 3.关闭文件 保存文件
w write
q quit
wq wirte and quit
w! !表强制
q!
w filename 写入并保存带fielname里面
qa quit all
qa!
e file : edit file
e! 表示放弃对文件的所有修改，恢复文件到上次保存的位置；
saveas IOI.cpp , 表示另存为 IOI.cpp;
Sex , 表示水平分割一个窗口，浏览文件系统；
Vex , 表示垂直分割一个窗口，浏览文件系统。
ZZ 关闭文件并保存

:filetype on 开启文件类型检测，不启用语法高亮
:filetype plugin indent on
开启文件类型检测，包括自动缩进及设置

## 多窗口命令
split也可以为sp
vim -On a.cpp b.cpp c.cpp 初始打开多个分屏文件
CTRL-W s 或 :split 将窗口分割成上下两部分 (split)
CTRL-W v 或 :vsplit 将窗口分割成左右两部分 (split)
:split {file} 分隔窗口并在其中一个编辑 {file}
:vsplit :vsplit {file} 同上，但垂直分割
:vertical :vertical {cmd} 使命令 {cmd} 垂直分割
:sfind :sf[ind] {file} 分割窗口，从 {path} 中找到文件
{file} 并编辑之
:terminal :terminal {cmd} 打开新终端窗口
CTRL-W f 分割窗口并编辑光标下的文件名 (file)
CTRL-W n 或 :new 创建新空白窗口 (new)
CTRL-W q 或 :q[uit] 退出编辑并关闭窗口 (quit)
CTRL-W c 或 :clo[se] 隐藏当前缓冲区并关闭窗口 (close)
CTRL-W o 或 :on[ly] 使当前窗口成为唯一窗口 (only)
CTRL-W s 复制一个当前的同步窗口，命令窗口也会同步
CTRL-W r 向下旋转窗口 (rotate)
CTRL-W R 向上旋转窗口 (Rotate)
CTRL-W x 将当前窗口与后一个窗口对调 (eXchange)
CTRL-W = 使所有窗口等高等宽
resize {number} 设置当前窗口高度，可为负
CTRL-W < 减少当前窗口宽度
CTRL-W > 增加当前窗口宽度

## 查找与替换
map <key> <operation> , 表示设置快捷键 key 为操作 operation;
示例：设置 Ctrl + x 为显示行号，命令为：
map ^x <ESC>:set nu<ESC>

其中 ^x 的嵌入方式就是摁下 Ctrl + x,<ESC> 就是代表 ESC

ab noip lxl , 表示将以后输入的 noip 自动替换为 lxl；
<F1> 打开help
n （n 为具体数字） ， 表示将光标移至第 n 行的缩进后（自认为很鸡肋的一个命令）；
/字符串 , 表示在文件中查找该字符串（区分大小写），匹配到后按下 n 查找下一个 ， 按下 N 查找上一个（从光标开始查找）；注意不要输入冒号
ce , 表示将光标所在行文本居中；
ri , 表示将光标所在行文本居右；
le , 表示将光标所在行文本居左；

s/lxl/noip , 表示将当前行第一个 lxl 替换为 noip；
s/lxl/noip/g , 表示将当前行所有的 lxl 替换为 noip；
第 11 和 第 12 的命令还有一个用法，就是在命令开头加上数字表示对指定行操作，或者加上 dollor符 表示最后一行，或者两个用逗号隔开的数字表示区间。

e.g.
将 520 行到 1314 行的 lxl 替换为 noip :520,1314s/lxl/noip
将 最后一行的 lxl 替换为 noip :$s/lxl/noip
将 第 1 行的 lxl 替换为 noip: 1s/lxl/noip
%s/lxl/noip , 表示将所有的 lxl 替换为 noip

## shell
:shell 打开终端
!Commond （其中 Commond 是 Linux 命令） ， 表示执行 Linux 命令
如执行 !ping www.luogu.com.cn
r !Commond （其中 Commond 是 Linux 命令） , 表示执行命令，并且添加结果至操作文本光标处；
示例： r !echo I Love LXL FOREVER


## 移动
Vim 普通模式基本快捷键
移动 h,l,j,k
0 表示移动到当前行行头，相当于 Home 键；
^ 表示移动到当前行第一个非 blank 的字符；
$ 表示移动到当前行行尾，相当与 End 键（忽视 dollar 符后的反斜杠）；
w/W 表示移动到本行下一个单词开头；
e/E 表示移动到本行下一个单词结尾；
b/B 表示移动到本行上一个单词开头；
fa 表示移动到本行下一个 a 字符处；
f. 表示移动到本行下一个 . 字符处；
nfa （n 是自然数） 表示移动至光标后本行第 n 个 a 字符处；
nG 表示移动至第 n 行的行首；
H 表示移动至当前显示的文档第一行行首；
M 表示移动至当前显示的文档中间行行首；
L 表示移动至当前显示的文档最后一行行首；
gg 表示移动到第一行行首；
G 表示移动到最后一行行首；
zt 表示将当前行移动至当前显示的文档第一行；
zz 表示将当前行移动至当前显示的文档中间行；
zb 表示将当前行移动至当前显示的文档最后一行；
Ctrl + d 表示向下翻半页；
Ctrl + u 表示向上翻半页；
Ctrl + f 表示向上翻整页；
Ctrl + b 表示向下翻整页；

## 复制、删除
删除的内容会在寄存器里面保存，可以粘贴。
x 表示删除光标后的字符；
X 表示删除光标前的字符；
dd 表示删除光标所在行；
ndd （n 是自然数） 表示删除光标所在行（包括）下的 n 行
d1G 表示删除光标所在行到第一行；
dG 表示删除光标所在行到最后一行；
d+end d+home 删除一行内光标后面或者前面
d0 表示删除光标所在字符到光标所在行第一个字符；
yy 复制光标所在行；
nyy （n 是自然数） 表示复制光标所在行（包括）下的 n 行
y1G 表示复制光标所在行到第一行；
yG 表示复制光标所在行到最后一行；
y$\ 表示复制光标所在字符到光标所在行最后一个字符（同上，不用管美元符号）；
y0 表示复制光标所在字符到光标所在行第一个字符；
u 表示撤销上一个操作；
Ctrl + r 表示反撤销
p 表示粘贴内容，如果复制内容是整行，则从下一行开始粘贴。如果复制的是一部分内容，则从光标的下一个字符开始粘贴；
P 表示粘贴内容，如果复制内容是整行，则从上一行开始粘贴。如果复制的是一部分内容，则从光标所在位置开始粘贴。
纠错(INSERT模式下) 从光标前匹配
CTRL+h 删除上一个字符
ctrl+w 删除上一个单词
ctrl+u 删除当前行

## 配置&&配置文件

Vim 的基本配置
配置文件
配置文件分为两种，一种是系统配置文件，存放于 /usr/share/vim/vimrc , 另一种是用户配置文件，存放于用户主目录 ~/.vimrc 中。
/etc/vim/vimrc

注意：用户配置文件高于系统配置文件！
vim --clean a.cpp就没有配置了
set ai 设置自动缩进
set nu? 加问号表示询问，返回number or nonumber
set tabstop=4 "设置tab位四个空格
set shiftwidth=4 （n 为具体数字），表示将自动缩进设为 n （但不会改变 tab 的宽度）；
set mouse=a "设置鼠标
set ic , 关闭区分大小写（关闭后查找 lxl 和查找 LXL 是一样的）
set noic , 打开区分大小写；
set ruler "显示光标位置
set cul 突出显示当前行
set cuc 突出显示当前列
set nu 显示行号
set showmatch 显示括号匹配
set tabstop=4 设置 tab 长度为 4 个空格
set shiftwidth=4 设置自动缩进长度为 4 个空格
set autoindent 继承上一行的缩进方式
set ruler 显示光标所在位置
设置中文编码：
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
syntax on 开启语法高亮
filetype plugin indent on 开启文件类型检测
最后奉上蒟蒻的配置：（蒟蒻配置了 F5 一键运行）
set nu
set tabstop=4
set showmatch
set cul
set shiftwidth=4
set ruler
filetype plugin indent on
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
set autoindent

map <F5> :call CompileRunGcc()<CR>

func! CompileRunGcc()
exec "w"
if &filetype == 'c'
exec '!g++ % -o %.exe'
exec '!time ./%.exe'
elseif &filetype == 'cpp'
exec '!g++ % -o %.exe -std=c++14 -O2'
exec '!time ./%.exe'
elseif &filetype == 'python'
exec '!time python %'
elseif &filetype == 'sh'
:!time bash %
endif
endfunc



1. vim教程
	功能：
	    (1) 命令行模式下的文本编辑器。
	    (2) 根据文件扩展名自动判别编程语言。支持代码缩进、代码高亮等功能。
	    (3) 使用方式：vim filename
		如果已有该文件，则打开它。
		如果没有该文件，则打开个一个新的文件，并命名为filename
	模式：
	    (1) 一般命令模式
		默认模式。命令输入方式：类似于打游戏放技能，按不同字符，即可进行不同操作。可以复制、粘贴、删除文本等。
	    (2) 编辑模式
		在一般命令模式里按下i，会进入编辑模式。
		按下ESC会退出编辑模式，返回到一般命令模式。
	    (3) 命令行模式
		在一般命令模式里按下:/?三个字母中的任意一个，会进入命令行模式。命令行在最下面。
		可以查找、替换、保存、退出、配置编辑器等。
	操作：
	    (1) i：进入编辑模式
	    (2) ESC：进入一般命令模式
	    (3) h 或 左箭头键：光标向左移动一个字符
	    (4) j 或 向下箭头：光标向下移动一个字符
	    (5) k 或 向上箭头：光标向上移动一个字符
	    (6) l 或 向右箭头：光标向右移动一个字符
	    (7) n<Space>：n表示数字，按下数字后再按空格，光标会向右移动这一行的n个字符
	    (8) 0 或 功能键[Home]：光标移动到本行开头
	    (9) $ 或 功能键[End]：光标移动到本行末尾
	    (10) G：光标移动到最后一行
	    (11) :n 或 nG：n为数字，光标移动到第n行
	    (12) gg：光标移动到第一行，相当于1G
	    (13) n<Enter>：n为数字，光标向下移动n行
	    (14) /word：向光标之下寻找第一个值为word的字符串。
	    (15) ?word：向光标之上寻找第一个值为word的字符串。
	    (16) n：重复前一个查找操作
	    (17) N：反向重复前一个查找操作
	    (18) :n1,n2s/word1/word2/g：n1与n2为数字，在第n1行与n2行之间寻找word1这个字符串，并将该字符串替换为word2
	    (19) :1,$s/word1/word2/g：将全文的word1替换为word2
	    (20) :1,$s/word1/word2/gc：将全文的word1替换为word2，且在替换前要求用户确认。
	    (21) v：选中文本
	    (22) d：删除选中的文本
	    (23) dd: 删除当前行
	    (24) y：复制选中的文本
	    (25) yy: 复制当前行
	    (26) p: 将复制的数据在光标的下一行/下一个位置粘贴
	    (27) u：撤销
	    (28) Ctrl + r：取消撤销
	    (29) 大于号 >：将选中的文本整体向右缩进一次
	    (30) 小于号 <：将选中的文本整体向左缩进一次
	    (31) :w 保存
	    (32) :w! 强制保存
	    (33) :q 退出
	    (34) :q! 强制退出
	    (35) :wq 保存并退出
	    (36) :set paste 设置成粘贴模式，取消代码自动缩进
	    (37) :set nopaste 取消粘贴模式，开启代码自动缩进
	    (38) :set nu 显示行号
	    (39) :set nonu 隐藏行号
	    (40) gg=G：将全文代码格式化
	    (41) :noh 关闭查找关键词高亮
	    (42) Ctrl + q：当vim卡死时，可以取消当前正在执行的命令
异常处理：
    每次用vim编辑文件时，会自动创建一个.filename.swp的临时文件。
    如果打开某个文件时，该文件的swp文件已存在，则会报错。此时解决办法有两种：
        (1) 找到正在打开该文件的程序，并退出
        (2) 直接删掉该swp文件即可

