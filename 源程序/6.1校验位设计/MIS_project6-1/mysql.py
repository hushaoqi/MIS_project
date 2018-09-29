import pymysql
config = {
          'host':'localhost',#数据库所在主机IP
          'port':3306,#MySQL默认端口
          'user':'root',#mysql默认用户名
          'password':'root',
          'db':'com_information',#数据库
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

def InsertInformation(commodityCode, commodityName, specification, chargeUnit,unitPrice,outputCode):
    print('调用成功')
    try:
        db= pymysql.connect(**config)
        print("数据库连接成功！")
        cursor = db.cursor()
        print("数据库指针寻找成功！")
        try:
            sql = "INSERT INTO information('commodityCode', 'commodityName', 'specification', 'chargeUnit','unitPrice','outputCode') VALUES (%s, %s, %s, %s ,%s ,%s)"
            data = (commodityCode, commodityName, specification, chargeUnit,unitPrice,outputCode)
            n = cursor.execute(sql, data)
            print(n)
            db.commit()# 提交到数据库执行
            print("数据库插入成功！")
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()
            db.close()
        print("数据库关闭成功！")
        return 1
    except Exception as e:
        raise e

def getAllInformation():
    try:
        db = pymysql.connect(**config)

        cursor = db.cursor()
        sql = "SELECT * FROM information"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except Exception:
        return 0

def CreactTable():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "com_information")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # 使用预处理语句创建表
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)
    print("CREATE TABLE OK")
    # 关闭数据库连接
    db.close()
def daioyong():
    print('调用成功')