"""
ONE PIECE 是真实存在的！
人的梦想是不会终结的
"""

# 打印的使用
print("hello world")

# 变量的使用
name = 'zhangsan'
print(name)

# 格式化输出
name = '小明'
age = 18
shengao = 1.71
print('我的名字叫%s,我的年龄是%d,我的身高%.2fm' % (name, age, shengao))
print('我的年龄是%06d' % (age))

# 显示百分号 %%
print('考试及格率%d%%' % (age))

# F-string 格式化方法，使用需要python版本>3.6
# 需要在字符串前面加上f'' 或者 F""
# 占位符统一使用{}
# 需要填充的变量 写在{}中
print(f'我的名字叫{name},我的年龄是{age},我的身高{shengao}m')
print(f'我的名字叫{name},我的年龄是{age:06d},我的身高{shengao:.2f}m,\n哈哈哈')

# 字符串格式化补充
# 在需要使用变量的地方使用{}占位
# '{},{},....'.format(变量，变量，....)
print('我的名字叫{},我的年龄是{:06d},我的身高{:.2f}m,\n哈哈哈'.format(name, age, shengao))
