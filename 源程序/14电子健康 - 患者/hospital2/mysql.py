# -*- coding:utf-8 -*-
import sys
import pymysql
import contextlib

#首先是一个正常连接的例子
def mysql_example():
    '''
    展示 一个MySQL连接经常用到的方法
    '''
    result = x = y = None
    conn = pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd= "12345",
                         use_unicode=True, charset="utf8",db="hospital_management")
    cursor = conn.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    # 使用字典，默认元组
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM 热点健康问题"
    try:
        numbers = cursor.execute(sql)
        # fetchall()  fetchone()  fetchsome(4)
        result = cursor.fetchall()
        for i in range(int(3)):
            print(result[i])
    except Exception as e:
        raise e
        db.rollback()
        print("rollback")
    db.close()

#定义上下文管理器，连接后自动关闭连接
#建议使用此方法
@contextlib.contextmanager
def conn_mysql(host='127.0.0.1', port=3306, user='root', passwd='12345',
          db='hospital_management', charset='utf8',dict_or_tuple = 0):
    '''
    mysql 连接的上下文管理器方法
    dic_or_tuple 0返回字典 1返回元组
    '''
    #定义连接 conn
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd,
                           use_unicode=True,db=db, charset=charset)
    # 定义游标 cursor
    if dict_or_tuple == 0:
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    else:
        cursor = conn.cursor()
    # 事务
    try:
        yield cursor
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # 执行sql
    with conn_mysql() as cursor:
        sql = "SELECT * FROM 热点健康问题"
        rows = cursor.execute(sql)
        print("row = ",int(rows))
        result = cursor.fetchall()
        for i in range(int(3)):
            print(result[i])
            pass


