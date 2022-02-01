#定义一个函数add()对两个数字进行求和计算
def add(a, b):
    return a + b


# 凡是在导入的时候不想执行的代码，都可以if判断里面
if __name__== "__main__": #
    # 调用函数
    print('在代码中调用函数')
    print(add(1,2))
    print(add(10,20))
    print('tools : ',__name__)
