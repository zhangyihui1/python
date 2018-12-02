# -*- coding:utf-8 -*-
def func():
    print("this is a function!")


def func_parm(b=[]):
    print(b)
    b.append("4")


def func_args(a, *args, **kwargs):
    print(a)
    print("args:", args)
    print("kwargs:", kwargs)


def func_return(a):
    if a == '123':
        return True
    elif a == '456':
        return False
    elif a == 'abc':
        return a, 12


if __name__ == '__main__':
    func()
    a = [1, 2, 3]
    func_parm(b=a)
    print a
    print("-------------")
    func_parm()
    func_parm()
    print("-------------")
    # 可变参数 args, 关键字参数 kwargs
    func_args("123", "456", "789")
    func_args("123", "456", "789", name="zhang", age=30)
    print("-------------")
    print(func_return('123'))
    print(func_return('456'))
    print(func_return('789'))
    print(func_return('abc'))