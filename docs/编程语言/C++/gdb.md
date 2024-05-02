# [GDB](https://www.sourceware.org/gdb/)
go,c,c++,rust都可以用
## 语法

### 使用调试符号编译程序

-g 或者 -ggdb
区别：-g 标准形态，兼容性高，-ggdb，专一形态

调试的时候最好别开优化，源代码和汇编代码差太多。
### 打印代码
`l(or list) [<line number> or <function name>]` 打印最近的10行代码

### 断点
`b(or break)  [filename:] <line number> or <function name>`
`b +<number>` 当前行+number
`b *(memory address)`
`b <...> if condition`
`d(or delete) <break-number>` 也可以删除display

break（简写b）是我们最熟悉的。
tbreak（简写tb）：临时断点，也就是触发一次后自动消失。与break用法相同。
hbreak（简写hb）：硬件断点。对我们来说没什么用。
rbreak（简写rb）：根据正则表达式设置断点。用法：rbreak [正则表达式]。
`Example: rbreak dfs* ，由于dfs1与dfs2均匹配，所以这两个函数均会被加上断点`

命令：disable（简写为dis）
格式：disable 类型 [编号]
作用：临时禁用某些类型的对应编号的东西，待会儿讲。

命令：delete（简写为d）
格式：delete 类型 [编号]
作用：删除某些类型的对应编号的东西。

命令：enable（简写为en）
格式：enable 类型 [编号]
作用：启用某些类型的对应编号的东西。

condition
`用法：condition [断点编号] [条件]。condition可缩写为cond。`
效果：触发断点时，只有指定的条件为真时才停下。

commands（简写为comm）可以在触发某个（或多个）断点的时候运行指定gdb命令。
`用法：commands [断点编号1] [断点编号2] ...`
之后，它会让你逐行输入要指定的gdb命令。
在到你指定的断点时，他都会逐行运行你之前输入的命令。

用法：watch/rwatch/awatch [变量名]
作用：监视指定变量。
watch（简写wa）：当指定变量被写时停下。
rwatch（简写rwa）：当指定变量被读时停下。
awatch（简写awa）：当指定变量被读/写时停下。


有时候，我们要复现某个bug，这个时候，我们可以创建一个快照，即checkpoint。
命令：checkpoint（可简写为ch）
用法：无参数。
效果：创建一个快照，包含当前调试的所有信息。同时会输出这个checkpoint的信息，就像这样：
checkpoint 1: fork returned pid 2577.
其中，数字1便是这个checkpoint的编号。
那么，如何回滚到以前的快照呢？那就是restart命令啦！
用法：restart [checkpoint编号]
效果：回退到指定checkpoint的快照。

### 修改
`call <function>` 调用，可以赋值
`set <aur> = <value>`

### 输出变量
`p(or print) <var-name>` 打印一次变量
`disp(or display) <var-name>` 监控变量
`d disp <disp-number>`
### 打印调试信息
`info stack/locals/b/disp` 
`bt(or breaktrace)` 查看栈帧
    up/down [num] 往栈顶/栈底移动num帧。num默认为1。
    frame [num] 切换到第num帧。frame简写为f。num默认为0
`where` 打印当前的stack
`whatis <var-name>` 查看类型名
`ptype var` 打印类型名
### 运行程序
`r(or run)` 从头运行程序
`c(or continue) [number]` 运行到下一个断点
`u(or until) number`  运行到指定行号停止
`n(or next) [number]`  单步执行。若当前行有函数调用，则把这个函数作为一个整体执行（即不进入函数内部）。若给出参数 n，则执行 n 步。
`s(or step) [number]` 单步执行。若当前行有函数调用，则进入该函数内部。若给出参数 n，则执行 n 步。
单步执行遇到断点结束
`fin(or finish)` 执行到函数返回

`用法：ignore [断点编号] [num]。ignore可缩写为ig。`
效果：在前num次触发指定断点时都不停止（即到了第num+1次触发断点才停下）
这在调一些循环结构的代码时比较有用。

用法：`jump [num]`
作用：强制使跳转至第num行。（中间的行都跳过了）
注意，这个不能跨函数跳转，否则会出错。

return
用法：`return [argu]`
作用：强制使当前函数退出，并返回argu值。（如果该函数本来就没有返回值，则argu可以省略）

### shell
`shel <shel-command>`

### 日志
`set logging enabled`

### 保存
用法：save breakpoints [文件名]
效果：将当前所有的断点信息保存到一个指定的文件里。
用法：source [文件名]

### 退出
`q(or quit)`

## Python
1.Python
    gdb在不低的版本里面内置了python解释器
    输入python或者python加语句即可
        python print(gdb.breakpoints()[0].location)
        python gdb.Breakpoint('7')

## 反向操作
程序运行之后执行`record` 录制命令
没有录制是不能进行反向操作的的
`reverse-continue,reverse-next,reverse-next,reverse-step...`
```
- reverse-next(rc): 参考next(n), 逆向执行一行代码，遇函数调用不进入
- reverse-nexti(rni): 参考nexti(ni), 逆向执行一条指令，与函数调用不进入
- reverse-step(rs): 参考step(s), 逆向执行一行代码，遇函数调用则进入
- reverse-stepi(rsi): 参考setpi(si)， 逆向执行一条指令，与函数调用则进入
- reverse-continue(rc): 参考continue(c), 逆向继续执行
- reverse-finish: 参考finish，逆向执行，一直到函数入口处
- reverse-search(): 参考search，逆向搜索
- set exec-direction reverse: 设置程序逆向执行，执行完此命令后，所有常用命令如next, nexti, step, stepi, continue、finish等全部都变成逆向执行
- set exec-direction forward: 设置程序正向执行，这也是默认的设置
```
有人说：gdb的反向不好用，推荐[rr](https://github.com/rr-debugger/rr)。

## TUI
### 快捷键
CTRL x a 进入tui模式，小小的可视化吧。
CTRL l 刷新tui模式
CTRL x 1/2 打开1/2个窗口,多摁切换
CTRL o 切换窗口
tui reg float 
### cgdb  
一个开源项目，可能比TUI好用一点。

## Core dump（核心转储）
是指在程序运行过程中发生错误或异常时，操作系统将程序的内存内容保存到磁盘上的一种文件。这个文件包含了程序崩溃时的内存状态，包括变量的值、函数调用栈、寄存器状态等信息。通过分析 coredump 文件，可以了解程序崩溃的原因，以便进行调试和修复。
### ulimit命令
首先默认是生成不了core文件的，得ulimt调整限制，修改只对当前shell起作用
`ulimit -a`
`ulimit -c unlimited`
当看到`(core dumped)`的时候就是说明成功了
```shell
vim /etc/profile                                   
ulimit -c unlimited
```
### 存储位置
在 Linux 系统中，core dump 文件的路径是由 /proc/sys/kernel/core_pattern 定义的，如果这个文件不存在，或者内容为空，那么 core dump 文件就会生成在当前目录下

也可以通过修改 /proc/sys/kernel/core_pattern 指定 core 文件生成的路径和文件名
```shell
# 查看当前 core 文件路径
cat /proc/sys/kernel/core_pattern 

# 指定 core 文件路径
sudo echo "yourpath/core.%e.%p.%h.%t" > /proc/sys/kernel/core_pattern
sudo sysctl -w kernel.core_pattern=yourpath/core.%e.%p.%h.%t  # # 也可以使用 sysctl 修改 kernel.core_pattern 来指定 core 文件路径

#  core 文件名称定义中，可以使用占位符保留一些有用信息
%p: pid
%u: uid
%g: gid
%s: signal number
%t: UNIX time of dump
%h: hostname
%e: executable filename
```

### 调试
`gdb a.out core`进行调试

### 注意
如果程序是在docker中运行的，记得启动docker的时候加上--privileged 参数，该参数让 container内的root拥有真正的root权限。否则，container内的root只是外部的一个普通用户权限。privileged启动的容器，可以看到很多host上的设备，并且可以执行mount。甚至允许你在docker容器中启动docker容器。


如果最后报出的信息是系统库，则可以在gdb下输入bt来调出堆栈信息，如果是多线程，则输入thread apply all backtrace 来显示所有线程栈回溯.
