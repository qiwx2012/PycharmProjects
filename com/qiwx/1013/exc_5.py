import  pymysql
#打开数据库连接
db=pymysql.connect('localhost','root','123456','student')
#使用cursor方法获取操作游标
cursor=db.cursor()
#SQL查询语句
sql='select * from book'
try:
    #执行SQL语句
    cursor.execute(sql)
    #获取所有记录列表
    results=cursor.fetchall()
    for row in results:
        bookId=row[0]
        bookName=row[1]
        bookPrice=row[2]
        bookThumb=row[3]
     #打印结果
        print('bookId=%d,bookName=%s,bookPrice=%f,bookThumb=%s'%(bookId,bookName,bookPrice,bookThumb))
except:
    print('Error:unalbe to fetch data')
#关闭数据库
db.close()













