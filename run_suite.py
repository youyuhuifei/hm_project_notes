"""
    目标：搜索组装测试套件
        运行测试套件并生成测试报告

"""

# 导包
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner

# 组装测试套件
suit = unittest.defaultTestLoader.discover("./case",pattern="test*.py")

# 指定报告存放路径及文件名称
filepath = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

# 运行测试套件并生成测试报告

with open(filepath, "wb") as f:
    HTMLTestRunner(stream=f).run(suit)

