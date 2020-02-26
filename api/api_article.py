# 导包
import requests


# 新建文章对象类
class ApiArticle(object):
    # 新建收藏文章方法
    def api_post_collection(self, url, headers, data):
        return requests.post(url, headers=headers, json=data)


    #新建取消文章方法
    def api_delete_atricle(self, url, headers):
        return requests.delete(url, headers=headers)


