# 条件变量(Condition Variables) 和 信号量(semaphore)
## 临界区

临界区：每个进程中，访问临界资源的那段代码

临界资源：一次仅允许一个进程使用的资源。例如：物理设备中的打印机、输入机和进程之间共享的变量、数据。

## 条件变量
## 信号量
```cpp
wait(sem* S){
    if(S->value==0){
        add this process to S->list;
        block();
    }
    S->value--;

}               

signal(sem* S){
    S->value++;
        if(S->list非空){
            remove a process P from S->list;
            wakeup(P);
        }
}
```