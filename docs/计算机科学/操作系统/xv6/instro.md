# instroduction
一个基于risc-v的简单的类unix教学操作系统，使用ANSI C编写，支持多处理器。
受Unix Version 6影响。
代码的话九千行左右，规模类似linux的0.xx版本
## debug tips

- You may find that your print statements produce a lot of output that you would like to search through; one way to do that is to run make qemu inside of script (run man script on your machine), which logs all console output to a file, which you can then search. Don't forget to exit script.
您可能会发现您的打印语句会产生大量您想要搜索的输出;一种方法是在 script （在计算机上运行 man script ）内部运行 make qemu ，它将所有控制台输出记录到一个文件中，然后您可以搜索该文件。别忘了退出 script 。

## QEMU
`ctrl+a x` 关闭虚拟机

## problem