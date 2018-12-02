# -*- coding:utf-8 -*-

a = 1
b = "1234"
c = 123.456
d = [1, '1234', 'abc']
e = (1,)
f = {'name': 'zhang', 'age': 30}
g = set(f)
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print("-----------------")
print(a, id(a))
a = 2
print(a, id(a))
# list、set、dict：是不可哈希的
# f = {d: 123}
# int、float、str、tuple：是可以哈希的
print("a __hash__:", a.__hash__)
print("b __hash__:", b.__hash__)
print("c __hash__:", c.__hash__)
print("d __hash__:", d.__hash__)
print("e __hash__:", e.__hash__)
print("f __hash__:", f.__hash__)
print("g __hash__:", g.__hash__)
print("-----------------")
# list set , tuple str, dict: 可迭代对象
# int float: 不是可迭代对象
#print(iter(a))
print(iter(e))
print(dir(f))
print("-----------------")
print(dir(a))
print("-----------------")
# str 常用函数
a = "123:456"
print(a.split(":"))
print(a.find('4'))
print(a.replace("123", 'abc'))
print(a[1:3])
print("-----------------")
# list 常用方法
d.append("efg")
print(d)
d.pop(0)
print(d)
d.extend("12")
print(d)
d.remove("efg")
print(d)
print("-----------------")
# dict  常用方法
print(f.get("name", None))
print(f['name'])
f.setdefault("address", "shanghai")
print f
f['address'] = "beijing"
print f
f.pop('address')
print f
# 3,x 去掉了 dict.items() 方法
print(f.items())
print(f.iteritems())
print(f.iterkeys(), f.itervalues())