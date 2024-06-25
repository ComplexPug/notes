# Virtual Function
## 内存对齐
内存是对其的。
```cpp
class A {
    int a;
    char b;
    short c;
}
/*
00 00 00 00
[A         )
00 00 00 00
[b)   [c   )
*/
```