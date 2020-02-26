"""
    目标：完成登录业务层实现

"""


# 导包 unittest requests
import unittest
import requests
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

# 读取数据函数
def get_data():
    data = ReadJson("login.json").read_json()
    # 新建空列表，添加读取json数据
    # print("shuju", data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect_result"),
                 data.get("status_code"))
                )
    return arrs


# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测方法
    @parameterized.expand(get_data())
    def test_login(self,url, mobile, code, expect_result, status_code):
        # 暂时存放数据 url mobile code
        # url = "http://www.baidu.com"
        # mobile = "13500001111"
        # code = "123"
        # 调用登录方法 返回响应信息
        s = ApiLogin().api_post_login(url, mobile, code)
        # 查看响应结果
        print("查看响应结果：",s.json())

        # 断言  响应信息  及  响应码
        self.assertEquals(expect_result, s.json()["message"])

        self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()


