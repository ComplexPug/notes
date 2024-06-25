# File System
```cpp
nmeta 46 (boot, super, log blocks 30 inode blocks 13, bitmap blocks 1) blocks 1954 total 2000
balloc: first 746 blocks have been allocated
balloc: write bitmap block at sector 45
```
xv6的block是1KB。

inode里面存储的block `uint addrs[NDIRECT+1];`可以设计为多级索引（可能是设为做作业去实现了），这里直接就是inode里面的12个指针，如果不够再用第13个当索引block（1k/4），再不够就error。

对于一种解决方案是设计一二三级索引。

可以在`kernel/fs.c:bmap`函数里面查看。

## 对于mkfs/mkfs.c
用于创建xv6文件系统的工具，它在xv6文件系统的初始化阶段使用。这个程序的主要功能是构建一个新的、空的文件系统结构，包括超级块、i节点区、数据块等，同时创建必要的文件和目录（如根目录）。运行在xv6操作系统之外，通常在系统编译阶段运行，用于准备文件系统镜像，这个镜像随后会被加载到xv6启动时使用的磁盘或虚拟磁盘中。

## fs结构
一开始说的是磁盘结构。