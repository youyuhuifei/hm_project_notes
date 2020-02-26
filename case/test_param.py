"""
    目标：parameterized参数化组件使用
    安装： pip install parameterized
    使用：
        @parameterized.expant(参数)
        参数：
            单个参数格式：列表[值1,值2]
            多个参数格式：列表嵌套元组[(),()]

"""

import unittest
from parameterized import parameterized


# 新建测试类
class TestPara(unittest.TestCase):
    @parameterized.expand([("admin", "123456"), ("user1", "123")])
    def test_para(self, username, password):
        print("用户名：", username)
        print("密码：", password)
