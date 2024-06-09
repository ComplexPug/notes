```shell
pstree # ps的tree形式
wc # 默认输出行数，单词数，字节数
stat <filename> # 查看inode信息，ls -i 或者 tree --inodes
cloc <dictory-path> # 统计代码行数 
netstat -tuln # 查看端口占用 tcp,udp,listen,number  
objdump -d <filename> # 反汇编二进制可执行文件
type/which/where -a <command> # 查看二进制文件的位置，识别别名
du -h <file> # 查看实际文件占用磁盘大小
sudo fdisk -l # 查看硬盘分区的扇区大小和I/O大小
```