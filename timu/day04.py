# ### 题目 1：动态添加属性
#
# 定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。

class Person:
    pass  # Java中是 {}，Python中如果类里面什么都不写，必须用 pass 占位

# 题目1 正确答案：
print("--- 题目1 ---")
p = Person()
# Python 极度灵活，可以在类外直接给对象赋予新属性（Java绝对做不到）
p.hobby = "reading"
print(p.hobby)


# ### 题目 2：动态添加方法
#
# 定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：\(S = π r^2），
# 然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用 types.MethodType）

import types

class Circle:
    def __init__(self, radius):
        self.radius = radius

# 题目2 正确答案：
print("\n--- 题目2 ---")
# 1. 在类外部定义一个普通函数，注意第一个参数依然留给 self
def calculate_area(self):
    # 🚨 Java 陷阱警告：平方在 Python 里是 **，不是 ^ (在Python里^是异或)
    return 3.14 * (self.radius ** 2)

c = Circle(5)
# 2. 动态将外部函数绑定给 c 对象，变成它的实例方法
c.calculate_area = types.MethodType(calculate_area, c)
print("圆的面积是:", c.calculate_area())


# ### 题目 3：封装特性
#
# 定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），提供一个 deposit 方法用于存钱，
# 一个 withdraw 方法用于取钱，取钱时如果余额不足则打印提示信息。

# 题目3 正确答案：
print("\n--- 题目3 ---")
class BankAccount:
    def __init__(self):
        # 🚨 Java 陷阱警告：Python 没有 private，双下划线 __ 开头代表私有变量
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print(f"存钱成功，存入: {amount}，当前余额: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"取钱失败！余额不足。欲取: {amount}，当前余额: {self.__balance}")
        else:
            self.__balance -= amount
            print(f"取钱成功！取出: {amount}，当前余额: {self.__balance}")

account = BankAccount()
account.deposit(100)
account.withdraw(150)
account.withdraw(50)


# ### 题目 4：多态特性
# 定义一个 Shape 类，有一个抽象方法 area（方法体为空）。再定义 Rectangle 类和 Circle 类继承自 Shape 类，分别实现 area 方法
# 计算矩形面积（长 × 宽）和圆的面积（\(\pi r^2\)）。创建 Rectangle 和 Circle 类的对象，将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。

# 题目4 正确答案：
print("\n--- 题目4 ---")
class Shape:
    def area(self):
        # 🚨 Java 陷阱警告：Python 用 pass 占位，代表方法体为空
        pass

class Rectangle(Shape): # 继承语法：class 子类(父类):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# 利用列表和循环展现多态特性
shapes = [Rectangle(4, 5), CircleShape(3)]
for s in shapes:
    # 同样是调用 area()，由于对象实际类型不同，触发了多态
    print("多态调用面积计算:", s.area())
