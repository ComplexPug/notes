# Vim

h           左
j           下
k           上
l           右
^ 或 0      首
$           尾
 
A   在一行结尾处附加文本
I   在一行的开头处插入文本
o   沟槽所在位置下一行打开新行
O   沟槽所在位置上一行打开新行

d   delete
w   使命令光标移动一个单词
W   移动下一个大写单词
b   倒退一个单词
B   倒退时标点/符号不算
 
[{  Jump to block start
   Move cursor to matching parenthesis
 
 
 
G   移动到文件结尾
1G  到达文件顶端
42G 移动到42行.G(转至)命令

## normal -> insert

输入后由正常模式转换插入模式，光标跳转。
i/I    insert，即光标的左侧，大写跳转到行的最左侧
a/A    append，即光标的右侧，大写跳转到行的最右侧
c/C    change，即删掉某些部门来重写，大写清空一行。
o/O    新增一行，o下面加，O上面加
s/S    删除后面的字母，S删除一
cc     等于S
## normal下的修改
D   清空一行
dd  复制一行并删除
r   替换字母，只替换一次，R可以一直替换，直到Esc。
s   同c加space
S   删除一行并插入 同cc
x   删除一个字母
~   大小写转换
 
移动时先用d做删除,再用p进行放置
复制时选用y做"拖曳"动作,再用p进行放置.
 
cw  从光标到这个单词的结尾
c2b 从光标往前两个单词
c$ 从光标到本行结尾  同 "C"
c0
 
cc  将一整行换成输入文本
cw 和 cc工作方式不同.使用cw时,原来的文本会先留着,直到输入内容逐渐将它覆盖掉,而任何余下的原文本(到$为止的文本),在按下ESC后立即消失.但使用cc时,原文本会立即消失
 
dw  删除单词
dd与D   删除一行
db  向前删除
d$ 和 d0
 
D 是d$的简写
 
 
xp  对调两个字母
 
y   拖曳
yw  y$  4yy
yy  一整行 与Y相同,与D或C不太同
 
yy  -> 2j   -> P
 
jp  光标往下移一行再将粘贴
 
 
 
50i*ESC #会插入50星号
||换成&&    2r&
 
 
 
 
J   光标所有行与下一行合并
.   重复上一个命令
 
``  回到上一个记号或上下文
''  回到包含上一个记号的行的开头处
 
 
## 修改
x
u
y 复制选中
y$ 复制

## 复制粘贴 
y   copy the selected text to clipboard
p   paste clipboard contents
D   Cut to the end of line
dd  Cut current line
y$  copy to end line
yy  copy current line

## 跳转
基本通用于各种模式下，也是。
[[
][
[]
]]
gg
G
w
e

## 查找和替换
搭配正则更好用。

## 选中
选中需要切换模式，与normal，insert模型平级。
v：visual
V: visual line, 按行选,可以与v相互切换
模式下可以G,gg,w都可以用于跳转使用，o切换到选中部分的另一端继续选择。
可以删除复制操作特定的选中。