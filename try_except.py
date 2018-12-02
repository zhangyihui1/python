# -*- coding:utf-8 -*-

# a = 1/0
try:
    a = 1/0
    a = 1/1
except (ZeroDivisionError, Exception) as e:
    print(e)
else:
    print("no exception")
finally:
    print("done")


f = open("111.txt", 'r')
print(f.read())
f.close()
with open("111.txt", 'r') as f:
    print(f.read())
print("----------------")


class OpenTxt(object):
    def __init__(self):
        print("__init__")

    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def do_something(self):
        print(1/0)

    def __enter__(self):
        self.set_up()
        return self

    # retrun true (不会抛出异常) , false(抛出异常)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exc_type',exc_type)
        print('exc_val', exc_val)
        print('exc_tb', exc_tb)
        self.tear_down()
        return True


with OpenTxt() as f:
    f.do_something()
