# 导入pymysql模块
import pymysql
# 导入excel模块
import xlwt
import importlib
import sys
importlib.reload(sys)
import os
import shutil
import time

# 连接database
conn = pymysql.connect(host="47.98.229.80", port=3306, user="van", password="73ESckfa", database="mk", charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = """
select * from t_ord 
where `EDIT_FLAG` ='1100.10' and prod_type_nm = '鲜牛奶' limit 23;
"""
# 执行SQL语句
ret = cursor.execute(sql)
results = cursor.fetchall()
fields = cursor.description
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('table_'+'t_order', cell_overwrite_ok=True)

# 写上字段信息
for field in range(0, len(fields)):
    sheet.write(0, field, fields[field][0])

# 获取并写入数据段信息
row = 1
col = 0
for row in range(1, len(results)+1):
    for col in range(0, len(fields)):
        sheet.write(row, col, u'%s' % results[row-1][col])

epath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fileName = '/lky.xls'
alist = [epath, fileName]
exPath = ''.join(alist)
dateName = int(time.time())
backPath = epath +'/back/'+'lky_'+str(dateName)+'.xls'

if(os.path.isfile(exPath)):
    f = open(backPath, 'a')
    f.write(os.popen('').read())
    f.close()
    shutil.copyfile(exPath, backPath)
    os.remove(exPath)

workbook.save(exPath)
# 遍历结果
for row in results:
    ord_postpone_cd = row[0]
    NM_CN = row[1]
    QTY = row[2]
    CRT_TM = row[3]

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()

