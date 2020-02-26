# 导包
import unittest
from api.api_channels import ApiChannel
from parameterized import parameterized

from tools.read_json import ReadJson


def get_data():
    data = ReadJson("channel.json").read_json()
    # 新建空列表，添加读取json数据
    # print("shuju", data)
    arrs = []
    arrs.append((data.get("url"),
                data.get("headers"),
                data.get("expect_result"),
                data.get("status_code"))
                )
    return arrs



# 新建测试类 继承
class TestChannel(unittest.TestCase):
    # 新建方法
    @parameterized.expand(get_data())
    def test_channel(self,url, headers, expect_result, status_code):
        # 临时数据
        # 获取用户列表频道方法
        # 断言 状态码
        # url = ""
        # headers = {}
        r = ApiChannel.api_get_channels(url, headers)
        print(r.json())
        self.assertEquals(status_code, r.status_code)
        self.assertEquals(expect_result, r.json()["message"])


if __name__ == '__main__':
    unittest.main()

