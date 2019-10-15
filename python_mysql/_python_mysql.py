# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="47.98.229.80:3306", user="van",password="73ESckfa",database="mk",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = """
select * from t_ord limit 12;
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
ret = conn.close()

print(ret)