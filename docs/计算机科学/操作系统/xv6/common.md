# Common
## 前言
2020的lab貌似跑不动，这里跑2023的吧，看着区别不是很大。
查看进程（类似`ps`）使用`ctrl + p`
退出qemu `ctrl+a x`
- [ ] main(int argc, char *argv[]) :argc是argv的长度
## 文件结构
kernel，user，和一个mkfs
mkfs里面有一个`mkfs.c`,make file system
- [ ] 为什么这里独立出来了呢，而不是放到kernel里面
`ls.c ls.asm ls.o _ls` 源代码的几个阶段
`ls.d`是gcc生成的引用的头文件信息，用于make处理依赖
`ls.sym`
```
## GDB
```shell
# 第一个 terminal
cd xv6-labs-2023
# 第一次执行 gdb 需要 执行 下面条语句 
echo "add-auto-load-safe-path $(pwd)/.gdbinit " >> ~/.gdbinit # 第一次执行，保存gdb初始配置

make CPUS=1 qemu-gdb # 开了个端口可以进行gdb调试

# 第二个 terminal
cd xv6-labs-2023
gdb-multiarch
```
## 测试
```
./grade-lab-util sleep
```

## Vscode
最好是新开一个配置，不然太多插件有点乱。
安装了clangd和clangd插件，可以正常跳转,但有些地方还是报错的。
bear生成compile_commands.json就可以了`make clean && bear -- make qemu`。 这里我好像没起作用。
在xv6目录下执行make clean && bear -- make qemu ，将会生成一个 compile_commands.json
将 compile_commands.json 移动到 .vscode目录下
在.vscode目录下新建c_cpp_properties.json文件
```
{
  "configurations": [
      {
          "name": "Linux",
          // "includePath": [],
          // "defines": [],
          // "compilerPath": "/usr/bin/riscv64-linux-gnu-gcc",
          // "cStandard": "gnu17",
          "intelliSenseMode": "${default}",
          "compileCommands": "${workspaceFolder}/.vscode/compile_commands.json"
          // "configurationProvider": "ms-vscode.makefile-tools"
      }
  ],
  "version": 4
}
```
clangd-format

对于在vscode debug，可以attach到gdb。
也可以luanch再配置一遍。

## gcc的作用
在代码里面不会有gcc的库，比如`<stdio.h>`，所有的函数都是自己实现的。
gcc在这里就是纯粹的编译器，编译二进制和汇编代码。
- [] 链接用没用有待商讨

对于想打断点的程序，需要打开，即`-exec file ./user/_ls`才能调试（不然gdb不知道）。
## SystemCall tables
| function name             | description                     |
| :-----------:             | :---------:                    |  
| fork()                    |	创建进程                      |
| exit()                    |	结束当前进程                  |
| wait()                    |	等待子进程结束                 |
| kill(pid)                 |	结束 pid 所指进程              |
| getpid()                  |	获得当前进程 pid               |
| sleep(n)                  |	睡眠 n 秒                     |
| exec(filename, *argv)     |	加载并执行一个文件             |
| sbrk(n)                   |	为进程内存空间增加 n 字节       |
| open(filename, flags)     |	打开文件，flags 指定读/写模式  |
| read(fd, buf, n)          |	从文件中读 n 个字节到 buf      |
| write(fd, buf, n)         |	从 buf 中写 n 个字节到文件     |
| close(fd)                 |	关闭打开的 fd                 |
| dup(fd)                   |	复制 fd                       |
| pipe( p)                  |	创建管道，并把读和写的fd返回到p |
| chdir(dirname)            |	改变当前目录                   |
| mkdir(dirname)            |	创建新的目录                   |
| mknod(name, major, minor) |	创建设备文件                   |
| fstat(fd)                 |	返回文件信息                   |
| link(f1, f2)              |	给 f1 创建一个新名字(f2)       |
| unlink(filename)          |	删除文件                      |

## 什么是fd
fd 是 File descriptor 的缩写，中文名叫做：文件描述符。文件描述符是一个非负整数，本质上是一个索引值（这句话非常重要）。
在 POSIX 语义中，0，1，2 这三个 fd 值已经被赋予特殊含义，分别是标准输入（ STDIN_FILENO ），标准输出（ STDOUT_FILENO ），标准错误（ STDERR_FILENO ）。
文件描述符是有一个范围的：0 ～ OPEN_MAX-1 ，最早期的 UNIX 系统中范围很小，现在的主流系统单就这个值来说，变化范围是几乎不受限制的，只受到系统硬件配置和系统管理员配置的约束。
你可以通过 ulimit 命令查看当前系统的配置： 
```shell
$ ulimit -n
4864 
```
如上，我系统上进程默认最多打开 4864 文件。

## Problems
- [ ] fork的具体设计，他是什么时候的copy
- [x] ls,mkdir这些是shell自带的程序还是什么 抱歉不是
- [ ] 为什么cpp编译的内存地址都很大，他是怎么设计的呢。
sol:错误的，其实看到的是栈的地址，栈比较靠大段所以就看很大了。
- [x] gdb的pc显示了48位，但其实他是64位寄存器，线程的为什么是40位倒是不知道，估计是省略前导0了。
- [x] elf格式是什么格式:是二进制执行文件，a.o a.out a.so 就可以看到是一种elf文件( 可重定位文件relocatable,可执行文件executable,共享文件shared object动态库)。