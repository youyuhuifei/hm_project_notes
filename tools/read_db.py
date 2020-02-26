"""
完成数据库相关工具类封装
    主要方法
        def get_sql_one(sql)
    辅助方法
        获取连接对象
        获取游标对象
        关闭游标
        关闭连接
"""

# 导包 pymysql
import pymysql

# 新建工具类 数据库
class ReadDB:
    # 获取连接对象方法封装
    conn = None

    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("127.0.0.1",
                                       "root",
                                       "123456",
                                       "hmtt",
                                       charset="utf8")
        return self.conn
    # 获取游标对象方法

    def get_cursor(self):
        return self.get_conn().cursor()
    # 关闭游标对象

    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭连接
    def close_conn(self):
        if self.conn:
            self.conn.close()
            # 关闭连接对象后，对象还存在内存中，需要手动设置为None
            self.conn = None

    # 主要方法
    def get_sql_one(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)
            # 获取结果
            data = cursor.fetchone()
        except Exception as e:
            print("get_sql_one_error:", e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 获取所有数据库结果集
    def get_sql_all(self, sql):
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)
            # 获取结果
            data = cursor.fetchall()
        except Exception as e:
            print("get_sql_one_error:", e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 修改删除新增
    def update_sql(self, sql):
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            # 事务回滚
            self.conn.rollbck()
            print("get_sql_one_error:", e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接对象
            self.close_conn()

        




