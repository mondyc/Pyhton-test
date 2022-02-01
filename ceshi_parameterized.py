'''参数化'''

# 1．导包unittest/ parameterized
import unittest
from parameterized import parameterized
from ceshi_test_login import login

# 组织测试数据[(),()] or [[],[]]
data = [
    ('admin', '123456', '登录成功'),
    ('root', '123456', '登录失败'),
    ('admin', '123123', '登录失败')
]

'''
组织数据的第二种方式，懒得写了
https://www.bilibili.com/video/BV11g411V7Kf?p=138
'''


# 2．定义测试类
class TestLogin(unittest.TestCase):
    # 3．书写测试方法(用到的测试数据使用变量代替）
    @parameterized.expand(data)
    def test_login(self, username, password, ecpect):
        self.assertEqual(ecpect, login(username, password))

# 4．组织测试数据并传参(装饰器 @)(运行光标要放在参数化装饰器的上面)
