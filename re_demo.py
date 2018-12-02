# -*- coding:utf-8 -*-
import re


def match(p, str):
    m = p.match(str)
    if m is not None:
        print("match", m.group())
    else:
        print("match can not find")


def search(p, str):
    m = p.search(str)
    if m is not None:
        print("serach", m.group())
    else:
        print("serach can not find")


# 正则表达式常用知识点
a = '12345\nabc'
# .(匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. )
p = re.compile(".*")
match(p, a)
# + (匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+)
# * (匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*)
p = re.compile(".+")
match(p, a)
print("-----------------")
# 非贪婪
p = re.compile(".+?")
match(p, a)
p = re.compile(".*?")
match(p, a)
print("-----------------")

# \d (匹配一个数字字符。等价于[0-9]) \w（匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]
p = re.compile("\d+")
match(p, a)
a = "1234abc"
p = re.compile("\w+")
match(p, a)
print("-----------------")
# [],字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的 "a"
# {n,m}, m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次
p = re.compile("[0-9]+")
match(p, a)
p = re.compile("[0-9]{1,3}")
match(p, a)
p = re.compile("[0-9A-Za-z_]{1,10}")
match(p, a)
print("-----------------")
# match (从字符串开头),search（任意地方）
a = " 1234 abc"
p = re.compile("\d+")
search(p, a)
match(p, a)
p = re.compile("\w+")
search(p, a)
print("-----------------")
# ^ (匹配输入字符串的开始位置。如果设置了RegExp对象的Multiline属性，^也匹配“\n”或“\r”之后的位置)
# & （匹配输入字符串的结束位置。如果设置了RegExp对象的Multiline属性，$也匹配“\n”或“\r”之前的位置）
a = " 1234 abc"
p = re.compile("^\d+")
search(p, a)
a = '1234 '
p = re.compile("^\d+&")
search(p, a)
print("-----------------")
# (),匹配pattern并获取这一匹配。所获取的匹配可以从产生的Matches集合得到，要匹配圆括号字符，请使用“\(”或“\)”
a = "1234abc"
p = re.compile("(\d+)(\w+)")
m = p.match(a)
print(m.group(0), m.group(1), m.group(2))
print("-----------------")
# split (用正则分割字符串)
a = "1234 abc  456"
print(re.split("\s+", a))
