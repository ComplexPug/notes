# C++
## null and nullptr
null 简单。
nullptr是c++11引入的新的更安全的空指针。
## auto
类型推导
## condition_variable

## Bugs
很有意思，之前一直以为后缀没啥。直到我
```
int *p = malloc(sizeof(int));
```
的时候没有修改.cpp为.c只修改了g++/gcc居然还是报错。