'''封装'''
'''就是定义类的过程'''

# 封装(定义类的过程)
#     案例(存放家具)
# 继承
# 多态
# 封装的补充
#     私有和公有权限
#     属性的分类(实例属性,类属性)
#     方法的分类(实例方法,类方法,静态方法)

# 练习案例2
'''
需求:
1.房子(House)有户型、总面积和家具名称列表
    新房子没有任何的家具
2家具(Houseltem)有名字和占地面积，其中
    席梦思(bed)占地4平米
    衣柜(chest)占地2平米
    餐桌(table)占地1.5平米
3.将以上三件家具添加到房子中
4.打印房子时，要求输出:户型、总面积、剩余面积、家具名称列表

剩余面积
1．在创建房子对象时，定义一个剩余面积的属性，初始值和总面积相等
2．当调用add_item方法，向房间添加家具时，让剩余面积-=家具面积

'''


# 类名:房子
# 属性:户型 name、总面积area、剩余面积total_area、家具名称列表 item_list=[]
# 方法:
# 添加属性__init__
# 添加属性__str__
# 添加家具方法 add_item：
#    先判断房子的剩余面和总面积的关系
#    修改房子的剩余面积
#    修改房子的家具名称列表

# 类名:家具类
# 属性:名字 name 占地面子 area
# 方法:
# 添加属性__init__
# 添加属性__str__

# 定义家具类
class HouseItem:
    # 定义家具类
    def __init__(self, name, area):
        '''添加属性的方法'''
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名字{self.name}，占地面积{self.area}平米'


class House:
    """房子类"""

    def __init__(self, name, area):
        self.name = name  # 户型
        self.total_area = area  # 总面积
        self.free_area = area  # 剩余面积
        self.item_list = []  # 家具名称列表

    def __str__(self):
        return f"户型:{self.name}，总面积:{self.total_area}平米，剩余面积:{self.free_area}平米，" \
               f"家具名称列表:{self.item_list}"

    def add_item(self, item):  # 表示的家具的对象
        # 判断房子的剩余面积(self.free_area)和家具的占地面积之间的关系
        # seLf表示的房子对象,缺少一个家具对象
        if self.free_area > item.area:
            # 添加家具，向列表添加数据
            self.item_list.append(item.name)
            # 修改剩余面积
            self.free_area = self.free_area - item.area
            print(f'{item.name} 添加成功')
        else:
            print('剩余面具不足，换的')


# 创建家具对象
bed = HouseItem('新梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
house = House('三室一厅', 150)
print(house)
# 添加床
house.add_item(bed)
print(house)

print('-----------------------------------------------------------')

# 封装案例
'''
需求:某web项目登录页面包含:用户名，密码，验证码，
登录按钮和登录的方法书写代码实现以上功能,登录方法中使用print输出即可

类名: LoginPage
属性:用户名(username)，密码(password)，验证码(code)，登录按钮(button)
方法:登录(login)__init__
'''


class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code
        self.btn = '登录'

    def login(self):
        print(f'1.输入用户名{self.username}')
        print(f'2.输入密码{self.password}')
        print(f'3.输入验证码{self.code}')
        print(f"4.点击按钮{self.btn}")


login = LoginPage('admin', '123456', '8888')
login.login()

print('-----------------------------------------------------------')

# 私有和公有

# 1．在 Python中定义的方法和属性，可以添加访问控制权限(即在什么地方可以使用这个属性和方法)
# 2．访问控制权限分为两种，公有权限，私有权限
# 3．公有权限
#     >直接书写的方法和属性,都是公有的
#     >公有的方法和属性,可以在任意地方访问和使用
# 4．私有权限
#     >在类内部，属性名或者方法名前边加上两个下划线，这个属性或者方法就变为私有的
#     >私有的方法和属性，只能在当前类的内部使用
# 5．什么时候定义私有
#     >1．某个属性或者方法，不想在类外部被访问和使用，就将其定义为私有即可
#     >2．测试中，一般不怎么使用，直接公有即可
#     >3．开发中，会根据需求文档，确定什么作为私有
# 6．如果想要在类外部操作私有属性，方法是，在类内部定义公有的方法，我们通过这个公有方法去操


# 案例
'''
定义一个 Person类，属性name，age(私有)
'''


class Person:
    def __init__(self, name, age):
        # 私有的本质，是 Python解释器执行代码，发现属性名或者方法名前有两个_，会将这个名字重命名
        # 会在这个名字的前边加上_类名前缀,即self._age ===> self._Person__age
        self.name = name  # 姓名
        self.__age = age  # 年龄，将其定义为私有属性,属性名前加上两个_

    def __str__(self):
        return f'名字：{self.name}，年龄：{self.__age}'


xm = Person('小明', 18)
print(xm)
# 在类外部直接访问 age 属性
# print(xm.__age) #在类外部不能直接使用私有属性
print(xm.__dict__)

xm.__age = 20  # 这个不是修改私有属性,是添加了一个公有的属性_age
print(xm.__dict__)
xm.age = 20
print(xm)  # 名字:小明，年龄:18
print(xm._Person__age)  # 能用但是不要用
xm._Person_age = 19
print(xm)  # 名字:小明，年龄:19

# 补充:
# 对象.__dict__魔法属性，可以将对象具有的属性组成字典返回
