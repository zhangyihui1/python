class Animal(object):
    def __init__(self):
        pass

    def speak(self):
        print("animal speak")


class Dog(Animal):
    def __init__(self):
        pass

    def speak(self):
        print("dog speak")


class Cat(Animal):
    def __init__(self):
        pass

    def speak(self):
        print("cat speak")


def speak(animal=Animal()):
        animal.speak()


speak(Dog())
speak(Cat())
speak()


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_email(self, email):
        self.email = email

    def do_print(self):
        if hasattr(self, 'email'):
            print(self.name, self.age, self.email)
        else:
            print(self.name, self.age)


class Classes(object):
    def __init__(self, name):
        self.name = name
        self.person_list = []

    def set_person(self, person):
        self.person_list.append(person)

    def get_person(self, name):
        result = None
        for item in self.person_list:
            if item.name == name:
                result = item
                break
        return result

    def _print(self):
        for item in self.person_list:
            item.do_print()


c = Classes("one")
c.set_person(person=Person("zhang", 30))
c.set_person(person=Person("lisi", 20))
c.set_person(person=Person("wang", 40))
c.set_person(person=Person("zhao", 60))
lisi = c.get_person("lisi")
lisi.set_email("111@qq.com")
print("-----------------")
c._print()

print("-----------------")


# self and cls
class A(object):
    class_attr = "class_a"

    @classmethod
    def set_class_method(cls, class_attr):
        cls.class_attr = class_attr


a = A()
b = A()
a.class_attr = 'class_1'
a.set_class_method('class_2')
#a.class_attr = 'class_1'
print(a.class_attr)
print(b.class_attr)

