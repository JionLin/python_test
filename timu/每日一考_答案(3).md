### 题目 1：动态添加属性

定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。

**答案**：

```python
class Person:
    pass
p = Person()
p.hobby = "reading"
print(p.hobby)
```

**分析**：Person 类定义较为简单，没有属性和方法。创建 Person 类的对象 p 后，直接通过 对象.属性名 = 值 的方式动态添加了 hobby 属性，并赋值为 "reading"。最后打印该属性，体现了 Python 中对象动态添加属性的灵活性。

### 题目 2：动态添加方法

定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：\(S = π r^2），然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用 types.MethodType）

**答案**：

```python
import types
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
def calculate_area(self):
    return math.pi * self.radius ** 2
c = Circle(5)
c.calculate_area = types.MethodType(calculate_area, c)
area = c.calculate_area()
print(area)
```

**分析**：Circle 类有一个用于初始化半径的构造函数。calculate_area 函数接收 self 参数（代表对象本身），计算圆的面积。通过 types.MethodType 将 calculate_area 函数绑定到 Circle 类的对象 c 上，使其成为 c 的一个方法。调用 c.calculate_area() 即可计算并打印出半径为 5 的圆的面积，展示了动态添加方法的过程。

### 题目 3：封装特性

定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），提供一个 deposit 方法用于存钱，一个 withdraw 方法用于取钱，取钱时如果余额不足则打印提示信息。

**答案**：

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入{amount}元，当前余额为{self.__balance}元")
        else:
            print("存入金额需大于0")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"取出{amount}元，当前余额为{self.__balance}元")
        else:
            print("余额不足或取出金额不合法")
```

**分析**：通过在属性名前加双下划线 __ 将 __balance 设置为私有属性，外部无法直接访问和修改。deposit 方法和 withdraw 方法用于对 __balance 进行合法操作，体现了封装特性，即把数据和对数据的操作封装在一起，对外隐藏内部实现细节，保证数据的安全性。

### 题目 4：多态特性

定义一个 Shape 类，有一个抽象方法 area（方法体为空）。再定义 Rectangle 类和 Circle 类继承自 Shape 类，分别实现 area 方法计算矩形面积（长 × 宽）和圆的面积（\(\pi r^2\)）。创建 Rectangle 和 Circle 类的对象，将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。

**答案**：

```python
import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self): 
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self): 
        return math.pi * self.radius ** 2
    
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())
```

**分析**：Shape 类定义了一个抽象方法 area，作为子类必须实现的接口。Rectangle 类和 Circle 类继承自 Shape 类，并分别实现了 area 方法。将不同子类的对象放入同一个列表 shapes 中，遍历列表时，尽管 shape 变量在不同循环中引用不同类型的对象，但都能正确调用各自实现的 area 方法，这就是多态的体现，即不同对象对同一消息（方法调用）做出不同的响应。