'''面向对象'''

# 基本的介绍

# 面向对象是一个编程思想（写代码的套路）

# 编程思想：
# 1、面向过程
# 2、面向对象
# 以上两种都属于写代码的套路（方法），最终目的都是为了将代码写出来，只不过过程和思考方法不太一样

# 面向过程
#     关注的是具体步骤的实现,所有的功能都自己书写
#     亲力亲为
#     定义一个个函数，最终按照顺序调用函数

# 面向对象
#     关注的是结果,谁(对象)能帮我做这件事
#     偷懒
#     找一个对象(),让对象去做

# 类和对象
# 面向对象的核心思想是找一个对象去帮我们处理事情
# 在程序代码中 对象 是由 类 创建的

# 类和对象,是面向对象编程思想中非常重要的两个概念

# 类：
#     抽象的概念，对多个特征和行为相同或者相似事物的统称
#     泛指的(指代多个,而不是具体的一个)

# 对象：
#     具体存在的一个事物,看得见摸得着的
#     特指的(指代一个)

# 类的组成
# 1、类名（给这多个事物起一个名字，在代码中满足大驼峰命名法(每个单词的首字母大写）
# 2、属性（事物的特征，一般文字中的名词）
# 3、方法（事物的行为，即做什么事，一般是动词）

# 类的抽象
# 类的抽象,其实就是找到类的类名,属性和方法

print('-----------------------------------------------------------')


# 需求:
# 小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
# 小美今年17岁，身高1.65，小美不跑步，小美喜欢吃东西
# 类名:人类(Person，People)
# 属性:名字(name)，年龄( age)，身高( height)
# 方法:跑步(run)，吃(eat)

# 需求:
# 一只黄颜色的狗狗叫大黄
# 看见生人汪汪叫
# 看见家人摇尾巴
# 类名:狗类(Dog)
# 属性:颜色(color)，名字(name)
# 方法:汪汪叫(bark)，摇尾巴(shake)

# 面向代码的步骤
# 1．定义类，在定义类之前先设计类
# 2．创建对象，使用第一步定义的类创建对象
# 3．通过对象调用方法

# 面向对象基本代码的书写

# 1、定义类
# 先定义简单的类，不包含属性，在python中定义类需要使用关键字class
# 方法:方法的本质是在类中定义的函数，只不过,第一个参数是self
# 语法：
# class 类名:
#     在缩进中书写的内容，都是内容的代码
#     def 方法名(self): # 就是一个方法
#         pass

# 2、创建对象
# 创建对象是使用类名()进行创建，即
# 类名() #创建一个对象，这个对象在后续不能使用
# 创建的对象想要在后续的代码中继续使用，需要使用一个变量,将这个对象保存起来
# 一个类可以创建多个对象，只要出现类名()就是创建一个对象,每个对象的地址是不一样的
# 语法：
# 变量=类名() #这个变量中保存的是对象的地址，一般可以成为这个变量为对象


# 3、调用方法
# 语法：
# 对象.方法名()

# 4、案例的实现
# 需求：小猫爱吃鱼，小猫要喝水
# 类名：猫类
# 属性：暂无
# 方法：吃鱼，喝水

# 定义类
class Cat:
    # 在缩进中书写 方法
    def eat(self):  # self会自动出现
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建对象
blue_cat = Cat()

# 通过对象调用类中的方法
blue_cat.eat()
blue_cat.drink()

print('-----------------------------------------------------------')


# self的说明
class Cat1:
    def eat(self):
        print(f'id{self},self')
        print("小猫爱吃鱼")


# 1．从函数的语法上讲，self是形参，就可以是任意的变量名，只不过我们习惯性将这个形参写作self
# 2．self 是普通的形参，但是在调用的时候没有传递实参值，原因是python解释器在执行代码的时候，会自动将调用这个方法的对象 传递给了 self ，即self的本质就是对象
# 3．验证，只需要确定通过哪个对象调用，对象的引用和self 的引用是一样的
blue_cat1 = Cat1()
print(f'id{blue_cat1},blue_cat1')  # blue_cat 对象调用eat方法，解释器将blue_cat对象传给了self
blue_cat1.eat()

black_cat1 = Cat1()
print(f'id{black_cat1},blue_cat1')  # black_cat 对象调用eat方法，解释器将blue_cat对象传给了self
black_cat1.eat()

print('-----------------------------------------------------------')


# 对象的属性操作

# 添加属性
# 语法：
# 对象.属性名 = 属性值

# 类内部添加，self是对象
# self.属性名 = 属性值
# 在内种添加属性一般写作__init__方法中

# 类外部添加
# 对象.属性名 = 属性值 #一般不使用

# 获取属性
# 语法：
# 对象.属性名

# 类内部
# 在内部方法中，self是对象
# self.属性名

# 类外部
# 对象.属性名 #一般很少使用

class Cat2:
    def eat(self):
        print(f'id{self},self')
        print(f"小猫{self.name}爱吃鱼")


blue_cat2 = Cat2()
print(f'id{blue_cat1},blue_cat1')
blue_cat2.name = '蓝色'
blue_cat2.eat()

black_cat2 = Cat2()
print(f'id{blue_cat1},blue_cat1')
black_cat2.name = '黑色'
black_cat2.eat()

print(16*16)