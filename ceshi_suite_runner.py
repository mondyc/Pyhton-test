'''
学习TestSuite和TestRunner的使用
'''

# 步骤
# 1．导包(unittest)
import unittest
from ceshi_testcase import TestDemo
from ceshi_testcase1 import TestDemo1
from ceshi_testcase2 import TestDemo2

# 2．实例化(创建对象)套件对象
suite = unittest.TestSuite()

# 3．使用用套件对象添加用例方法
# 方式1，套件对象.addTest(测试类名('方法名'))#建议测试类名和方法名直接去复制,不要手写
suite.addTest(TestDemo('test_method1'))
suite.addTest(TestDemo('test_method2'))
suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))
suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))

# 方式2，将一个测试类中的所有方法进行添加
# 套件对象.addTest(unittest.makeSuite(测试类名))
# 缺点: makeSuite() 不会提示
suite.addTest(unittest.makeSuite(TestDemo))
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))
# 4．实例化运行对象
runner = unittest.TextTestRunner()

# 5．使用运行对象执行套件对象
# 运行对象.run(套件对象)
runner.run(suite)
