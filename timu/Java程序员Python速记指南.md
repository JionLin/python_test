# ☕ Java 程序员的 Python 速记指南

## 🟢 第一部分：扫一眼就懂（与 Java 高度相似，千万别花时间背）

这些概念在两种语言中**底层逻辑完全一致**，你只需要知道它们在 Python 里也存在即可：

1. **基本控制流**：`if`、`while`、`for` 的业务逻辑作用一模一样。
2. **面向对象思想**：都有类（Class）、对象、继承、多态。
3. **异常处理原则**：都有 `try-except(catch)-finally`。**考点：** 无论是否报错，`finally` 块都会执行，用于释放资源。
4. **命名规范**：只能是字母、数字、下划线，**且数字不能开头**，区分大小写。
5. **值传递机制**：Python 的参数传递和 Java 一样，本质上都是“对象的引用传递”（对可变对象修改会影响原对象）。

---

## 🔴 第二部分：核心反直觉清单（⚠️最容易写错，必须死记！）

这是 Java 程序员写 Python 时最容易踩坑的 7 个地方，请把它们刻在脑子里：

| 陷阱点 | Java 的习惯 (会报错) | Python 的正确写法 | 记忆口诀 |
| :--- | :--- | :--- | :--- |
| **1. 布尔与空值** | `true`, `false`, `null` | `True`, `False`, `None` | **Python 首字母必须大写** |
| **2. 逻辑运算符** | `&&`, `||`, `!` | `and`, `or`, `not` | **全用纯英文** |
| **3. 多个条件分支**| `else if (...) { }` | `elif ...:` | **只有 4 个字母 `elif`** |
| **4. 字符串拼接** | `"Age: " + 18` (隐式转串) | `"Age: " + str(18)` | **Python 强类型，不会自动转字符串**，会报 `TypeError` |
| **5. 获取长度** | `arr.length` 或 `list.size()` | `len(arr)` 或 `len(list)` | **长度是全局函数 `len()`** |
| **6. 当前对象** | `this.name = name` | `self.name = name` | **Java 用 `this`，Python 用 `self`** (且必须在方法参数里声明) |
| **7. 代码块边界** | 依赖大括号 `{}` | 依赖冒号 `:` 和 **缩进** | **凡是有 `{` 的地方，Python 都换成 `:` 加回车缩进** |

---

## 🟡 第三部分：核心语法替换对照表 (Cheat Sheet)

写代码或做题时，如果在脑海中想到了 Java 的写法，直接查表替换为 Python 写法：

### 1. 变量与数据类型
| 场景 | Java | Python |
| :--- | :--- | :--- |
| **声明变量** | `int a = 1;` <br> `String s = "A";` | `a = 1` <br> `s = "A"` (无需声明类型，单双引号皆可) |
| **常量定义** | `final int MAX = 100;` | `MAX = 100` (没有 final 关键字，全大写仅为约定) |
| **类型转换** | `int a = Integer.parseInt("1");` | `a = int("1")` |

### 2. 循环结构
| 场景 | Java | Python |
| :--- | :--- | :--- |
| **常规 for 循环**| `for (int i=0; i<10; i++) { }` | `for i in range(10):` (左闭右开 0~9) |
| **增强 for 循环**| `for (String item : list) { }` | `for item in list:` |

### 3. 数据结构 (集合框架)
| 场景 | Java | Python |
| :--- | :--- | :--- |
| **列表 (List)** | `List<Integer> lst = new ArrayList<>();`<br>`lst.add(1);` | `lst = []`<br>`lst.append(1)` |
| **字典 (Map)** | `Map<String, Int> map = new HashMap<>();`<br>`map.put("A", 1);` | `map = {}`<br>`map["A"] = 1` |
| **读 Map 的坑** | `map.get("Not_Exist")` -> 返回 `null` | `map["Not_Exist"]` -> **报错 `KeyError` (考点)** <br> *(注: 用 `map.get("x")` 才会返回 `None`)* |

### 4. 函数与类
| 场景 | Java | Python |
| :--- | :--- | :--- |
| **定义函数** | `public int add(int a, int b) { return a+b; }` | `def add(a, b): return a + b` (用 `def` 关键字) |
| **定义类** | `public class User { ... }` | `class User:` |
| **构造方法** | `public User(String name) { ... }` | `def __init__(self, name):` (固定叫 `__init__`) |

### 5. 常用内置方法与 API 对照 (基于 day02)
这些是在处理字符串、元组、集合时最高频使用的 API，注意它们与 Java 的区别：

| 场景 / 操作 | Java 的写法 | Python 的写法 |
| :--- | :--- | :--- |
| **字符串转大写** | `str.toUpperCase()` | `str.upper()` |
| **字符串截取** | `str.substring(0, 5)` | `str[0:5]` (即切片操作 Slice，极高频使用) |
| **查找字符位置** | `str.indexOf("P")` | `str.find("P")` (找不到返回 -1) 或 `str.index("P")` (找不到报错) |
| **字符串分割** | `str.split(",")` | `str.split(",")` |
| **获取长度/大小**| `arr.length` 或 `list.size()` | `len(obj)` (通用全局函数：支持字符串、列表、元组、集合、字典) |
| **统计元素出现次数**| `Collections.frequency(list, 4)` | `obj.count(4)` (支持列表、元组、字符串) |
| **集合求并集** | `set1.addAll(set2)` (会修改原集合) | `set1 \| set2` 或 `set1.union(set2)` (返回新集合) |
| **集合求交集** | `set1.retainAll(set2)` (会修改原集合) | `set1 & set2` 或 `set1.intersection(set2)` (返回新集合) |
| **集合移除元素** | `set.remove(3)` | `set.remove(3)` (元素不存在会报错) 或 `set.discard(3)` (元素不存在不报错) |

### 6. 核心数据结构对比 (列表、元组、集合、字典)
Python 的四大基础数据结构是重中之重，理解它们的区别能帮你避开 80% 的新手坑：

| 数据结构 | 符号定义 | 特点 | 适用场景 | 对应的 Java 结构 |
| :--- | :--- | :--- | :--- | :--- |
| **列表 (List)** | `[1, 2]` | 有序，**可变**，允许重复 | 日常存储一系列数据 | `ArrayList` |
| **元组 (Tuple)**| `(1, 2)` | 有序，**不可变 (只读)**，允许重复 | 固定的数据记录，函数返回多个值 | `Collections.unmodifiableList()` 或只读数组 |
| **集合 (Set)** | `{1, 2}` | 无序，**不可重复**，元素必须可哈希 | 去重、集合运算 (交/并/差集) | `HashSet` |
| **字典 (Dict)** | `{"a": 1}`| 键值对，键不可重复，**键必须不可变** | 映射存储，快速查找 | `HashMap` |

**💡 核心使用注意（Java 程序员容易踩的坑）：**
1. **空集合与空字典的初始化**：
   - `a = {}` 默认创建的是**空字典** (Dict)。
   - 创建**空集合** (Set) 必须使用全局函数：`a = set()`。
2. **单元素元组的陷阱**：
   - `a = (1)` 定义的是一个普通的整数 `1`（括号会被当做数学优先级运算符）。
   - 创建**单元素元组**必须加逗号：`a = (1,)`。
3. **可变性限制 (Hashable)**：
   - 字典的 Key 和集合的元素必须是**不可变对象**（如数字、字符串、元组）。
   - 绝对不能用列表（List）作为字典的 Key 或塞进集合中，否则会报 `TypeError: unhashable type: 'list'`。

### 7. 进阶语法：Python 独有的“黑魔法” (Pythonic)
作为 Java 开发者，掌握以下几个 Python 特有语法，能让你的代码瞬间变得地道，这也是中高级考试的必考点：

| 功能场景 | Java 的实现方式 | Python 的优雅写法 | 核心区别 / 优势 |
| :--- | :--- | :--- | :--- |
| **程序入口** | `public static void main(String[] args)` | `if __name__ == '__main__':` | 脚本自顶向下执行，此语句保证代码被当做模块导入时，不会意外执行主逻辑。 |
| **列表推导式**<br>*(极高频)* | 用 `for` 循环不断 `add()`，或使用 Java 8 Stream API | `res = [x*2 for x in list if x > 0]` | 将循环、条件过滤、数据转换浓缩在一行，极其简洁。 |
| **自动释放资源**<br>*(文件操作等)* | `try (BufferedReader br = ...) { }` (try-with-resources) | `with open('file.txt') as f:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`f.read()` | 使用 `with` 关键字（上下文管理器），离开缩进块后自动 close，告别 `finally`。 |
| **重写打印格式** | `@Override`<br>`public String toString()` | `def __str__(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return ...` | Python 称之为“魔法方法”(Dunder)，以双下划线包裹。 |
| **重写比较逻辑** | `@Override`<br>`public boolean equals(Object o)` | `def __eq__(self, other):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return ...` | **重点：** Python 用 `==` 比较值（自动调 `__eq__`），用 `is` 比较内存地址（等于 Java 的 `==`）。 |
| **多值返回** | 需封装成 `Object[]` 或自定义实体类 | `return a, b` | 本质是返回了一个元组，外部可以轻松解包：`x, y = func()`。 |
| **无限可变参数** | `void func(String... args)` | `def func(*args, **kwargs):` | `*args` 接收未命名的参数（存为元组），`**kwargs` 接收键值对参数（存为字典）。 |

### 8. 工程化：包管理、导包与打包 (对应 Maven 体系)
在实际工程开发和操作题中，文件结构的组织和打包发布有严格的规范。

| Python 概念 / 场景 | Java 对应概念 | 详细解析 / 注意事项 |
| :--- | :--- | :--- |
| **将文件夹标记为包** | 自动识别 `package` | 文件夹下**必须有 `__init__.py`** 文件（空文件即可），否则老版本 Python 无法将其识别为包。 |
| **精确导包 (推荐)** | `import java.util.List;` | `from vehicle.car import Car` <br> (作用等同 Java，导入后可直接使用 `Car`) |
| **整体/空间导包** | (无严格对应，必须写全名) | `import vehicle.car`<br>导入后，调用时必须带上完整的命名空间：`vehicle.car.Car()` |
| **打包配置文件** | `pom.xml` (Maven) <br> `build.gradle` | **`setup.py`**（传统）或 `pyproject.toml`（现代）。这是 Python 标准的项目配置脚本，定义了包名、版本、依赖。 |
| **打包发布命令** | `mvn clean package` | `python setup.py sdist` <br> (将代码打包成 `tar.gz` 压缩包发布给其他人使用) |
| **安装第三方包** | Maven 自动通过 POM 下载 | `pip install xxx` <br> (例如 `pip install vehicle-package-1.0.0.tar.gz`) |

---

## 🟣 第四部分：高频报错/异常对应表（针对选择题）

考题中经常考察报什么错。作为 Java 程序员，你只需要做映射：

| 你的 Java 直觉会报什么错 | Python 实际会抛出的异常 (考点) | 触发场景举例 |
| :--- | :--- | :--- |
| `ArrayIndexOutOfBoundsException` | **`IndexError`** | `lst = [1]`, 访问 `lst[2]` |
| `NullPointerException` (NPE) | **`AttributeError`** | `a = None`, 调用 `a.do_something()` |
| `IllegalArgumentException` | **`ValueError`** | `int("abc")` (值不合法) |
| `ClassCastException` | **`TypeError`** | `"a" + 1` (类型不匹配，不支持的操作) |
| (Java Map 返回 null) | **`KeyError`** | `my_dict["不存在的键"]` |
