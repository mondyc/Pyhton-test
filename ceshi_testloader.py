"""TestLoader的使用"""

# 1．导包
import unittest

# 2．实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在的路径','用例的代码文件名')
# 用例所在的路径,建议使用相对路径用例的代码文件名可以使用*(任意多个任意字符)通配符
# suite = unittest.TestLoader().discover('./case', 'ceshi*.py')
# suite = unittest.TestLoader().discover('./case', '*ceshi*')
# suite = unittest.TestLoader().discover('./case', '*ceshi*.py')
suite = unittest.TestLoader().discover('./case', '*ceshi*.py')

# 3．实例化运行对象
runner = unittest.TextTestRunner()

# 4．实例化运行对象
runner.run(suite)

# 可以将34步变为一步
# unittest.TextTestRunner().run(suite)
