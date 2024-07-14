# 异常控制流
## 8.1

### 异常分类
1. 中断interrupt：异步发生（剩下三个是同步的），io设备引起
2. 陷阱trap，有意的，system call，
3. 故障fault
4. 终止abort

- [x] xv6的trapframe和context为什么不一样。这里提出，答案见os/xv6