import unittest
from api.api_article import ApiArticle
from parameterized import parameterized
from tools.read_json import ReadJson

def get_data_add():
    data = ReadJson("article_add.json").read_json()
    # 新建空列表，添加读取json数据
    # print("shuju", data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")
                ))
    return arrs

def get_data_cancel():
    data = ReadJson("artic le_cancel.json").read_json()
    # 新建空列表，添加读取json数据
    # print("shuju", data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code"))
                )
    return arrs

class TestArticle(unittest.TestCase):
    @parameterized.expand(get_data_add())
    def test01_collection(self, url, headers, data, expect_result, status_code):
        #临时数据
        # url = ""
        # headers = {}
        # data = {}

        r = ApiArticle.api_post_collection(url, headers, data)

        print("响应数据为：",r.json())

        self.assertEquals(status_code, r.status_code)
        self.assertEquals(expect_result, r.json()["message"])

    @parameterized.expand(get_data_cancel())
    def test02_cancel(self, url, headers, status_code):
        # url = ""
        # headers = {}
        r = ApiArticle().api_post_collection(url, headers)

        self.assertEquals(status_code, r.status_code)


if __name__ == '__main__':
    unittest.main()



