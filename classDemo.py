# -*- coding:utf-8 -*-
class A(object):
    class_attr = 'class'

    def __init__(self):
        print("A __init__")
        self.self_attr = "self_a"
        self.__private_attr = "private_attr_a"

    def func(self):
        print('a', dir(self))
        print(self.class_attr)
    # 只能在内部使用,实例属性都无法使用
    def __private_func_a(self):
        print("this is private function", self.__private_attr)

    def func_a(self):
        print("this is A function: ", self.self_attr)
        self.__private_func_a()

    @classmethod
    def func_class(cls):
        print('a', dir(cls))
        #print(cls.self_attr)

    @staticmethod
    def func_static():
        print("this is a static function")


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.self_attr = "self_b"

    def func(self):
        print("this is B function")

    def func1(self):
        print("this is B function1")


class C(object):
    def __init__(self):
        print("C __init__")
        self.self_attr = "self_c"
        self.self_c_attr = "__self_c"

    def func_c(self):
        print("this is c function", self.self_attr)
        #print("this is c function", self.self_c_attr)


class D(A,C):
    def __init__(self):
        super(D, self).__init__()
        
if __name__ == '__main__':
    a = A()
    b = A()
    dir(a)
    print("--------------")
    a.func()
    a.func_a()
    print("--------------")
    a.func_class()
    print("--------------")
    A.class_attr = "class1"
    a.self_attr = "self1"
    print(a.class_attr)
    print(b.class_attr)
    print(a.self_attr)
    print(b.self_attr)
    a.class_attr = "class2"
    print(a.class_attr)
    print(b.class_attr)
    print("--------------")
    A.func_static()
    print("--------------")
    b = B()
    print('b', dir(b))
    print("--------------")
    b.func()
    # 注意self.self_attr的值
    b.func_a()
    print("--------------")
    # 判断b 是否是a 的子类
    print(isinstance(b, A))
    print("--------------")
    # 多继承
    d = D()
    print(dir(d))
    d.func_c()
