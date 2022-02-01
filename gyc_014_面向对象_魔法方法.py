'''魔法方法'''

# python中有一类方法，以两个下划线开头,两个下划线结尾,并且在满足某个条件的情况下，会自动调用，这类方法称为魔法方法

# 学习：
# 1．什么情况下自动调用
# 2．有什么用,用在哪
# 3．书写的注意事项

# __init__方法
# 1．什么情况下自动调用
#     创建对象之后会自动调用
# 2．有什么用,用在哪
#     给对象添加属性的（初始化方法，构造方法）
#     某些代码，在每次创建对象之后，都要执行，就可以将这行代码写在__init__方法
# 3．书写的注意事项
#     不要写错了
#     如果init方法中，存在出了 self 之外的参数，在创建对象的时候必须传参


"""
猫类，属性 name,age,show_info(输出属性信息)
"""


class Cat:
    # 定义添加属性的方法
    def __init__(self):
        self.name = '蓝猫'  # 给对象个添加 name 属性
        self.age = 2  # 给对象添加 age 属性
        # 下方代码只是为了验证改方法被调用了，实际代码不要书写
        print('我是__init__，我被调用了')

    # 输出属性信息
    def show_info(self):
        print(f'小猫的名字是：{self.name},年龄是：{self.age}')


blue_cat = Cat()

print('-----------------------------------------------------------')


# 带参数的__init__魔法方法
# 给对象添加初始属性的
class Cat1:
    # 定义添加属性的方法
    def __init__(self, name, age):
        self.name = name  # 给对象个添加 name 属性
        self.age = age  # 给对象添加 age 属性
        # 下方代码只是为了验证改方法被调用了，实际代码不要书写
        print('我是__init__，我被调用了')

    # 输出属性信息
    def show_info(self):
        print(f'小猫的名字是：{self.name},年龄是：{self.age}')


blue_cat = Cat1('蓝猫', 2)
blue_cat.show_info()
'''
blue_cat = Cat1('蓝猫',2)
blue_cat.show_info()
以上创建对象，将属性传递给了Cat1()，就可以在show_info()方法中使用
# 对象的属性，只要变成属性了，就可以任意的函数中使用，忘记的话需要在本视频中多看几遍
https://www.bilibili.com/video/BV11g411V7Kf?p=62
'''

black_cat = Cat1('黑猫', 2)
black_cat.show_info()

print('-----------------------------------------------------------')


# __str__方法
# 1．什么情况下自动调用
#     使用print(对象)打印对象的时候会自动调用
# 2．有什么用,用在哪
#     在这个方法中一般书写对象的属性信息的，即打印对象的时候想要查看什么信息，在这个方法中进行定义的
#     如果类中没有定义__str__方法， print(对象），默认输出对象的引用地址
# 3．书写的注意事项
#     这个方法必须返回一个字符串

class Cat2:
    # 定义添加属性的方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('我是__init__，我被调用了')

    def __str__(self):
        # 这个方法返回一个字符串，只要是字符串就行
        return f'小猫的名字是：{self.name},年龄是：{self.age}'


blue_cat = Cat2('蓝猫', 2)
print(blue_cat)
black_cat = Cat2('黑猫', 2)
print(black_cat)

print('-----------------------------------------------------------')


# __del__方法 【了解就行】
# __init__方法，创建对象之后，会自动调用（构造方法）
# __del__方法，对象被删除销毁时，自动调用的（遗言，处理后事）（析构方法）
# 1．调用场景，程序代码运行结束，所有对象都被销毁
# 2．调用场景，直接使用del删除对象(如果对象有多个名字(多个对象引用一个对象)，需要吧所有的对象都删除才行)


class Demo:
    def __init__(self, name):
        print('我是__init__，我被调用了')
        self.name = name

    def __del__(self):
        print(f'{self.name}没了，给她处理后事')


# Demo('a')

a = Demo('a')
b = Demo('b')
del a  # 删除对象
print('代码运行结束')

print('-----------------------------------------------------------')

# 练习案例
'''
需求:
1.小明体重75.0 公斤
2.小明每次跑步会减肥0.5公斤
3.小明每次吃东西体重增加1公斤
'''


# 类名:人类Person
# 属性:姓名name,体重weight
# 方法:跑步run
#     吃东西eat
#     添加属性__init__
#     添加属性__str__

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"姓名：{self.name}，体重：{self.weight}kg"

    def run(self):
        print(f"姓名：{self.name}跑了5km，体重减少了")
        self.weight -= 0.5

    def eat(self):
        print(f"姓名：{self.name}大餐一顿，体重增加了")
        self.weight += 1


xm = Person('小明', 75.0)
print(xm)
xm.run()
print(xm)
xm.eat()
print(xm)