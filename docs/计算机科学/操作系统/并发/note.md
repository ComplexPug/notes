# 条件变量(Condition Variables) 和 信号量(semaphore)
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