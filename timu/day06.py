# ### 一、编程题
#
# 1. 创建一个简单的 Python 模块math_operations.py，其中定义两个函数add和multiply，分别用于实现两个数的加法和乘法运算。
# 在另一个 Python 文件中导入该模块，并调用这两个函数计算3 + 5和3 * 5的结果。

import math_operations

print(math_operations.add(3,4))

print(math_operations.multiply(3,4))

# 2. 使用生成器表达式创建一个生成器，生成 1 到 10 的偶数。然后使用for循环遍历该生成器，打印每个偶数。
even_numbers = (num for num in range(1, 11) if num % 2 == 0)
for i in even_numbers:
    print(i)

# 【第2题结果分析】
# 结果：依次打印出 2, 4, 6, 8, 10。
# 通俗大白话解析（生成器就像是一台“按需生产的自动售货机”）：
# 1. 括号 (...) 把代码变成了一台售货机，现做现卖，省内存。
# 2. `if num % 2 == 0` 相当于在售货机内部装了个“质检员”，在机器里就已经把奇数过滤扔掉了。
# 3. 所以外层 for 循环从机器里拿东西的时候，吐出来的绝对都是偶数，拿出来后完全不需要再自己多写一个 if 去检查一遍，直接打印就行。

# 3. 创建一个迭代器类MyIterator，用于遍历一个给定列表的元素。实现__iter__和__next__方法。使用该迭代器类遍历列表[10, 20, 30, 40]，并打印每个元素。

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        # 迭代器本身也是可迭代对象，返回自己
        return self

    def __next__(self):
        # 如果索引还没有越界，返回当前元素并将索引加1
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            # 越界后抛出StopIteration异常，结束遍历
            raise StopIteration

# 使用该迭代器类遍历列表
my_iter = MyIterator([10, 20, 30, 40])
for item in my_iter:
    print(item)

# 【第3题结果分析】
# 结果：依次打印出 10, 20, 30, 40。
# 通俗大白话解析（迭代器就像是你雇了一个“带书签的阅读员”来帮你一页页翻书）：
# 1. __init__(准备工作): 你塞给他一本列表当作书(self.data)，他准备一张书签，一开始夹在第 0 页(self.index = 0)。
# 2. __iter__(确认身份): Python 问“这书谁来读？”，他指了指自己(return self)，表示我自己来。
# 3. __next__(核心动作): 每次 for 循环找他要数据，他就看看书签越界没。没越界就抄下这一页的值，然后【一定记得把书签往后翻一页】(self.index += 1)，把抄好的值交给你。
# 4. StopIteration(大喊结束): 如果书签挪到书本外面去了（越界了），他不能一声不吭，必须抛出异常大喊一声“读完了！”(raise StopIteration)。for 循环一听到这句大喊，就知道该聪明地结束循环了。