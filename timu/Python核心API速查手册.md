# Python 核心语法与 API 全景速查手册（7天速成版）

结合实际代码库提炼，专为有经验的开发者准备的纯语法与 API 速查表。

## Day 1：基础语法、内置函数与字符串 API

**1. 全局内置函数 (Built-in Functions)**
```python
# 类型转换与判断
int(x) / float(x) / str(x) / bool(x)
type(obj)           # 获取对象类型
id(obj)             # 获取对象内存地址

# 交互与控制台
print(value, ..., sep=' ', end='\n', file=sys.stdout)
input("提示信息: ")  # 无论输入什么，返回的都是 str
```

**2. 字符串专属 API (`str` 常用方法)**
```python
s = " hello world "
# 查找与统计
s.find("o")         # 查找子串，找不到返回 -1 (极高频)
s.index("o")        # 同 find，但找不到会报错 ValueError
s.count("o")        # 统计子串出现次数
s.startswith("he") / s.endswith("ld") # 判断开头/结尾

# 清理与替换
s.strip()           # 去除两端空白字符
s.lstrip() / s.rstrip() # 去除左/右侧空白
s.replace("old", "new", count) # 替换指定次数

# 分割与拼接
s.split(" ")        # 按照空格分割，返回 List: ['hello', 'world']
"-".join(['a', 'b'])# 将可迭代对象拼接成字符串，返回 "a-b"

# 大小写转换与判断
s.upper() / s.lower() / s.capitalize() / s.title()
s.isdigit()         # 判断是否全是数字
s.isalpha()         # 判断是否全是字母
```

## Day 2：函数基础与高阶 API

**1. 序列通用数学/统计 API**
```python
len(obj)            # 获取长度/元素个数 (字符串、列表、字典通用)
max(iterable) / min(iterable) # 获取最大/最小值
sum(iterable)       # 快速求和
abs(n)              # 绝对值
round(n, ndigits)   # 四舍五入，保留 ndigits 位小数
divmod(a, b)        # 同时返回商和余数，格式为元组 (商, 余数)
```

**2. 函数定义与控制参数**
```python
def func(pos_only, /, normal, *, kw_only):
    pass
# / 之前的必须用位置传参，* 之后的必须用关键字传参

def func_pack(*args, **kwargs):
    # args 为 Tuple, kwargs 为 Dict
    pass
```

**3. 函数式编程处理 API (高阶函数)**
```python
# map: 对序列每个元素执行映射，返回 map 迭代器
list(map(lambda x: x*2, [1, 2, 3]))     # 结果: [2, 4, 6]

# filter: 条件过滤，返回 filter 迭代器
list(filter(lambda x: x>0, [-1, 0, 1])) # 结果: [1]

# sorted: 排序 (不改变原序列)
sorted(iterable, key=lambda x: x[1], reverse=True)

# 序列组合与枚举
enumerate(iterable, start=0)  # 同时返回索引和值: (0, val0), (1, val1)
zip(list1, list2)             # 将多个序列打包成元组的列表: (l1_0, l2_0)
```

## Day 3：四大内置容器的专属 API

**1. 列表专属 API (`list`)**
```python
lst = [1, 2, 3]
lst.append(4)           # 尾部追加单个元素
lst.extend([5, 6])      # 尾部批量追加另一集合
lst.insert(index, val)  # 在指定索引前插入
lst.pop(index=-1)       # 弹出并返回指定索引元素
lst.remove(val)         # 删除第一个匹配的值 (不存在报 ValueError)
lst.clear()             # 清空列表
lst.index(val)          # 查找值的索引
lst.count(val)          # 统计元素个数
lst.sort(key=..., reverse=False) # 就地排序
lst.reverse()           # 就地反转
```

**2. 字典专属 API (`dict`)**
```python
d = {"a": 1, "b": 2}
d.get("c", default_val) # 安全获取值，不存在返回 default_val
d.setdefault("c", 3)    # 如果键不存在，则插入并返回该值
d.keys()                # 返回所有键的视图
d.values()              # 返回所有值的视图
d.items()               # 返回 (键, 值) 元组的视图
d.pop("a")              # 删除并返回值
d.popitem()             # 随机弹出并返回一个 (键, 值) 元组
d.update({"c": 3})      # 合并/更新字典
```

**3. 集合专属 API (`set`)**
```python
s = {1, 2, 3}
s.add(4)                # 添加元素
s.remove(4)             # 移除元素 (不存在会报 KeyError)
s.discard(4)            # 移除元素 (不存在不会报错)
s1.intersection(s2)     # 交集 (同 s1 & s2)
s1.union(s2)            # 并集 (同 s1 | s2)
s1.difference(s2)       # 差集 (同 s1 - s2)
s1.issubset(s2)         # 判断 s1 是否是 s2 的子集
```

## Day 4：面向对象反射与内建 API

**1. 对象探针与反射 API**
```python
isinstance(obj, Class)     # 判断对象是否属于某个类或其子类
issubclass(ClassA, ClassB) # 判断 A 是否是 B 的子类

hasattr(obj, "name")       # 检查是否有某属性
getattr(obj, "name", def)  # 获取属性值，支持默认值
setattr(obj, "name", val)  # 动态设置属性值
delattr(obj, "name")       # 动态删除属性

dir(obj)                   # 返回对象所有属性和方法的列表
```

**2. 核心魔法方法 (Dunder Methods)**
```python
len(obj)    => obj.__len__()
str(obj)    => obj.__str__()
obj == obj2 => obj.__eq__(obj2)
obj[key]    => obj.__getitem__(key)
obj()       => obj.__call__()   # 让对象像函数一样被调用
```

## Day 5：异常类体系与迭代器 API

**1. 常见内置异常类**
```python
Exception               # 所有普通异常的基类
ValueError              # 传入无效参数 (如 int("abc"))
TypeError               # 操作应用于不适当类型的对象 (如 "a"+1)
IndexError              # 序列越界 (如 lst[99])
KeyError                # 字典中找不到键
AttributeError          # 找不到对象属性/方法 (如 None.func())
StopIteration           # 迭代器耗尽时触发
```

**2. 迭代器底层 API**
```python
it = iter(iterable)     # 转换为迭代器 (底层调用 __iter__)
next(it, default)       # 获取下一个值 (底层调用 __next__)
```

## Day 6：文件系统与 IO 操作 API

**1. 文件读写 API (`open` 对象)**
```python
# mode: 'r'读, 'w'写(覆盖), 'a'追加, 'b'二进制
with open("path", mode="r", encoding="utf-8") as f:
    f.read(size)        # 读取全部或 size 个字节/字符
    f.readline()        # 读取单行
    f.readlines()       # 读取所有行并返回列表
    f.write(string)     # 写入字符串
    f.writelines(list)  # 批量写入字符串列表
    f.flush()           # 强制将内存缓冲区写入磁盘
    f.seek(offset, whence) # 移动光标位置
```

**2. 常用目录与路径 API (`os` 标准库)**
```python
import os
os.listdir("path")      # 列出目录下所有文件和文件夹名称
os.remove("file.txt")   # 删除文件
os.rename("old", "new") # 重命名

import os.path as path
path.exists("file.txt") # 判断路径是否存在
path.join("dir", "a")   # 拼接路径
path.abspath("a.txt")   # 获取绝对路径
path.isdir("path") / path.isfile("path") # 判断是目录还是文件
```

## Day 7：多进程与多线程核心 API

**1. 多进程 API (`multiprocessing` 模块)**
```python
from multiprocessing import Process, Queue, Pool

# Process 对象控制
p = Process(target=func, args=(1,2), kwargs={"a":1})
p.start()               # 启动进程
p.join(timeout)         # 阻塞等待进程结束
p.terminate()           # 强制杀死进程

# IPC 进程间通信 (Queue)
q = Queue(maxsize=3)
q.put(obj, block=True, timeout=None) # 放入数据
q.get(block=True, timeout=None)      # 取出数据

# 进程池 Pool API
pool = Pool(processes=4)
pool.apply_async(func, args=(1,))    # 异步提交单个任务
pool.map(func, iterable)             # 阻塞式批量提交任务
pool.close()                         # 停止接收新任务
pool.join()                          # 等待池中任务执行完毕
```

**2. 多线程 API (`threading` 模块)**
```python
import threading

t = threading.Thread(target=func, args=(1,))
t.start()
t.join()

# 线程锁 API
lock = threading.Lock()
with lock:
    # 线程安全的操作
    pass
```