# -*- coding: utf-8 -*-
# 定义一个类
class A(object):

    # 类属性
    # 实例属性
    # 类方法
    # 实例方法
    # 静态方法

    # 类属性，直接在类中定义的属性是类属性
    # 类属性可以通过类或类的实例访问到
    # 但是类属性只能通过类对象来修改，无法通过实例对象修改
    count = 0

    def __init__(self):
        # 实例属性，通过实例对象添加的属性属于实例属性
        #   实例属性只能通过实例对象来访问和修改，类对象无法访问修改
        self.name = '孙悟空'

    # 实例方法
    #   在类中定义，以self为第一个参数的方法都是实例方法
    #   实例方法在调用时，Python会将调用对象作为self传入
    #   实例方法可以通过实例和类去调用
    #       当通过实例调用时，会自动将当前调用对象作为self传入
    #       当通过类调用时，不会自动传递self，此时我们必须手动传递self
    def test(self):
        print('这是test方法~~~ ' , self)

    # 类方法
    # 在类内部使用 @classmethod 来修饰的方法属于类方法
    # 类方法的第一个参数是cls，也会被自动传递，cls就是当前的类对象
    #   类方法和实例方法的区别，实例方法的第一个参数是self，而类方法的第一个参数是cls
    #   类方法可以通过类去调用，也可以通过实例调用，没有区别
    @classmethod
    def test_2(cls):
        print('这是test_2方法，他是一个类方法~~~ ',cls)
        print(cls.count)

    # 静态方法
    # 在类中使用 @staticmethod 来修饰的方法属于静态方法
    # 静态方法不需要指定任何的默认参数，静态方法可以通过类和实例去调用
    # 静态方法，基本上是一个和当前类无关的方法，它只是一个保存到当前类中的函数
    # 静态方法一般都是一些工具方法，和当前类无关
    @staticmethod
    def test_3():
        print('test_3执行了~~~')


a = A()
# 实例属性，通过实例对象添加的属性属于实例属性
# a.count = 10
# A.count = 100
# print('A ,',A.count)
# print('a ,',a.count)
# print('A ,',A.name)
# print('a ,',a.name)

# a.test() 等价于 A.test(a)

# A.test_2() 等价于 a.test_2()

A.test_3()
a.test_3()


