# DataBase Storge
计算机存储器在设计的时候是分层的，速度，易失性，价格和容量也有很大的差距。

为什么db不直接使用虚拟内存的缺页机制或者mmap机制：因为db更聪明。

## page 

不管怎么说，os中最小的读取单位就是page。所以db会以page为单位操作。每个page都有header和data

## tuple
什么是tuple，就是一行数据。

如何存储tuple。可以在page里面通过head计数器和定长数据，但这样不能避免linear scan。

还有一种是slotted pages。很有意思的一个结构（两个指针，一个在头，一个在尾存储slot array（just like map to search tuple address and sizeof is ），一个存储tuple）

![alt text](.assert/image.png)