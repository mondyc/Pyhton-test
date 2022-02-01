'''while循环'''

# 1、设置初始循环
# 2、书写循环条件

# 语法：
# while 判断条件:
#     需要重复执行的代码
#     改变循环的计数器

i = 0
while i <= 5:
    print(i)
    i = i + 1

print('-----------------------------------------------------------')

# 死循环和无限循环
# 死循环：一般是由写代码的人不小心造成的bug
# 无限循环：写循环的人故意让代码无限制的去执行，
# 所以在无线循环中，一般会增加一个 if 判断，当 if 成立后，使用 break 来终止执行
# 当不知道需要循环的次数后，会写无限循环
while True:
    gyc = input('请输入任意字符：')
    if gyc == '0':
        break

print('-----------------------------------------------------------')

# 练习
# 求1-100的和
i = 1
num = 0
while i <= 100:
    num = num + i
    i = i + 1
print(num)

# 练习
# 求1-100的偶数和
i = 1
num = 0
while i <= 100:
    # 判断是不是偶数
    if (i % 2 == 0):
        num = num + i
    i = i + 1
print(num)
