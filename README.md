# hm_project_notes


自动化目录结构：
1、接口对象层（api）
2、用例执行业务层(case)
3、数据驱动(data)
4、测试报告(report)
5、工具(toos)
6、运行入口(run.py)

1、接口对象层
login.py
    1、导包
    2、新建对象类，登录对象
    3、新建登录方法
        定义headers
        定义data报文
        调用post并返回

用户频道
api_channels.py
导包
新建对象类
新建方法获取用户频道列表
    url headers通过参数传递

api_articel.py
    文章对象类
        收藏文章 post
        取消收藏 delete


2、业务执行
test_login.py
    1、导包
    2、新建测试类，继承unittest.Testcase
    3、新建测试方法
        参数化数据准备
            url mobile code
        实例化ApiLogin（）类并调用登录方法
        断言 响应信息，响应状态码

test_channels
导包
新建测试类 继承
    新建方法
        临时数据
        获取用户列表频道方法
        断言 状态码

test_articel.py



3、data
解决数据存储问题
步骤
1、编写数据存储文件，login.json
    data目录下
    内容：
    {
  "url": "",
  "mobile": "",
  "code": "",
  "expect_result": "",
  "status_code": 201
}

2、编写读取json工具
    导包 json
    新建读取工具类
        使用初始化方法 获取要读取的文件名称
        读取文件方法
            打开json文件获取文件流
            调用load方法加载文件流
            返回结果
3、使用参数化动态获取参数数据
    结合parameterized组件使用
    方式：
        # get_date  返回列表嵌套元组的数据格式
        @parameterized.expend(get_date())

多条用例数据扩展

json文件
    以用例编号作为键名，值使用单条字典测试数据
读取json文件
    使用字典values()方法获取所有值
    其他操作方法和单条接口用例数据方法一样
参数化应用
    修改get_data数据格式
    调用时不做任何修改
提示：json串不能使用单引号


run_suite.py

导包  unittest  HTMLTestRunner  time
组装测试套件
定义报告存放路径及文件名称
运行测试套件并生成测试报告
注意路径

数据获取连接mysql
操作：
    导包 pymysql
    获取连接对象
    获取游标对象
    执行方法
    获取执行结果
    断言
    关闭游标对象
    关闭连接

问题
    流水线代码编写无法复用
