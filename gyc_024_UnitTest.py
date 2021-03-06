'''UnitTest框架'''

# 框架
# 说明：
# 1．框架英文单词framework
# 2．为解决一类事情的功能集合

# 什么是UnitTest框架？
# 概念：UnitTest是Python自带的一个单元测试框架，用它来做单元测试

# 自带的框架：不需要单外安装，只要安装了Python，就可以使用
# 第三方框架：想要使用需要先安装后使用(pytast)

# 单元测试框架：主要用来做单元测试，一般单元测试是开发做的
# 对于测试来说，unittest框架的作用是自动化脚本(用例代码）执行框架
# (使用unittest框架来管理运行多个测试用例的)

# 为什么使用UnitTest框架?
# 1．能够组织多个用例去执行
# 2．提供丰富的断言方法(让程序代码代替人工自动的判断预期结果和实际结果是否相符)
# 3．能够生成测试报告

# UnitTest核心要素(unitest的组成)
# 1．TestCase
# Testcase(测试用例)，注意这个测试用例是unittest框架的组成部分，不是手工和自动化中我们所说的用例(Test case)
# 主要作用:每个Testcase(测试用例)都是一个代码文件，在这个代码文件中 来书写 真正的用例代码

# 2．TestSuite
# TestSuite(测试套件)，用来管理组装(打包)多个Testcase(测试用例)的

# 3．TestRunner
# TestRunner(测试执行,测试运行)，用来执行Testsuite(测试套件)的

# 4．TestLoader
# TestLoader(测试加载)，功能是对Testsuite(测试套件)功能的补充，管理组装(打包)多个Testcase(测试用例)的

# 5．Fixture
# Fixture(测试夹具)，书写在TestCase(测试用例)代码中，是一个代码结构,可以在每个方法执行前后都会执行的内容
# 举例:
# 登录的测试用例，每个用例中重复的代码就可以写在Fixture 代码结构中，只写一遍，但每次用例方法的执行，都会执行 Fixture中的代码
# 1．打开浏览器
# 2．输入网址


print('-----------------------------------------------------------')

# TestCase(测试用例)
# 1．是一个代码文件，在代码文件中来书写真正的用例代码
# 2．代码文件的名字必须按照标识符的规则来书写(可以将代码的作用在文件的开头使用注释说明）

# 步骤
# 1．导包(unittest)
# 2．自定义测试类
# 3．在测试类中书写测试方法
# 4．执行用例

'''
例子指向项目目录的 ceshi_testcase.py 文件
'''

'''
【Pycharm以unittest运行，不用加unittest.main()】
在查询unitest和pytest的过程中看到测试类中必须执行unittest.main()
如下：
if __name__ == '__main__':
    unittest.main()
但是我的没有执行，但是测试类依然可以正常执行
查询得知在运行配置中选择unittest，可以不执行unittest.main()
https://www.cnblogs.com/sammisammi/p/15031606.html
'''
print('-----------------------------------------------------------')

# 问题1——代码文件的命名不规范
# 1．代码文件的名字以数字开头
# 2．代码文件名字中有空格
# 3．代码文件名字有中文
# 4．其他的特殊符号
# (数字，字母，下划线组成，不能以数字开头)

# 问题2——代码运行没有结果
# 右键运行没有 unittests for的提示，出现的问题
# 解决方案：
# 方案1．重新新建一个代码文件,将写好的代码复制进去
# 方案2．删除已有的运行方式

# 问题3——没有找到用例
# 测试方法中不是以test_开头的，或者单词写错了

print('-----------------------------------------------------------')

# TestSuite & TestRunner
# TestSuite(测试套件):管理打包组装Testcase(测试用例)文件的
# TestRunner(测试执行):执行TestSuite(套件)

# 步骤
# 1．导包(unittest)
# 2．实例化(创建对象)套件对象
# 3．使用用套件对象添加用例方法
# 4．实例化运行对象
# 5．使用运行对象执行套件对象

'''
例子指向项目目录的 ceshi_suite_runner.py 文件
例子指向项目目录的 ceshi_testcase.py 文件
例子指向项目目录的 ceshi_testcase1.py 文件
例子指向项目目录的 ceshi_testcase2.py 文件
'''

# 测试结果中 “.” 是通过测试的，“F”是用例不通过 “E” Error代表用例代码有问题

print('-----------------------------------------------------------')

# TestLoader (测试加载)
# TestLoader(测试加载)，作用和 TestSuite 的作用是一样的，对TestSuite 功能的补充，用来组装测试用例的

# 比如:如果Testcase 的代码文件有很多，(10，20，30)

# 步骤
# 1．导包(unittest)
# 2．实例化测试加载对象并添加用例--->得到的是 suite对象
# 3．实例化运行对象
# 4．使用运行对象执行套件对象

# 代码实现
# 在一个项目中 Testase(测试用例)的代码，一般放在一个单独的目录 (case)

'''
例子指向项目目录的 ceshi_testloader.py 文件
例子指向项目目录/case的 ceshi_testcase1.py 文件
例子指向项目目录/case的 ceshi_testcase2.py 文件
例子指向项目目录/case的 testcase3.py 文件
'''

print('-----------------------------------------------------------')


# Fixture(测试夹具)
# Fixture(测试夹具)是一种代码结构
# 在某些特定的情况下会自动执行

# 方法级别[掌握]
# 在每个测试方法(用例代码)执行前后都会自动调用的结构
# 方法执行之前
# def setUp(self):
#     # 每个测试方法执行之前都会执行
#     pass


# 方法执行之后
# def tearDown(self):
#     # 每个测试方法执行之后都会执行
#     pass


# 类级别[掌握]
# 在每个测试类中所有方法执行前后都会自动调用的结构(在整个类中执行之前执行之后个一次)
# 类级别的Fixture方法,是一个类方法

# 类中所有方法之前
# @classmethod
# def setUpClass(cls):
#     pass


# 类中所有方法之后
# @classmethod
# def tearDownClass(cls):
#     pass


# 模块级别[了解]
# 模块:代码文件
# 在每个代码文件执行前后执行的代码结构
# 模块级别的需要写在类的外边直接定义函数即可
# 代码文件之前
# def setupModule():
#     pass


# 方法级别和类级别的前后的方法,不需要同时出现,根据用例代码的需要自行的选择使用

# 案例
# 1、打开浏览器(整个测试过程中就打开一次浏览器)类级别
# 2、输入地址 (每个测试方法都需要一次) 方法级别
# 3、输入用户名验证码密码点击登录（不同的测试数据） 测试方法
# 4、关闭当前页面 (每个测试方法都需要一次) 方法级别
# 5、关闭浏览器 (整个测试过程中就打开一次浏览器)类级别

'''
例子指向项目目录的 ceshi_Fixture.py 文件
'''

print('-----------------------------------------------------------')

# 断言
# 让程序代替人工自动的判断预期结果和实际结果是否相符

# 断言的结果有两种:
# > True,用例通过
# > False,代码抛出异常,用例不通过

# 在unittest中使用断言,都需要通过self.断言方法来试验

# assertEqual
# self.assertEqual(预期结果，实际结果) # 判断预期结果和实际结果是否相等
# 1．如果相等，用例通过
# 2．如果不相等，用例不通过，抛出异常

# assertln
# self.assertIn(预期结果，实际结果) # 判断预期结果是否包含在实际结果中
# 1．包含，用例通过
# 2．不包含，用例不通过，抛出异常

'''
例子指向项目目录的 ceshi_assert.py 文件
例子指向项目目录的 ceshi_test_login.py 文件
'''

print('-----------------------------------------------------------')

# 参数化
# 参数化在测试方法中，使用变量来代替具体的测试数据，然后使用传参的方法将测试数据传递给方法的变量
# 好处:相似的代码不需要多次书写.

# 工作中场景:
# 1．测试数据一般放在json文件中
# 2．使用代码读取json文件，提取我们想要的数据--->[(),()] or [[],[]]

# 安装插件
# unittest框架本身是不支持参数化，想要使用参数化，需要安装插件来完成

# 联网安装(在cmd窗口安装或者)
# pip install parameterized
# pip 是 Python中包(插件)的管理工具，使用这个工具下载安装插件

# 验证
# pip list # 查看到parameterized

# 新建一个python代码文件，导包验证 from parameterized import parameterized

# from parameterized import parameterized

# 参数化代码
# 1．导包unittest/ parameterized
# 2．定义测试类
# 3．书写测试方法(用到的测试数据使用变量代替）
# 4．组织测试数据并传参

'''
例子指向项目目录的 ceshi_parameterized.py 文件
例子指向项目目录的 ceshi_test_login.py 文件
'''

print('-----------------------------------------------------------')

# 跳过
# 对于一些未完成的或者不满足测试条件的测试函数和测试类，不想执行，可以使用跳过使用方法，装饰器完成

#直接将测试函数标记成跳过
# @unittest.skip('跳过额原因')

#根据条件判断测试函数是否跳过，判断条件成立，跳过
# @unittest.skipIf(判断条件，'跳过原因')

'''
例子指向项目目录的 ceshi_skip.py 文件
'''

print('-----------------------------------------------------------')

# unittest测试流程
# 1．组织用例文件(TestCase 里边)，书写参数化，书写断言，书写Fixture，书写跳过，如果单个测试测试文件，直接运行，得到测试报告，如果有多个测试文件，需要组装运行生成测试报告
# 2．使用套件对象组装，或者使用加载对象组装
# 3．运行对象运行
# 3.1运行对象=第三方的运行类(文件对象(打开文件需要使用wb方式))
# 3.2运行对象.run(套件对象)
