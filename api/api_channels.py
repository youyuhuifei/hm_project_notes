import requests


class ApiChannel(object):
    def api_get_channels(self, url, headers):
        # 调用get方法
        return requests.get(url, headers=headers)


