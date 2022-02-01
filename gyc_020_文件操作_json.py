"""文件操作 json"""

# json文件的处理
# json 文件也是一个文本文件，就可以直接使用read()和 write()方法去操作文件，只是使用这两个方法，不方便，所以对json文件有自己独特的读取和写入的方法

# 常用在在做测试的时候，将测试数据定义为json文件格式，使用代码读取json文件,即读取测试数据，进行传参(参数化)

# json基于文本，独立于语言的轻量级的数据交换格式
# -基于文本，是一个文本文件，不能包含音频
# -独立于语言，不是某个语言特有的，每种编程语言都可以使用的
# -轻量级，相同的数据，和其他格式相比,占用的大小比较小
# -数据交换格式，后端程序员给前端的数据(json，html，xml)

# json文件的语法
# 1. json文件的后缀是.json
# 2. json中主要数据类型为对象（{}类似 Python中字典）和数组（[],类似 Python中的列表），对象和数组可以互相嵌套
# 3．一个json文件是一个对象或者数组(即json文件的最外层要么是一个{}，要么是一个数组[])
# 4. json中的对象是由键值对组成的，每个数据之间使用逗号隔开，但是最后一个数据后边不要写逗号
# 5. json中的字符串必须使用双引号
# 6. json 中的其他数据类型
#     >数字类型 ----> int float
#     >string字符串 ----> str
#     >布尔类型true，false ----> True，False
#     >nul1 ----> None

print('-----------------------------------------------------------')

# 案例数据
# {
#   "name" : "小明","age" : 18,
#   "isMen" : true,
#   "like" : ["听歌","游戏","购物","吃饭","睡觉","打豆豆"],
#   "address" : {"country":"中国","city":"上海"}
# }

# 读取json文件
# 1．导包import json
# 2．读打开文件
# 3．读文件
# json.load(文件对象)

# 返回的是字典(文件中是对象)或者列表(文件中是数组)

# 1、导入json
import json

# 2、读打开文件
with open('info.json', encoding='utf-8') as f:
    # 3、读取文件
    result = json.load(f)
    print(type(result))
    # 姓名
    print(result.get('name'))
    # 年龄
    print(result.get('age'))
    # 城市
    print(result.get('address').get('city'))

print('-----------------------------------------------------------')

# 写入json文件
# 文件对象.write(字符串) 不能直接将 Python 的列表和字典作为参数传递
# 想要将Python中的数据类型存为json文件，需要使用json提供的方法不再使用write

# 写入json文件
# 1．导包import json
# 2．写(w)打开方式
# 3．写入
# json.dump( Python中的数据类型，文件对象)

my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123123', '登录失败')]

with open('info4.json', 'w', encoding='utf-8') as m:
    # json.dump(my_list,m)
    # json.dump(my_list, m, ensure_ascii=False)#直接显示中文,不以、ASCII 的方式显示
    json.dump(my_list, m, ensure_ascii=False, indent=4)  # indent显示缩进

print('-----------------------------------------------------------')
