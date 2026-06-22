# ### 题目 1：字符串操作
#
# 给定字符串 my_string = "Hello, Python!"，请完成以下任务：
#
# 1. 将字符串转换为大写形式。  2.查找字符串中字符 'P' 的位置。  3.将字符串按照 ',' 进行分割。

my_string = "Hello, Python!"

my_string2=my_string.upper();
print(my_string2)

num=my_string.index("P");
print(num)

split1=my_string.split(",");
print(split1)

# ### 题目 2：元组特性
#
# 创建一个元组 my_tuple = (1, 2, 2, 3, 4, 4, 4)，请完成：
# 1. 计算元组中元素 4 出现的次数。
my_tuple = (1, 2, 2, 3, 4, 4, 4)
count_4 = my_tuple.count(4)
print("4出现的次数:", count_4)

count5=my_tuple.count("2");
print(count5)
# 2.获取元组的长度。
num2 = len(my_tuple)
print("元组的长度:", num2)

# ### 题目 3：集合操作
#
# 现有集合 set1 = {1, 2, 3, 4, 5} 和 set2 = {3, 4, 5, 6, 7} 。

# 1. 求这两个集合的并集。
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# 🚨 Java 陷阱警告：Python 没有 addAll，使用 | 运算符或 union()
set3 = set1 | set2
print("并集:", set3)

set12=set1|set2
print("并集12:", set12)

# 2. 求这两个集合的交集。
# 🚨 Java 陷阱警告：Python 没有 retainAll，使用 & 运算符或 intersection()
set4 = set1 & set2
print("交集:", set4)
set21=set1&set2
print("交集2:",set21)

# 3. 从 set1 中移除元素 3 。
# 🚨 Java 陷阱警告：remove() 是原地修改，返回值为 None，不要用变量去接收它
set1.remove(3)
print("移除3后的set1:", set1)

# ### 题目 4：集合与字典综合
#
# 创建一个集合，包含数字 1 到 5 。再创建一个字典，键为集合中的数字，值为该数字的平方。
arr1 = {1, 2, 3, 4, 5}

# 方案1：标准的 for 循环（符合 Java 直觉）
my_dict = {}
for n in arr1:
    my_dict[n] = n ** 2  # n ** 2 表示 n 的平方
print("for循环创建的字典:", my_dict)

# 方案2：字典推导式（极其推荐的 Pythonic 进阶写法）
my_dict2 = {n: n ** 2 for n in arr1}
print("字典推导式创建的字典:", my_dict2)
# 🔍 1. 拆解这行代码
# 这行代码其实是由三部分拼起来的，请你按照 2 -> 3 -> 1 的倒叙逻辑来读它：
#
#1 { ... } ：最外层的大括号，告诉 Python“我要生成一个新的字典”。
#2 for n in arr1 ：这是数据源。相当于 Java 里的 for (Integer n : arr1)，意思是“遍历 arr1 这个集合，每次取出的元素叫 n”。
#3 n: n ** 2 ：这是键值对的生成规则。冒号左边是 Key（键），右边是 Value（值）。意思是“把 n 作为键，把 n 的平方 作为值”。
# 连起来读就是：
#
# “我要生成一个字典 {}，遍历 arr1 中的每一个元素 n，把它按照 n : n的平方 的格式塞进这个字典里。”