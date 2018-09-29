import pymysql
conn = pymysql.connect(#建立一个连接，命名为conn
    host ='localhost',#主机
    user ='root',#本地用户
    passwd ='12345',#密码
    db ='test',#连接数据库名
    )
cur = conn.cursor()#定义游标(创建表)
cur1 = conn.cursor()#定义游标(插入，删除，查找数据)
#cur.execute("create database fristDb")创建数据库
sql = """create table users( ID char(15) NOT NULL,
                               Password char(15) NOT NULL,
                               PRIMARY KEY (ID,Password)
                                      )"""#创建表
cur.execute("DROP TABLE IF EXISTS users")
cur.execute(sql)#创建表
#插入数据
t= [ ('user','user')]
sql1 = "insert into users(ID,Password) values (%s,%s)"
try:
    cur1.executemany(sql1,t)
    conn.commit()
except:
    print('false')
    conn.rollback()
cur1.close();
cur.close();
conn.close()