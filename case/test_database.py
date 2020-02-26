# 导包 pymysql
import pymysql


# 获取连接对象
conn = pymysql.connect("127.0.0.1",
                       "root",
                       "123456",
                       "hmtt",
                       charset="utf8")

# 获取游标对象
cursor = conn.cursor()

# 执行方法sql
sql = "select is_deleted from table1 where user_id=1 and id=2"
cursor.execute(sql)

# 获取结果并断言
# print(cursor.fetchone())
result = cursor.fetchone()

# 断言 元组
assert 0 == result(0)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
