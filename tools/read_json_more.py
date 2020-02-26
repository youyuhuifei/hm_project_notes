# 导包 json
import json

# 打开文件获取文件流
# with open("../data/login.json", "r", encoding=utf-8) as f:
#     # 调用json。load 方法加载文件流
#     data = json.load(f)
#     print("获取数据为：", data)

# 使用函数进行封装
# def read_json():
#     with open("../data/login.json", "r", encoding=utf - 8) as f:
#         # 调用json。load 方法加载文件流
#         return json.load(f)


# 使用参数替换 静态文件名
class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf - 8") as f:
            # 调用json。load 方法加载文件流
            return json.load(f)

if __name__ == '__main__':
    # ReadJson("login.json").read_json()
    datas = ReadJson("login_more.json").read_json()
    # 新建空列表，添加读取json数据
    # print("shuju", data)
    arrs = []
    # 使用遍历获取所有的values
    for data in datas.values():
        arrs.append((data.get("url"),
                    data.get("mobile"),
                    data.get("code"),
                    data.get("expect_result"),
                    data.get("status_code"))
                    )
    print(arrs)




"""
    问题：
        1、未经封装的无法在其他模块内调用
        2、数据文件有多个，若写死，在读取其他文件时无法使用
        3、预期格式为列表嵌套元组[()]
        4、多个参数预期格式为列表嵌套多个元组[(),()]
    解决：
        1、进行封装
        2、使用参数替换静态写死文件
        3、读取字典内容，并添加到新的列表中
        4、可以利用字典中values()读取所有的值
"""
