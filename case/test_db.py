"""
在unittest框架中使用数据库工具类
"""

# 导包 unittest pymysql
import unittest
from tools.read_db import ReadDB


# 新建测试类
class TestDB(unittest.TestCase):
    # 新建测试方法
    def test_db(self):
        # 定义sql语句
        sql = "select * from table1 where id=1"
        # 调用方法
        data = ReadDB().get_sql_one(sql)
        # 调试 查看响应数据
        print(data)
        # 断言
        self.assertEquals(0, data[0])


if __name__ == '__main__':
    unittest.main()

