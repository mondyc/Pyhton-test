'''字典'''

# 字典键值对组成
# key键：代表数据的名字
# value值：就是具体的数据
# 定义变量的方法
# 变量 = (key:value,key2:value2,....)
# 字典中的键，一般都是字符串，也可以是数字，但是不可以是list

print('-----------------------------------------------------------')

# 定义字典

# 类实例化的方法
zidian = dict()
print(type(zidian))

# 定义空字典
zidian2 = {}
print(type(zidian2))

# 定义非空字典
zidian3 = {'name': '小明', 'age': '18', 'height': '1.71'}
print(zidian3)
print(len(zidian3))

print('-----------------------------------------------------------')

# 增加修改操作
# 存在就修改，不存在就添加
# 语法：
# 字典[键] = 数据值
zidian4 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
zidian4['aihao'] = 'wan'
print(zidian4)
zidian4['name'] = '小红'
print(zidian4)
zidian4['xihuan'].append('huhuh')
print(zidian4)

print('-----------------------------------------------------------')

# 删除指定的键值对
# 语法：
# del 字典[键]
zidian5 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
del zidian5['name']
print(zidian5)

# 语法2：
# 字典.pop(键)
zidian7 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
zidian7.pop('age')
print(zidian7)

# 清空
# 语法：
# 字典.clear()
zidian6 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
zidian6.clear()
print(zidian6)

print('-----------------------------------------------------------')

# 字典的查询
# 字典中没有下标的概念
# 获取数据的需要使用key获取

# 键没有的话会报错
# 语法：
# 字典[键]
zidian8 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
print(zidian8['name'])
# print(zidian8['aaa']) 这段key不存在就报错了

# 如果键不存在返回None
# 语法2：
# 字典.get(键)
zidian9 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
print(zidian9.get('age'))
print(zidian9.get('aaa'))

# 获取字段中值为列表的数据
print(zidian9['xihuan'][1])

print('-----------------------------------------------------------')

# 字典的遍历

# 对字典的键遍历
# 语法：
# for 变量 in 字典:
#     print(变量)
zidian10 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
for i in zidian10:
    print(i)

# 语法2：
# for 变量 in 字典.keys():
#     print(变量)
zidian11 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
for i in zidian11.keys():
    print(i)

# 对字典的值遍历
# 语法：
# for 变量 in 字典.values():
#     print(变量)
zidian12 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
for i in zidian12.values():
    print(i)

# 对字典的键值对遍历
# 语法：
# for 变量1,变量2 in 字典.items():
#     print(变量1,变量2)
zidian13 = {'name': '小明', 'age': '18', 'height': '1.71', 'xihuan': ['hahah', 'heheh']}
for i, m in zidian13.items():
    print(i, m)
