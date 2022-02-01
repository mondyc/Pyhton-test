'''列表'''

# list是使用最多的一种容器
# 列表中可以存储多个数据，每个数据用逗号隔开
# 列表可以存放任意数据

# 定义空列表
list1 = list()
print(type(list1), list1)
# 类型转换
list2 = list('hello')
print(type(list2), list2)
# 定义非列表
list3 = [1, 'xiaoming', 3.13, False]
print(type(list3), list3)

print('-----------------------------------------------------------')

# 列表的切片
# 切片操作和字符串的方法是一致的
# 区别：列表的切片得到结果是列表
list4 = [1, 'xiaoming', 18, False]
print(list4[0])
print(list4[-1])
# 获取两个数据
print(list4[0:2])
# 列表支持长度
print(len(list4))

print('-----------------------------------------------------------')

# 列表的中数据下标
# 和find方法一样，同事字符串中也有index
# 区别：返回index()，找到第一次出现的下标，没有找到直接报错
# 语法：
# 列表.index(数据,开始,结束)
list5 = [1, 'xiaoming', 18, False]
num = list5.index(False)
print(num)

# 判断是否存在
# 判断容器中某个数据是否存在是否存在
# 语法：
# 数据 in 容器 # 如果存在返回 True ，如果不存在，返回 False

list24 = [1, 'xiaoming', 18, False]
print('xiaoming' in list24)

# 统计出现次数
# 统计出现的次数，使用count()方法
# 语法：
# 列表.count(数据) #返回出现的次数
list6 = [1, 'xiaoming', 18, False]
num = list6.count(False)
print(num)

print('-----------------------------------------------------------')

# 列表添加数据

# 尾部添加
# 返回:返回的 None(关键字,空)，一般就不再使用变量来保存返回的内容想要查看添加后的列表,需要打印的是列表
# 语法：
# 列表.append(数据)
list7 = []
list7.append(123)
print(list7)

list7.append(321)
print(list7)

list9 = [456, 789]
list7.append(list9)  # 也可以直接添加整个列表
print(list7)

# 指定下标添加
# 如果指定的下标已经有数据了，本位置的数据会后移
# 返回:返回的 None(关键字,空)，一般就不再使用变量来保存返回的内容想要查看添加后的列表,需要打印的是列表
# 语法：
# 列表.insert(下标,数据)
list7.insert(1, '大少爷')
print(list7)

# 列表合并
# 将列表2的数据逐个到列表1
# 返回:返回的 None(关键字,空)，一般就不再使用变量来保存返回的内容想要查看添加后的列表,需要打印的是列表
# 语法：
# 列表1.extend(列表2)
list8 = [456, 789]
list7.extend(list8)
print(list7)

print('-----------------------------------------------------------')

# 列表修改数据

# 语法：
# 列表[下标] = 数据

list10 = [1, 2, 18, 3]
list10[1] = 3
print(list10)

print('-----------------------------------------------------------')

# 列表删除数据

# 根据下表删除
# 下标不写，默认删除左右一个数据常用
# 语法：
# 列表.pop(下标)
# 返回:是删除数据
list11 = [1, 2, 18, 3]
num = list11.pop()
print(list11)
print(num)

# 根据数据值删除
# 语法:
# 列表.remove(数据值)
# 返回:None
list12 = [1, 2, 18, 3]
list12.remove(3)  # 列表中有多个数据，只能删除第一个
print(list12)

# 清空数据（一般不用）
# 语法:
# 列表.clear()
list13 = [1, 2, 18, 3]
list13.clear()
print(list13)

print('-----------------------------------------------------------')

# 列表的反转倒置
# 语法:
# 列表[::-1] #回得到一个列表
list14 = [1, 2, 18, 3]
list15 = list14[::-1]
print(list15)
print(list14)

# 语法2:
# 列表.reverse()
list16 = [1, 2, 18, 3]
list16.reverse()
print(list16)

print('-----------------------------------------------------------')

# 列表的复制
# 语法:
# 变量 = 列表1[:]
list17 = [1, 2, 18, 3]
list18 = list17[:]
print(list18)

# 语法2:
# 变量 = 列表.copy()
list19 = [1, 2, 18, 4]
list20 = list19.copy()
print(list20)

print('-----------------------------------------------------------')

# 列表的排序
# 一般来说是对数字进行排序
# 语法:
# 列表.sort() # 默认按照升序排序，从小到大
list21 = [1, 2, 18, 4]
list21.sort()
print(list21)

# 列表.sort(reverse=True) # 降序
list22 = [1, 2, 18, 4]
list21.sort(reverse=True)
print(list21)

print('-----------------------------------------------------------')

# 列表的嵌套
# 列表中的内容还是列表
list23 = [[1, 2, 18, 4], [3, 7, 21, 9]]
print(list23[0])
print(list23[0][0])

list23[1].append(5)  # 在嵌套列表中添加数据
print(list23[1])

print('-----------------------------------------------------------')
'''
# 判断容器中某个数据是否存在是否存在
# 语法：
# 数据 in 容器 # 如果存在返回 True ，如果不存在，返回 False
'''
# 列表去重
# 语法1
# 可以用in的方法
# 写法1
list30 = [1, 2, 18, 4, 1]
list31 = []
for i in list30:
    if i in list31:
        pass
    else:
        list31.append(i)
print(list31)

# 写法2
list32 = [1, 2, 18, 4, 1]
list33 = []
for m in list32:
    if m not in list33:
        list33.append(m)
print(list33)

# 语法2
# 容器列表转换类型为集合 set 会自动去重
# 集合 set 不允许有重复数据
list31 = [1, 2, 18, 4, 1]
set1 = set(list31)
print(set1)
