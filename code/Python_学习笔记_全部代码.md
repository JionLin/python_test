# Python 完整学习笔记

> 基于尚硅谷 Python 教程整理，包含第1章到第13章的全部代码内容。

---

## 目录

- [第1章 · 环境搭建](#第1章-环境搭建)
- [第2章 · 开发工具](#第2章-开发工具)
- [第3章 · 基础语法（变量、类型、运算符）](#第3章-基础语法)
- [第4章 · 流程控制（条件判断、循环）](#第4章-流程控制)
- [第5章 · 函数](#第5章-函数)
- [第6章 · 数据容器（列表、元组、集合、字典、字符串）](#第6章-数据容器)
- [第7章 · 面向对象编程](#第7章-面向对象编程)
- [第8章 · 高阶函数与进阶特性](#第8章-高阶函数与进阶特性)
- [第9章 · 异常处理](#第9章-异常处理)
- [第10章 · 模块与包](#第10章-模块与包)
- [第11章 · 迭代器与生成器](#第11章-迭代器与生成器)
- [第12章 · 文件操作](#第12章-文件操作)
- [第13章 · 多进程与多线程](#第13章-多进程与多线程)

---

## 第1章 · 环境搭建

> 本章无代码，具体内容，请看笔记。

## 第2章 · 开发工具

> 本章无代码，具体内容，请看笔记。

## 第3章 · 基础语法（变量、类型、运算符）

### 01_字面量

```python
'张三'
18
65.2

'李四'
22
74.6

'王五'
25
80

print(25)
print(80)
```

### 02_变量

```python
name = '张三'
age = 18
weight = 59
weight = 58

print('张三的体重是', weight)
print('对于', weight, '这个体重，张三不是很满意')
print('张三决定开始减肥，希望体重比', weight, '还要小')
```

### 03_标识符命名规则

```python
name2 = '张三'
age_2 = 18
_weight_ = 60.2

name = '熊大'
Name = '熊二'

userName = '刘海柱'
UserName = '刘海柱'
user_name = '刘海柱'
```

### 04_常量

```python
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
PASSING_SCORE = 60
MAX_USERS = 1300

print(ADULT_AGE, MONTHS_IN_YEAR, MAX_USERS, PASSING_SCORE)
```

### 05_注释

```python
"""在该文件中，我主要学习了注释相关的内容"""

# name是张三的名字
name = '张三'
# age是张三的年龄
age = 18
# weight是张三的体重（单位：kg）
# 张三的体重还可以
weight = 65.2

print(name, age, weight)  # 下面是一句打印

"""
下面是一些常量
ADULT_AGE是法定成人年龄
MONTHS_IN_YEAR是一年中的几个月
MAX_USERS是最大同时在线人数
"""
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
print(ADULT_AGE,MONTHS_IN_YEAR,MAX_USERS)
```

### 06_字符编码

```python
message1 = '你好啊'
message2 = 'hello'
message3 = 'สวัสดี'
message4 = 'မင်္ဂလာပါ'

print(message1, message2, message3, message4)
```

### 07_数据类型

```python
print(type('张三'))
print(type(18))
print(type(65.2))


name = '张三'
print(type(name))

print('********************************')
print(type('18'))
print(type(18))
print(type('65.2'))
print(type(65.2))
```

### 08_整型

```python
# 所谓整型，就是没有小数点的数字，可以是正数，也可以是负数，也可以是0。
age = 18
temp = -15
score = 0

# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读。
salary = 300_000
house_price = 3_200_000
graduates = 12_000_000
print(salary, house_price, graduates)

# Python中整数的上限值，取决于执行代码的计算机的内存和处理能力。
a = 9 ** 9999
```

### 09_浮点型

```python
# 浮点型就是带有小数点的数字。
weight = 65.2
balance = 1425.58
out_temp = -25.2
price = 120.0

# 浮点型的科学计数法表示。
speed_of_sound = 3.4e+2  # 3.4乘以10的2次方。
world_population = 7.8e9  # 7.8乘以10的9次方。
distance_sun_earth = 1.496E8  # 1.496乘以10的8次方。
speed_of_light = 2.998E+8  # 2.998乘以10的8次方。

one_ml = 1e-3  # 1乘以10的-3次方。
one_mg = 1E-3  # 1乘以10的-3次方。
```

### 10_字符串_四种定义方式

```python
# 单引号和双引号的写法是等价的，二者都不能直接换行（要用圆括号才能换行），单引号用的多。
message1 = '尚硅谷，让天下没有难学的技术!'
message2 = "尚硅谷，让天下没有难学的技术!"

# 三个单引号的写法，可以直接换行，并且可以作为多行注释使用。
message3 = '''尚硅谷，让天下没有难学的技术!'''

# 三个双引号的写法，可以直接换行，也可以作为多行注释使用，还能作为文档字符串使用。
message4 = """尚硅谷，让天下没有难学的技术!"""
```

### 11_字符串_格式化输出

```python
name = '张三'
gender = '男'
weight = 65.2
age = 12

# 写法一：直接用加号进行拼接，写起来很麻烦且代码很乱，而且只能是字符串之间拼接。
info1 = '我叫' + name + '，我是' + gender + '生'

# 写法二：使用占位符
# %s占位字符串，%f占位浮点数，%i占位整数，%d占位十进制的整数，%s是万能的。
info2 = '我叫%s，我是%s生，我体重是%d，年龄是%d' % (name, gender, weight, age)

# 写法三：使用f-string，是目前Python最推荐的方式。
info3 = f'我叫{name}，我是{gender}生，我体重是{weight}，年龄是{age}'
print(info3)
```

### 12_字符串_占位符精度控制

```python
name = '张三'
gender = '男'
weight = 65.55
age = 12

info = '我叫%-4.1s，性别是%3.2s，体重是%-9.3f，年龄是%-6.4d' % (name, gender, weight, age)
print(info)
```

### 13_字符串_转义字符

```python
# 使用 \' 输出 '
# print('在Python中，可以使用\'包裹一个字符串')

# 使用 \" 输出 "
# print("在Python中，可以使用\"包裹一个字符串")

# 使用 \n 进行换行
# print('注册会员需要以下信息：\n姓名\n年龄\n手机号')

# 使用 \\ 输出 \
# print('D:\\nice')

# 使用 \b 删除前一个字符
# print('helloo\b')

# 使用 \r 使光标回到本行开头，覆盖输出
# print('67%\r68%')

# 使用 \t 表示水平制表符（让光标跳转到下一个制表位）
# print('1234123412341234')
# print('ab\tcd')
# print('abc\td')
# print('abcd\ta')
# print('我是\t中文')

print('12341234123412341234')
print('姓名\t性别\t年龄')
print('张三\t男\t\t18')
print('李四\t女\t\t25')
print('王五\t男\t\t32')
```

### 14_数据类型转换

```python
# 使用str()将指定数据转换为字符串。
# result1 = str(18)
# result2 = str(75.6)
# result3 = str(1.8e3)
# result4 = str(12_000)
#
# print(type(result1),result1)
# print(type(result2),result2)
# print(type(result3),result3)
# print(type(result4),result4)

# 使用int()将指定数据转换为整型。
# result1 = int(15.6)
# result2 = int('79')
# result3 = int('   79   ')
# result4 = int(48)

# 以下是错误示例
# int('   7 9   ')
# int('你好')
# int('79个')
# int('15.6')

# print(type(result1),result1)
# print(type(result2),result2)
# print(type(result3),result3)
# print(type(result4),result4)

# 使用float()将指定数据转换为浮点型。
result1 = float(18)
result2 = float('15.6')
result3 = float('   5.7   ')
result4 = float(14.8)
result5 = float('48')

# 以下是反例
# float('   5.  7   ')
# float('你好')
# float('5.7元')
# float('5.23.12')

print(type(result1), result1)
print(type(result2), result2)
print(type(result3), result3)
print(type(result4), result4)
print(type(result5), result5)
```

### 15_算数运算符

```python
# 加
print(9 + 7)
# 减
print(7 - 2)
# 乘
print(3 * 4)
# 除
print(9 / 3)
# 取整
print(9 // 6)
# 取余
print(9 % 6)
# 指数
print(2 ** 3)
```

### 16_赋值运算符

```python
age = 18
age += 1
print(age)

price = 52
freight = 6
price += freight
print(price)
```

### 17_赋值_复合赋值运算符

```python
# age = 18
# # 加法复合运算符
# age += 1  # 等价于：age = age + 1
# print(age)
#
# price = 52
# freight = 6
# # 加法复合运算符
# price += freight  # 等价于：price = price + freight
# print(price)

# 减法复合运算符
# age = 18
# age -= 1  # 等价于：age = age - 1
# print(age)

# 乘法复合运算符
# price = 100
# discount = 0.8
# price *= discount  # 等价于：price = price * discount
# print(price)

# 除法复合运算符
# pay = 100
# num = 5
# pay /= 5  # 等价于：pay = pay / num
# print(pay)

# 取整赋值运算符
# apple = 31
# num = 14
# apple //= num  # 等价于：apple = apple // num
# print(apple)

# 取模赋值运算符
# seconds = 386
# minutes = 60
# seconds %= minutes  # 等价于：seconds = seconds % minutes
# print(seconds)

# 指数赋值运算符
a = 2
b = 3
a **= b  # 等价于：a = a ** b
print(a)
```

### 18_比较运算符

```python
# 使用==判断左右两侧是否相等
# a = 5
# b = 7
# c = '5'
# result = a == c
# print(result)

# 使用!=判断左右两侧是否不等
# a = 5
# b = 7
# c = '5'
# result = a != c
# print(result)

# 使用>判断左侧是否大于右侧
# a = 9
# b = 7
# c = '5'
# result = a > b
# print(result)

# 使用<判断左侧是否小于右侧
# a = 3
# b = 7
# c = '5'
# result = a < b
# print(result)

# 使用>=判断左侧是否大于等于右侧
# a = 6
# b = 7
# c = '5'
# result = a >= b
# print(result)

# 使用<=判断左侧是否小于等于右侧
# a = 9
# b = 7
# c = '5'
# result = a <= b
# print(result)

# 以上这些比较运算符，同样适用于字符串
# msg1 = 'abc'
# msg2 = 'abc666'
# print(msg1 == msg2)

# msg1 = 'abc'
# msg2 = 'abc'
# print(msg1 != msg2)

# 使用ord()查看指定字符的Unicode编码
# print(ord('a'))
# print(ord('我'))

# 使用chr()将Unicode编码转为字符
print(chr(97))
print(chr(25105))

msg1 = 'abc'
msg2 = 'xyz'
msg3 = '我爱你'
msg4 = '中国'
msg5 = 'abc'
msg6 = 'abcdef'
print(msg1 <= msg5)
```

### 19_布尔类型

```python
# 自己定义的布尔值
a = True
b = False
# 靠程序执行得到的布尔值
c = 5 > 3
d = 7 < 2
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)

# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
# print(int(True))
# print(int(False))

# print(4 + True)
# print(8 - False)

# print(True + True)
# print(True - False)

# print(7 > True)
# print(False <= 0)

# 使用bool()将指定内容转为布尔类型
# print(bool(1))
# print(bool(0))

# Python中除0以外的任何数，转为布尔值后都为True
# print(bool(300))
# print(bool(25.6))
# print(bool(1.8e3))
# print(bool(12_000))
# print(bool(-10))

# Python中除空字符串以外的任何字符串，转为布尔值都是True
print(bool('hello'))
print(bool('0'))
print(bool('18.5'))
print(bool('-9'))
print(bool(''))
```

### 20_逻辑运算符

```python
# and用于判断其两侧的值，是否都为True
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print(8 > 7 and 8 > 7)
# print(8 > 7 and 2 > 3)
# print(2 > 3 and 8 > 7)
# print(2 > 3 and 2 > 3)

# and具备“逻辑短路”能力
# print(False and 3 / 0)
# print(3 > 9 and 3 / 0)

# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
# print(2 - 2 and True)
# print('' and True)
# print(True and 8 / 2)
# print(3 + 3 and 3 * 4)

# or用于判断其两侧，是否至少有一个为True（只要有一个是True，那就返回True）
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# print(9 > 2 or 9 > 2)
# print(9 > 2 or 3 < 1)
# print(3 < 1 or 9 > 2)
# print(3 < 1 or 3 < 1)

# or同样具备“逻辑短路”的能力
# print(True or 3 / 0)
# print(9 > 3 or 3 / 0)

# or返回的也不一定是布尔值，它返回的是参与计算的值本身
# 规则：or会先看左边，如果左边为“真”，就直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
# print(7 - 2 or False)
# print('你好' or '尚硅谷')
# print(False or 8 / 2)
# print(2 - 2 or 3 * 4)

# not用于取反
# 备注：若参与not运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
# print(not True)
# print(not False)
# print(not 3 > 2)
# print(not 3 < 2)

# not返回的值，一定是布尔值！
print(not 0)
print(not 3 > 2)
print(not 9 // 4)
print(not 'abc')
print(9 //4)
```

### 21_进制

```python
# 0b开头表示二进制
num1 = 0b11001
# 0o开头表示八进制
num2 = 0o1034
# 0x开头表示十六进制
num3 = 0x1cf

# Python中所有的非十进制数字，只是代码层面的编写方式，是给程序员看的
# Python在对上面的num1、num2、num3进行计算、打印等操作时，会自动将其转为十进制
# print(num1, num2, num3)
# print(num1 + 1)
# print(str(num2))
# print(num3 > 400)

# 使用bin()将十进制转为二进制
result1 = bin(25)
# 使用oct()将十进制转为八进制
result2 = oct(540)
# 使用hex()将十进制转为十六进制
result3 = hex(463)
# 注意：bin() oct() hex()他们返回的值类型都是字符串
print(result1, result2, result3)
print(type(result1), type(result2), type(result3))

# 使用int()将指定进制的数，转为十进制数字
value1 = int('0b11001', 2)
value2 = int('0o1034', 8)
value3 = int('0x1cf', 16)
print(value1, value2, value3)
print(type(value1), type(value2), type(value3))
```

### 22_输入语句

```python
# 使用input()获取用户的输入
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')

# input()获取到的内容全都是字符串类型
# print(type(age))

# 将age转为整型
age = int(age)

# 打印信息
print(f'{name}，你今年的年龄是{age}')
print(f'{name}，你明年的年龄是{age + 1}')
print(f'asdasd{type(1)}')
```

---

## 第4章 · 流程控制（条件判断、循环）

### 01_单分支

```python
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你是成年人')
    print('成年人的世界，虽不容易，但很精彩！')
print('欢迎你来学习Python！')
```

### 02_双分支

```python
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你是成年人')
    print('成年人的世界，虽不容易，但很精彩！')
else:
    print('你是未成年人')
    print('好好加油，努力学习，未来可期！')
print('欢迎你来学习Python！')
```

### 03_多分支

```python
age = int(input('请输入你的年龄：'))
if age <= 10:
    print('你是幼儿')
elif age <= 18:
    print('你是青少年')
elif age <= 30:
    print('你是青年')
elif age <= 50:
    print('你是中年')
elif age <= 60:
    print('你是中老年')
elif age > 60:
    print('你是老年')
```

### 04_嵌套分之

```python
age = int(input('请输入你的年龄：'))
has_report = input('您是否提交了体检报告？（是/否）')
level = int(input('请输入你的会员等级（1/2/3）'))

print('******⬇️程序的识别结果如下⬇️：******')
if 18 <= age <= 45:
    print('✅️您的年龄符合比赛要求！')
    if has_report == '是':
        print('✅️您已提交体检报告！')
        print('✅️您可以参加比赛！')
        if level == 1:
            print(f'😊尊敬的{level}会员，比赛结束后，您可以领取纪念T恤👕一件！')
        elif level == 2:
            print(f'😊尊敬的{level}会员，比赛结束后，您可以领取专业跑鞋👟一双！')
        elif level == 3:
            print(f'😊尊敬的{level}会员，比赛结束后，您可以领取运动耳机🎧️一副！')
        else:
            print('❌您输入的会员等级不正确！')
    elif has_report == '否':
        print('❌您未提交体检报告，不能参加比赛！')
    else:
        print('❌您输入的体检报告有误！')
else:
    print('❌抱歉，参赛年龄需要在18~45之间！')
```

### 05_while_循环

```python
n = 1
while n <= 10:
    print(f'第{n}次你好啊')
    n += 1
print(f'我是while循环以外的代码，执行到这里时，循环已经结束了，此时的n是：{n}')
```

### 06_while_循环案例

```python
print('😦您现在身处密室，需要正确回答问题之后，才能逃出密室！')
riddle = '你是什么人？'
answer = '你的心上人'
guess = ''

while guess != answer:
    print(f'问题：{riddle}')
    guess = input('请输入答案：')
    if guess == answer:
        print('✅️答案正确，逃脱成功！')
    else:
        print('❌️回答错误，请再想想！')
```

### 07_for_循环

```python
# 使用for循环遍历range()所指定的数字范围
n = 0
for n in range(1, 11):
    print(f'第{n}次你好啊')
print(f'我是for循环以外的代码，执行到这里时，循环已经结束了，此时的n是：{n}')

# 使用for循环遍历字符串
for m in 'abcdef':
    print(m)

# 演示由于误操作造成的死循环（下面代码中，用到了列表，我们后面会讲解）
# 备注：for循环还能遍历很多我们没有讲到的东西，比如：元组、列表、对象......
nums = [1,2,3]
for i in nums:
    # nums.append(4)
    print(i)
```

### 08_for_循环案例

```python
# 加密代码
text = input('📝请输入要加密的文字：')
secret = ''
for t in text:
    secret += chr(ord(t) + 1)
print(f'㊙️经过加密后的内容为：{secret}')

# 解密代码
# secret = input('📝请输入要解密的文字：')
# text = ''
# for s in secret:
#     text += chr(ord(s) - 1)
# print(f'📃经过解密后的内容为：{text}')
```

### 09_嵌套循环

```python
# for循环实现
# day = 1
# for day in range(1,31):
#     print(f'********📅第{day}天********')
#     for group in range(1,4):
#         print(f'💪这是第{group}组仰卧起坐')
#     print(f'✅第{day}天任务已完成！明天继续！\n')
# print(f'🎉为期{day}天的健身计划完成，我的腹肌在闪闪发光！')

# while循环实现
day = 1
while day <= 30:
    print(f'********📅第{day}天********')
    group = 1
    while group <= 3:
        print(f'💪这是第{group}组仰卧起坐')
        group += 1
    print(f'✅第{day}天任务已完成！明天继续！\n')
    day += 1
print(f'🎉为期{day - 1}天的健身计划完成，我的腹肌在闪闪发光！')
```

### 10_九九乘法表

```python
# 前序知识
# print('你好', end='')
# print('尚硅谷', end='')

# for循环实现九九乘法表
for row in range(1, 10):
    for item in range(1, row + 1):
        print(f'{item}*{row}={item * row}', end='\t')
    print()
```

### 11_continue与break

```python
# 测试continue
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     continue
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         continue
#     print('睡觉')

# for day in range(1, 5):
#     if day == 2:
#         continue
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         continue
#         print(f'牛奶{item}')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         if day == 4 and item == 2:
#             continue
#         print(f'牛奶{item}')
#     print('睡觉')

# 测试break
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     break
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         break
#     print('睡觉')

# for day in range(1, 5):
#     if day == 2:
#         break
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1,3):
#         print(f'面包{item}')
#         if day == 4 and item == 2:
#             break
#         print(f'牛奶{item}')
#     print('睡觉')
```

### 12_综合案例

```python
print('🏆欢迎来到：答题闯关挑战赛（输入q可随时退出）\n')

# 题目与答案
ques1, ans1 = 'Python中用于输出的函数是？', 'print'
ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是？', 'and'
ques3, ans3 = 'Python属于编译型还是解释型？', '解释型'

# 最多可尝试次数
max_tries = 3
# 总关卡数
total_levels = 3
# 是否处于可游戏状态
is_playing = True

# 根据题目数量开始循环
for level in range(1, total_levels + 1):
    # 打印当前是第几关
    print(f'********🎯第{level}关********')
    # 取出当前关卡所对应的题目和答案
    if level == 1:
        question, answer = ques1, ans1
    elif level == 2:
        question, answer = ques2, ans2
    else:
        question, answer = ques3, ans3
    # 记录当前关卡的尝试次数
    tries = 1
    # 若已经尝试的次数，小于等于最大尝试次数，则进入循环
    while tries <= max_tries:
        # 向用户提问
        user_input = input('📢'+question)
        # 根据用户的输入，来决定做什么
        if user_input == answer:
            print('✅回答正确！\n')
            break
        elif user_input == '':
            print('⚠️您的输入为空，请重新作答！\n')
            continue
        elif user_input == 'q':
            print('👋您已退出游戏！\n')
            is_playing = False
            break
        else:
            # 计算剩余次数
            leave = max_tries - tries
            # 判断是否还有剩余次数
            if leave > 0:
                print(f'❌回答错误，您还剩{leave}次机会！\n')
                tries += 1
                continue
            else:
                print(f'😢挑战失败，本题的正确答案是：{answer}，游戏结束！')
                is_playing = False
                break
    # 每次进入下一关之前，都要看一下is_playing，如果is_playing为False就要结束游戏！
    if not is_playing:
        break
# 如果到了这里，is_playing的值依然为True，那就意味着用户已经通关了！
if is_playing:
    print('🎉🎉🎉恭喜您！全部通关！🎉🎉🎉')
```

---

## 第5章 · 函数

### 01_函数_基本使用

```python
# 定义函数
def welcome():
    print('欢迎来到尚硅谷课堂！')
    print('尚硅谷，让天下没有难学的技术！')

# 调用函数（让函数中的代码运行起来）
welcome()
welcome()
welcome()
```

### 02_函数_参数的使用

```python
def order(num, dish):
    print(f'您点的是：{num}份 {dish}')
    print(f'{dish}可是很好吃的！')
    print(f'你只点了{num}份，够吃吗？\n')

# 函数的形参：num，dish 只能在函数内去使用
# print(num)

order(1, '辣椒炒肉')
order(2, '辣子鸡')

# 以下是错误示范
# order(3)
# order(4, '宫保鸡丁', 7)
```

### 03_函数_位置参数

```python
# 定义函数（接收位置参数）
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我的身高是{height}，今年{age}岁了，我叫{name}')

# 调用函数
greet('张三', '男', 18, 172)

# 错误示例
# greet('张三', 18, 172)
# greet('男', '张三', 172, 18)
```

### 04_函数_关键字参数

```python
# 定义函数
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 调用函数（使用关键字参数）
greet(name='张三', gender='男', age=18, height=172)
greet(height=172, age = 18, gender='男', name='张三')
greet('张三', '男', height=172, age=18)

# 错误示例
# greet(height=172, age=18, '张三', '男')
# greet(name='张三', '男', 18, 172)
# greet(name='张三', '男', age=18, 172)
# greet(height=172, age=18, gender='男', name='张三', age=19)
# greet(height=172, age=18, gender='男', name='张三', school='尚硅谷')
```

### 05_函数_限制传参方式

```python
# 定义函数（使用/和*限制传参方式）
def greet(name, /, gender, *, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 正确示例
greet('张三', '男', age=18, height=172)
greet('张三', gender='男', age=18, height=172)

# 错误示例
# greet(name='张三', gender='男', age=18, height=172)
# greet('张三', '男', 18, height=172)
```

### 06_函数_参数默认值

```python
# 定义函数（设置参数默认值）
def greet(name, gender, age, height, msg='你好', /):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说：{msg}')

# 调用函数
# greet('张三', '男', 18, 172)
# greet('张三', '男', 18, 172, 'hello')
# greet('张三', '男', 18, 172, msg='hello')

# print函数底层给end参数设置了默认值
print('尚硅谷', end='!!')
```

### 07_函数_可变参数

```python
# 定义函数（使用*args去接收：可变位置参数）
def test1(*args):
    # 此处args的值，是一种新的数据类型，叫：元组，我们下一章就去讲元组
    print(args)
# 调用函数
test1('张三', '男', 18, 172)

# 定义函数（使用**kwargs去接收：可变关键字参数）
def test2(**kwargs):
    # 此处kwargs的值，是一种新的数据类型，叫：字典，我们下一章就去讲字典
    print(kwargs)
# 调用函数
test2(name='张三', gender='男', age=18, height=172)

# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print('@@@@@@@@@@@@@@@@')
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
# 调用函数
test3('张三', '男', '抽烟', '喝酒', age=18, height=172)
```

### 08_None

```python
# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'
```

### 09_函数_返回值

```python
# 定义函数
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}，二者相加是：{n1 + n2}')
    print('add函数执行完毕了')
    return n1 + n2

# 调用函数
result = add(100, 200)
print(result)

# print函数是没有返回值的
# res = print('hello')
# print(res)
```

### 10_全局作用域_局部作用域

```python
# 全局作用域 与 局部作用域，以及global的使用
a = 100
b = 200

def test():
    c = '尚硅谷'
    d = '你好啊'
    global a
    a = 300
    print('函数中的打印（a）', a)
    print('函数中的打印（b）', b)
    print('函数中的打印（c）', c)
    print('函数中的打印（d）', d)
test()
print('***************')
print('全局的打印（a）', a)
print('全局的打印（b）', b)
print(c)
print(d)


# 局部作用域 和 局部变量，会在函数调用时创建，在函数执行结束后自动销毁
# def test2():
#     m = 100
#     m += 1
#     print(f'我是test2函数中打印的m：{m}')
# test2()
# test2()
# test2()


# 全局作用域 与 全局变量，会在程序开始时创建，在程序结束后销毁
# n = 100
# def test3():
#     global n
#     n += 1
#     print(f'我是test3函数中打印的n：{n}')
# test3()
# test3()
# test3()
# print(n)
```

### 11_函数_嵌套调用

```python
# 函数嵌套调用测试1
# def greet(name, msg):
#     print(f'我叫{name}，我想说的话在下面：')
#     speak(msg)
#     print('嗯，我想说的结束了')
#
# def speak(msg):
#     print('----------')
#     print(msg)
#     print('----------')
#
# greet('张三', '你好啊')

# 函数嵌套调用测试2
def test1():
    print('进入 test1 函数')
    test2()
    print('退出 test1 函数')

def test2():
    print('进入 test2 函数')
    test3()
    print('退出 test2 函数')

def test3():
    print('进入 test3 函数')
    print('***正在执行 test3 函数')
    print('退出 test3 函数')

test1()
```

### 12_函数_递归调用

```python
# 使用递归打印n次“你好啊”（从大到小）
def welcome(n):
    print(f'你好啊{n}')
    if n > 1:
        welcome(n - 1)
# 调用函数
welcome(5)

# 使用递归打印n次“你好啊”（从小到大）
def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'你好啊{n}')
# 调用函数
welcome(5)
```

### 13_函数_递归的应用

```python
# 使用递归求阶乘
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
# 调用函数，求5的阶乘
result = factorial(6)
print(result)
```

### 14_函数_说明文档

```python
def add(n1, n2):
    """
    计算两个数相加的结果
    :param n1:第一个数
    :param n2:第二个数
    :return:二者相加的结果
    """
    return n1 + n2

result = add(1, 2)
```

### 15_综合案例

```python
def calc_total(*nums):
    """
    计算总运动量（个）
    :param nums: 每一天的运动量（可变参数）
    :return: 总运动量（个）
    """
    # 备注：nums的类型是元组（下一章马上就讲了），sum是内置函数，可以对元组中的数据求和
    return sum(nums)

def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量（个）
    :param days: 天数（默认值是7）
    :return: 平均值
    """
    return total / days

def check_success(total, goal=120):
    """
    判断本次挑战是否成功
    :param total: 总运动量
    :param goal: 成功数量（默认值为120）
    :return: 成功或失败的具体信息
    """
    if total >= goal:
        return '✅恭喜！挑战成功！'
    else:
        return '❌抱歉！挑战失败！'

def main(title, duration, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param duration: 比赛持续天数
    :param goal: 目标运动量
    :return: None
    """
    print(f'【{title}】【{duration}天】✊️挑战赛（请输入每天的数量）')
    num1 = int(input('第1天：'))
    num2 = int(input('第2天：'))
    num3 = int(input('第3天：'))
    # 计算总数
    total = calc_total(num1, num2, num3)
    # 计算平均值
    avg = calc_avg(total, duration)
    # 判断挑战是否成功
    result = check_success(total, goal)
    # 打印相关信息
    print(f'【{title}】【{duration}天】健身总结')
    print(f'总数：{total}，平均值：{avg:.1f}')
    print(result)

main('俯卧撑', 3, 40)
```

---

## 第6章 · 数据容器（列表、元组、集合、字典、字符串）

### 01_列表_定义列表

```python
# 定义有内容的列表
list1 = [34, 56, 21, 56, 11]
list2 = ['北京', '尚硅谷', '你好啊']
list3 = [23, '尚硅谷', True, None]
list4 = [23, '尚硅谷', True, None, [100, 200, 300]]
# 定义空列表（列表中的数据，后期会通过特定写法填充）
list5 = []
list6 = list()

print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(list4, type(list4))
print(list5, type(list5))
print(list6, type(list6))
```

### 02_列表_下标(索引值)

```python
# 定义一个列表
nums = [10, 20, 30, 40, 50]

# 测试正索引
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])

# 测试负索引
# print(nums[-1])
# print(nums[-2])
# print(nums[-3])
# print(nums[-4])
# print(nums[-5])

# 测试错误索引
# print(nums[5])

# 定义一个嵌套列表
nums2 = [10, 20, ['你好啊','尚硅谷'], 40, 50]
# 取出“尚硅谷”
print(nums2[2][1])
```

### 03_列表_增删改查

```python
# 新增操作
# 方式一：通过列表的append方法，在列表尾部追加一个元素
nums = [10, 20, 30, 40]
nums.append(50)
print(nums)

# 方式二：通过列表的insert方法，在列表的指定下标处添加一个元素
# nums = [10, 20, 30, 40]
# nums.insert(2, 666)
# print(nums)

# 方式三：通过列表的extend方法，将可迭代对象中的内容依次取出，追加到列表尾部
# nums = [10, 20, 30, 40]
# nums.extend('尚硅谷')
# nums.extend(range(1, 4))
# nums.extend([70, 80, 90])
# print(nums)

# 删除操作
# 方式一：通过列表的pop方法，删除指定位置的元素，并返回该元素
# nums = [10, 20, 10, 40, 50]
# result = nums.pop(1)
# print(nums)
# print(result)

# 方式二：通过列表的remove方法，删除列表中第一次出现的指定值
# nums = [10, 20, 10, 40, 50]
# nums.remove(10)
# print(nums)

# 方式三：通过列表的clear方法，删除列表中所有的元素（清空列表）
# nums = [10, 20, 10, 40, 50]
# nums.clear()
# print(nums)

# 方式四：通过del关键字，删除指定元素
# nums = [10, 20, 10, 40, 50]
# del nums[3]
# print(nums)

# 修改操作
# nums = [10, 20, 10, 40, 50]
# nums[2] = 66
# print(nums)

# 查询操作
# nums = [10, 20, 10, 40, 50]
# print(nums[3])
```

### 04_列表_常用方法

```python
# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
# fruits = ['香蕉', '苹果', '橙子', '香蕉']
# result = fruits.index('香蕉')
# print(result)

# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数。
# nums = [10, 20, 10, 30, 10, 40, [10, 10, 10]]
# result = nums.count(10)
# print(result)

# 3.使用 reverse 方法，对列表进行反转（会改变原列表）。
# nums = [23, 11, 32, 30, 17, [6, 7, 8, 9]]
# nums.reverse()
# print(nums)

# 4.使用 sort 方法，对列表排序（默认从小到大），若想从大到小，可以将 reverse 参数设为True。
# 4.1 若列表中的元素：都是数字，则按照数字的大小顺序进行排序。
# nums = [23, 11, 32, 30, 17]
# nums.sort(reverse=True)
# print(nums)

# 4.2 若列表中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# nums.sort()
# print(nums)

# 4.3 若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序
# msg_list = ['北京', '北硅谷', '北好']
# msg_list.sort()
# print(msg_list)
# print(ord('京'), ord('好'), ord('硅'))

# 备注：所有的列表方法，都只作用于“当前层”的元素（浅层操作），不会自动进入嵌套的“里层”结构中。
```

### 05_列表_常用内置函数

```python
# 1.使用内置的 sorted 函数，返回一个排序后的新容器（不改变原容器，默认顺序：从小到大）
# 1.1 若列容器中的元素：都是数字，则按照数字的大小顺序进行排序。
# nums = [23, 11, 32, 30, 17]
# result = sorted(nums, reverse=True)
# print(nums)
# print(result)

# 1.2 若列容器中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# sorted(nums)

# 1.3 若列容器中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序。
# msg_list = ['北京', '尚硅谷', '你好']
# result = sorted(msg_list)
# print(msg_list)
# print(result)

# 2.使用内置的 len 函数，获取容器中元素的总数量，返回值是：元素总数量。
# nums = [10, 20, 10, 30, 10, 40, [50, 60, 70]]
# result = len(nums)
# print(result)


# 3.使用内置的 max 函数，获取容器中的最大值，返回值是：最大值。
# 3.1 如果容器中的元素：都是数字，那 max 返回的是最大的数。
# nums = [23, 11, 32, 30, 17]
# result = max(nums)
# print(nums)
# print(result)

# 3.2 如果容器中的元素：既有数字又有字符串，那 max 会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# max(nums)

# 3.3 如果容器中的元素：都是字符串，那 max 会返回：Unicode 编码最大的字符。
# msg_list = ['北京', '尚硅谷', '你好']
# result = max(msg_list)
# print(msg_list)
# print(result)

# 3.4 max 函数也可以接收多个值，并筛选出最大值
# result = max(33, 45, 12, 78, 99)
# print(result)

# 4.使用内置的 min 函数，获取容器中的最小值，返回值是：最小值。
# 备注：min 函数的使用方式与注意点与 max 函数一样，只不过 min 函数返回的是最小值
# nums = [23, 11, 32, 30, 17]
# result = min(nums)
# print(result)

# 5.使用内置的 sum 函数，对容器中的数据进行求和（元素只能是数值）。
# nums = [10, 20, 30, 40, 50]
# result = sum(nums)
# print(result)
```

### 06_列表_循环遍历

```python
# 定义一个成绩列表
score_list = [62, 50, 60, 48, 80, 20, 95]

# 使用while循环遍历列表
index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1

# 使用for循环遍历列表
# for item in score_list:
#     print(item)

# 使用for循环遍历列表（通过range函数 和 len函数按照索引遍历）
# for index in range(len(score_list)):
#     print(score_list[index])

# 使用for循环遍历列表（通过enumerate函数，同时获取下标（索引值）和元素）
# enumerate 的 start 参数，可以让计数从指定值开始（改变的是循环时的“编号”，不是真正的索引值）
# for index, item in enumerate(score_list, start=5):
#     print(index, item, score_list[0])
# print('最后的打印', score_list[0])
```

### 07_列表_小练习

```python
print('请输入学生成绩，输入“结束”停止录入')
score_list = []

# 持续循环，让用户输入学生成绩
while True:
    data = input('📝请输入成绩：')
    if data == '结束':
        break
    else:
        score_list.append(int(data))

# 如果score_list中有数据，则开始统计
if score_list:
    # 统计平均分
    avg = sum(score_list) / len(score_list)
    # 合格人数
    pass_count = 0
    # 优秀人数
    excellent_count = 0
    # 遍历列表，开始统计
    for item in score_list:
        if item >= 60:
            pass_count += 1
        if item >= 90:
            excellent_count += 1
    # 合格率
    pass_rate = pass_count / len(score_list) * 100
    # 优秀率
    excellent_rate = excellent_count / len(score_list) * 100
    # 打印信息
    print('********⬇️统计信息如下⬇️********')
    print(f'🧑‍🎓总人数为：{len(score_list)}')
    print(f'🔺最高分为：{max(score_list)}')
    print(f'🔻最低分为：{min(score_list)}')
    print(f'✅合格人数：{pass_count}人')
    print(f'📈合格率为：{pass_rate:.1f}%')
    print(f'🏆优秀人数：{excellent_count}人')
    print(f'📈优秀率为：{excellent_rate:.1f}%')
    print(f'📊平均分数：{avg:.1f}')
else:
    print('您没有输入任何成绩！')
```

### 08_元组

```python
# 定义元组
# t1 = (28, 67, 21, 67, 11)
# t2 = ('北京', '尚硅谷', '你好')
# t3 = (100, True, '你好', None)
# t4 = (100, True, '你好', None, (50, 60, 70))
# print(type(t1), t1)
# print(type(t2), t2)
# print(type(t3), t3)
# print(type(t4), t4)

# 元组的下标
# t1 = (28, 67, 21, 67, 11)
# print(t1[3])
# print(t1[-1])

# 元组中的元素，不可修改
# t1 = (28, 67, 21, 67, 11)
# t1[0] = 100

# 元组中的元素，不可修改，但元组中如果存放了可变类型（列表），那可变类型中的内容仍可修改
# t2 = (28, 67, 21, 67, 11, [100, 200, 300, ('你好', '尚硅谷')])
# # t2[5] = 400
# t2[5][2] = 400
# t2[5][3][0] = 'hello'
# print(t2)

# 定义空元组
# t1 = ()
# t2 = tuple()
# print(type(t1), t1)
# print(type(t2), t2)

# 定义只有一个元素的元组
# t1 = ('你好',)
# t2 = (18,)
# print(type(t1), t1)
# print(type(t2), t2)

# 常用方法：
# index 方法：获取指定元素在元组中第一次出现的下标。
# t1 = (28, 67, 21, 67, 11)
# result = t1.index(67)
# print(result)

# count 方法：统计指定元素在元组中出现的次数。
# t1 = (28, 67, 21, 67, 11)
# result = t1.count(67)
# print(result)

# 常用内置函数
# max 函数，返回元组中的最大值
# t1 = (23, 11, 32, 30, 17)
# result = max(t1)
# print(result)

# min 函数，返回元组中的最小值
# t1 = (23, 11, 32, 30, 17)
# result = min(t1)
# print(result)

# len 函数，返回元组中元素的个数（元组长度）
# t1 = (23, 11, 32, 30, 17)
# result = len(t1)
# print(result)

# sorted 函数，对元组进行排序（不修改原元组，返回一个新的列表）
# t1 = (23, 11, 32, 30, 17)
# result = sorted(t1, reverse=True)
# print(tuple(result))

# sum 函数，统计元组中所有元素的和（元素必须是纯数字）
# t1 = (23, 11, 32, 30, 17)
# result = sum(t1)
# print(result)

# 实际开发中的元组，不一定是我们自己定义的，比如函数的可变参数*args就是一个元组
# def demo(*args):
#     return sum(args)
# result = demo(100, 200, 300)
# print(result)

# 元组的循环遍历
t1 = (23, 11, 32, 30, 17)

# while循环遍历
# index = 0
# while index < len(t1):
#     print(t1[index])
#     index += 1

# for循环遍历
for item in t1:
    print(item)
```

### 09_函数_解包列表或元组传参

```python
# 定义函数时，使用*args（变量不一定非要用args，比如写：*data也可以），将收到的多个参数，打包成一个元组
def test(*args):
    print(f'我是test函数，我收到的参数是：{args}，参数类型是：{type(args)}')

list1 = [100, 200, 300, 400]
tuple1 = ('你好', '北京', '尚硅谷')

# 函数调用时，正常传递：列表 或 元组
# test(list1)
# test(tuple1)

# 函数调用时，使用*对：列表 或 元组进行解包后，再传递参数
test(*list1)  # 此种写法相当于：test(100, 200, 300, 400)
test(*tuple1)  # 此种写法相当于：test('你好', '北京', '尚硅谷')
```

### 10_函数_综合案例（优化版）

```python
def calc_total(*nums):
    """
    计算总运动量（个）
    :param nums: 每一天的运动量（可变参数）
    :return: 总运动量（个）
    """
    return sum(nums)

def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量（个）
    :param days: 天数（默认值是7）
    :return: 平均值
    """
    return total / days

def check_success(total, goal=120):
    """
    判断本次挑战是否成功
    :param total: 总运动量
    :param goal: 成功数量（默认值为120）
    :return: 成功或失败的具体信息
    """
    if total >= goal:
        return '✅恭喜！挑战成功！'
    else:
        return '❌抱歉！挑战失败！'

def main(title, duration, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param duration: 比赛持续天数
    :param goal: 目标运动量
    :return: None
    """
    print(f'【{title}】【{duration}天】✊️挑战赛（请输入每天的数量）')
    # 定义一个nums列表，用于存储每天的健身数据
    nums = []
    # 根据duration的值，循环让用户输入
    for index in range(duration):
        nums.append(int(input(f'请输入第{index + 1}天的数据：')))
    # 计算总数
    total = calc_total(*nums)
    # 计算平均值
    avg = calc_avg(total, duration)
    # 判断挑战是否成功
    result = check_success(total, goal)
    # 打印相关信息
    print(f'【{title}】【{duration}天】健身总结')
    print(f'总数：{total}，平均值：{avg:.1f}')
    print(result)

main('俯卧撑', 6, 40)
```

### 11_字符串（数据容器角度）

```python
# 字符串的下标
# msg = 'welcome to atguigu'
# print(msg[3])
# print(msg[-1])

# 字符串中的字符，不可修改
# msg = 'welcome to atguigu'
# msg[0] = 'a'

# 字符串不能嵌套
# msg = 'welcome to'hello' atguigu'
# msg = 'welcome to"hello" atguigu'
# msg = 'welcome to\'hello\' atguigu'

# 常用方法
# index 方法：获取指定字符，在字符串中第一次出现的下标
# msg = 'welcome to atguigu'
# result = msg.index('t')
# print(result)

# split 方法：将字符串按照指定字符进行分隔，并将分隔后的内容存入一个列表
# msg  = '尚硅谷@atguigu@你好'
# result = msg.split('@')
# print(msg)
# print(result)

# msg  = 'welcome to atguigu'
# result = msg.split(' ')
# print(msg)
# print(result)

# replace 方法：将字符串中的某个字符片段，替换成目标字符串（不修改原字符串，返回新字符串）
# msg = 'welcome to atguigu'
# result = msg.replace('atguigu', '尚硅谷')
# print(msg)
# print(result)

# count 方法：统计指定字符，在字符串中出现的次数
# msg = 'welcome to atguigu'
# result = msg.count('g')
# print(result)

# strip 方法：从某个字符串中删除：指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下
# msg = '666尚6硅6谷666'
# result = msg.strip('6')
# print(msg)
# print(result)

# msg = '1234尚12硅34谷4321'
# result = msg.strip('1324')
# print(msg)
# print(result)

# msg = '34215尚12硅34谷4132'
# result = msg.strip('5432')
# print(msg)
# print(result)

# msg = '  尚硅谷  '
# result = msg.strip()
# print(msg)
# print(result)

# 常用内置函数
# len 函数：统计字符串中字符的个数（字符串长度）
# msg = 'welcome to atguigu'
# result = len(msg)
# print(result)

# 字符串的循环遍历
msg = 'welcome to atguigu'
# while循环遍历
# index = 0
# while index < len(msg):
#     print(msg[index])
#     index += 1

# for循环遍历
# for item in msg:
#     print(item)
```

### 12_序列的切片操作

```python
# 对列表进行切片
# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[0:5:1]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[1:8:2]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[1:8:3]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[::]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[:999:]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[3::]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[:5:]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[::4]
# print(list2)

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[7:2:-1]
# print(list2)

# 一个特殊情况：当同时省略起始索引和结束索引时，如果步长为负数，那Python会自动对调：起始位置和结束位置
# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list2 = list1[::-1]
# print(list2)

# 对元组进行切片
# tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# tuple2 = tuple1[0:5:1]
# print(tuple2)

# 对字符串进行切片
msg1 = 'welcome to atguigu'
msg2 = msg1[2:9:2]
print(msg2)
```

### 13_序列的其他操作

```python
# 序列相加
# list1 = [10, 20, 30, 40]
# list2 = [50, 60, 70, 80]
# list3 = list1 + list2
# print(list3)

# tuple1 = (10, 20, 30, 40)
# tuple2 = (50, 60, 70, 80)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# str1 = 'hello'
# str2 = 'atguigu'
# str3 = str1 + str2
# print(str3)

# 错误示例
# list1 = [10, 20, 30, 40]
# str1 = 'hello'
# print(list1 + str1)

# 序列相乘（重复）
# list1 = [10, 20, 30, 40]
# list2 = list1 * 3
# print(list2)

# tuple1 = (10, 20, 30, 40)
# tuple2 = tuple1 * 3
# print(tuple2)

str1 = 'hello'
str2 = str1 * 6
print(str2)
```

### 14_集合_定义集合

```python
# 定义有内容的【可变集合】
# s1 = {10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100}
# s2 = {'你好', 'hello', '你好', 'atguigu', '北京'}
# s3 = {10, '你好', True, 1, 12.4}
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定义有内容的【不可变集合】
# s1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
# s2 = frozenset({'你好', 'hello', '你好', 'atguigu', '北京'})
# s3 = frozenset({10, '你好', True, 1, 12.4})
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# frozenset 接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
# s1 = frozenset([10, 20, 30, 40, 50])
# s2 = frozenset((10, 20, 30, 40, 50))
# s3 = frozenset('hello')
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定义空集合（可变集合）
# s1 = set()
# print(type(s1), s1)

# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
# s2 = {}
# print(type(s2), s2)

# 定义空集合（不可变集合）
# s3 = frozenset()
# print(type(s3), s3)

# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 通俗理解：只有“不可变”的东西，才能安全的放进集合里
s1 = {10, 20, 30, 40, 50}
s2 = frozenset({100, 200, 300, 400, 500})
l1 = [666, 777, 888]
t1 = ('hello', 'atguigu', '北京')

# s3 = {11, 22, 33, s1}  # 报错
# s3 = {11, 22, 33, s2}  # 没问题
# s3 = {11, 22, 33, l1}  # 报错
s3 = {11, 22, 33, t1}  # 没问题
print(s3)
```

### 15_集合_增删改查

```python
# 增
# add方法：向集合中添加元素
s1 = {10, 20, 30, 40, 50}
s1.add(60)
print(s1)

# update方法：向集合中添加元素（必须传递可迭代对象，例如：列表、元组、集合等）
s1 = {10, 20, 30, 40, 50}
s1.update([60, 70])
s1.update((80, 90))
s1.update({100, 200})
s1.update(range(300, 308))
print(s1)

# 删
# remove方法：从集合中移除元素（移除不存在的元素，会报错）
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
print(s1)

# discard方法：从集合中移除元素（移除不存在的元素，不会报错）
s1 = {10, 20, 30, 40, 50}
s1.discard(80)
print(s1)

# pop方法：从集合中移除一个任意元素，返回值是移除的那个元素
s1 = {10, 20, 30, 40, 50}
s2 = {'你好', '北京', '尚硅谷', 'hello'}
result = s1.pop()
print(s1)
print(result)

# clear方法：清空集合
s1 = {10, 20, 30, 40, 50}
s1.clear()
print(s1)

# 改
# 使用 add + remove 的组合，来实现修改的效果
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
s1.add(66)
print(s1)

# 查：集合不能通过下标去读取元素，但能通过 【成员运算符】去查看集合中是否包含指定元素
# 由于成员运算符适用于所有数据容器，所以我们会等所有数据容器都讲完以后，再说成员运算符
s1 = {10, 20, 30, 40, 50}
# s1[0] # 此行报错，因为集合不能通过下标访问元素
# 先提前感受一下成员运算符
result = 20 not in s1
print(result)
```

### 16_集合_常用方法

```python
# 集合A.difference(集合B)：
# 作用：找出集合A中，不同于集合B的元素（集合A 与 集合B 都不变，返回的是一个新的集合）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s1.difference(s2)
# print(s1)
# print(s2)
# print(result)

# 集合A.difference_update(集合B)：
# 作用：从集合A中，删除集合B中存在的元素（集合A会被修改，集合B不会）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s1.difference_update(s2)
# print(s1)
# print(s2)


# 集合A.union(集合B)：
# 作用：合并两个集合，集合A 和 集合B 都不变，返回的是一个新的集合
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s2.union(s1)
# print(s1)
# print(s2)
# print(result)

# 集合A.issubset(集合B)：
# 作用：判断集合A是否为集合B的子集
# 如果 集合A的所有元素都在集合B中，那就返回True，否则返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s3.issubset(s1)
# print(result)

# 集合A.issuperset(集合B)：
# 作用：判断集合A是否是集合B的超集
# 如果集合A中，包含了集合B中的所有元素，那就返回True，否则返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s1.issuperset(s3)
# print(result)

# 集合A.isdisjoint(集合B)：
# 作用：判断集合A和集合B是否没有交集
# 如果没有交集，返回True；只要有一个公共元素，就返回False
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {80, 90}
result = s1.isdisjoint(s2)
print(result)
```

### 17_集合_数学运算

```python
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}

# 并集
result = s1 | s2
print(result)

# 交集
result = s1 & s2
print(result)

# 差集
result = s1 - s2
print(result)

# 对称差集
result = s1 ^ s2
print(result)
```

### 18_集合_循环遍历

```python
s1 = {10, 20, 30, 40, 50, 60}

# 集合不能使用while循环遍历（以下是错误示例）
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1

# 集合可以使用for循环遍历
for item in s1:
    print(item)
```

### 19_字典_定义字典

```python
# 定义有内容的字典
d1 = {'张三': 72, '李四': 60, '王五': 85}
# print(type(d1), d1)

# 字典中的key不能重复，若出现重复，则后写的会覆盖之前写的
d1 = {'张三': 72, '李四': 60, '王五': 85, '张三': 99}
print(d1)

# 定义空字典
d1 = {}
d2 = dict()
print(type(d1), d1)
print(type(d2), d2)

# 字典中的key必须是不可变类型，但value可以是任意类型
# 通俗理解：只有不可变的东西，才能作为key
d1 = {250: 72, '李四': 60, '王五': 85}
d2 = {('抽烟', '喝酒'): 72, '李四': 60, '王五': 85}
# print(d1)
# print(d2)
# 错误示例：将列表作为key，是不行的
# d2 = {['抽烟', '喝酒']: 72, '李四': 60, '王五': 85}

# 字典可以嵌套
student_dict = {
    2025001: {
        '姓名': '张三',
        '年龄': 18,
        '成绩': 72,
        '爱好': ['抽烟', '喝酒', '烫头']
    },
    2025002: {
        '姓名': '李四',
        '年龄': 19,
        '成绩': 60,
        '爱好': ['唱歌', '跳舞', '打台球']
    },
    2025003: {
        '姓名': '王五',
        '年龄': 20,
        '成绩': 85,
        '爱好': ['学习', '看书', '打太极']
    }
}
print(student_dict)
```

### 20_字典_增删改查

```python
# 查询
# d1 = {'张三': 72, '李四': 60, '王五': 85}
# 直接取值，若键（key）不存在，会报错
# result = d1['张三']
# 安全取值，若键（key）不存在，会返回默认值（若没有设置默认值，则会返回None）
# result = d1.get('奥特曼', '抱歉，key不存在！')
# print(result)

# 新增
# d1 = {'张三': 72, '李四': 60, '王五': 85}
# d1['赵六'] = 100
# print(d1)

# 修改
# d1 = {'张三': 72, '李四': 60, '王五': 85}
# 修改的写法，与新增的写法一样，若字典中有对应的key，就是修改；若没有，就是新增
# d1['张三'] = 97
# print(d1)
# 批量修改
# d1.update({'李四': 40, '王五': 67})
# print(d1)

# 删除
d1 = {'张三': 72, '李四': 60, '王五': 85}

# 删除指定key所对应的那组键值对
# del d1['张三']
# print(d1)

# 删除指定key所对应的那组键值对，并返回这个key所对应的值
# result = d1.pop('张三')
# print(d1)
# print(result)

# pop方法可以设置默认值
# 默认值可以保证：当要删除的key不存在的情况下，程序不会报错，并且返回这个默认值
# result = d1.pop('奥特曼', '删除失败！')
# print(d1)
# print(result)

# 清空字典
d1.clear()
print(d1)
```

### 21_字典_常用方法

```python
# keys方法：用于获取字典中所有的键
# d1 = {'张三': 72, '李四': 60, '王五': 85}

# keys方法的返回值不是list，而是一种叫做dict_keys的类型
# result = d1.keys()
# print(result)
# print(type(result))

# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
# for item in result:
#     print(item)
# print(result[0])

# 借助内置的list函数，可以将dict_keys转换成list
# l1 = list(result)
# print(l1)
# print(type(l1))

# values方法：获取字典中所有的值
# d1 = {'张三': 72, '李四': 60, '王五': 85}
# values方法的返回值类型是：dict_values，它的特点和dict_keys一样
# result = d1.values()
# print(result)
# print(type(result))

# items方法：获取字典中所有的键值对（每组键值对以元组的形式呈现）
d1 = {'张三': 72, '李四': 60, '王五': 85}
# items方法返回的类型是：dict_items，它的特点也和dict_keys一样
result = d1.items()
print(result)
print(type(result))
```

### 22_字典_循环遍历

```python
# 字典不能使用while循环遍历，但可以使用for循环遍历
d1 = {'张三': 72, '李四': 60, '王五': 85}

for key in d1:
    print(f'{key}的成绩是{d1[key]}')

for key in d1.keys():
    print(f'{key}的成绩是{d1[key]}')
```

### 23_数据容器_通用操作

```python
# 以下这五个函数：既能定义对应的【空容器】，又能将【其他类型】转换为对应的数据类型

# 1.list 函数：1.定义空列表。2.将【可迭代对象】转换为列表
# res1 = list(range(8))
# res2 = list('欢迎来到尚硅谷')
# res3 = list({10, 20, 30, 40, 50})
# res4 = list({'张三': 75, '李四': 60, '王五':85}.items())
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 2.tuple 函数：1.定义空元组。2.将【可迭代对象】转换为元组
# res1 = tuple(range(8))
# res2 = tuple('欢迎来到尚硅谷')
# res3 = tuple({10, 20, 30, 40, 50})
# res4 = tuple({'张三': 75, '李四': 60, '王五':85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 3.set 函数：1.定义空集合。2.将【可迭代对象】转换为集合
# res1 = set(range(8))
# res2 = set('欢迎来到尚硅谷')
# res3 = set({10, 20, 30, 40, 50})
# res4 = set({'张三': 75, '李四': 60, '王五':85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)


# 4.str 函数：1.定义空字符串。2.将【任意类型】转换为字符串
# res1 = str(range(8))
# res2 = str('欢迎来到尚硅谷')
# res3 = str({10, 20, 30, 40, 50})
# res4 = str({'张三': 75, '李四': 60, '王五':85})
# res5 = str(False)
# res6 = str(None)
# res7 = str(100)
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)
# print(type(res5), res5)
# print(type(res6), res6)
# print(type(res6), res6)
# print(type(res7), res7)

# 5.dict 函数：1.定义空字典。2.将【可迭代对象】转换为字典
# 备注：交给dict函数的内容必须是键值对才可以，否则就会报错
# res1 = dict({'张三': 75, '李四': 60, '王五':85})
# res2 = dict([('张三', 75), ('李四', 60), ('王五', 85)])
# res3 = dict((('张三', 75), ('李四', 60), ('王五', 85)))
# res4 = dict({('张三', 75), ('李四', 60), ('王五', 85)})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 所有的数据容器，都支持【成员运算符】： in / not in  作用：判断某个“元素”是否在于容器中。
hobby = ['抽烟', '喝酒', '烫头']
nums = (10, 20, 30, 40, 50)
message = 'hello,atgiugu'
citys = {'北京', '天津', '上海', '重庆'}
score = {'张三': 75, '李四': 60, '王五':85}

print('喝酒' not in hobby)
print(20 not in nums)
print('hel' not in message)
print('上海' not in citys)
print('李华' not in score)
```

### 24_数据容器_小练习

```python
# 练习一：水果清单
fruits = {
    '苹果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.0,
    '哈密瓜': 8.8
}

# 需求1：打印所有的水果
# for key in fruits:
#     print(f'{key}：{fruits[key]} 元/斤')

# 需求2：找到最贵水果
# key = max(fruits, key=fruits.get)
# print(f'最贵的水果是{key}，价格是{fruits[key]} 元/斤')

# --------------------------------------------------------------------

# 练习二：学生成绩表
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    }
]

# 需求1：计算每位学生的平均分
# for stu in students:
#     # 获取当前学生的成绩列表
#     score_list = stu['scores'].values()
#     # 计算平均值
#     avg = sum(score_list) / len(score_list)
#     print(f'{stu['name']}的平均成绩是：{avg:.1f}')


# 需求2：找到总分最高的学生
# def find_best():
#     # 记录分数最高的学生
#     best_students = []
#     # 记录最高分
#     best_score = 0
#     # 循环遍历
#     for stu in students:
#         # 获取当前学生的总成绩
#         total = sum(stu['scores'].values())
#         # 当前学生的成绩，如果大于best_score，就会更新数据
#         if total > best_score:
#             best_students = [stu['name']]
#             best_score = total
#         # 当前学生的成绩与最高分相同，就加入列表
#         elif total == best_score:
#             best_students.append(stu['name'])
#     print(f'最高分为{best_score}，取得最高分的学生有：{best_students}')
# find_best()

# --------------------------------------------------------------------

# 练习三：评论内容
comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1：统计“好喝”出现次数
print(comment.count('好喝'))

# 需求2：将字符串中的“贵”替换为“略高”
comment2 = comment.replace('贵', '略高')
print(comment2)

# 需求3：是否包含“推荐”两个字
print('推荐' in comment)
```

---

## 第7章 · 面向对象编程

### 01_类的定义

```python
# 定义一个Person类（类名通常使用：大驼峰写法）
class Person:
    # 说明：当一个函数被定义在了类中时，那这个函数就被称为：方法。
    # __init__方法：初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
    # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值）
        self.name = name
        self.age = age
        self.gender = gender
```

### 02_创建实例

```python
# 定义一个Person类
class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 如果直接打印一个实例的话，我们是看不到实例身上的属性的
# print(p1)
# print(p2)

# 通过点语法可以访问或修改实例身上的属性
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print('-' * 20)
# print(p2.name)
# print(p2.age)
# print(p2.gender)
# p1.name = '阿三'
# print(p1.name)

# 通过 实例.__dict__ 可以查看实例身上的所有属性
# print(p1.__dict__)
# print(p2.__dict__)

# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
# p1.address = '北京昌平宏福科技园'
# print(p1.__dict__)

# 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
# print(type(p1))
# print(type(p2))
```

### 03_自定义方法

```python
# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法（给实例添加行为）
    # speak方法收到的参数是：调用speak方法的实例对象（self）、其它参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

# 验证一下：speak方法是存在Person类身上的
# print(Person.__dict__)

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 验证一下：Person的实例对象身上是没有speak方法的
# print(p1.__dict__)
# print(p2.__dict__)

# 所有Person类的实例对象，都可以调用到speak方法
# 当执行p1.speak()的时候，查找speak方法的过程：1.实例对象自身(p1)  =>  2.实例的“缔造者”的身上(Person)
# p1.speak('好好学习')
# p2.speak('天天向上')

# 验证一下上述的查找过程
def speak():
    print('巴拉巴拉巴拉巴拉巴拉')
p1.speak = speak
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
p1.speak()
```

### 04_实例属性

```python
# 定义一个Person类
class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        # 通过【实例.属性名 = 值】给实例添加的属性，就叫实例属性
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己【独一份的】实例属性，各个实例之间是互不干扰的
        self.name = name
        self.age = age
        self.gender = gender

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 实例属性只能通过实例访问，不能通过类访问
# print(p1.name)
# print(Person.name)
```

### 05_类属性

```python
# 定义一个Person类
class Person:
    # max_age、planet 他们都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age = 120
    planet = '地球'

    # 初始化方法
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.gender = gender
        # 限制age的最大值
        if age <= Person.max_age:
            self.age = age
        else:
            print(f'年龄超出范围了，已经将年龄设置为最大值：{Person.max_age}')
            self.age = Person.max_age

# 验证一下：类属性是保存在类身上的
# print(Person.__dict__)

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 验证一下：实例身上是没有类属性的
# print(p1.__dict__)
# print(p2.__dict__)


# 验证一下：类属性可以通过类访问，也可以通过实例访问
# print(Person.max_age)
# print(p1.max_age)  # 查找max_age的过程：1.实例自身(p1)  => 2.实例的“缔造者”(Person)
# print(p2.planet)

# 测试一下年龄超出范围
# p3 = Person('王五', 170, '女')
# print(p3.__dict__)

# 注意点：进行【实例.属性名 = 值】操作时，只会对实例自身的属性起作用，不会影响类属性
p1.planet = '火星'
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
print(p1.planet)
print(p2.planet)
```

### 06_实例方法

```python
# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
    # 自定义方法（给实例添加行为）
    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# print(Person.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)

# 通过实例调用实例方法
# p1.speak('你好')
# p1.run(300)

# 通过类去调用实例方法(能调用，但不推荐)
Person.run(p2, 100)
```

### 07_类方法

```python
from datetime import datetime

# 定义一个Person类
class Person:
    # 类属性
    max_age = 120
    planet = '地球'

    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak方法、run方法，他们都属于：实例方法
    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    # 使用 @classmethod 装饰过的方法，就叫：类方法，类方法保存在类身上的
    # 类方法收到的参数：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def create(cls, info_str):
        # 从info_str中获取到有效信息
        name, year, gender = info_str.split('-')
        # 获取当前年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - int(year)
        # 创建并返回一个Person类的实例对象
        return cls(name, age, gender)


# 验证一下：类方法保存在类身上的
# print(Person.__dict__)

# 类方法需要通过类调用
# Person.change_planet('月球')
# print(Person.__dict__)

# 创建Person实例
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 验证一下：类属性planet已经修改了
# print(p1.planet)
# print(p2.planet)

# 测试一下类方法 —— create
# p3 = Person.create('李华-2003-女')
# print(p3.__dict__)

# 注意点：类方法，也能通过实例调用到，但是非常不推荐
p4 = p1.create('李华-2003-女')
print(p4.__dict__)
```

### 08_静态方法

```python
from datetime import datetime

# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫：静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数
    # 由于静态方法没有收到：self、cls参数，所以其内部不会访问任何：类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前的年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年True，未成年False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]


# 验证一下：静态方法也是保存在类身上的
# print(Person.__dict__)

# 静态方法需要通过类去调用
# result = Person.is_adult(2015)
# print(result)
# result2 = Person.mask_idcard('212101198802030028')
# print(result2)

# 注意点：通过实例也能调用到静态方法，但非常不推荐
p1 = Person('张三', 18, '男')
res = p1.mask_idcard('212101198802030028')
print(res)
```

### 09_继承

```python
# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

# 定义一个Student类（子类、派生类）， 继承自Person类（父类、超类、基类）
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 在子类中，有两种方式去调用父类的初始化方法，来实现对继承属性：name, age, gender 初始化操作
        # 方式1（更推荐）
        super().__init__(name, age, gender)

        # 方式2
        # Person.__init__(self, name, age, gender)

        # 子类独有的属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，我在努力的学习，争取做到{self.grade}年级的第一名')

# 创建Student类的实例对象
s1 = Student('李华', 16, '男', '2025001', '初二')
# print(s1.__dict__)
# print(type(s1))

# 查找speak方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
# s1.speak('你好')

# print(s1.__dict__)

# 查找study方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
# s1.study()
```

### 10_方法重写

```python
# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')


# 定义一个Student类，继承自Person类
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法
    def speak(self, msg):
        super().speak(msg)
        print(f'我是学生，我的学号是{self.stu_id}，我正在读{self.grade}，我想说：{msg}')

s1 = Student('李华', 12, '男', '2025001', '初二')
s1.speak('好好学习')
```

### 11_两个常用方法

```python
# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 定义一个Student类，继承自Person类
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

p1 = Person('张三', 18, '男')
s1 = Student('李华', 12, '男', '2025001', '初二')

# 方法1：isinstance(instance, Class)，作用：判断某个对象是否为指定类或其子类的实例
print(isinstance(s1, Student))
print(isinstance(p1, Person))
print(isinstance(s1, Person))
print(isinstance(p1, Student))

# 方法2：issubclass(Class1, Class2)，作用：判断某个类是否是另一个类的子类
print(issubclass(Student, Person))
print(issubclass(Person, Student))
```

### 12_多重继承

```python
# 概念：多重继承指一个类同时继承多个父类，从而拥有多个父类的属性和方法。
# 举例：就像孩子不仅继承爸爸的长相，也能继承妈妈的性格。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}')

class Worker:
    def __init__(self, company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}做兼职')

class Student(Worker, Person):
    def __init__(self, name, age, gender, company, stu_id, grade):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我在努力的学习，争取做{self.grade}年级的第一名')

s1 = Student('张三', 18, '男', '麦当劳', '2025001', '初二')
print(s1.__dict__)
s1.speak()
s1.do_work()
s1.study()

# 类的__mro__属性：用于记录属性和方法的查找顺序
# 通过实例去查找属性或方法时，会先在实例自身上去查找，如果没有，就按照__mro__记录的顺序去查找
print(Student.__mro__)
```

### 13_三种权限

```python
class Person:
    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类中、子类中、类外部，都可以访问
        self._age = age         # 受保护的属性：当前类中、子类中，都可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类中访问
    def speak(self):
        print(f'我叫：{self.name}，年龄：{self._age}， 身份证：{self.__idcard}')

class Student(Person):
    def hello(self):
        print(f'我是学生（{self.name}-{self._age}）')

p1 = Person('张三', 18, '110101199001011234')
# print(p1.name)
# 在类的外部，如果强制访问【受保护的属性】也能访问到，但十分不推荐！
# print(p1._age)
# 在类的外部，如果强制访问【私有属性】不能访问到，而且会报错！
# print(p1.__idcard)

# Python底层是通过重命名的方式，实现私有属性的
# print(p1.__dict__)
# print(p1._Person__idcard)
```

### 14_getter与setter

```python
class Person:
    max_age = 120

    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类中、子类中、类外部，都可以访问
        self._age = age         # 受保护的属性：当前类中、子类中，都可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类中访问

    # 注册age属性getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age

    # 注册age属性setter方法，当修改Person实例的age属性时，下面的age方法就会被自动调用
    @age.setter
    def age(self, value):
        if value <= Person.max_age:
            self._age = value
        else:
            print('年龄非法，修改失败！')

    # 注册idcard属性getter方法，当访问Person实例的idcard属性时，下面的idcard方法就会被自动调用
    @property
    def idcard(self):
        return self.__idcard[:6] + '********' + self.__idcard[-4:]

    # 注册idcard属性setter方法，当修改Person实例的idcard属性时，下面的idcard方法就会被自动调用
    @idcard.setter
    def idcard(self, value):
        print('抱歉身份证号码不允许修改，如有特殊需求，请联系管理员！')

p1 = Person('张三', 18, '110101199001011234')
print(p1.name)
print(p1.age)
p1.age = 25
print(p1.age)
print(p1.idcard)
p1.idcard = '110101199001011456'
```

### 15_魔法方法

```python
# 概念：以 __xxx__ 命名的特殊方法（双下划线开头和结尾）。
# 特点：不需要我们手动调，我们只要准备好这些方法，Python会在特定场景下，去自动调用。

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 当执行print(Person的实例对象) 或 str(Person的实例对象) 时调用
    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}'

    # 当执行len(Person的实例对象) 时调用
    def __len__(self):
        return len(p1.__dict__)

    # 当执行 Person实例对象1 < Person实例对象2 时调用
    def __lt__(self, other):
        return self.age < other.age

    # 当执行 Person实例对象1 > Person实例对象2 时调用
    def __gt__(self, other):
        return self.age > other.age

    # 当执行 Person实例对象1 == Person实例对象2 时调用
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # 当访问Person实例对象身上不存在的属性时调用
    def __getattr__(self, item):
        return f'您访问的{item}属性不存在'

p1 = Person('张三', 22, '男')
p2 = Person('李四', 22, '男')
# print(p1)
# print(p2)
# res = len(p1)
# print(res)
# print(p1 < p2)
# print(p1 > p2)
# print(p1 == p2)
print(p1.address)
```

### 16_object类

```python
# Python 中，所有的类都继承了 object 类，即：object 类是所有类的顶层父类。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 验证一下：所有的类继承了object类
# print(issubclass(Person, object))
# print(issubclass(int, object))
# print(issubclass(str, object))
# print(issubclass(list, object))
# print(issubclass(bool, object))
# print(issubclass(tuple, object))

# 因为 object 是所有类的父类，所以 Python 中的所有对象，都间接是 object 类的实例。
# p1 = Person('张三', 18, '男')
# print(isinstance(p1, object))
# print(isinstance(100, object))
# print(isinstance('hello', object))
# print(isinstance(True, object))
# print(isinstance(None, object))
# print(isinstance([10, 20, 30], object))
# print(isinstance({'吃饭','睡觉'}, object))

# 所有对象都继承了object类所提供的：各种属性和方法，从而保证了每个对象都具备统一的基本能力
# for key in object.__dict__:
#     print(key)

p1 = Person('张三', 18, '男')
print(p1.__dict__)  # 对象身上自己的东西
print(dir(p1))      # 对象可以访问到的东西（自己的、继承过来的）

print(p1.__str__())
print(p1)
```

### 17_标准多态

```python
# 多态的概念：同一个方法名，在不同的对象上调用时，能呈现出不同的行为。
# Python中支持：标准多态、鸭子多态
class Animal:
    def speak(self):
        print('动物正在发出声音！')

class Dog(Animal):
    def speak(self):
        print('汪汪汪！')

class Cat(Animal):
    def speak(self):
        print('喵喵喵！')

class Pig:
    def speak(self):
        print('哼哼哼！')

def make_sound(animal:Animal):  # 类型注解
    # 多态的体现
    animal.speak()

# 创建实例对象
a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()

make_sound(a1)
make_sound(d1)
make_sound(c1)
make_sound(p1) # 此行代码如果在其它语言中会报错，Python不会报错，不推荐这样写
```

### 18_鸭子多态

```python
# 核心理念：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子。
# 鸭子类型是一种编程风格，它不检查对象的类型，只关注对象能否“做某件事”（是否有对应的方法）。

# 鸭子多态
class Dog:
    def speak(self):
        print('汪汪汪！')

class Cat:
    def speak(self):
        print('喵喵喵！')

class Pig:
    def speak(self):
        print('哼哼哼！')

class Fish:
    def speak(self):
        print('咕噜噜！')

class Computer:
    def speak(self):
        print('滋滋滋！')

def make_sound(animal):
    animal.speak()

# 创建实例对象
d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()
cm1 = Computer()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)
make_sound(cm1)
```

### 19_抽象类

```python
from abc import ABC, abstractmethod

#【抽象类】是一种不能直接实例化的类，它通常作为“规范”，让子类去继承，并实现其中定义的【抽象方法】。
# MustRun类一旦继承了ABC类，那么MustRun类就是抽象类了
class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass

    def speak(self):
        print(f'你好，我叫{self.name}')

class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑')

p1 = Person('张三', 18, '男')
p1.run()
p1.speak()
```

### 20_小练习

```python
from datetime import datetime

# 定义Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    # 计数器
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        # 给每个学生添加stu_id属性，格式为：年份-序号，序号靠计数器增长。
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        # 给学生添加成绩，格式为： {'数学':90, '语文':80, '英语':70}
        self.scores = {}

    # 给当前学生添加成绩
    def add_score(self, subject, score):
        # 给指定学生添加成绩，subject是学科，score是成绩
        self.scores[subject] = score

    # 计算平均分
    def calcu_avg(self):
        if self.scores:
            # 计算平均成绩
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    # 魔法方法
    def __str__(self):
        return f'{self.name}({self.age}-{self.gender})，成绩：{self.scores}，平均分:{self.calcu_avg():.1f}'

class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')
        # 创建学生实例对象
        stu = Student(name, age, gender)
        # 将当前学生添加到stu_list列表中
        self.stu_list.append(stu)
        print(f'添加成功！学号是：{stu.stu_id}')

    # 删除学生
    def del_student(self):
        sid = input('请输入学号：')
        # target用于保存要删除的学生
        target = None
        # 遍历所有学生，找到要删除的学生，并交给target变量
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
        # 如果找到了要删除的学生，就调用remove方法移除该学生
        if target:
            self.stu_list.remove(target)
            print('删除成功！')
        # 如果未找到要删除的学生
        else:
            print('学号有误，删除失败！')

    # 展示所有学生
    def show_all_student(self):
        # 如果当前stu_list中有学生，就遍历展示
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        # 如果当前stu_list中没有学生，就打印：暂无学生！
        else:
            print('暂无学生！')

    # 给指定学生设置成绩
    def set_score(self):
        sid = input('请输入学号：')
        # 遍历stu_list列表
        for stu in self.stu_list:
            # 如果当前学生学号，与输入的sid相等
            if stu.stu_id == sid:
                # 输入成绩字符串，格式为：学科-分数，学科-分数
                score_str = input('清输入成绩（学科-分数，学科-分数）')
                # 将输入的多个成绩，按照逗号拆分，形成成绩列表
                score_list = score_str.replace('，', ',').split(',')
                # 循环成绩列表，依次添加成绩
                for item in score_list:
                    # 获取科目与成绩
                    subject, score = item.split('-')
                    subject = subject.strip()
                    score = float(score.strip())
                    # 调用add_score方法，添加科目，成绩
                    stu.add_score(subject, score)
                print('添加成功！')
                # 结束循环，同时结束set_score函数
                return
        # 若程序能执行到此处，证明在stu_list中没有找到与sid对应的学生
        print('学号有误！')

    # 提供主菜单
    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            chocie = input('请输入操作编号：')
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.del_student()
            elif chocie == '3':
                self.show_all_student()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('再见！')
                break
            else:
                print('输入有误！')

m1 = Manager()
m1.run()
```

### 21_内存分析

```python
# a = 666
# print(id(a))
# b = a
# print(id(b))
# print(a)
# print(b)
# a = 888
# print(a)
# print(b)
# print(id(a))
# print(id(b))

stu_list = ['张三', '李四', '王五']
print(id(stu_list))
print(id(stu_list[0]))
stu_list[0] = '阿三'
print(id(stu_list))
print(id(stu_list[0]))
```

---

## 第8章 · 高阶函数与进阶特性

### 01_重新认识函数

```python
# 1.函数也是对象
# a1 = 100            # int类的实例对象
# a2 = 'hello'        # str类的实例对象
# a3 = [10, 20, 30]   # list类的实例对象
#
# def welcome():      # welcome函数function类的实例对象
#     print('你好啊')
#
# print(type(a1))
# print(type(a2))
# print(type(a3))
# print(type(welcome))

# 2.函数可以动态添加属性
# def welcome():
#     print('你好啊')
# welcome.desc = '这是一个打招呼的函数'
# welcome.version = 1.0
# print(welcome.desc)
# print(welcome.version)


# 3.函数可以赋值给变量
# def welcome():
#     print('你好啊')
# welcome.desc = '这是一个打招呼的函数'
# welcome.version = 1.0
#
# say_hello = welcome
# say_hello()
# print(say_hello.desc)
# print(say_hello.version)


# 4.可变参数 vs 不可变参数
# 不可变参数
# a = 666
# def welcome(data):
#     print('data修改前', data, id(data))
#     data = 888
#     print('data修改后', data, id(data))
#
# print('函数调用前', a, id(a))
# welcome(a)
# print('函数调用后', a, id(a))

# 可变参数
# a = [10, 20, 30]
# def welcome(data):
#     print('data修改前', data, id(data))
#     data[2] = 99
#     print('data修改后', data, id(data))
#
# print('函数调用前', a, id(a))
# welcome(a)
# print('函数调用后', a, id(a))


# 5.函数也可以作为参数
# def welcome():
#     print('你好啊')
#
# def caller(f):
#     print('caller函数调用了')
#     f()
#
# caller(welcome)

# 6.函数也可以作为返回值
def welcome():
    print('你好啊')
    def show_msg(msg):
        print(msg)
    return show_msg

# result = welcome()
# result('尚硅谷')
welcome()('尚硅谷')
```

### 02_多返回值_参数的打包与解包

```python
# 一、函数的多返回值
# def calculate(x, y):
#     res1 = x + y
#     res2 = x - y
#     return res1, res2
#
# result = calculate(30, 10)
# print(result)
#
# r1, r2 = calculate(30, 10)
# print(r1, r2)


# 二、参数的打包与解包

# 1.打包接收参数：
# *args    ：打包所有的位置参数（会形成一个元组）
# **kwargs ：打包所有的关键字参数（会形成一个字典）
# def show_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# show_info(10, 20, 30, name='张三', age=18, gender='男')


# 2.解包传递参数
# *变量名  ：将元组拆解成一个一个独立的位置参数
# **变量名 ：将字典拆解一个一个 key=value 形式的关键字参数
# def show_info(num1, num2, num3, name, age, gender):
#     print(num1, num2, num3)
#     print(name, age, gender)
#
# nums = (10, 20, 30)
# person = {'name':'张三', 'age':18, 'gender':'男'}
#
# show_info(*nums, **person)


# 3.打包接收参数 和 解包传递参数 一起使用
# def show_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# nums = (10, 20, 30)
# person = {'name':'张三', 'age':18, 'gender':'男'}
#
# show_info(*nums, **person)
```

### 03_高阶函数

```python
# 高阶函数：当一个函数的『参数是函数』或者『返回值是函数』那该函数就是『高阶函数』。

# 高阶函数的意义：
# 1. 代码复用性高：可以把行为“独立出去”，传入不同函数实现不同逻辑。
# 2. 能让函数更灵活，更通用。
# 3. 高阶函数是：装饰器、闭包的基础。（后面会讲）

def info(msg):
    return '[提示]：' + msg

def warn(msg):
    return '[警告]：' + msg

def error(msg):
    return '[错误]：' + msg

def log(func, text):
    print(func(text))

log(info, '文件保存成功！')
log(warn, '磁盘空间不足！')
log(error, '该用户不存在！')
```

### 04_条件表达式

```python
# 表达式：执行后能得到值的代码，就是表达式（表达式最终会形成一个值，可以写在任何需要值的地方）。
# a1 = 3 + 5
# a2 = 'abc' * 3
# print(5 > 3)
# int('y' in 'python')
# a5 = len('hello')

# 条件表达式：根据条件的真假，在两个值中二选一的表达式（又称：三元表达式、三目运算符）。
age = 21

# 传统的if-else去写：
# if age >= 18:
#     text = '成年'
# else:
#     text = '未成年'
# print(text)

# 条件表达式去写：值1 if 条件 else 值2
# text = '成年' if age >= 18 else '未成年'
# print(text)

# 条件表达式的使用场景：简单的二选一场景
rain = True
eat = '外卖' if rain else '出去吃'

is_vip = False
disscount = 0.8 if is_vip else 1.0

is_login = False
msg = '欢迎回来！' if is_login else print('哈哈哈')

print(eat)
print(disscount)
print(msg)
```

### 05_匿名函数

```python
# 概念：所谓『匿名函数』，就是没有名字的函数，它无需使用 def 关键字去定义。
# 语法：Python 中使用 lambda 关键字来定义『匿名函数』，格式为：lambda 参数: 表达式
# 使用场景： 当一个函数只用一次、只做一点点小事，使用匿名函数会更简洁。

# 使用普通函数实现计算效果
# def add(x, y):
#     return x + y
#
# def sub(x, y):
#     return x - y
#
# def calculate(func, a, b):
#     print(f'计算结果为：{func(a, b)}')
#
# calculate(add, 30, 10)
# calculate(sub, 30, 10)

# 匿名函数
# add1 = lambda x, y: x + y
# add2 = lambda x: x + x
# add3 = lambda: '我是add3函数'
#
# result1 = add1(30, 10)
# result2 = add2(30)
# result3 = add3()
# print(result1, result2, result3)

# 使用匿名函数实现计算效果
# def calculate(func, a, b):
#     print(f'计算结果为：{func(a, b)}')
#
# calculate(lambda x, y: x + y, 30, 10)
# calculate(lambda x, y: x - y, 30, 10)

# 注意点
# 1. 只能写一行，不能写多行代码。
# 2. 不能写代码块（if、for、while）
# 3. 冒号右边必须是表达式，且只能写一个表达式。
# 4. 表达式结果自动作为返回值。

is_adult = lambda age: '成年' if age >= 18 else '未成年'
print(is_adult(18))
print(is_adult(13))
```

### 06_数据处理_map函数

```python
# map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新数据。
# 语法格式：map(操作函数, 可迭代对象)

# 统一数据处理
# nums = [10, 20, 30, 40]
# map函数的返回值是一个迭代器对象，需要我们自己去手动遍历，或者手动类型转换
# result = map(lambda x: x * 2, nums)
# print(list(result))
# print(nums)

# 字符串转换
# names = ('python', 'java', 'js')
# result = map(lambda x: x.upper(), names)
# print(tuple(result))
# print(names)

# 类型转换
# str_number = {'1', '2', '3'}
# result = map(int, str_number)
# print(set(result))
# print(str_number)

# 注意点：
# 1.延迟执行：map 不会立刻计算，只有在“需要结果”时才执行计算。
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3.map不会影响元素数量。

nums = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, nums))
print(result)
print(result)
print(result)
print(result)
```

### 07_数据处理_filter函数

```python
# filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一组新数据。
# 语法格式：filter(过滤函数, 可迭代对象)

# 筛选数值
# nums = [10, 20, 30, 40, 50]
# result = filter(lambda n: n > 30, nums)
# print(list(result))
# print(nums)

# 筛选成年人
# persons = [
#     {'name':'张三', 'age':15, 'gender':'男'},
#     {'name':'李四', 'age':16, 'gender':'女'},
#     {'name':'王五', 'age':17, 'gender':'男'},
#     {'name':'李华', 'age':18, 'gender':'女'},
#     {'name':'赵六', 'age':19, 'gender':'女'},
#     {'name':'孙七', 'age':20, 'gender':'男'}
# ]
# result = filter(lambda p: p['age'] >= 18, persons)
# print(list(result))

# 过滤一下非法字符串
# names = ['张三', '', '李四', None, '王五']
# result = filter(lambda n: n, names)
# print(list(result))

# 注意点
# 1.延迟执行：filter不会立刻筛选，只有在“需要结果”时才执行。
# 2.返回的是迭代器对象，且一旦遍历完成就会被“耗尽”。
# 3.filter可能会影响元素数量。

# filter函数的特殊用法：如果不传递过滤函数，那么自动会过滤掉“假值”
data = [0, 1, '', 'hello', [], (), 5]
result = filter(None, data)
print(list(result))
```

### 08_数据处理_sorted函数

```python
# sorted函数：对一组数据进行排序，返回一组新数据。
# 语法格式：sorted(可迭代对象, key=xxx, reverse=xxx)

# 数字排序
# nums = [30, 40, 20, 10]
# result = sorted(nums, reverse=True)
# print(result)

# 按照字符串的长度去排序
# names = ['python', 'sql', 'java']
# result = sorted(names, key=len, reverse=True)
# print(result)

# 根据字典中的某个字段进行排序
persons = [
    {'name':'张三', 'age':15, 'gender':'男'},
    {'name':'李四', 'age':17, 'gender':'女'},
    {'name':'王五', 'age':19, 'gender':'男'},
    {'name':'李华', 'age':20, 'gender':'女'},
    {'name':'赵六', 'age':18, 'gender':'女'},
    {'name':'孙七', 'age':16, 'gender':'男'}
]
result = sorted(persons, key=lambda p: p['age'], reverse=True)
print(result)

# 我们之前讲的max函数、min函数，也可以传递key参数，用于设置筛选依据
result1 = max(persons, key=lambda p: p['age'])
result2 = min(persons, key=lambda p: p['age'])
print(result1)
print(result2)
```

### 09_数据处理_reduce函数

```python
# reduce函数：将一组数据不断“合并”，最终归并成一个结果。
# 语法格式：reduce(合并函数, 可迭代对象, 初始值)。
# 备注：reduce函数需要从 functools 模块中引入才能使用。

# 从 functools 模块中引入 reduce
from functools import reduce

# 数值统计
# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda a, b: a + b, nums, 10)
# print(result)

# 字符串拼接
str_list = ['ab', 'cd', 'ef']
result = reduce(lambda a, b: a + b, str_list)
print(result)
```

### 10_列表推导式

```python
# 列表推导式：用一条简洁语句，从可迭代对象中，生成新列表的语法结构。
# 备注：列表推导式本质上是对 for循环 + append() 的一种简写形式。
# 语法格式：[表达式 for 变量 in 可迭代对象]

# 需求：让列表中每个元素，都变为原来的2倍，得到是一个新的列表

# 方式一：用map函数
# nums = [10, 20, 30, 40]
# result = list(map(lambda n: n * 2, nums))
# print(result)

# 方式二：用 for循环 + append()
# nums = [10, 20, 30, 40]
# result = []
# for n in nums:
#     result.append(n * 2)
# print(result)

# 方式三：用列表推导式
# nums = [10, 20, 30, 40]
# result = [n * 2 for n in nums]
# print(result)

# 带条件的列表推导式
# nums = [10, 20, 30, 40]
# result = [n * 2 for n in nums if n > 20]
# print(result)

# 字典推导式
# names = ['张三', '李四', '王五']
# scores = [60, 70, 80]
# result = {names[i]: scores[i] for i in range(len(names))}
# print(result)

# 集合推导式
# names = ['张三', '李四', '王五']
# result = {n + '！' for n in names}
# print(result)

names = ['张三', '李四', '王五']
# Python中没有元组推导式，下面这种写法叫：生成器（后面会仔细讲）
result = (n + '！' for n in names)
print(result)
```

### 11_常用内置函数

```python
# 一、输入与输出
# print() ===> 输出指定内容
# 完整参数：print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数详解：
#   1.objects：要输出的内容
#   2.sep：分隔符
#   3.end：结束符
#   4.file：输出位置
#   5.flush：是否立即刷新

# f = open('a.txt', 'w', encoding='utf-8')
# print(10, 20, 30, 40, sep='-', end='!', file=f)

import time
# 第一种进度条
# print('加载中', end='')
# for index in range(5):
#     print('.', end='', flush=True)
#     time.sleep(1)
# print('完成！', end='')

# 第二种进度条
# for index in range(1, 101):
#     print(f'\r已加载{index}%', end='', flush=True)
#     time.sleep(0.1)


# input() ===> 获取用户输入

# 二、类型转换
# int() ======> 转为整数
# float() ====> 转为浮点数
# str() ======> 转为字符串
# bool() =====> 转为布尔值
# list() =====> 转为列表
# tuple() ====> 转为元组
# set() ======> 转为集合
# dict() =====> 转为字典

# 三、数学相关
# abs() =========> 取绝对值
# print(abs(-9))
# print(abs(-2.5))
# print(abs(3 - 5))


# round() =======> 四舍五入
# 注意：round函数的四舍五入，是银行家舍入法：小于5就舍，大于5就入，等于5看奇偶（奇入偶舍）
# print(round(3.4))
# print(round(4.6))
# print(round(6.5))
# print(round(7.5))
# print(round(7.543, 2))

# pow()	=========> 次方
# print(pow(2, 3))    # 2的3次方
# print(pow(2, -1))   # 2的-1次方
# print(pow(2, 0.5))  # 2的开平方
# print(pow(2, 3, 5)) # 2的3次方对5取模


# divmod() ======> 商和余数
# print(divmod(10, 3))


# max()	=========> 最大值（支持 key 函数）
# min()	=========> 最小值（支持 key 函数）
# sum()	=========> 求和
# map()	=========> 加工一组数据
# filter() ======> 按条件过滤数据（支持 key 函数）
# reduce() ======> 合并计算（需导入 functools）
# sorted() ======> 排序（支持 key 函数）

# 四、数据容器相关
# len()	==========> 获取容器中元素的个数
# range() ========> 生成一个数字序列（可用于循环）
# for index in range(0, 10, 2):
#     print(index)

# enumerate() ====> 给序列添加索引
# zip()	==========> 将多个序列一一配对
# names = ('张三', '李四', '王五')
# scores = [60, 70, 80]
# result = zip(names, scores)
# for item in result:
#     print(item)

# 五、类型判断与对象相关
# type() ==========> 查看类型
# isinstance() ====> 判断类型
# issubclass() ====> 判断两个类的继承关系
# id() ============> 查看对象的内存地址

# 六、逻辑判断相关
# all() ====> 全为真返回True
# l1 = [10, '尚硅谷', {1, 2, 3}, -9]
# print(all(l1))

# any() ====> 有一个为真即可
# l2 = [0, '', None, False, 10]
# print(any(l2))

# 七、字符串辅助相关
# ord() ====>  获取字符的 Unicode 编码值
# chr() ====>  将 Unicode 编码值转为字符
```

### 12_浅拷贝_深拷贝

```python
import copy

# 直接赋值：两个变量指向同一个对象，修改其中一个，就会影响另一个（互相影响）。
# nums1 = [10, 20, 30, 40]
# nums2 = nums1
# nums2[3] = 99

# 浅拷贝：创建一个新的外层容器，但内部元素仍然引用原来的对象
# nums1 = [10, 20, 30, 40]
# nums2 = copy.copy(nums1)
# nums2[3] = 99

# 浅拷贝存在的问题：嵌套数据仍然是共享的，修改嵌套数据会互相影响
# nums1 = [10, 20, 30, [40, 50]]
# nums2 = copy.copy(nums1)
# nums2[3][0] = 99

# 深拷贝：创建一个新的外层容器，并对其内部所有的【可变子对象】进行递归复制
# 备注：
#   1.深拷贝可以彻底消除数据之间的相互影响。
#   2.深拷贝遇到【不可变对象】不会复制，会直接引用。
# nums1 = [10, 20, 30, [40, 50]]
# nums2 = copy.deepcopy(nums1)
# nums2[3][0] = 99

# 注意点：
#   1.深拷贝只复制可变对象，不可变对象会直接引用。
# a = 666
# b = copy.deepcopy(a)
# print(id(a))
# print(id(b))

#   2.元组中如果只包含不可变对象，则深拷贝没有效果。
# nums1 = (10, 20, 30, [40, 50])
# nums2 = copy.deepcopy(nums1)
#
# print(id(nums1))
# print(id(nums2))
```

### 13_四种作用域

```python
a = 100

def test(b):
    print('我是test函数')
    print('test中打印的a是', a)
    print('test收到的参数b是', b)
    c = 200
    d = 300
    print('test中的c和d是', c, d)
    def inner():
        e = 400
        nonlocal c
        c = 999
        print('inner中的e是', e)
        print('inner中打印的c是', c)
        print('########', a)
    inner()
    print('***************', c)

print('全局打印的a是', a)
test(66)
```

### 14_闭包

```python
# 前置知识一：
# 1.每次调用函数时，Python 都会为函数创建一个新的局部作用域
# 2.函数执行完毕后，这个局部作用域会被销毁，其中的局部变量也会随之被释放
# def outer():
#     num = 10
#     num += 1
#     print(num)
#
# outer()
# outer()
# outer()

# 前置知识二：
# 1.在 Python 中，【内层函数】可以访问其【外层函数】作用域中的变量
# 2.访问外层函数变量无需使用 nonlocal；但修改外层变量时要使用 nonlocal
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num = 99
#         print(1, num)
#     inner()
#     print(2, num)
#
# outer()


# 什么是闭包？ ————  闭包 = 内层函数 + 被内层函数所引用的外层变量
# 闭包产生的条件：
#   1.要有函数嵌套。
#   2.在【内层函数】中，要访问【外层函数】的变量。
#   3.并且【外层函数】要返回【内层函数】。———— 只有返回了内层函数，闭包才能“活下来”
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f = outer()
# f()
# f()
# f()

# 结论：
# 1.outer函数中，被inner所使用到的那些变量，会被封存到【闭包单元(cell)】中。
# 2.这些 cell 会组成一个 __closure__ 元组，最终放在了 inner 函数身上。

# 打印 __closure__ 元组
# print(f.__closure__)

# 打印 __closure__ 元组中的某一项
# print(f.__closure__[0])

# 打印 __closure__ 元组中的某一项的具体值
# print(f.__closure__[0].cell_contents)


# 注意点：
# 1. 调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f1 = outer()
# f1()
# f1()
# f1()
# print('*****************')
# f2 = outer()
# f2()


# 2. 内层函数中用到的外层变量是可变对象，多个闭包之间依然互不影
# def outer():
#     nums = []
#
#     def inner(value):
#         nums.append(value)
#         print(nums)
#
#     return inner
#
# f1 = outer()
# f1(10)
# f1(20)
# f1(30)
# print('**********************')
# f2 = outer()
# f2(666)


# 闭包的优点：
# 1. 可以“记住”状态：不用全局变量，也不用写类，就能在多次调用之间保存数据。
# 2. 可以做“配置过的函数”：先传一部分参数，把环境固定住，得到一个定制版函数。
# 3. 可以实现简单的“数据隐藏”：外层变量对外不可见，只能通过内层函数访问。
# 4. 是装饰器（decorator）等高级用法的基础。
# def beauty(char, n):
#     def show_msg(msg):
#         print(char * n + msg + char * n)
#     return show_msg
#
# show1 = beauty('*', 3)
# show1('你好啊')
# show1('尚硅谷')
#
# show2 = beauty('@', 5)
# show2('你好啊')
# show2('尚硅谷')

# 闭包的缺点：
# 1. 理解成本较高：对初学者不太友好，滥用会让代码难读。
# 2. 如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
# 3. 很多场景下，其实用【类 + 实例属性】会更清晰，闭包不一定是最优解。
# class Beauty:
#     def __init__(self, char, n):
#         self.char = char
#         self.n = n
#
#     def show_msg(self, msg):
#         print(self.char * self.n + msg + self.char * self.n)
#
# b1 = Beauty('*', 3)
# b1.show_msg('你好啊')
# b1.show_msg('尚硅谷')
#
# b2 = Beauty('#', 5)
# b2.show_msg('你好啊')
# b2.show_msg('尚硅谷')
```

### 15_函数装饰器

```python
# 装饰器：
# 1.装饰器是一种【可调用对象】（通常是函数），它能接收一个函数作为参数，并且会返回一个新函数。
# 2.装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能。

# 实际应用：在不改变原函数的前提下，给函数统一加上：日志、计时、校验、缓存 等功能

# 关键点：
# 1.接收被装饰的函数、同时返回新函数（wrapper）
# 2.装饰器“吐出来”的是 wrapper 函数，以后别人调用的也是 wrapper 函数。
# 3.为了保证参数的兼容性，wrapper 函数要通过 *args 和 **kwargs 接收参数。
# 4.wrapper 函数中主要做的是：调用原函数（被装饰的函数）、执行其它逻辑，但要记得将原函数的返回值 return 出去。

# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print('你好，我要开始计算了')
#         return func(*args, **kwargs)
#     return wrapper
#
# @say_hello
# def add(x, y, z):
#     res = x + y + z
#     print(f'{x}和{y}和{z}相加的结果是：{res}')
#     return res

# 正常调用add函数
# result = add(10, 20, 30)
# print(result)

# 需求：在不修改add函数的前提下，给add函数增加一些额外的功能，例如：计算前先打印一句欢迎语。
# 实现方案：使用装饰器
# 下面这行代码，是手动装饰，写起来会麻烦一些，不推荐，推荐：@装饰器名
# add = say_hello(add)
# result = add(10, 20, 30)
# print(result)


# 进阶：带参数的装饰器(三层嵌套，外层接收配置、中间层接收函数、内层接收具体参数)
# def say_hello(msg):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(f'你好，我要开始{msg}计算了')
#             return func(*args, **kwargs)
#         return wrapper
#     return outer
#
#
# @say_hello('加法')
# def add(x, y, z):
#     res = x + y + z
#     print(f'{x}和{y}和{z}相加的结果是：{res}')
#     return res
#
# @say_hello('减法')
# def sub(x, y):
#     res = x - y
#     print(f'{x}和{y}相减的结果是：{res}')
#     return res
#
# result1 = add(10, 20, 30)
# print(result1)
#
# result2 = sub(20, 10)
# print(result2)

# 进阶：多个装饰器一起使用

def test1(func):
    print('我是test1装饰器')
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test1追加的逻辑')
        return res
    return wrapper

def test2(func):
    print('我是test2装饰器')
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test2追加的逻辑')
        return res
    return wrapper

@test1
@test2
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

resuult = add(10, 20)
# print(resuult)
```

### 16_类装饰器

```python
# 类装饰器：
# 1.包含 __call__ 方法的类，就是类装饰器。
# 2.像调用函数一样，去调用类装饰器的实例对象，就会触发 __call__ 方法的调用。
# 3.__call__ 方法通常接收一个函数作为参数，并且会返回一个新函数。

# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('你好，我要开始计算了')
#             return func(*args, **kwargs)
#         return wrapper

# 使用@语法糖使用类装饰器
# @SayHello()
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res

# 正常调用add函数
# result = add(10, 20)
# print(result)

# 使用 SayHello 去装饰 add 函数（手动装饰）
# say = SayHello()
# add = say(add)
# result = add(10, 20)
# print(result)

# 带参数的类装饰器
# class SayHello:
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(f'你好，我要开始{self.msg}计算了')
#             return func(*args, **kwargs)
#         return wrapper
#
# @SayHello('加法')
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
# result = add(10, 20)
# print(result)


# 多个类装饰器的使用
class Test1:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('我是Test1追加的逻辑')
            return func(*args, **kwargs)
        return wrapper

class Test2:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('我是Test2追加的逻辑')
            return func(*args, **kwargs)
        return wrapper

@Test1()
@Test2()
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

result = add(10, 20)
print(result)
```

### 17_变量类型注解

```python
# 变量类型注解：给变量加上类型说明，可增强代码的可读性、让 IDE 的提示更友好。
num: int = 100
prcie: float = 12.5
message: str = '你好啊'
is_vip: bool = True
result: None = None  # 语法上没有问题，但这么写没有意义

# 注意：可以先写变量的类型注解，以后再赋值
# school: str
# print('*******', school)
# school = '尚硅谷'

# hobby 是列表，并且列表中的所有元素必须是 str 类型
hobby: list[str] = ['抽烟', '喝酒', '烫头']

# hobby 是列表，并且列表中的元素，可以是：str 或 int 类型
hobby: list[str | int] = ['抽烟', '喝酒', '烫头']
# 上面这行代码的旧写法如下：
from typing import Union
hobby: list[Union[str, int]] = ['抽烟', '喝酒', '烫头']

# citys 是集合，并且集合中所有元素必须是 str 类型
citys: set[str] = {'北京', '上海', '深圳'}

# citys 是集合，并且集合中所有元素可以是：str 或 float 或 bool 类型
citys: set[str | float | bool] = {'北京', '上海', '深圳'}

# persons 是字典，键是 str 类型，值是 int 类型
persons: dict[str, int] = {'张三': 18, '李四': 19, '王五': 20}

# persons 是字典，键是 str 或 int 类型，值是 int 类型
persons: dict[str | int, int] = {'张三': 18, '李四': 19, '王五': 20}

# 元组的类型声明有点特殊，各位要留意一下：
# scores 是元组，并且元组中仅包含1个int类型的元素
scores: tuple[int] = (60,)

# scores 是元组，并且元组中包含3个int类型的元素
scores: tuple[int, int, int] = (60, 70, 80)

# scores 是元组，并且元组中包含任意个数的元素，但每个元素的类型必须是int
scores: tuple[int, ...] = (60, 70, 80, 90, 100)

# scores 是元组，并且元组中包含任意个数的元素，每个元素的类型可以是：int 或 str
scores: tuple[int | str, ...] = (60, '70', 80, '90', 100)

# Python 会根据初始赋值推导变量的类型：
# 1. 对于普通变量：后续如果改变类型，不会警告。
# 2. 对于容器变量：要求内部元素类型必须与推导出来的一致，否则就会警告。
x = 100
x = '尚硅谷'

y = [10, 20, 30]
y.append('40')
```

### 18_函数类型注解

```python
# 函数类型注解：给函数的【参数】和【返回值】添加类型说明。
# 语法格式：函数名(参数1: 类型, 参数2: 类型) -> 返回值类型:。

# 示例1：设置参数类型注解、设置返回值类型注解
# def add(x: int, y: int) -> int:
#     return x + y

# 示例2：参数有默认值(Python可以推导出参数的类型)、设置返回值类型
# def add(x=1, y=1) -> int:
#     return x + y

# 示例3：设置多个返回值的类型注解
# def show_nums_info(nums: list[int]) -> tuple[int, int, float]:
#     max_value = max(nums)
#     min_value = min(nums)
#     result = max_value / min_value
#     return max_value, min_value, result

# 示例4：设置 *args 的类型注解，要求 args 中的每个参数都必须是 int 类型
# def add(*args: int) -> int:
#     return sum(args)

# 示例5：设置 **kwargs 的类型注解，要求 kwargs 中的每组参数的值，必须是 str 或 int 类型
# def show_info(**kwargs: str | int):
#     print(kwargs)

# 获取函数的注解信息
# print(add.__annotations__)
```

---

## 第9章 · 异常处理

### 01_错误与异常

```python
# 错误：代码本身有语法错误，解释器无法执行代码。———— 无法通过异常处理机制解决
# age = 18
# if age >= 18
#     print('成年人')

# 异常：代码在语法上没问题，但执行过程中出现了问题。———— 可以通过异常处理机制解决
# 一些开发中常见的异常：

# 1.ZeroDivisionError：当除数为 0 时触发。
# num1 = 100
# num2 = 0
# result = num1 / num2

# 2.TypeError：当操作的数据类型不正确或不兼容时触发。
# result = '10' + 5

# 3.AttributeError: 当对象没有指定的属性或方法时触发。
# 演示1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('张三', 18)
# print(p1.name)
# print(p1.age)
# print(p1.gender)

# 演示2
# nums = [10, 20, 30]
# nums.add(40)

# 4.IndexError：当索引超出范围（索引越界）时触发。
# nums = [10, 20, 30, 40]
# print(nums[4])

# 5.NameError：当使用了不存在的变量时触发。
# print(school)

# 6.KeyError：当访问字典中不存在的 key 时触发。
# person = {'name':'张三', 'age':18}
# print(person['gender'])

# 7.ValueError：当值不合法，但类型正确时触发。
# int('hello')
```

### 02_异常处理

```python
# 1️⃣为什么要进行异常处理？
# 程序运行过程中出现的异常，如果得不到处理，那程序就会立即崩溃，导致后续代码无法执行。
# 异常处理不是让异常消失，而是将异常捕获到，随后根据异常的具体情况，来执行指定的逻辑。
# print('欢迎使用本程序')
# a = int(input('请输入第一个数：'))
# b = int(input('请输入第二个数：'))
# result = a / b
# print(f'{a}除以{b}的结果是：{result}')
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')


# 2️⃣异常处理（初级）：
# 1.将可能出现异常的代码放在 try 中，出现异常后的处理代码写在 except 中。
# 2.如果 try 中的代码出现异常，那 try 中的后续代码将不会执行，并自动跳转到 except 中处理异常。
# 3.如果 try 中的代码没有异常，那 except 中的代码就不会执行。
# 4.无论是否发生异常，try-except 后面的代码都会继续执行。
# 5.直接写 except 会捕获到 Python 中所有的异常 ———— 实际开发中不推荐这样做。
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数：'))
#     b = int(input('请输入第二个数：'))
#     result = a / b
#     print(f'{a}除以{b}的结果是：{result}')
# except:
#     print('抱歉，程序出现了异常！')
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')


# 3️⃣异常处理（捕获指定的类型的异常）
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数：'))
#     b = int(input('请输入第二个数：'))
#     result = a / b
#     print(f'{a}除以{b}的结果是：{result}')
# except ZeroDivisionError:
#     print('程序异常：0不能作为除数！')
# except ValueError:
#     print('程序异常：您输入的必须是数字！')
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')


# 4️⃣验证一下异常类之间的继承关系
# print(issubclass(ZeroDivisionError, ArithmeticError))
# print(issubclass(ZeroDivisionError, Exception))
# print(issubclass(ValueError, Exception))
# print(issubclass(KeyboardInterrupt, Exception))
# print(issubclass(KeyboardInterrupt, BaseException))


# 5️⃣多个 except 从上往下匹配，匹配成功后不再向下匹配。
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数：'))
#     b = int(input('请输入第二个数：'))
#     print(x)
#     result = a / b
#     print(f'{a}除以{b}的结果是：{result}')
# except ZeroDivisionError:
#     print('程序异常：0不能作为除数！')
# except ValueError:
#     print('程序异常：您输入的必须是数字！')
# except Exception:
#     print('程序异常!')
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')


# 6️⃣获取异常的具体信息
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数：'))
#     b = int(input('请输入第二个数：'))
#     print(x)
#     result = a / b
#     print(f'{a}除以{b}的结果是：{result}')
# except ZeroDivisionError:
#     print('程序异常：0不能作为除数！')
# except ValueError:
#     print('程序异常：您输入的必须是数字！')
# except Exception as e:
#     print(f'⚠程序异常，异常信息：{e}')
#     print(f'⚠程序异常，异常类型：{type(e)}')
#     print(f'⚠程序异常，异常参数：{e.args}')
#     print(f'⚠程序异常，异常的文件：{e.__traceback__.tb_frame.f_code.co_filename}')
#     print(f'⚠程序异常，异常的具体行数：{e.__traceback__.tb_lineno}')
#     # 通过 traceback 来回溯异常
#     # import traceback
#     # print(traceback.format_exc())
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')


# 7️⃣一个 except，也可以捕获不同的异常
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数：'))
#     b = int(input('请输入第二个数：'))
#     print(x)
#     result = a / b
#     print(f'{a}除以{b}的结果是：{result}')
# except (ZeroDivisionError, ValueError, Exception) as e:
#     if isinstance(e, ZeroDivisionError):
#         print('程序异常：0不能作为除数！')
#     elif isinstance(e, ValueError):
#         print('程序异常：您输入的必须是数字！')
#     else:
#         print(f'程序异常：{e}')
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')


# 8️⃣异常处理的完整写法：
#   1.try：    尝试去做可能会出现异常的事情
#   2.except： 出现异常时的处理（出现异常时怎么补救）
#   3.else：   如果一切顺利（没有异常出现）要做的事
#   4.finally：无论有没有异常，都要做的事
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数：'))
#     b = int(input('请输入第二个数：'))
#     result = a / b
#     print(f'{a}除以{b}的结果是：{result}')
# except (ZeroDivisionError, ValueError, Exception) as e:
#     if isinstance(e, ZeroDivisionError):
#         print('程序异常：0不能作为除数！')
#     elif isinstance(e, ValueError):
#         print('程序异常：您输入的必须是数字！')
#     else:
#         print(f'程序异常：{e}')
# else:
#     print('挺好的，try中的代码没有任何异常！')
# finally:
#     print('无论有没有异常，我的计算都结束了！')
# print('*******我是后续的其它逻辑1*******')
# print('*******我是后续的其它逻辑2*******')
```

### 03_手动抛出异常

```python
# 当程序遇到不符合预期情况时，可以使用 raise 语句手动触发（抛出）异常。
# print('欢迎使用年龄判断系统')
# try:
#     age = int(input('请输入你的年龄：'))
#     if 18 <= age <= 120:
#         print('成年')
#     elif 0 <= age < 18:
#         print('未成年')
#     else:
#         # print('输入的年龄有误！（年龄应该为0~120的整数）')
#         raise ValueError('年龄应该为0~120的整数')
# except Exception as e:
#     print(f'程序异常：{e}')

# raise NameError('ertghfgfggvb')
raise KeyboardInterrupt('ertghfgfggvb')
```

### 04_异常传递机制

```python
# 异常的传递机制：
# 1.如果异常没有被当前代码块所捕获处理，那该异常就会沿着调用链，逐层传递给其调用者。
# 2.如果所有调用者，都没有捕获该异常，那最终程序将因【未处理异常】而意外终止。
def test1():
    print('******test1开始******')
    result = '100' + 100
    print('******test1结束******')

def test2():
    print('******test2开始******')
    try:
        test1()
    except Exception as e:
        print(f'程序异常：{e}')
    print('******test2结束******')

def test3():
    print('******test3开始******')
    test2()
    print('******test3结束******')

test3()
```

### 05_自定义异常类

```python
# 自定义异常类：
# 1.由开发人员自己定义一个异常类，用来表示代码中“更具体、更有业务含义”的异常。
# 2.具体规则：定义一个类（类名通常以 Error 结尾），继承 Exception 类或它的子类。

class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__('【校名异常】' + msg)

def check_school_name(name):
    if len(name) > 10:
        raise SchoolNameError('学校名过长')
    else:
        print('学校名是合法的')

try:
    check_school_name('atguiguuuuuuuuuuuuuuu')
except SchoolNameError as e:
    print(f'程序异常：{e}')
```

---

## 第10章 · 模块与包

### 01_模块

```python
# 模块概述：
# 1.在 Python 中，一个.py文件就是一个模块（Module）。
# 2.模块中可以包含：变量、函数、类、等很多内容。
# 3.通常把能够实现某一特定功能的代码，集中放在一个模块中（模块就类似于一个工具箱）。
# 4.模块可以提高代码的可维护性 与 可复用性，还可以避免命名冲突。

# 模块的分类：
# Python 中的模块分为三类，分别是：标准库模块、自定义模块、第三方模块。

# 模块命名注意点：
#  1.要符合标识符命名规则
#  2.模块名（.py文件名）区分大小写
#  3.不要与标准库模块同名（一旦同名，Python会优先引入标准库模块）


# 常见的模块导入方式：
# 1️⃣import 模块名
# import order
# import pay
#
# print(order.max_order_amount)
# order.create_order()
# order.cancel_order()
# order.show_info()
# print('*' * 10)
# print(pay.timeout)
# pay.wechat_pay()
# pay.ali_pay()
# pay.show_info()


# 2️⃣import 模块名 as 别名
# import order as dd
# import pay as zf
#
# print(dd.max_order_amount)
# dd.create_order()
# dd.cancel_order()
# dd.show_info()
# print('*' * 10)
# print(zf.timeout)
# zf.wechat_pay()
# zf.ali_pay()
# zf.show_info()

# 3️⃣from 模块名 import 具体内容1, 具体内容2, ......
# from order import max_order_amount, show_info
# from pay import wechat_pay, ali_pay
#
# print(max_order_amount)
# show_info()
# wechat_pay()
# ali_pay()


# 4️⃣from 模块名 import 具体内容1 as 别名1, 具体内容2 as 别名2, ......
# from order import max_order_amount as max_amt, show_info as show1
# from pay import timeout as tm, show_info as show2
# print(max_amt)
# print(tm)
# show1()
# show2()


# 5️⃣from 模块名 import *
# from order import *
# from pay import *
#
# max_order_amount = 10
#
# print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()

# 关于__all__：
# ● 在 Python 模块中，可通过 __all__ 来控制【from 模块 import *】能导入哪些内容。
# ● __all__ 的值可以是：列表、元组。
#
#
# 关于__name__:
# ● __name__是每个 Python 模块（.py文件）都拥有的一个内置变量。
# ● 它的具体值取决于模块的运行方式：
#       1.作为主程序直接运行，__name__ 的值是 __main__
#       2.作为模块被导入到其他程序中运行，__name__的模块的文件名（不带.py）。

import pay
```

### 02_标准库模块

```python
# 1.Python 中的模块分为三类，分别是：标准库模块、自定义模块、第三方模块。
# 2.标准库模块：随着 Python 一起安装在我们电脑上的那些模块。
# 3.有一些标准库模块是用C语言实现的，这些用C语言实现的模块，又称：【内置模块】。


import copy     # 拷贝对象（浅拷贝、深拷贝）
import os       # 操作系统相关操作（文件、文件夹、路径系统层面的操作）
import random   # 随机数相关（生成随机数、随机选择、洗牌）
# print(copy.__file__)
# print(os.__file__)
# print(random.__file__)

# 如下的这些模块，属于内置模块（无法看到具体实现，也没有__file__属性）
import time     # 时间相关操作（获取时间、延时、格式化时间等。）
import math     # 数学相关（开平方、取绝对值 等等）
import sys      # Python 解释器相关操作

# 创建一个文件夹
# os.mkdir('demo')

# 随机选择一个人
# names = ['张三', '李四', '王五', '李华']
# print(random.choice(names))

# 洗牌
# names = ['张三', '李四', '王五', '李华']
# random.shuffle(names)
# print(names)

# 休眠
# time.sleep(2)
# print('ok')

# 获取当前时间
# print(time.strftime('%H:%M:%S'))
# print(time.strftime('%p %I:%M:%S'))

# 开平方
# print(math.sqrt(4))

# 取绝对值
# print(math.fabs(-11.2))

# 获取Python解释器的版本
# print(sys.version)
```

### 03_包

```python
# 包概述：
# 1.在 Python 中，【包含 __init__.py 的文件夹】就是一个包（Package）。
# 2.我们通常会把【某个特定功能相关的所有模块】放入一个包中。
# 3.使用包可以进一步提升代码的：可维护性、可复用性，便于管理大型项目。

# 包与模块的关系：
# 1.一个模块就是一个.py文件 ，包是用来“管理模块”的目录(文件夹)。
# 2.一个包中可以有多个模块，也可以有多个子包。

# 包的分类：
# Python 中的包分为三类，分别是：标准库包、自定义包、第三方包。

# 包命名注意点：
# 1.要符合标识符命名规范。
# 2.包名区分大小写（建议全部使用小写字母）
# 3.不要与标准库包同名。

# 1️⃣import 包名.模块名
# import trade.order
# import trade.pay
#
# trade.order.create_order()
# trade.pay.wechat_pay()

# 2️⃣import 包名.模块名 as 别名
# import trade.order as dd
# import trade.pay as zf
#
# dd.create_order()
# zf.wechat_pay()


# 3️⃣from 包名.模块名 import 具体内容1, 具体内容2, ......
# from trade.order import max_order_amount, create_order
# from trade.pay import timeout, wechat_pay
#
# print(max_order_amount)
# print(timeout)
# create_order()
# wechat_pay()


# 4️⃣from 包名.模块名 import 具体内容1 as 别名1, 具体内容2 as 别名2, ......
# from trade.order import max_order_amount as max_amt, create_order
# from trade.pay import timeout, wechat_pay as w_pay
#
# print(max_amt)
# print(timeout)
# create_order()
# w_pay()


# 5️⃣from 包名.模块名 import *
# from trade.order import *
# from trade.pay import *
#
# # print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()

# 6️⃣from 包名 import 模块名
# from trade import order, pay
# order.create_order()
# pay.wechat_pay()

# 7️⃣from 包名 import 模块名 as 别名
# from trade import order as dd, pay as p
# dd.create_order()
# p.wechat_pay()

# 关于 __init__.py 文件：
# 1.__init__.py 是包的初始化文件，在包被导入时，__init__.py 会被自动调用
# 2.__init__.py 中可以编写一些包的初始化逻辑
# 3.__init__.py 中所定义的内容，会被【from 包名 import *】形式全部引入
# 4.__init__.py 中也可以使用 __all__ 来控制包中的哪些模块可以被【from 包名 import *】引入


# 8️⃣from 包名 import *
# from trade import *
# # print(a)
# # print(b)
# print(order.max_order_amount)
# order.create_order()
# print(pay.timeout)
# pay.wechat_pay()

# 9️⃣import 包名
# import trade
# print(trade.a)
# print(trade.b)
# trade.order.create_order()
# trade.pay.wechat_pay()

# 测试一下引入子包
# from trade.hello.h1 import say_hello
# say_hello()

# 演示一下标准库包的使用
from collections import Counter
names = ['张三', '李四', '王五', '李华', '张三', '李四', '张三', '王五']
result = Counter(names)
print(result)
```

### order

```python
# 订单最大金额
max_order_amount = 1000000

# 创建订单
def create_order():
    print('订单创建成功！')

# 关闭订单
def cancel_order():
    print('订单关闭成功！')

# 提示函数
def show_info():
    print('我是来自【订单】模块的提示！')

# __all__ = ('cancel_order', 'show_info')
```

### pay

```python
# 支付超时时间
timeout = 1800

# 微信支付
def wechat_pay():
    print('我是微信支付！')

# 支付宝支付
def ali_pay():
    print('我是支付宝支付！')

# 提示函数
def show_info():
    print('我是来自【支付】模块的提示！')

# print('我是pay模块打印的内容', __name__)

# 测试代码
if __name__ == '__main__':
    wechat_pay()
    ali_pay()
```

### trade/__init__

```python
print('我是trade包的初始化内容1')
print('我是trade包的初始化内容2')
print('我是trade包的初始化内容3')
a = 100
b = 200
import order
import pay

__all__ = ['order', 'pay']
```

### trade/order

```python
# 订单最大金额
max_order_amount = 1000000

# 创建订单
def create_order():
    print('订单创建成功！')

# 关闭订单
def cancel_order():
    print('订单关闭成功！')

# 提示函数
def show_info():
    print('我是来自【订单】模块的提示！')

# __all__ = ('create_order', 'cancel_order')
```

### trade/pay

```python
# 支付超时时间
timeout = 1800

# 微信支付
def wechat_pay():
    print('我是微信支付！')

# 支付宝支付
def ali_pay():
    print('我是支付宝支付！')

# 提示函数
def show_info():
    print('我是来自【支付】模块的提示！')

# print('我是pay模块打印的内容', __name__)

# 测试代码
# if __name__ == '__main__':
#     wechat_pay()
#     ali_pay()
```

### order

```python
# 订单最大金额
max_order_amount = 1000000

# 创建订单
def create_order():
    print('订单创建成功！')

# 关闭订单
def cancel_order():
    print('订单关闭成功！')

# 提示函数
def show_info():
    print('我是来自【订单】模块的提示！')

# __all__ = ('cancel_order', 'show_info')
```

### pay

```python
# 支付超时时间
timeout = 1800

# 微信支付
def wechat_pay():
    print('我是微信支付！')

# 支付宝支付
def ali_pay():
    print('我是支付宝支付！')

# 提示函数
def show_info():
    print('我是来自【支付】模块的提示！')

# print('我是pay模块打印的内容', __name__)

# 测试代码
if __name__ == '__main__':
    wechat_pay()
    ali_pay()
```

---

## 第11章 · 迭代器与生成器

### 01_初识迭代器

```python
# 知识点1：能被 for 循环遍历的对象，被称为：可迭代对象(iterable)
# region
# names = ['张三', '李四', '王五']
# citys = ('北京', '上海', '深圳')
# msg = 'hello'
# age = 10
# def test():
#     pass
#
# for item in test:
#     print(item)
# endregion

# 知识点2：可迭代对象(iterable) 能调用到 __iter__ 方法。
# region
# names = ['张三', '李四', '王五']
# citys = ('北京', '上海', '深圳')
# msg = 'hello'
# age = 10
# def test():
#     pass

# names.__iter__()
# citys.__iter__()
# msg.__iter__()

# print(hasattr(names, '__iter__'))
# print(hasattr(citys, '__iter__'))
# print(hasattr(msg, '__iter__'))
# print(hasattr(age, '__iter__'))
# print(hasattr(test, '__iter__'))
# endregion

# 知识点3：调用 __iter__ 方法会得到：迭代器(iterator)
# 备注1：__iter__ 是一个魔法方法，当调用 iter 函数时，__iter__ 会自动调用。
# 备注2：可迭代对象.__iter__()  等价于  iter(可迭代对象)。
# 备注3：如果 iter(obj) 能得到一个迭代器(iterator)，那 obj 就是可迭代对象。
# region
# names = ['张三', '李四', '王五']
# citys = ('北京', '上海', '深圳')
# msg = 'hello'

# print(names.__iter__())
# print(citys.__iter__())
# print(msg.__iter__())

# print(iter(names))
# print(iter(citys))
# print(iter(msg))
# endregion

# 知识点4：迭代器(iterator)拥有 __next__ 方法，每次调用都会根据当前的状态，返回下一个元素。
# 备注1：迭代器.__next__()  等价于  next(迭代器)。
# 备注2：当所有元素全都取出后，若继续调用 __next__ 方法，Python会抛出 StopIteration 异常。
# region
# names = ['张三', '李四', '王五']
# it = iter(names)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# endregion

# for循环背后的工作逻辑
# region
# names = ['张三', '李四', '王五']
#
# # 编写for循环遍历names列表
# # for item in names:
# #     print(item)
#
# # for循环背后的逻辑
# # 1️⃣调用【可迭代对象的__iter__方法】获取到一个迭代器(iterator)
# it = iter(names)
# # 2️⃣开启一个无限循环
# while True:
#     try:
#         # 3️⃣调用__next__方法，获取下一个元素
#         item = next(it)
#         print(item)
#     except StopIteration:
#         # 4️⃣捕获 StopIteration 异常，随后结束循环
#         break
# endregion

# 知识点5：迭代器(iterator)也拥有 __iter__ 方法，并且其返回值是迭代器自身。
# 这么设计的原因如下：让 for 循环也能遍历迭代器（即：为了让 iter(迭代器) 不出错）。
# region
# names = ['张三', '李四', '王五']

# it = iter(names)
# print(it)
#
# result = iter(it)
# print(result)
#
# x = iter(result)
# print(x)

# it = iter(names)
# for item in it:
#     print(item)
# endregion

# 知识点6：迭代器协议
#   1.能被 iter() 接受
#   2.能被 next() 一步一步取值
```

### 02_手写迭代器

```python
# 迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）。
# region
# names = ['张三', '李四', '王五']
# it1 = iter(names)
# it2 = iter(names)

# print(it1)
# print(it2)

# print(next(it1))
# print(next(it1))
# print(next(it1))

# print(next(it2))
# print(next(it2))
# print(next(it2))

# for item in it1:
#     print(item)
#
# for item in it2:
#     print(item)
# endregion

# 需求：让for循环可以遍历Person的实例对象
# 实现方式1️⃣
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#
#     def __iter__(self):
#         return PersonIterator(self)
#
# class PersonIterator:
#     def __init__(self, p):
#         # 将外部传进来的数据保存好
#         self.p = p
#         # 设置迭代器的初始化状态（指针位置）
#         self.index = 0
#         # 配置好要遍历的内容
#         self.attrs = [p.name, p.age, p.gender, p.address]
#
#     # 迭代器的__iter__方法会返回迭代器自身
#     def __iter__(self):
#         return self
#
#     # 每次调用__next__方法，会根据当前的状态，返回下一个元素
#     def __next__(self):
#         # 如果指针的位置超出范围，那就抛出StopIteration异常
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.attrs[self.index]
#         # 更新迭代器状态（指针位置）
#         self.index += 1
#         # 返回value
#         return value
#
# # 目标：
# p1 = Person('张三', 18, '男', '北京昌平')
#
# for item in p1:
#     print(item)
#
# for item in p1:
#     print(item)
# endregion

# 实现方式2️⃣
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         # 设置迭代器的初始化状态（指针位置）
#         self.__index = 0
#         # 配置好要遍历的内容
#         self.__attrs = [name, age, gender, address]
#
#     def __iter__(self):
#         self.__index = 0
#         return self
#
#     def __next__(self):
#         # 如果指针的位置超出范围，那就抛出StopIteration异常
#         if self.__index >= len(self.__attrs):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.__attrs[self.__index]
#         # 更新迭代器状态（指针位置）
#         self.__index += 1
#         # 返回value
#         return value
#
# # 目标：
# # 下面的p1既是可迭代对象，又是迭代器
# p1 = Person('张三', 18, '男', '北京昌平')
#
# for item in p1:
#     print(item)
#
# for item in p1:
#     print(item)
# endregion

# 进阶：迭代器玩的就是__next__
from cn2an import an2cn
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置迭代器的初始化状态（指针位置）
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.__index >= len(self.__attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attrs[self.__index]
        # 将字符串转为大写
        if isinstance(value, str):
            value = value.upper()
        # 将数字转为汉语形式
        if isinstance(value, int):
            value = an2cn(value)
        # 更新迭代器状态（指针位置）
        self.__index += 1
        # 返回value
        return value

# 目标：
# 下面的p1既是可迭代对象，又是迭代器
p1 = Person('zhangsan', 18, '男', '北京昌平')

for item in p1:
    print(item)
```

### 03_迭代器的优势

```python
# 1.迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
# 2.当数据量很大，不确定要用多少结果时，推荐使用迭代器。

import tracemalloc

# 使用迭代器实现
class Fibo:
    def __init__(self, total):
        # 要生成多少个数
        self.total = total
        # 当前生成到第几个了（计数器，指针）
        self.index = 0
        # 初始的两个值
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 当生成足够数量后，抛出StopIteration异常
        if self.index >= self.total:
            raise StopIteration
        # 前两项都是1
        if self.index < 2:
            value = 1
        else:
            # 新的结果等于前两项的和
            value = self.pre + self.cur
            # 更新一下pre和cur
            self.pre = self.cur
            self.cur = value
        # 计数器+1
        self.index += 1
        # 返回value
        return value


# 不用迭代器实现
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for i in range(2, total):
        nums.append(nums[-1] + nums[-2])
    return  nums

# 看内存占用
# tracemalloc.start()
# f1 = Fibo(0)
# m = tracemalloc.get_traced_memory()[1]
# print(f'内存占用是：{m / 1024 / 1024}MB')

# tracemalloc.start()
# f1 = fibo(100000)
# m = tracemalloc.get_traced_memory()[1]
# print(f'内存占用是：{m / 1024 / 1024}MB')

# f1 = Fibo(100000)
# for n in f1:
#     if n > 100:
#         break
#     print(n)
```

### 04_生成器

```python
# 1️⃣生成器：
#   1.生成器函数：函数体中如果出现了 yield 关键字，那该函数是『生成器函数』。
#   2.生成器对象：调用『生成器函数』时，其函数体不会立刻执行，而是返回一个『生成器对象』。
#   备注：不管能否执行到 yield 所在的位置，只要函数中有 yield 关键字，那该函数，就是『生成器函数』。
# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     yield
#     a = 200
#     print(a)
#
# d = demo()
# print(d)
# endregion

# 2️⃣写在『生成器函数』中的代码，需要通过『生成器对象』来执行：
#   1.调用『生成器对象』的 __next__ 方法，会让『生成器函数』中的代码开始执行。
#   2.当『生成器函数』中的代码开始执行后，遇到 yield 会“暂停”执行，并且其内部会记录“暂停”的位置。
#   3.后续调用 __next__ 方法时，都会从上一次“暂停”的位置，继续运行，直到再次遇到 yield。
#   4.遇到 return 会抛出 StopIteration 异常，并将 return 后面的表达式，作为异常信息。
#   5.yield 后面所写的表达式，会作为本次 __next__ 方法的返回值。
# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     yield '我是第1个yield所返回的数据'
#     a = 200
#     print(a)
#     yield '我是第2个yield所返回的数据'
#     b = 300
#     print(b)
#     return '尚硅谷'
#
# d = demo()
# r1 = next(d)
# print(r1)
# r2 = next(d)
# print(r2)
# try:
#     next(d)
# except StopIteration as e:
#     print(e)
# endregion

# 3️⃣生成器对象是一种特殊的迭代器（本质是通过 yield 自动实现了迭代器协议）。
# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     yield '我是第1个yield所返回的数据'
#     a = 200
#     print(a)
#     yield '我是第2个yield所返回的数据'
#     b = 300
#     print(b)
#     return '尚硅谷'
#
# d = demo()
# 验证：生成器对象d，和迭代器一样，也拥有：__iter__  和 __next__ 方法
# print(hasattr(d, '__iter__'))
# print(hasattr(d, '__next__'))

# 验证：生成器对象的__iter__方法，和迭代器一样，返回的也是自身
# result = iter(d)
# print(result == d)

# for循环遍历生成器
# for item in d:
#     print(item)

# for循环背后的逻辑
# gen = iter(d)
# while True:
#     try:
#         value = next(gen)
#         print(value)
#     except StopIteration:
#         break
# endregion

# 4️⃣yield 也能写在循环里
# region
# def create_car(total):
#     for index in range(1, total + 1):
#         yield f'我是第{index}台车'

# cars是生成器对象
# cars = create_car(5)

# 调用一次cars的__next__方法，就会得到一台车
# c1 = next(cars)
# print(c1)
# c2 = next(cars)
# print(c2)
# c3 = next(cars)
# print(c3)
# c4 = next(cars)
# print(c4)
# c5 = next(cars)
# print(c5)

# for car in cars:
#     print(car)
# endregion

# 5️⃣yield from 能把一个『可迭代对象』里的东西依次 yield 出去。(替代：for + yield)
# region
# def demo():
#     nums = [10, 20, 30, 40]
#     yield from nums

# d = demo()
# r1 = next(d)
# print(r1)
# r2 = next(d)
# print(r2)
# r3 = next(d)
# print(r3)
# r4 = next(d)
# print(r4)

# for item in d:
#     print(item)
# endregion

# 6️⃣使用：生成器.send(值) 可以让生成器继续执行的同时，给上一次 yield 传值。
# 备注1：next 只能取值，send 既能取值，也能送值
# 备注2：第一次启动生成器，不能传值！
# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     a = yield '我是第1个yield所返回的数据'
#     print(a)
#     b = yield '我是第2个yield所返回的数据'
#     print(b)
#     return '尚硅谷'
#
# d = demo()
# r1 = d.send(None)
# print(r1)
# r2 = d.send(666)
# print(r2)
# try:
#     d.send(888)
# except StopIteration as e:
#     print(e)
# endregion

# 用生成器实现遍历Person类的实例对象
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__attr = [name, age, gender, address]
#
#     def __iter__(self):
#         # yield self.name
#         # yield self.age
#         # yield self.gender
#         # yield self.address
#         yield from self.__attr
#
# p1 = Person('张三', 18, '男', '北京昌平')
# # 目标：
# for attr in p1:
#     print(attr)
# endregion

# 用生成器实现斐波那契数列
# region
# def fibo(total):
#     pre = 1
#     cur = 1
#
#     for index in range(total):
#         if index < 2:
#             yield 1
#         else:
#             value = pre + cur
#             pre = cur
#             cur = value
#             yield value
#
# f1 = fibo(10)

# for item in f1:
#     print(item)

# 无论是迭代器，还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容（注意：容易挤爆内存）
# result = set(f1)
# print(result)
# endregion

# 生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方式。
# 语法格式：(表达式 for 变量 in 可迭代对象)
# 什么时候适合用生成器表达式？———— 当“每个结果，只依赖当前这一个元素”时。

# nums = [10, 20, 30, 40]

# 列表推导式
# result1 = [n * 2 for n in nums]
# print(result1)

# 生成器表达式
# result2 = (n * 2 for n in nums)
# for item in result2:
#     print(item)
```

---

## 第12章 · 文件操作

### 01_前序知识

```python
# 文件的分类：1.纯文本文件、2.二进制文件

# 纯文本文件：
#   1.读取和存储时，要遵循某种『字符编码』规范（如：UTF-8 等）进行编码和解码，最终以『二进制』的形式存储。
#   2.『纯文本文件』最终会呈现为：可以直接阅读的文本信息。
#   3.常见的『纯文本文件』有：.txt  .py  .md  .html 等。


# 二进制文件：
#   1.读取和存储时，不涉及字符编码，会按照某种『文件格式规范』把内容转为『二进制』数据进行存储。
#   2.二进制文件需要由『能够识别其格式的软件』进行解析，最终的呈现形式多种多样（音频、视频、图像、幻灯片等）。
#   3.常见的二进制文件有：.mp3  .mp4  .doc  .ppt  .jpg  .png 等。


# 绝对路径 vs 相对路径：
#   1.绝对路径：从文件系统的『根目录』开始，完整描述文件或目录所在的位置。
#   2.相对路径：以当前『工作目录』为参照，描述目标文件或目录相对于它的位置。
```

### 02_读取文件

```python
# Python中操作文件的标准流程：
#   1.创建『文件对象』
#   2.操作文件（读取、写入 等）
#   3.关闭文件

# 文件操作的核心 ———— open函数：它可以打开或创建文件，且支持多种操作模式，返回值是『文件对象』。
# open 函数最常用的三个参数如下：
#   1.file：要操作的文件路径
#   2.mode：文件的打开模式
#       r ：读取（默认值）
#       w ：写入，并先截断文件
#       x ：排它性创建，如果文件已存在，则创建失败
#       a ：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#       b ：二进制模式
#       t ：文本模式（默认值）
#       + ：打开用于更新（读取与写入）
#   3.encoding：字符编码


# 读取操作1️⃣：使用『文件对象』的 read 方法，读取文件中的内容。
# read 方法说明：
#   1.read(size)中的 size 是可选参数。
#      🔸若不传递 size 参数，表示：读取文件中所有的内容（注意内存占用！）。
#      🔸若传递了 size 参数，表示：读取文件中指定个数的字符，或指定大小的字节。
#   2.read 会从上一次 read 的位置继续读取（指针思想），若到达文件末尾后继续读取，将返回空字符串。
# region
# 第一步：创建『文件对象』
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# file = open('a.txt', 'rt', encoding='utf-8')
# file = open('D:/test/atguigu.txt', 'rt', encoding='utf-8')
# file = open('D:/test/girl.jpg', 'rb')

# 第二步：操作文件（读取）
# 多次调用read去逐步读取文件
# r1 = file.read(2)
# r2 = file.read(3)
# r3 = file.read(4)
# r4 = file.read()
# print(r1, end='')
# print(r2, end='')
# print(r3, end='')
# print(r4, end='')

# 用循环配合多次read（对内存友好）
# while True:
#     result = file.read(10)
#     if result == '':
#         break
#     print(result, end='')

# 第三步：关闭文件
# file.close()
# endregion


# 读取操作2️⃣：使用文件对象的 readline 方法，读取文件中的一行。
# readline 方法说明：
#   1.readline(size) 中的 size 是可选参数。
#      🔸若不传递 size 参数，表示：读取当前这一行所有的内容。
#      🔸若传递了 size 参数，表示：表示读取当前行时，最多能读取的字符数，或字节数（size不是行数）。
#   2.readline 方法，也是从上一次位置继续读取，若到达文件末尾后继续读取，也是返回空字符串。
# region
# 第一步：创建『文件对象』
# file = open('a.txt', 'rt', encoding='utf-8')

# 第二步：操作文件（读取）
# 依次调用readline逐行读取
# r1 = file.readline()
# r2 = file.readline()
# r3 = file.readline()
# r4 = file.readline()
# print(r1.strip())
# print(r2.strip())
# print(r3.strip())
# print(r4.strip())

# 通过循环配合readline逐行读取
# while True:
#     line = file.readline()
#     if line == '':
#         break
#     # print(line.strip())
#     print(line, end='')

# 第三步：关闭文件
# file.close()
# endregion


# 读取操作3️⃣：使用 for 循环直接遍历文件对象
# region
# 第一步：创建『文件对象』
# file = open('a.txt', 'rt', encoding='utf-8')

# 第二步：操作文件（读取）
# for line in file:
#     print(line, end='')

# 第三步：关闭文件
# file.close()
# endregion


# 读取操作4️⃣：使用文件对象的 readlines 方法，一次性按“行”读完，返回一个列表。
# readlines 方法说明：
#   1.readlines(hint) 中的 hint 是可选参数。
#       🔸若不传递 hint 参数，表示：读取当前文件的所有行。
#       🔸若传递了 hint 参数，表示：期望读取的【字符个数 或 字节数的上限】（hint不是行数）。
#   2.注意：由于 readlines 是一次性读取文件的所有内容，所以不适合读取体积较大的文件。
# region
# 第一步：创建『文件对象』
# file = open('a.txt', 'rt', encoding='utf-8')

# 第二步：操作文件（读取）
# result = file.readlines()
# print(result)

# 第三步：关闭文件
# file.close()
# endregion


# ⭐️最佳实践：使用 with 上下文管理器，结合for循环遍历，逐行读取文件。
# with open('a.txt', 'rt', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
```

### 03_关于with

```python
# 1.Python 中的 with 主要用于管理程序中“需要成对出现的操作”，例如：
#    🔸上锁 / 解锁
#    🔸打开 / 关闭
#    🔸借用 / 归还

# 2.最终目标：编码者只管做具体的事，“进入”和“离开”的事，让 Python 自动处理。

# 3.语法格式如下：
#   with 能得到一个上下文管理器的表达式 as 变量:
#       具体的事1
#       具体的事2
#       具体的事3

# 4.上下文管理器协议：
#    (1). __enter__ 方法：with 中的代码执行【之前】调用，其返回值会赋值给 as 后的变量。
#    (2). __exit__  方法：with 中的代码执行【结束后】调用（无论是 with 中否出现异常都会调用）。

# 定义一个 Person 类，让其实例对象遵循：上下文管理器协议
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'我叫{self.name}，年龄是{self.age}')

    def __enter__(self):
        print('-----我是进入的逻辑-----')
        return self

    # 当 with 中的代码发生异常时，__exit__ 方法的返回值规则如下：
    #   🔸返回“真”：表示异常【已经】被处理，异常【不会】被继续抛出。
    #   🔸返回“假”：表示异常【没有】被处理，异常【会】被继续抛出。
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('-----我是离开的逻辑-----')
        # exc_type  : 异常类型
        # exc_val   : 异常对象
        # exc_tb    : 异常追踪信息
        if exc_type:
            print(f'异常类型：{exc_type}')
            print(f'异常对象：{exc_val}')
            print(f'异常追踪信息：{exc_tb}')
        return True

# 1.计算 with 后面的表达式，得到一个『上下文管理器』。
# 2.调用『上下文管理器』的 __enter__() 方法，并将其返回值赋给 as 后面的变量。
# 3.执行 with 所管理的代码。
# 4.无论代 with 中的代码，是正常结束，还是发生异常，都会自动调用『上下文管理器』的 __exit__ 方法。

with Person('张三', 18) as p1:
    p1.speak()
    # p1.study()
    print(666)
```

### 04_写入文件

```python
# open 函数最常用的三个参数如下：
#   1.file：要操作的文件路径
#   2.mode：文件的打开模式
#       r ：读取（默认值）
#       w ：写入，并先截断文件
#       x ：排它性创建，如果文件已存在，则创建失败
#       a ：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#       b ：二进制模式
#       t ：文本模式（默认值）
#       + ：打开用于更新（读取与写入）
#   3.encoding：字符编码
import time

# 测试 w 模式
# with open('b.txt', 'wt', encoding='utf-8') as file:
#     file.write('你好')

# 测试 x 模式
# with open('demo.txt', 'xt', encoding='utf-8') as file:
#     file.write('你好')

# 测试 a 模式
# with open('a.txt', 'at', encoding='utf-8') as file:
#     file.write('你好')

# 在 Python 中文件写入时，并不是每写一次就立刻落盘，而是：先写到“缓冲区”里。
# 文件对象的 flush 方法：把缓冲区中的数据，立刻写入到文件中。
# with open('demo.txt', 'at', encoding='utf-8') as file:
#     file.write('你好1')
#     file.write('你好2')
#     file.flush()
#     time.sleep(10000)
#     file.write('你好3')
#     file.write('你好4')

# 测试 rt+
# with open('a.txt', 'rt+', encoding='utf-8') as file:
#     # seek(offset, whence)方法：用于改变文件对象指针的位置，参数说明如下：
#     #   offset：偏移量，要移动多少距离
#     #   whence：参考点，从哪里开始计算偏移，有三种取值：
#     #       0：从文件开头计算（默认值）
#     #       1：从当前位置计算
#     #       2：从文件末尾计算
#     #  注意：在文本模式下，不要随意去定位中文字符位置，否则可能破坏文件编码。
#     file.seek(0, 0)
#     file.write('你好')

# 测试 wt+
# with open('a.txt', 'wt+', encoding='utf-8') as file:
#     file.write('你好')
#     file.seek(0, 0)
#     result = file.read()
#     print(result)

# 测试 xt+
# with open('demo3.txt', 'xt+', encoding='utf-8') as file:
#     file.write('你好')
#     file.seek(0, 0)
#     result = file.read()
#     print(result)

# 测试 at+
# with open('a.txt', 'at+', encoding='utf-8') as file:
#     file.write('你好')
#     file.seek(0, 0)
#     result = file.read()
#     print(result)
```

### 05_目录操作

```python
import os
import shutil

# 1️⃣os.mkdir(path)：创建“单级”目录（如果目录已经存在，则会抛出异常）
# os.mkdir('D:/demo')

# 2️⃣os.makedirs(path)：创建“多级”目录（如果路径中的所有目录都已经存在，则会抛出异常）
# os.makedirs('D:/demo/aa/bb')

# 3️⃣os.rmdir(path)：删除空目录（如果目录不存在，或目录非空，都会抛出异常）
# os.rmdir('D:/demo/aa/bb')

# 4️⃣os.removedirs(path)：递归删除空目录，在成功删除末尾一级目录后，会“向上”尝试把父级目录也删除（直到父目录不是空目录）
# os.removedirs('D:/demo/aa/bb')

# 5️⃣os.path.exists(path)：判断路径是否存在（文件/目录都算）
# result = os.path.exists('D:/demo/aa/bb')
# print(result)

# 6️⃣os.path.isdir(path)：用于判断路径，具体规则如下：
#   1.路径不存在 ==================> 返回 False
#   2.路径存在，但指向的是文件 =====> 返回 False
#   3.路径存在，并且是目录 =======> 返回 True
# result = os.path.isdir('D:/demo/aa/bb')
# print(result)

# 7️⃣os.path.isfile(path)：判断是否为文件
# result = os.path.isfile('D:/demo/aa/bb')
# print(result)

# 8️⃣os.scandir(path)：扫描指定目录
# result = os.scandir('D:/demo')
# for item in result:
#     print('目录' if item.is_dir() else '文件', item.name)

# 9️⃣os.walk(path)：按层级，递归地遍历指定目录下，所有的子目录和文件
# result = os.walk('D:/demo')
# for item in result:
#     print(item)

# ⚠️危险操作：删除有内容的目录
# shutil.rmtree('D:/demo')
```

### 06_小练习

```python
# 练习1：将一个二进制文件复制到指定位置。
# region
# import os
# # 源文件
# source = 'music.mp3'
# # 目标目录
# target = 'D:/media'
#
# # 如果目标目录不存在，那就去创建
# if not os.path.isdir(target):
#     os.makedirs(target)
#
# with open(source, 'rb') as f1, open(target + '/' + 'my_music.mp3', 'wb') as f2:
#     while True:
#         # 每次只读取1KB
#         data = f1.read(1024)
#         # 如果文件读取完毕了，就跳出循环
#         if not data:
#             break
#         # 向目标文件中写入数据
#         f2.write(data)
#     print('复制完毕')
# endregion

# 练习2：日志记录。
#   1.用户输入用户名和密码后，程序进行校验：
#   2.用户名不存在，提示“用户名未注册”，并记录日志。
#   3.用户名存在，但密码错误，提示“密码错误”，并记录日志。
#   4.用户名和密码均正确，提示“登录成功”，并记录日志。

import time
# 准备一些用户
users = {
    '张三': '123456',
    '李四': '888888',
    '王五': 'abc123'
}

# 提示输入信息
username = input('请输入用户名：')
password = input('请输入密码：')

# 获取当前的时间
now = time.strftime('%Y-%m-%d %H:%M:%S')

# 如果用户名不在users中
if username not in users:
    print('用户名未注册')
    with open('log.txt', 'at', encoding='utf-8') as file:
        file.write(f'{now}  {username}  登录失败（用户未注册）\n')

# 如果密码不正确
elif users[username] != password:
    print('密码不正确')
    with open('log.txt', 'at', encoding='utf-8') as file:
        file.write(f'{now}  {username}  密码错误 \n')

# 登录成功
else:
    print('登录成功！')
    with open('log.txt', 'at', encoding='utf-8') as file:
        file.write(f'{now}  {username}  登录成功 \n')
```

---

## 第13章 · 多进程与多线程

### 01_一些概念

```python
# 一、并发 vs 并行：
# 	1.并发：
# 		🔸概念：在一段时间内，当CPU面对多个任务时，会将每个任务交替着执行一段时间。
# 		🔸特点：
# 			(1).对于某个瞬间，CPU实际上只在执行一个任务。
# 			(2).CPU通过高频切换不同的任务，让每个任务都能得到推进，仿佛多个任务在“同时执行”。
# 	2.并行：
# 		🔸概念：并行依赖于多个CPU，或多核心的CPU，在同一时刻，每个核心都在执行不同的任务。
# 		🔸特点：
# 			(1).对于某个瞬间，每个CPU（或每个核心）都在执行不同的任务。
# 			(2).通过多个CPU（或多个核心）同时工作的方式，让多个任务真的在同时执行。

#   说明：在现代操作系统中，并发与并行通常都是同时存在的。
import os
print(os.cpu_count())

# 二、同步 vs 异步：
# 	1.同步(sync)：
# 		🔸概念：发起一个任务之后，需要等该任务完成后，才能继续执行后续任务。
# 		🔸表现：当前执行流会被『阻塞』。
# 	2.异步(async)：
# 		🔸概念：发起一个任务之后，不必等该任务完成，就可以继续执行其他任务。
# 		   备注：虽然不必等待任务完成，但任务完成后，仍然可以通过特定方式获取结果。
# 		🔸表现：当前执行流不会被『阻塞』。

# 三、注意区分概念：
# 		并发 / 并行：描述的是任务如何被执行，即：多个任务在执行时，CPU要如何处理。
# 		同步 / 异步：描述的是任务如何被组织和等待，即：要不要等当前发起的任务执行完，再进行下一个任务。
#
# 		⚠️注意点：CPU 的核心数和执行速度，不会改变任务之间的逻辑依赖关系！例如：
# 		一旦任务1、任务2、任务3 之间被设计为同步关系，那么：即便 CPU 切换任务的速度再快，核心数量再多，也不会在【任务1】没完成的情况下去启动【任务2】

# 四、进程与线程
# 	1.进程：
# 		(1).一个正在运行的程序或软件，背后就对应着一个或多个进程。
# 		(2).进程是操作系统进行资源分配的基本单位。
# 		(3).每个进程都有自己独立的一块内存空间。
#
# 	2.线程：
# 		(1).线程是进程内部的执行单元（一个进程中可以有多个线程）。
# 		(2).线程是操作系统进行 CPU 调度的基本单位。
# 		(3).同一进程内的线程共享进程资源。
```

### 02_主进程_子进程

```python
# 在windows操作系统中，查看：进程名、父进程pid、进程pid、 的命令如下：
# wmic process get Name,ParentProcessId,ProcessId

import os
import time

print(f'当前进程的pid是：{os.getpid()}')
print(f'当前进程的父进程pid是：{os.getppid()}')
time.sleep(10000)
```

### 03_使用Process_创建进程

```python
import os
import time
from multiprocessing import Process
print(100, __name__, os.getpid())

# 定义一个 speak 函数，功能是：每隔一秒说话一次（一共说话10次）
def speak():
    for index in range(10):
        print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

# 定义一个 study 函数，功能是：每隔一秒学习一次（一共学习15次）
def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

# 注意：一定要写 if __name__ == '__main__' 这个判断，原因如下：
#   1.当创建子进程时，Python 并不会把父进程内存里的 speak 函数直接交给子进程。
#   2.Python会启动一个全新的 Python 解释器进程，重新执行当前的 .py 文件（作为模块）。
#   3.在执行过程中，重新定义出一个 speak 函数，交给子进程。
if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    # 创建两个 Process 类的实例对象（进程对象），分别是 p1 和 p2。
    # 注意点1：p1 和 p2 就对应着以后的两个子进程，在创建它们的时候，就要指定好他们要执行的任务。
    # 注意点2：此时的 p1 和 p2 只是代码层面的两个进程对象，操作系统还没有真的创建 p1 和 p2 两个进程。
    p1 = Process(target=speak)
    p2 = Process(target=study)

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()

    print('我是主进程中的【最后一行】打印')
```

### 04_关于Process_参数

```python
import os
import time
from multiprocessing import Process, current_process

def speak(a, b, msg):
    for index in range(10):
        print(f'{msg}--{a}--{b}--{current_process().name}--我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    # Process的参数：
    #   🔸group： 默认值为None（应当始终为None）。
    #   🔸target：子进程要执行的可调用对象，默认值为 None。
    #   🔸name：  进程名称，默认为 None ，如果设置为 None，Python 会自动分配名字。
    #   🔸args：  给 target 传的位置参数（元组）
    #   🔸kwargs：给 target 传的关键字参数（字典）。
    #   🔸daemon：标记进程是否为守护进程，取值为布尔值（默认为 None，表示从创建方进程继承）。
    p1 = Process(target=speak, name='说话进程', args=(666, 888), kwargs={'msg':'尚硅谷'})
    p2 = Process(target=study)
    # print(p1.name)
    # print(p2.name)
    p1.start()
    p2.start()
    print('我是主进程中的【最后一行】打印')
```

### 05_Lock

```python
import os
import time
from multiprocessing import Process, Lock,RLock

def speak(lock):
    for index in range(10):
        # 上锁：如果锁是空闲的，立刻上锁，继续往下执行；如果锁被别人拿着：当前进程会阻塞等待（原地等）
        lock.acquire()
        lock.acquire()
        print('好好', end='')
        print('学习', end='')
        print('天天', end='')
        print('向上')
        # 释放锁：acquire 和 release 必须成对出现，否则会永远卡住（死等）
        lock.release()
        lock.release()
        time.sleep(1)


def study(lock):
    for index in range(15):
        # with lock: 会自动完成两件事：
        #   (1).进入前：自动执行 lock.acquire() 上锁
        #   (2).离开后：自动执行 lock.release() 释放锁
        # 好处：即便代码块里发生异常，也能保证释放锁，避免“卡死”
        # 备注：RLock 可以多次上锁
        with lock:
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    lock = RLock()
    p1 = Process(target=speak, args=(lock,))
    p2 = Process(target=study, args=(lock,))
    p1.start()
    p2.start()
    print('我是主进程中的【最后一行】打印')
```

### 06_join_方法

```python
# join 方法的作用：阻塞当前进程，等 join 前面的进程执行完，再继续往下执行。
# join(timeout)，其中 timeout 是可选参数，表示等多久，单位是秒。

# 注意点：
#   1.p.join() 不是让进程 p 等，而是让“执行这行 join 代码的那个进程”去等，等的是 p 这个进程。
#   2.当达到了 timeout 所指定的时间后，进程并不会终止，只是“不再等”了。
#   3.join 必须在 start 之后
import os
import time
from multiprocessing import Process

def speak():
    for index in range(10):
        print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    # 让主进程等 p1 5秒钟
    p1.join(5)

    p2.start()
    # p1.join() # 让主进程等 p1 进程执行完毕后，主进程再继续执行。
    # p2.join() # 让主进程等 p2 进程执行完毕后，主进程再继续执行。
    print('我是主进程中的【最后一行】打印')
```

### 07_terminate_方法

```python
import os
import time
from multiprocessing import Process

def speak():
    try:
        for index in range(10):
            print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
            time.sleep(1)
    # 注意：使用 terminate 终止进程，不会引起 finally 执行！
    finally:
        print('我是finally里的逻辑')

def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    p2.start()

    time.sleep(3)
    print('我是主进程，我准备强制终止p1进程........')
    # 向操作系统申请强制终止p1进程
    p1.terminate()
    # 等操作系统彻底终止掉了p1进程
    p1.join()
    # 看一下p1进程是否“活着”
    print(p1.is_alive())

    print('我是主进程中的【最后一行】打印')
```

### 08_守护进程

```python
# 什么是守护进程？
#   1.一种 “依附于主进程存在的子进程”，一旦主进程结束，它就会被自动终止。
#   2.简言之：主进程一死，守护进程必跟着死。
#
# 守护进程的使用场景：
#   1.后台监控类任务
#   2.日志 / 统计 / 采样 类任务
#   3.辅助型“陪跑任务”
#
# 注意点：
#   1.守护进程必须是 子进程。
#   2.主进程结束，守护进程也会随之结束。
#   3.守护进程中，不允许再创建新的子进程。
#   4.必须在 start 之前，start() 之后，不能再设置 daemon

import os
import time
from multiprocessing import Process

def monitor():
    while True:
        try:
            with open('log.txt', 'r', encoding='utf-8') as file:
                lines = sum(1 for _ in file)
        except FileNotFoundError:
            lines = 0
        print(f'我是【守护进程({os.getpid()})】，log.txt 共有{lines}行')
        time.sleep(1)

def test():
    for index in range(30):
        print(f'我是test({os.getpid()})')
        time.sleep(1)

if __name__ == '__main__':
    print(f'我是主进程({os.getpid()})中的【第一行】代码')

    p1 = Process(target=monitor, daemon=True)
    p2 = Process(target=test)

    p1.start()
    p2.start()

    # 向文件中写入数据
    with open('log.txt', 'a', encoding='utf-8') as file:
        for index in range(10):
            file.write(f'尚硅谷{index}\n')
            file.flush()
            time.sleep(1)

    print(f'我是主进程({os.getpid()})中的【最后一行】代码')
```

### 09_进程之间不共享变量

```python
# 进程之间不共享内存，因此也就不共享任何变量。
from multiprocessing import Process

def test1(num, names):
    num += 10
    names.append('张三')
    print(f'我是 test1 进程，操作之后的num是{num}，操作之后的names是{names}')

def test2(num, names):
    num -= 10
    names.append('李四')
    print(f'我是 test2 进程，操作之后的num是{num}，操作之后的names是{names}')

if __name__ == "__main__":
    num = 100
    names = []

    print('主进程中的【第一行】代码')
    p1 = Process(target=test1, args=(num, names))
    p2 = Process(target=test2, args=(num, names))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('主进程中的【最后一行】代码', num, names)
```

### 10_Queue_队列

```python
# 我们之前学过 list、tuple、dict，它们的特点是：数据想怎么拿数据，就怎么拿。
# 队列(Queue)是：一种“先进先出”的数据结构（先放进去的数据，一定会先取出来）
import time
from multiprocessing import Queue, Process

# 创建一个队列（不限制大小，即：不设置容量上限）
# q1 = Queue()

# 创建一个队列（最多能保存3个元素）
# q2 = Queue(3)

# 1️⃣put方法：往队列里放数据（入队）
# q1.put(10)
# q1.put(20)
# q1.put(30)

# 2️⃣get方法：从队列里取数据（出队）
# value1 = q1.get()
# value2 = q1.get()
# value3 = q1.get()
# print(value1)
# print(value2)
# print(value3)

# 3️⃣empty方法：判断队列是否为空
# result = q1.empty()
# print(result)

# 4️⃣full方法：判断队列是否已满
# q1.put(10)
# q1.put(20)
# q1.put(30)
# result = q1.full()
# print(result)

# q2.put(100)
# q2.put(200)
# q2.put(300)
# result = q2.full()
# print(result)

# 5️⃣qsize方法：获取队列长度
# q1.put(10)
# q1.put(20)
# q1.put(30)
# result = q1.qsize()
# print(result)

# 6️⃣队列具备等待模式
# q2.put(100)
# q2.put(200)
# q2.put(300)

# (1).当队列已满，继续 put，就会进入等待模式，等别人调用get方法，取走一个元素
# q2.put(400)
# print('放入完毕')

# (2).当队列已满，执行：put(元素, timeout=秒数)，就会等待指定秒数。
# q2.put(400, timeout=3)
# print('放入完毕')

# (3).put_nowait 方法，会直接向队列中添加元素，不会进入等待模式，若队列已满，会抛出异常。
# 备注：put_nowait 等价于 put(元素, block=False)，block的默认值为 True
# q2.put_nowait(400)
# q2.put(400, block=False)

# get读多了，也会进入等待模式
# q2.get()
# q2.get()
# q2.get()

# (1).当队列已空，继续 get，就会进入等待模式。x
# q2.get()

# (2).当队列已空，执行 get(timeout=秒数)，就会等待指定秒数。
# q2.get(timeout=3)

# (3).get_nowait 方法，会直接读取队列中的元素，不会进入等待模式，若队列已空，会抛出异常
# 备注：get_nowait 等价于 get(block=False)
# q2.get_nowait()
# q2.get(block=False)

def test(q):
    time.sleep(3)
    result = q.get()
    print('我从队列中取出了一个元素：',result)


# 通过多进程，演示一下：当队列满了以后，再次put会等待，当有人从队列中取出元素后，put会继续。
if __name__ == '__main__':
    # 创建一个队列，让其最多能保存2个元素
    q = Queue(2)
    # put两次，把队列填满
    q.put('尚硅谷')
    q.put('atguigu')
    print(f'队列是否已满：{q.full()}')

    # 创建子进程p1
    p1 = Process(target=test, args=(q, ))
    # 开启子进程p1，让其3秒钟后，从队列中取出一个元素
    p1.start()

    print('即将向已满的队列中添加一个元素........')
    q.put('hello')

    print('目前队列中有的元素是：')
    print(q.get())
    print(q.get())
```

### 11_使用Queue_进程通信

```python
import time
from multiprocessing import Process, Queue

# 子进程1：往队列里放数据
def test1(q):
    for index in range(5):
        print(f'【test1】放入数据：{index}')
        q.put(index)
        time.sleep(0.5)

# 子进程2：从队列里取数据
def test2(q):
    for index in range(5):
        data = q.get()
        print(f'【test2】取出数据：{data}')
        time.sleep(1)

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=test1, args=(q,))
    p2 = Process(target=test2, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

### 12_使用Pipe_进程通信

```python
import time
from multiprocessing import Process, Pipe

def test1(con1):
    time.sleep(2)
    con1.send(100)
    print('test1发送了100')

def test2(con2):
    data = con2.recv()
    print(f'test2接收了{data}')


if __name__ == '__main__':
    con1, con2 = Pipe(duplex=False)
    p1 = Process(target=test1, args=(con1,))
    p2 = Process(target=test2, args=(con2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

### 13_继承Process_创建进程

```python
from multiprocessing import Process
import os, time

class SpeakProcess(Process):
    def __init__(self, a, b, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.b = b

    def run(self):
        for index in range(10):
            print(f'{self.a}--{self.b}--我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
            time.sleep(1)

class StudyProcess(Process):
    def run(self):
        for index in range(15):
            print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
            time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = SpeakProcess(100, 200)
    p2 = StudyProcess()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('我是主进程中的【最后一行】打印')
```

### 14_进程池

```python
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# 1️⃣ 创建『进程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     executor.submit(work, 1)
#     executor.submit(work, 2)
#     executor.submit(work, 3)
#     executor.submit(work, 4)
#     executor.submit(work, 5)
#     executor.submit(work, 6)
#     executor.submit(work, 7)
#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print('---------end-------------')


# 2️⃣ 获取子进程执行后的返回结果（Future类的实例对象 + result方法）
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     # f1 = executor.submit(work, 1)
#     # f2 = executor.submit(work, 2)
#     # f3 = executor.submit(work, 3)
#     # f4 = executor.submit(work, 4)
#     # f5 = executor.submit(work, 5)
#     # f6 = executor.submit(work, 6)
#     # f7 = executor.submit(work, 7)
#     futures = [executor.submit(work, index) for index in range(1, 8)]
#     # 阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # print(f1.result())
#     # print(f2.result())
#     # print(f3.result())
#     # print(f4.result())
#     # print(f5.result())
#     # print(f6.result())
#     # print(f7.result())
#     for f in futures:
#         print(f.result())
#     print('---------end-------------')


# 3️⃣ 使用 as_completed：按“完成顺序”获取结果
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     futures = [executor.submit(work, index) for index in range(1, 8)]
#     # 准备一个 result_list 去收集任务的具体结果
#     result_list = []
#     # 收集每个任务的结果
#     for f in as_completed(futures):
#         result_list.append(f.result())
#     # 阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # 打印最终的结
#     print(result_list)
#     print('---------end-------------')


# 4️⃣使用 add_done_callback 方法，为任务添加完成时的回调函数
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 准备一个 result_list 列表去收集任务的结果
#     result_list = []
#     # 任务完成后的回调函数
#     def done_func(futrue):
#         result_list.append(futrue.result())
#     # 开启7个任务，并指定回调函数
#     for index in range(1, 8):
#         f = executor.submit(work, index)
#         f.add_done_callback(done_func)
#     # 等所有任务都完成
#     executor.shutdown(wait=True)
#     # 打印最终的结果（按“完成的顺序”获取）
#     print(result_list)
#     print('---------end-------------')


# 5️⃣使用 map 方法批量提交任务（注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
#  换一种说法：map方法会把这一批任务提交到进程池里执行，它会立刻返回一个生成器，真正的阻塞发生在：生成器取结果时（如 list(result)
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 通过 map 方法批量提交任务（结果按照提交的顺序来）
#     results = executor.map(work, [1, 2, 3, 4, 5, 6, 7])
#     # 获取 results 生成器中的内容
#     print(list(results))
#     # 等所有任务都完成
#     executor.shutdown(wait=True)
#     print('---------end-------------')


# 6️⃣使用 with：进程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个进程池执行器
#     with ProcessPoolExecutor(3) as executor:
#         # 通过 map 方法批量提交任务（结果按照提交的顺序来）
#         results = executor.map(work, [1, 2, 3, 4, 5, 6, 7])
#         # 获取 results 生成器中的内容
#         print(list(results))
#     print('---------end-------------')
```

### 15_使用Thread_创建线程

```python
import os
import time
from threading import get_native_id, Thread, RLock

def speak(lock):
    for index in range(5):
        with lock:
            print(f'我在说话{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
        time.sleep(1)

def study(lock):
    for index in range(5):
        with lock:
            print(f'我在学习{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'-------start------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
    lock = RLock()
    # Thread 的参数：
    # 🔸group： 默认值为 None（应当始终为 None）。
    # 🔸target： 子线程要执行的可调用对象，默认值为 None。
    # 🔸name： 线程名称，默认为 None。如果设置为 None，Python 会自动分配名字
    # 🔸args： 给 target 传的位置参数（元组）。
    # 🔸kwargs： 给 target 传的关键字参数（字典）。
    # 🔸daemon： 标记线程是否为守护线程，取值为布尔值（默认为 None）。
    # 使用 Thread 创建线程对象
    t1 = Thread(target=speak, args=(lock,))
    t2 = Thread(target=study, args=(lock,))
    # 调用线程对象的 start 方法，会立刻将该线程交由操作系统进行调度。
    t1.start()
    t2.start()
    # 让主线程等 t1和t2 线程执行完毕后，主线程再继续执行。
    t1.join()
    t2.join()
    print('-------end-------')
```

### 16_继承Thread_创建线程

```python
import os
import time
from threading import get_native_id, Thread, RLock

class SpeakThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock
        
    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在说话{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
            time.sleep(1)

class StudyThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在学习{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
            time.sleep(1)

if __name__ == '__main__':
    print(f'-------start------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
    lock = RLock()
    # 继承 Thread 类创建线程对象
    t1 = SpeakThread(lock)
    t2 = StudyThread(lock)
    # 调用线程对象的 start 方法，会立刻将该线程交由操作系统进行调度。
    t1.start()
    t2.start()
    # 让主线程等 t1和t2 线程执行完毕后，主线程再继续执行。
    t1.join()
    t2.join()
    print('-------end-------')
```

### 17_线程池

```python
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id, RLock

# 1️⃣ 创建『线程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     executor.submit(work, 1, lock)
#     executor.submit(work, 2, lock)
#     executor.submit(work, 3, lock)
#     executor.submit(work, 4, lock)
#     executor.submit(work, 5, lock)
#     executor.submit(work, 6, lock)
#     executor.submit(work, 7, lock)
#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print('---------end-------------')


# 2️⃣ 获取子线程执行后的返回结果（Future类的实例对象 + result方法）
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     futures = [executor.submit(work, index, lock) for index in range(1, 8)]
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # 打印结果
#     for f in futures:
#         print(f.result())
#     print('---------end-------------')

# 3️⃣ 使用 as_completed：按“完成顺序”获取结果
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     futures = [executor.submit(work, index, lock) for index in range(1, 8)]
#     # 收集每个线程返回的结果
#     result_list = []
#     # 将每个线程返回的结果，存入result_list
#     for f in as_completed(futures):
#         result_list.append(f.result())
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # 打印最终的结果
#     print(result_list)
#     print('---------end-------------')


# 4️⃣使用 add_done_callback 方法，为任务添加完成时的回调函数
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 收集每个线程的执行结果
#     result_list = []
#     # 定义一个线程执行成功后的回调函数
#     def done_func(f):
#         result_list.append(f.result())
#     # 使用submit提交任务，并指定回调函数
#     for index in range(1, 8):
#         f = executor.submit(work, index, lock)
#         f.add_done_callback(done_func)
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # 打印最终的结果
#     print(result_list)
#     print('---------end-------------')


# 5️⃣使用 map 方法批量提交任务（注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
#  换一种说法：map方法会把这一批任务提交到线程池里执行，它会立刻返回一个生成器，真正的阻塞发生在：生成器取结果时（如 list(result)

# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 使用map方法批量提交任务
#     result = executor.map(work, [1, 2, 3, 4, 5, 6, 7], [lock]*7)
#     # 打印最终的结果
#     print(list(result))
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print('---------end-------------')


# 6️⃣使用 with：线程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
def work(n, lock):
    with lock:
        print(f'work正在执行任务{n}.........{get_native_id()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    with ThreadPoolExecutor(3) as executor:
        # 创建线程锁
        lock = RLock()
        # 使用map方法批量提交任务
        result = executor.map(work, [1, 2, 3, 4, 5, 6, 7], [lock]*7)
        # 打印最终的结果
        print(list(result))
    print('---------end-------------')
```

### 18_GIL锁

```python
# 一、关于GIL（Global Interpreter Lock）
#   1️⃣GIL锁是 CPython 解释器中的一把互斥锁。
#   2️⃣GIL锁的作用：无论 CPU 有多少个核心，在某一时刻，只允许同一个进程中的一个线程去执行 Python 代码。

# 二、结论：CPython 解释器中的多线程模型，本质上是并发，而不是并行！（是快速切换，而不是同时进行）

# 三、为何要这样设计？———— 为了确保解释器级别的数据安全。

# GIL锁和编码时使用的 Lock 和 Rlock 不是同一个东西。
# Lock 和 Rlock是业务层面的锁，目标是：让业务逻辑别出错
# Rlock示例1：让打印是完整的

import time
from threading import Thread, RLock,current_thread
# def show_info1(lock):
#     for index in range(10):
#         with lock:
#             print('尚', end='')
#             print('硅', end='')
#             print('谷')
#
# def show_info2(lock):
#     for index in range(10):
#         with lock:
#             print('at', end='')
#             print('gui', end='')
#             print('gu')
#
# if __name__ == '__main__':
#     lock = RLock()
#     t1 = Thread(target=show_info1, args=(lock,))
#     t2 = Thread(target=show_info2, args=(lock,))
#     t1.start()
#     t2.start()

# Rlock示例2：不要让两个窗口卖出同一张票
current = 1

def sale(lock):
    global current
    while True:
        with lock:
            if current <= 20:
                print(f'{current_thread().name}出售了第{current}张票！')
                current += 1
            else:
                print('票已售空')
                break
        time.sleep(0.3)

if __name__ == '__main__':
    lock = RLock()
    t1 = Thread(target=sale, name='窗口1', args=(lock,))
    t2 = Thread(target=sale, name='窗口2', args=(lock,))
    t3 = Thread(target=sale, name='窗口3', args=(lock,))
    t1.start()
    t2.start()
    t3.start()
```

### 19_CPU密集型任务

```python
# CPU密集型任务，更适合用多进程。
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# 准备一个 CPU 密集型任务
def cpu_task(n):
    print(f'任务{n}开始了')
    total = 0
    for i in range(10000000):
        total += i * i
    return total

if __name__ == '_main_':
    print('===== 多进程完成【CPU密集型任务】=====')
    start = time.time()
    #开启四个进程进行计算
    with ProcessPoolExecutor(4) as executor:
        list(executor.map(cpu_task, [1, 2, 3, 4]))
    end = time.time() - start
    print(f'多进程总耗时：{end}秒')


    # print('===== 多线程完成【CPU密集型任务】=====')
    # start = time.time()
    # # 开启四个线程进行计算
    # with ThreadPoolExecutor(max_workers=4) as executor:
    #     results = list(executor.map(cpu_task, [1, 2, 3, 4]))
    # end = time.time() - start
    # print(f'多线程总耗时：{end}秒')
```

### 20_IO密集型任务

```python
# IO密集型任务，更适合用多线程。
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 拷贝文件
def copy_file(index):
    with open('a.zip', 'rb') as src, open(f'a_副本{index}.zip', 'wb') as dst:
        while True:
            data = src.read(1024 * 1024)  # 每次读 1MB
            if not data:
                break
            dst.write(data)

if __name__ == '__main__':
    # print('===== 使用多进程完成【IO密集型任务】 =====')
    # start = time.time()
    # with ProcessPoolExecutor(4) as executor:
    #     for i in range(4):
    #         executor.submit(copy_file, i)
    # end = time.time() - start
    # print(f'多进程耗时：{end} 秒')

    print('===== 使用多线程完成【IO密集型任务】 =====')
    start = time.time()
    with ThreadPoolExecutor(4) as executor:
        for i in range(4):
            executor.submit(copy_file, i)
    end = time.time() - start
    print(f'多线程耗时：{end} 秒')
```

---
