# Random 随机数

## 开始之前

之前用随机数很随性，一开始用c++ random，后来用pbds的什么“mt19937真随机数”。也知道一些`ax+b`的到随机数的原理。直到后面遇到一个脑筋题：

> 用 `get_7()` 函数的到 `get_41()` 函数，其中的 `get_7()` 是等概率的的到 `[0,7)` 区间的正整数。

虽然后面知道答案了，但联想到之前写代码的到较大随机数临时自己写的 `def get_big_random() {get_small_random()**2` 加上最近编译内核出现了`/dev/urandom`丢失的问题。

探究一下。

## 分类

随机数的特征是不可预测的，无周期的，概率均等出现。在这些前提下肯定是性能越高越好。

伪随机数通过设置种子这个不变量来生成伪随机数。
真随机数通过动态获取参数来生成真随机数。参数可以是任何随机的事件，放射性衰变，大气噪声等。

## 伪随机数发生器

伪随机数发生器 Pseudo-Random Number Generator，简称 PRNG

需要设置种子参数来初始化。存在周期，可预测，性能比TRNG好。

### 线性同余生成器 LCG

$$ X(n+1) = (a * X(n) + c) % m $$

简单，存在周期性和固定性。

可能c语言的random是用这个写的。

### 梅森旋转算法（Mersenne Twister）

[wekipeida](https://zh.wikipedia.org/wiki/%E6%A2%85%E6%A3%AE%E6%97%8B%E8%BD%AC%E7%AE%97%E6%B3%95)
感兴趣可以看，我不感兴趣。

MT19937是其最常见的变体，得名于其周期为2^19937−1的梅森素数。

c++中的mt19937,`mt19937_64`分别是32bit和64bit的。

周期长，速度快，占用缓存大，依旧是伪随机算法。

## 关于rand()%n和`rand()*rand()`

对于想获得 $[0,n)$ 来说， random()%n 并不是真正随机的，因为如果`RAND_MAX%n`不等于0，那么1%n到`RAND_MAX%n`中必定会有两个数出现的次数不相同。

对于 rand() * rand() 来说，出现概率和他的因子个数有关，比如质数那她两个rand就必然得出现一个1才可以，概率并不均等。

## 得到随机数范围

```python
# 如get_7得到get_41，通常是这样的
def get_49():
    return get_7()*7+get_7()

def get_41():
    val = get_49()
    while val > 41:
        val = get_49()
    return val

# 更通用的
def get_MAX_INT():
    pass

def get_random(x:int):
    limit = MAX_INT - MAX_INT % x
    val = get_MAX_INT()
    while val > limit:
        val = get_MAX_INT()
    return val % x
```

## `/dev/random` `/dev/urandom`是干什么用的

定位内核源码的`drivers/char/random.c`位置,基于熵（这几天开启服务器时候，无聊看远程屏幕的开机日志/dev/random的会停留一下hh）

`urandom`的u是unblocked的意思，random调用的时候熵不够多会阻塞直到满。不过那是以前了。

现在的random程序的是一个：安全的伪随机数字生成。（来自源码）

而且从[Arch Linux rng doc](https://wiki.archlinux.org/index.php?title=Random_number_generation) 中看，两者效果差不多。

而且现在不会阻塞了，也不会消耗熵（256保持），因为CRNG。

那她就是单纯的把熵作为随机种子吗,不是。密钥会动态抹除的重算。

代码大概就是多了熵的收集、累计处理和fast-key-erasure RNG : crng 快速擦出密钥生成。

不过没有周期和种子也不可复现和预测了。而且默认`/dev/random`是`/dev/urandom`

```shell

/proc/sys/kernel/random # 查看系统熵池的容量，熵的多少等。
# 可以查看源码中的注释: sysctl interface 部分

cat /dev/random # 查看随机数
```

