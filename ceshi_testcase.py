'''
代码的目的:学习Testcase(测试用例)模块的书写方法
'''

# 步骤
# 1．导包(unittest)
import unittest


# 2．自定义测试类，需要继承unittest模块中的Testcase类即可
class TestDemo(unittest.TestCase):
    # 3，书写测试方法，即用例代码．目前没有真正的用例代码，使用print代替
    # #书写要求，测试方法必须以test_开头(本质是以 test开头)
    def test_method1(self):
        print('测试方法 1')

    def test_method2(self):
        print('测试方法 2')


# 4．执行用例
# 4.1 将光标放在类名的后边运行，会执行类中的所有的测试方法
# 4.2将光标放在方法名的后边运行，只执行当前的方法


print('-----------------------------------------------------------')
