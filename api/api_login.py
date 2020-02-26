"""
    目标：实现登录接口对象
"""

import requests

# 新建类 登录接口对象
class ApiLogin():
    # 新建登录方法
    def api_post_login(self, url, mobile, code):
        # headers定义
        headers = {"Content-Type": "application/json"}

        # data 定义
        data = {"mobile": mobile, "code": code}
        # 调用post并返回响应对象
        return requests.post(url, headers=headers, json=data)



"""
url,mobile,code:最后都需要从data数据文件读取出来
"""