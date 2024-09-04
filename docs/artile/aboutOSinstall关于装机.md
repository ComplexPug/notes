# 关于装机

之前装机都是用的官网的iso镜像，然后用软件制作一个usb启动器来引导安装。这里探究一下相关知识和更方便的安装。

## Intro

BIOS Basic Inout Output System 作用：自检，初始化硬件，硬中断，引导。更准确应叫legacy BIOS.

UEFI Unified Extensible Firmware Interface ：现在的主板都是UEFI.

MBR Master Boot Record 主引导记录 作用：启动os加载程序，分区表（支持最大2TB和四个主分区）

GPT GUID Partition Table 全局唯一标识分区列表，最大内存和分区都很大。

分区表；划分磁盘区域呗,可以认为是一个被划分的(begin,end,type),type就是文件系统类型ext4等。

更多时候习惯把传统BIOS和UEFI统称为BIOS

| BIOS | 分区表 |
| -------------- | --------------- |
| legacy | MBR |
| UEFI | GPT |

可以不严谨地说没人不用UEFI+GPT

## 如何制作自己的iso镜像


## 各种硬盘格式

## 关于磁盘挂载是什么
