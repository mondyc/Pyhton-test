'''函数的参数'''


# a和b定义函数的时候的参数，占位的作用，没有具体的值，称为 形参

def qiuhe(a=2, b=4):
    # 这时的a和b是可以设置为默认值，调用的时候，如果不入参，默认的参数
    sum = a + b
    print(sum)


# 调用时必须传递参数，而且要一一对应
qiuhe(30, 45)  # 这是调用函数传递的参数，称为 实参
qiuhe()  # 不入参使用默认值

print('-----------------------------------------------------------')


# 函数的返回值
# 为了在后续代码中使用，函数的结果
def qiuhe2(a, b):
    # 这时的a和b是可以设置为默认值，调用的时候，如果不入参，默认的参数
    sum = a + b
    return sum  # 只能在函数中使用，函数代码遇到函数遇到return会结束
    print('我是return之后的代码，不会执行')


print(qiuhe2(11, 11))
sum2 = qiuhe2(11, 12)  # 使用变量保存函数返回结果
print(sum2)


# 返回值说明
def 函数名():  # 返回值是None
    pass


def 函数名():  # return没有数据，返回值也是None
    return
