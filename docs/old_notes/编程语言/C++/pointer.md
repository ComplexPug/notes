# 指针
## NULL and nullptr
为什么使用0作为空指针？
对于`foo(int)`和`foo(int*)`如何区分


NULL是一个宏定义
```cpp
#if defined(__need_NULL)
#undef NULL
#ifdef __cplusplus
#  if !defined(__MINGW32__) && !defined(_MSC_VER) // 不是mingw或者msc
#    define NULL __null
#  else
#    define NULL 0
#  endif
#else
#  define NULL ((void*)0) //c中
#endif
```
- [ ] 为什么使用0作为空指针
- [ ] c++为什么不用void* 0
> 因为c++不允许隐式地将 void* 转换为其他类型的指针

对于nullptr，是一个关键字了。
```cpp
namespace std {
    typedef decltype(nullptr) nullptr_t; // 使用 decltype 获取 nullptr 的类型，并定义为 nullptr_t
    constexpr nullptr_t nullptr = {};    // 定义一个 constexpr 常量 nullptr，其类型是 nullptr_t
}
```
相当于是在编译阶段的时候你的类型是什么，就给你什么样的0
```cpp
int *x = (int*)0;
double *x = (double*)0;
```