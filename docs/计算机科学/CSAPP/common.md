# Common
## Tools
```
gcc
gdb
objdump
readelf
vscode/vim

```

## Q&A

- [ ] c++引入头文件.o文件和直接链接.cpp有什么区别?
貌似没有什么可比性？
- [ ] 如何解决头文件的重复引用问题。
对于单个文件，通过头文件避免重复引用。对于多文件，链接的时候也会通过符号和重定向来重用（静态动态链接只不过是是放在可执行文件还是.dll里面，是对于多个程序而言）。
```cpp
#ifndef MYHEADER_H
#define MYHEADER_H

#endif
```