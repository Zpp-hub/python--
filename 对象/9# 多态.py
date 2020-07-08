# -*- coding: utf-8 -*-
# 多态是面向对象的三大特征之一
# 多态从字面上理解是多种形态
# 狗（狼狗、藏獒、哈士奇、古牧 。。。）
# 一个对象可以以不同的形态去呈现

# 1. 对象所属的类之间没有继承关系
class Duck(object):                                  # 鸭子类
    def fly(self):
        print("鸭子沿着地面飞起来了")

class Swan(object):                                  # 天鹅类
    def fly(self):
        print("天鹅在空中翱翔")

class Plane(object):                                 # 飞机类
    def fly(self):
        print("飞机隆隆地起飞了")

def fly(obj):                                        # 实现飞的功能函数
    obj.fly()

duck = Duck()
fly(duck)

swan = Swan()
fly(swan)

plane = Plane()
fly(plane)

# 对象所属的类之间有继承关系（应用更广）
class gradapa(object):
    def __init__(self, money):
        self.money = money

    def p(self):
        print("this is gradapa")


class father(gradapa):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job

    def p(self):
        print("this is father,我重写了父类的方法")


class mother(gradapa):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job

    def p(self):
        print("this is mother,我重写了父类的方法")
        return 100


# 定义一个函数，函数调用类中的p()方法
def fc(obj):
    obj.p()


gradapa1 = gradapa(3000)
father1 = father(2000, "工人")
mother1 = mother(1000, "老师")

fc(gradapa1)  # 这里的多态性体现是向同一个函数，传递不同参数后，可以实现不同功能.
fc(father1)
print(fc(mother1))








# 定义两个类
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass


a = A('孙悟空')
b = B('猪八戒')
c = C()


# 定义一个函数
# 对于say_hello()这个函数来说，只要对象中含有name属性，它就可以作为参数传递
#   这个函数并不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('你好 %s' % obj.name)

# 在say_hello_2中我们做了一个类型检查，也就是只有obj是A类型的对象时，才可以正常使用，
#   其他类型的对象都无法使用该函数，这个函数就违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型对象，这样导致函数的适应性非常的差
# 注意，向isinstance()这种函数，在开发中一般是不会使用的！
def say_hello_2(obj):
    # 做类型检查
    if isinstance(obj, A):
        print('你好 %s' % obj.name)
    say_hello(b)


say_hello_2(b)

# 鸭子类型
# 如果一个东西，走路像鸭子，叫声像鸭子，那么它就是鸭子

# len()
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取它的长度
l = [1, 2, 3]
s = 'hello'

# print(len(l))
# print(len(s))
print(len(b))
# print(len(c))

# 面向对象的三大特征：
#   封装
#       - 确保对象中的数据安全
#   继承
#       - 保证了对象的可扩展性
#   多态
#       - 保证了程序的灵活性
