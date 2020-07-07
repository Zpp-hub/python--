# -*- coding: utf-8 -*-

print('------------------------ 创建一个空的类 --------------------------')
a = int(10)   # 创建一个int类的实例
b = str('hello')   # 创建一个str类的实例
class MyClass():
    pass
print(MyClass)
mc = MyClass()   # mc就是通过MyClass创建的对象，mc是MyClass的实例
print(isinstance(mc, MyClass))
print(isinstance(mc, str))
print(mc, type(mc))

# 可以添加变量和属性，语法：对象.属性名 = 属性值
mc.name = 'zpp'
print(mc.name)

print('------------------------ 创建一个非空的类 ------------------------')
class Person:
    # 类中的变量我们叫属性，所有实例都可以访问
    name = 'zpp'
    # 类中的函数我们叫方法， 这些方法可以通过该类的所有实例来访问
    def say_hello(self):
        #   方法每次调用的时候，解析器都会自动传入第一个实参， 指代实例
        #   第一个参数，就是调用方法的对象本身，
        #   如果是p1调的，则第一个参数就是p1对象
        #   一般我们都会将这个参数命名为self

        #   在方法中不能直接访问类中的属性，要加self
        print('你好！我是 %s' % self.name)

p1 = Person()
print(p1.name)
p1.say_hello()

p1.name = 'anan'
print(p1.name)
p1.say_hello()

print('------------------------ 对象的初始化 ------------------------')
class Person :
    # 在类中可以定义一些特殊方法（魔术方法）
    # 特殊方法都是以__开头，__结尾的方法
    # 特殊方法不需要我们自己调用，不要尝试去调用特殊方法
    # 特殊方法将会在特殊的时刻自动调用
    # 学习特殊方法：
    #   1.特殊方法什么时候调用
    #   2.特殊方法有什么作用
    # 创建对象的流程
    # p1 = Person()的运行流程
    #   1.创建一个变量
    #   2.在内存中创建一个新对象
    #   3.__init__(self)方法执行
    #   4.将对象的id赋值给变量

    # init会在对象创建以后离开执行
    # init可以用来向新创建的对象中初始化属性
    # 调用类创建对象时，类后边的所有参数都会依次传递到init()中
    def __init__(self, name):
        print(self)
        # 通过self向新建的对象中初始化属性
        self.name = name

    def say_hello(self):
        print('大家好，我是%s' % self.name)
#   目前来讲，对于Person类来说name是必须的，并且每一个对象中的name属性基本上都是不同
#   而我们现在是将name属性在定义为对象以后，手动添加到对象中，这种方式很容易出现错误
#   我们希望，在创建对象时，必须设置name属性，如果不设置对象将无法创建
#   并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成
p1 = Person('魏无羡') # 这就是一个对象，一个实例化后的对象
print(p1.name)
p1.say_hello()
print('------------------------ 练习 ------------------------')
class Dog:
    '''
        表示狗的类
    '''
    def __init__(self , name , age , gender , height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        '''
            狗叫的方法
        '''
        print('汪汪汪~~~')

    def yao(self):
        '''
            狗咬的方法
        '''
        print('我咬你~~')

    def run(self):
        print('%s 快乐的奔跑着~~'%self.name)


d = Dog('小黑', 8, 'male', 30)

d.name = '阿黄'
d.age = -10
d.run()
print(d.age)