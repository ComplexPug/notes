# Code of XV6
对于注释多的地方，都是精华。
## Kernel
### param
```cpp
#define NINODE       50  // maximum number of active i-nodes
#define NDEV         10  // maximum major device number
#define MAXOPBLOCKS  10  // max # of blocks any FS op writes
#define LOGSIZE      (MAXOPBLOCKS*3)  // max data blocks in on-disk log
#define NBUF         (MAXOPBLOCKS*3)  // size of disk block cache
```
### proc.h
context 切换上下文的，保存的不多。
trapframe 中断保存，全保存了，还有别的。 
cpu 有一些中断的信息。
```
// Per-CPU state.
struct cpu {
  struct proc *proc;          // The process running on this cpu, or null.
  struct context context;     // swtch() here to enter scheduler().
  int noff;                   // Depth of push_off() nesting.
  int intena;                 // Were interrupts enabled before push_off()?
};
```
- [ ] context为什么要出现?

noff和intena是用来记录中断层数和初始中断值的。
### spinlock.c
很不错的自旋锁实现的代码（不断的cas）。
- [x] 为什么获取释放的时候分别关中断和开中断。
因为要保证锁的原子性，中断的时候可能造成程序再次获取锁，造成死锁。

> 注意：中断和进程调度切换是不一样的。进程调取切换可以认为是暂停了程序，去运行与该程序无关的程序，但中断却不一样，他是暂停了程序去做了一些影响该程序的事情。

### sleeplock.c
自旋锁适合短作业，长期的话需要sleep锁了(其实就是重量级锁)。
```
# !/kernel/sleeplock.h
// Long-term locks for processes
struct sleeplock {
  uint locked;       // Is the lock held?
  struct spinlock lk; // spinlock protecting this sleep lock
  
  // For debugging:
  char *name;        // Name of lock.
  int pid;           // Process holding lock
};

```

### 

### proc.c

## User