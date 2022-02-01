'''数据序列'''

'''字符串'''

# 字符串可以包含多个字符
# 使用引号（单引号，双引号，三引号）引起来的字符就是字符串

zifuc1 = 'hello'
print(zifuc1, type(zifuc1))
zifuc2 = "hello"
print(zifuc2, type(zifuc2))
zifuc3 = '''hello'''
print(zifuc3, type(zifuc3))

# 字符串本身包含单引号，定义的时候就不能使用单引号
zifuc4 = "I'm hello"
# 字符串中需要使用，使用\转义字符
zifuc5 = 'I\'m hello'
print(zifuc5, type(zifuc5))
zifuc6 = 'I\\\'m hello'
print(zifuc6, type(zifuc6))

# 字符串前边加上 r""原生字符串，字符串中的\不会作为转义字符
zifuc7 = r'I\'m hello'
print('zifuc7', zifuc7, type(zifuc7))

print('-----------------------------------------------------------')

# 字符串的下标

# 下标（索引），字符串字符中的位置编号，这个编号就是下标
# 这个编号一般都是从左到右的，python当中支持负数下标，就是从右到左

# 语法：
# 字符串[]

zifuc8 = 'abcdefg'
print(zifuc8[0])
print(zifuc8[-1])
zifucd = len(zifuc8)
print(zifuc8[zifucd - 1])

print('-----------------------------------------------------------')

# 字符串的切片

# 默认是1的可以不写，但是冒号必须有
# 切片会得到一个字符串，既可以获取字符串的多个字符

# 语法：
# 字符串[开始:结束:步长] #步长就字符串之间的差值

zifuc8 = 'abcdefg'
print(zifuc8[:3:])
print(zifuc8[4:7:])
print(zifuc8[-3:7:])
# 如果最后一个字符也要去，可以不写
print(zifuc8[-3::])
# 获取全部内容
print(zifuc8[::])
# 获取步长为2的
print(zifuc8[::2])
# 步长为负数，开始结束不变，意思全变
# 反转字符串
print(zifuc8[::-1])

print('-----------------------------------------------------------')

# 字符串的查找方法 find

# 开始：就是开水下标，默认为0
# 结束：就是结束下标，默认是len()
# sub_str:要查找的小的字符串
# 如果字符串找到sub_str，返回sub_str第一出现的整数下标
# 如果没有找到返回-1

# 语法：
# 字符串.find(sub_str,开始,结束)

zifuc9 = 'one piece is zhen shi cun zai'
fanhui = zifuc9.find(' ')
print(fanhui)

print('-----------------------------------------------------------')

# 字符串的查找方法 replace

# old_str
# new_str
# 次数：替换的次数，默认全部替换

# 语法：
# 字符串.replace(old_str,new_str,次数)

zifuc10 = 'one piece is zhen shi cun zai'
zifuc11 = zifuc10.replace('o', 'O')
print(zifuc11)
zifuc12 = zifuc10.replace('one piece', 'ONE PIECE')
print(zifuc12)

print('-----------------------------------------------------------')

# 字符串的差分 split

# sep：是字符串按照什么进行差分，默认是空白字符（空额，换行\n，teb键\t）
# max_split，是分割次数，一般不写，全部分割
# 返回：将以个字符串产拆分为多个，存在列表当中
# 如果sep不写，想要制定分割次数，字需要按照以下方式使用
# 字符串.split(maxsplit=n)

# 语法：
# 字符串.split(sep,maxsplit)

zifuc13 = 'one piece is zhen shi cun zai'
zifuc14 = zifuc13.split('is')
print('zifuc14', zifuc14)

zifuc15 = zifuc13.split(' ', 1)
print('zifuc15', zifuc15)
zifuc16 = zifuc13.split(maxsplit=1)
print('zifuc16', zifuc16)

print('-----------------------------------------------------------')

# 字符串的连接 join

# 括号中的内容主要是列表，也可以是其他容器
# 作用:将字符串插入到列表中每相邻的两个数据之间，
# 组成一个新的字符串-列表中的数据使用使用逗号隔开的
# 注意点:列表中的数据必须都是字符串,否则会报错

# 语法：
# 字符串.join(sep,maxsplit)

list1 = ['one', 'piece', 'is', 'zhen', 'shi', 'cun', 'zai']
zifuc17 = ' '.join(list1)
print('zifuc17', zifuc17)
