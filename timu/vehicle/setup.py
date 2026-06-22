from setuptools import setup, find_packages

setup(
    name="vehicle-package",   # 包的名字
    version="1.0.0",          # 版本号
    packages=find_packages(), # 自动寻找带有 __init__.py 的文件夹作为包
)