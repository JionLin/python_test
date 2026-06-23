# ### 一、选择题
#
# - 以下哪种异常通常在尝试访问字典中不存在的键时引发？（ A ）
#
#   A. KeyError	B. IndexError	C. ValueError	D. TypeError
#
# 【解析说明】：
# A. KeyError：针对映射类型（如字典 dict）。当访问字典中不存在的键时触发，本题选A。
# B. IndexError：针对序列类型（如列表、字符串）。当访问超出长度范围的索引时触发。
# C. ValueError：当函数接收到类型正确但内容不合法的参数时触发（如 int("abc")）。
# D. TypeError：当操作被应用于不合适的类型时触发（如 1 + "abc"）。
# 总结：KeyError和IndexError都属于LookupError，区别在于一个是查键，一个是查下标。
#
# - 以下关于try - except - finally语句的描述，正确的是（B  ）
#
#   A. finally块中的代码只有在没有异常发生时才会执行	B. finally块中的代码无论是否发生异常都会执行
#
#   C. 如果try块中发生异常，except块和finally块都不会执行	D. except块和finally块只能存在一个
#
# ### 二、编程题
#
# 1. 编写一段 Python 代码，尝试将字符串 "123abc" 转换为整数，如果转换失败，捕获 ValueError 异常，
# 将异常信息记录到一个文本文件 error.log 中。

str1="123abc"
try:
  int(str1)
except ValueError as e:
  # 【with open 入参说明】：
  # 1. 'error.log': 目标文件名。相对路径，表示在当前运行目录下寻找或创建该文件。
  # 2. 'a': 打开模式（Append 追加模式）。记录日志通常用 'a'，以便将新错误追加到文件末尾而不覆盖历史记录。
  # 3. encoding='utf - 8': 指定文件编码为 UTF-8，防止中文等报错信息在写入时出现乱码。
  # （💡 建议：代码中的 'utf - 8' 带有空格，虽受 Python 容错支持，但最好写成标准的 'utf-8'）
  with open('error.log', 'a', encoding='utf - 8') as file:
    file.write(str(e) + '\n')




class InvalidAgeError(Exception):
  pass

class UnrealisticAgeError(Exception):
  pass


# 2. 定义一个函数check_age，该函数接受一个年龄参数。如果年龄小于 0，抛出一个自定义异常InvalidAgeError；如果年龄大于 120，
# 抛出UnrealisticAgeError。这两个自定义异常类都继承自Exception类。调用该函数并传入一个不合法的年龄值，捕获并处理异常。
def check_age(age):
    if age< 0:
      raise InvalidAgeError("年龄不能为负数")
    if age >= 120:
      raise UnrealisticAgeError("年龄超过120不太现实")



try:
  check_age(-1)
except UnrealisticAgeError as e:
  print(e)
except InvalidAgeError as e:
  print(e)
