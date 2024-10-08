# semaphore 信号量

主要是看看Linux Kernel的实现的计数信号量。比较短。

## Definition

信号量：用来同时限制访问资源的数量。
临界区：访问共享资源的代码片段

## vs lock

也就是说有什么用，其实定义来看就是这样的作用，而且semaphore是由spinlock实现的。

- [ ] 可以提出问题：如果count最大是1，那他和锁的区别还存在吗


## Code

```c
kernel-source/include/linux/semaphore.h
#include <linux/list.h>
#include <linux/spinlock.h>

struct semaphore {
	raw_spinlock_t		lock;
	unsigned int		count;
	struct list_head	wait_list;
};

...
初始化相关宏和函数
...

extern void down(struct semaphore *sem);
extern int __must_check down_interruptible(struct semaphore *sem);
extern int __must_check down_killable(struct semaphore *sem);
extern int __must_check down_trylock(struct semaphore *sem);
extern int __must_check down_timeout(struct semaphore *sem, long jiffies);
extern void up(struct semaphore *sem);
```

结构是一个自旋锁，一个计数，一个线程任务列表。

剩下的函数感觉上只看down和up就可以了，其他都是一些down plus。

## What is down and up

`down`就是获取信号量 也就是想让count--。
```c
kernel-source/kernel/locking/semaphore.c
/**
 * down - acquire the semaphore
 * @sem: the semaphore to be acquired
 *
 * Acquires the semaphore.  If no more tasks are allowed to acquire the
 * semaphore, calling this function will put the task to sleep until the
 * semaphore is released.
 *
 * Use of this function is deprecated, please use down_interruptible() or
 * down_killable() instead.
 */
void down(struct semaphore *sem)
{
	unsigned long flags;

	might_sleep();// 看名字和查定义知道是可忽略的语句。
	raw_spin_lock_irqsave(&sem->lock, flags);//获得锁，禁用当前cpu core的中断，保存中断状态
	if (likely(sem->count > 0))
		sem->count--;
	else
		__down(sem);
	raw_spin_unlock_irqrestore(&sem->lock, flags);//那就是解锁相关的了。
}
EXPORT_SYMBOL(down);

static noinline void __sched __down(struct semaphore *sem)
{
	__down_common(sem, TASK_UNINTERRUPTIBLE, MAX_SCHEDULE_TIMEOUT); //大写的都是宏定义的数字参数，比如可以是（举例的，不一定对的）2,INT_MAX
}

/*
 * Because this function is inlined, the 'state' parameter will be
 * constant, and thus optimised away by the compiler.  Likewise the
 * 'timeout' parameter for the cases without timeouts.//有意思的东西
 */
static inline int __sched __down_common(struct semaphore *sem, long state,
								long timeout)
{
	struct semaphore_waiter waiter;

    //添加到任务列表头
	list_add_tail(&waiter.list, &sem->wait_list);
	waiter.task = current; //当前线程
	waiter.up = false;

	for (;;) {
		if (signal_pending_state(state, current))//中断是否可以被杀死或中断：state满足并且线程任务是中断或者杀死。
			goto interrupted;
		if (unlikely(timeout <= 0))//超时
			goto timed_out;
		__set_current_state(state);//刷新当前线程状态
		raw_spin_unlock_irq(&sem->lock);//解锁，开启中断
		timeout = schedule_timeout(timeout);//睡眠该进程
		raw_spin_lock_irq(&sem->lock);//加锁
		if (waiter.up)
			return 0;
	}

 timed_out:
	list_del(&waiter.list);//这样会退出临界区资源访问
	return -ETIME;

 interrupted:
	list_del(&waiter.list);
	return -EINTR;
}

```

up函数是释放临界区的操作，也就是想让count增加的操作，简单的多
```c
kernel-source/kernel/locking/semaphore.c

/**
 * up - release the semaphore
 * @sem: the semaphore to release
 *
 * Release the semaphore.  Unlike mutexes, up() may be called from any
 * context and even by tasks which have never called down().
 */
void up(struct semaphore *sem)
{
	unsigned long flags;

	raw_spin_lock_irqsave(&sem->lock, flags);
	if (likely(list_empty(&sem->wait_list)))
		sem->count++;
	else
		__up(sem);
	raw_spin_unlock_irqrestore(&sem->lock, flags);
}
EXPORT_SYMBOL(up);

static noinline void __sched __up(struct semaphore *sem)
{
	struct semaphore_waiter *waiter = list_first_entry(&sem->wait_list,
						struct semaphore_waiter, list);
	list_del(&waiter->list);
	waiter->up = true;
	wake_up_process(waiter->task);
}

```
