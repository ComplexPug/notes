# Lock 锁

并发得力好帮手。

## 列举&分类

- 同步锁
- 自旋锁Spin Lock
- 互斥锁Mutex
- 读写锁
- 条件变量Condition variable
- 信号量Semaphore
- 乐观锁 Optimistic Lock
- 悲观锁 Pessimistic Lock
- 可重入锁

## 一些实现

## RCU

Read-Copy Update

针对读取较多的情况。

优点：

 - 读者侧开销很少、不需要获取任何锁，不需要执行原子指令或者内存屏障；
 - 没有死锁问题；
 - 没有优先级反转的问题；
 - 没有内存泄露的危险问题；
 - 很好的实时延迟；
缺点：

 - 写者的同步开销比较大，写者之间需要互斥处理；
 - 使用上比其他同步机制复杂；

[Linux kernel Documents RCU](https://www.kernel.org/doc/html/latest/RCU/whatisRCU.html) or `kernel-source/Documentation/RCU/*`

## SpinLock

自旋锁
