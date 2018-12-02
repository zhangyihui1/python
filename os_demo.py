# -*- coding:utf-8 -*-
import os

# 常用方法

# 获取当前文件名 （__file__）
print(__file__)
# 获取绝对路径 （os.path.abspath）
print(os.path.abspath(__file__))
# 获取父路径 （os.path.dirname）
this_path = os.path.abspath(os.path.dirname(__file__))
print(this_path)
print("-------------")
# 文件路径拼接
path1 = os.path.join(this_path, '111.txt')
print(path1)
# 判断文件是否存在
print(os.path.exists(path1))
path1 = os.path.join(this_path, '222.txt')
print(os.path.exists(path1))
print("-------------")
# 判断是文件还是文件夹
print(os.path.isdir(os.path.join(this_path, 'module1')))
print(os.path.isfile(os.path.join(this_path, '111.txt')))
# 遍历文件路径 listdir, walk(区分文件和文件夹)
print(os.listdir(this_path))
print(os.walk(this_path))
for root, dirs, files in os.walk(this_path):
    print('root', root)
    print('dirs', dirs)
    print('files', files)
    #for file in files:
    #    print(os.path.join(root, file))
print("-------------")
# 获取文件名，后缀
path1 = os.path.join(this_path, '222.txt')
print(os.path.split(path1))
print(os.path.splitext(path1))
