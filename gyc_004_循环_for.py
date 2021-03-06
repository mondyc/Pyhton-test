'''for循环'''

# for循环也可以让指定的代码重复执行（循环)
# for循环可以遍历容器中的数据(
# 遍历:从容器中把数据一个一个取出
# 容器:可以简单理解为盒子，盒子中可以存放很多的数据
# （字符串str，列表list，元组tuple，字典dict)
# for循环也可以称为for遍历
#1、for和 in都是关键字
#2、容器中有多少个数据,循环会执行多少次(0个数据,执行日次，...)
#3、每次循环,会将容器中数据取出一个保存到in 关键字前边的变量中

# 语法：
# for 变量名 in 容器
#     重复执行的代码

rongqi = '5' #定义字符串
for i in rongqi:
    print('我去')
    print(i)

print('-----------------------------------------------------------')

# for 指定次数的循环

# 语法：
# for 变量 in range(n):
#     重复执行的代码
# range(n)是python中的函数，作用是生成[0,n)之间的整数，不包含n，有一个n个数字，所以循环n次
# 想让for循环循环多少次，n就写几
# 变量值也是每次循环从[0,n)去一个值，第一次取得是0，最后取的是n-1
for i in range(5):
    print(i)

print('-----------------------------------------------------------')

# range()变形
# 语法：
# for 变量 in range(a,b):
#     重复的代码
for m in range(5,11):
    print(m)

print('-----------------------------------------------------------')

# break 和 continue
# break 和 continue 是python中的两个关键字
# break：终止循环，代码执行遇到break，循环不在执行，立即结束
# continue：跳过本次循环，代码执行遇到continue，本次循环剩下的代码不在执行，继续执行下一次循环
zifu = input('请输入任意字符')
for i in zifu:
    #在遍历的时候,如果这个字符是e，不打印(即后续的代码不执行)
    if i == 'e' :
        continue #本次循环后续的代码不执行,执行下一次循环print(i).
    print(i)   # !!!! print(i)不能写在if的下面，在这代码里面如果不满足if条件 就不执行print(i)

# 或者

for i in zifu:
    if i !='e':
        print(i)