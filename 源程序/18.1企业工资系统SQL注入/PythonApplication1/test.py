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
sql = """create table salary_month( ID int(15) NOT NULL,
                                      Month int(6)  NOT NULL, 
                                      Name char(10) DEFAULT NULL,
                                      Basic_salary int(5) DEFAULT NULL,
                                      Bonus int(5) DEFAULT NULL,
                                      Fine int(5) DEFAULT NULL,
                                      True_salary int(8) DEFAULT NULL,
                                      PRIMARY KEY (ID,Month)
                                      )ENGINE=InnoDB DEFAULT CHARSET=utf8"""#创建表
cur.execute("DROP TABLE IF EXISTS salary_month")
cur.execute(sql)#创建表
#插入数据
t= [('12345678','201807','张三','5000','4000','400','8600'),
    ('12345678','201806','张三','5000','4000','500','8500'),
    ('12345678','201805','张三','5000','3000','400','7600')]
sql1 = "insert into salary_month(ID,Month,Name,Basic_salary,Bonus,Fine,True_salary) values (%s,%s,%s,%s,%s,%s,%s)"
try:
    cur1.executemany(sql1,t)
    conn.commit()
except:
    print('false')
    conn.rollback()
cur1.close();
cur.close();
conn.close()
