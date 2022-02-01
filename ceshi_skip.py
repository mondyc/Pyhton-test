import unittest

banben = 29


class TestDemo(unittest.TestCase):
    @unittest.skip('没有原因')
    def test_1(self):
        print('测试方法1')

    @unittest.skipIf(banben >= 30, '版本号大于等于30不用测试')
    def test_2(self):
        print('测试方法2')

    def test_3(self):
        print('测试方法3')
