'''函数的进阶'''


# 返回值-返回多个数据值
# 使用return关键

# 讲多个数据值组成容器进行返回，一般是元组（组包）

def jisuan(a, b):
    num = a + b
    num1 = a - b
    return num, num1


# 写法1
result = jisuan(10, 5)
print(result, result[0], result[1])

# 写法2
x, y = jisuan(20, 10)
print(x, y)

print('-----------------------------------------------------------')


# 函数参数
# 形参的不同书写方法
# 函数传参的方式

def chuanan(a, b, c):
    print(a, b, c)


# 位置传参
# 在函数调用的时候,按照形参的顺序,将实参值传递给形参
chuanan(1, 2, 3)

# 关键字传参
# 在函数调用的时候,指定数据值给到那个形参
chuanan(a=1, b=2, c=4)

# 混合使用
# 关键字传参必须写在位置传参的后面
# 不要给一个形参传递多个数据值
chuanan(1, 3, c=4)

print('-----------------------------------------------------------')


# 缺省参数，默认参数

# 定义方式
# 在函数定义的时候，给形参一个默认的数据值，这个形参就变为缺省参数，注意，缺省参数的书写要放在普通参数的后边
# 特点：
# 缺省参数，在函数调用的时候，可以传递实参值，也可以不传递实参值
# 如果传参,使用的就是传递的实参值，如果不传参,使用的就是默认值

def moren(name, sex='保密'):
    print(name, sex)


moren("xianwang")
moren("xianwang", '男')

print('-----------------------------------------------------------')

# 多值参数【可变参数/不定长参数】

print(1)
print(1, 2)
print(1, 2, 3)
print(1, 2, 3, 4)


# 当我们在书写函数的时候，不确定参数的具体个数时，可以使用不定长参数

# 不定长位置参数(不定长元组参数)
# 1．在普通参数的前边,加上一个*，这个参数就变为不定长位置参数
# 2．特点，这个形参可以接收任意多个位置传参的数据
# 3．数据类型,形参的类型是元组
# 4．注意,不定长位置参数要写在普通的参数的后面
# 5，一般写法，不定长位置参数的名字为args 即(*args) # arguments


# 不定长关键字参数(不定长字典参数)
# 1．书写，在普通参数的前边,加上两个 *，这个参数就变为不定长关键字参数
# 2．特点，这个形参可以接收任意多个关键字传参的数据
# 3．数据类型,形参的类型是字典
# 4，注意,不定长关键字参数,要写在所有参数的最后边
# 5，一般写法，不定长关键字参数的名字为 kwargs，即(**kwargs)，keyword arguments


# 完整的参数顺序
# 一般在使用的时候,使用1-2种，按照这个顺序挑选书写即可
# 语法：
# def 函数名(普通函数,*args,缺省参数,**kwargs):
#     pass
def budingc(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    print(' -' * 30)


budingc()
budingc(1, 2, 3)  # 位置传参，数据都给args
budingc(a=1, b=2, c=3)  # 关键字传参，数据都给kwargs
budingc(1, 2, 3, a=4, b=5, c=6)

print('-----------------------------------------------------------')

# print()函数解析
# sep=' '， 多个位置参数之间的间隔
# end='\n' 每一个print函数结束，都会打印的内容结束符
print(1, end=' ')
print(2, end=' ')
print(3)
print(1, 2, 3, 4, 5, 6, sep='_')
print(1, 2, 3, 4, 5, 6, sep='_*_')

print('-----------------------------------------------------------')


# 入参为列表，拆包操作
def my_sum(*args, **kwargs):
    num = 0  # 定义变量,保存求和的结果
    for i in args:
        num += i
    for j in kwargs.values():
        num += j
    print(num)


# 需求，
# my_list = [1，2，3，4]
# 字典my_dict = { 'a': 1，'b': 2， 'c ': 3, 'd ': 4}

my_list = [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2, 'c ': 3, 'd ': 4}
# 将字典和列表中的数据使用my_sum函数进行求和，改如何传参的问题
# my_sum(1,2，3，4)
# my_sum (a=1,b=2,c=3,d=4)

# 想要将列表中的数据分别作为位置参数,进行传参,需要对列表进行拆包操作
my_sum(*my_list)  # my_sum(1,2,3,4)

# 想要将字典中的数据,作为关键字传参,，需要使用 **对字典进行拆包
my_sum(**my_dict)  # my_sum(a=1,b=2,c=3,d=4)

print('-----------------------------------------------------------')


# 匿名函数
# 就是使用lambda定义的函数
# 一般称为使用 def 关键字定义的韩式为，标准函数

# 匿名函数只能写一行代码
# 匿名函数的返回不需要 return，一行代码（表达式）的结果就是返回值
# 语法：
# lambda 参数:一行代码  这一行代码我们称为表达式

# 匿名函数一般不需要我们主动的调用，一般作为函数的参数使用的
# 我们在学习阶段为了查看匿名函数定义的是否正确,可以调用
# 1．在定义的时候,将匿名函数的引用保存到一个变量中变量= lambda参数:一行代码
# 2．使用变量进行调用
# 变量()

# 一、无参数，无返回值
def niming():
    print('gugugu')


niming()
# lambda: print('gugugu') # 匿名函数的定义
# 匿名函数一般不起名，不调用
niming2 = lambda: print('gugugu')
niming2()


# 二、无参数，有返回值
def niming3():
    return 10


print(niming3())

niming4 = lambda: 10
print(niming4())


# 三、有参数，无返回值
def qiuhe1(a, b):
    print(a + b)


qiuhe1(1, 3)

qiuhe2 = lambda a, b: print(a + b)
qiuhe1(10, 20)


# 四、有参数，有返回值
def qiuhe3(a, b):
    return a + b


print(qiuhe3(1, 4))

qiuhe4 = lambda a, b: a + b
print(qiuhe3(1, 5))

# 1．定义一个匿名函数可以求两个数的乘积（参数需要两个，)
func1 = lambda a, b: a * b
print(func1(1, 2))
print(func1(3, 2))
# 2．定义一个匿名函数，参数为字典,返回字典中键为aqe 的值
# 参数只是一个占位的作用,定义的时候没有具体的数据值，形参的值是在调用的时候进行传递,此时,形参才有数据值
# 形参的类型就是由实参来决定的，在函数定义的时候,参数只是一个符号,写什么都可以，想让其是字典类型,只需要保证
# 实参是字典即可
func2 = lambda x: x.get('age')
func3 = lambda x: x['age']

my_dict = {'name': '张三', 'age': 18}
print(func2(my_dict))
print(func3(my_dict))

print('-----------------------------------------------------------')

# 匿名函数的应用：作为其他的函数的参数
# 列表中的字段排序
user_list = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]

# user_list.sort()
# 列表的排序，默认是对列表中的数据进行比大小的，可以对数字类型和字符串进行比大小,
# 但是对于字典来说,就不知道该怎么比大小，此时,我们需要使用sort函数中的key这个参数，来指定字典比大小的方法
# key这个参数，需要传递一个函数,一般是匿名函数，字典的排序,其实要指定根据字典的什么、键进行排序，我们只需要使用
# 匿名函数返回字典的这个键对应的值即可
# 列表.sort(key=lambda x:[键])
# 根据年龄排序
user_list.sort(key=lambda x: x['age'])
user_list.sort(key=lambda x: x['age'], reverse=True)
print(user_list)

# user_List.sort( key=Lambda x: x['age'])
# 说明:匿名函数中的参数是列表中的数据，在 sort函数内部,会调用key这个函数(将列表中每个数据作为实参传递给形参),
# 从列表中的获取函数的返回值，对返回值进行比大小操作

print('-----------------------------------------------------------')

# 字符串的比大小
# 字符串的比大小，是比较字符对应的 ASCII码值
# A<Z < a < z
# ord(字符)  # 获取字符对应的ASCII的值
# chr(ASCII值) # 获取对应的字符
# 字符串比大小:
# 对应下标位置字符的大小
