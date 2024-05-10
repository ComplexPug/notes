# 操作系统
## 分类
```
内存管理，进程管理，调度，硬件管理（磁盘io，网络io），文件系统，内核，基础设计
```

## [*Operating Systems:Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/preface.pdf)
```
虚拟化（virtualization）、并发（concurrency）和持久性（persistence）。
```

操作系统对gpu的讲解几乎是没有的，有空可以去看看[tiniy gpu](https://www.github.com)的GitHub项目

## Problems 
- [ ] fork的具体设计，他是什么时候的copy
- [x] ls,mkdir这些是shell自带的程序还是什么 抱歉不是
- [ ] 为什么cpp编译的内存地址都很大，他是怎么设计的呢。
sol:
- [x] gdb的pc显示了48位，但其实他是64位寄存器，线程的为什么是40位倒是不知道，估计是省略前导0了。
- [ ] elf格式是什么格式，貌似是裸机启动的相关
## NJU jyy's OS
讲的很好的，自动机，看手册，重代码实现，利用大模型。

## MIT 6.081
