# Class

## 基础认识

成员变量，成员函数：Class里面的变量和函数。

```c
class Demo {
private:
    int x;
    Demo() {
        cout << "构造函数" << endl;
        this->a = 0; // this是指向对象的指针，隐含在函数里面
    }
    ~Demo() {
        cout << "析构函数" << endl;
    }
public:

protected: // 子类可访问
};
```
### 继承
```c
class Demo2 : public Demo {}; // Demo中的成员属性不变。
class Demo3 : private Demo {}; // Demo中的成员变为private
class Demo4 : protected Demo {}; // Demo中的成员变为protected
// 所有的Demo的private成员都不能被访问，始终是private。
```

## 高级认识

```c
class Demo {
    Demo() = default; // 默认构造函数，在没有构造函数的时候生成，加default表示始终生成
    Demo(const Demo&) = default; // 拷贝构造函数
    Demo(Demo&&) = default; // 移动构造函数
    Demo& operator=(const Demo&) = default; // 拷贝赋值操作符
    Demo& operator=(Demo&&) = default; // 移动赋值操作符
}
int main() {
    Demo demo1;// Demo();
    Demo demo2 = demo1; //Demo(const Demo&)
    demo2 = demo1; //operator = 
}
```


