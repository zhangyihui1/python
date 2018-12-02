import sys
from classDemo import A as claasA
import classDemo
from module1 import test1
from module2 import test2

a = claasA()
a.func_a()
print(dir(classDemo))
a = classDemo.A()
a.func_a()
print("---------------")
print(dir(classDemo))
a = getattr(classDemo, 'A')
print(dir(a))
a().func_a()
print("---------------")
print(sys.path)
test1.func_test1()
print("---------------")
test2.func_test2()
