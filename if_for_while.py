# -*- coding:utf-8 -*-
a = "12345"
if a == '12345':
    print("a == 12345")
elif a != "abcd":
    print("a != abcd")
else:
    print('other')

if '1' in a and '2' in a or 'b' not in a:
    print('find 1 and 2 and not find b')

if 2:
    print('true')
else:
    print('false')
a = None
if a:
    print('None')
else:
    print('not None')

if a is None:
    print('None')
else:
    print('not None')

# 只有可迭代对象才能循环
a = '123456'
for sub_str in a:
    print sub_str
print("-------------")
a = [1, 2, 3, 4, 5, 6]
for item in a:
    print item
print("-------------")
a = {'name': "zhang", "age": 30}
for key in a:
    print(key, a.get(key))
print("-------------")
for key, value in a.iteritems():
    print(key, value)
print("-------------")
# break (退出循环),contiune（用于跳过该次循环）
a = '123456'
for item in a:
    if item == '5':
        break
    if item == '3':
        continue
    print(item)
print("-------------")
# while 条件为真进入循环，知道为假是跳出循环
index = 0
while index != 5:
    print(index)
    index += 1

