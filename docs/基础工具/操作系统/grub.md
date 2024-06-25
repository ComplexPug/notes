# grub

## 前言
G15 5520换过主板后开机进入grub，不能引导Windows（哪来的grub，居然还有ubuntu，难道是之前移动ubuntu的东西吗，那为什么grub还留下了呢）。

首先只看硬盘就好了，找到引导盘,windows一般都是这个路径
可以使用ls和cat查看file system的格式，大小和内容来判断是引导盘还是数据盘。
```shell
ls (hd0,gpt1)
ls (hd0,gpt1)/ 
上面俩命令不一样
grub>chainloader (hd0,gpt1)/efi/Microsoft/Boot/bootmgfw.efi
grub>boot
```
之后再开机就能移动引导，不懂。

虽然开机了，但过了三分钟主板又烧了，sad😭。