import pymysql
conn = pymysql.connect(#建立一个连接，命名为conn
    host ='localhost',#主机
    user ='root',#本地用户
    passwd ='12345',#密码
    db ='test',#连接数据库名
    )
cur = conn.cursor()#定义游标
cur1 = conn.cursor()
#cur.execute("create database fristDb")创建数据库
sql = """create table self_information ( ID char(15) NOT NULL,
                                          Name char(10) DEFAULT NULL,
                                          Sex char(4) DEFAULT NULL,
                                          Age int(3) DEFAULT NULL,
                                          Hobbies char(100) DEFAULT NULL,
                                          PRIMARY KEY (ID)
                                          )"""#创建表
cur.execute("DROP TABLE IF EXISTS self_information")
cur.execute(sql)#创建表
sql1 = """insert into self_information(ID,Name,Sex,Age,Hobbies) values ('user','张三','男','32','书法、羽毛球、游泳')"""
try:
    cur1.execute(sql1)
    conn.commit()
except:
    conn.rollback()
cur.close();
conn.close();