'''HTMLTestRunner.py【重点】'''

# 自带的测试报告
# 只有单独运行Testcase的代码，才会生成测试报告

# 生成第三方的测试报告
# 1．获取第三方的测试运行类模块，将其放在代码的目录中
# 2．导包unittest
# 3．使用﹑套件对象，加载对象去添加用例方法
# 4．实例化第三方的运行对象并运行套件对象

# 1．获取第三方的测试运行类模块,将其放在代码的目录中#
# 2．导包unittest
import unittest
from HTMLTestRunner import HTMLTestRunner

# 3．使用套件对象,加载对象去添加用例方法
suite = unittest.defaultTestLoader.discover('.', 'ceshi_parameterized.py')
# 4．实例化第三方的运行对象并运行套件对象
# HTMLTestRunner.py()
# stream=sys.stdout，必填,测试报告的文件对象(open)，注意点,要使用wb 打开
# verbosity=1，可选，报告的详细程度,默认1简略,2详细
# title=None，可选,测试报告的标题
# description=None 可选，描述信息，Python的版本，pycharm 版本
file = 'report1.html'  # 报告的后缀是.htmL

with open(file, 'wb') as f:
    # runner = HTMLTestRunner(f) # 运行对象
    runner = HTMLTestRunner(f, 2, '测试报告', 'python3.7.5')
    # 运行对象执行套件,要写在 with的缩进中
    runner.run(suite)
