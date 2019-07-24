# -*- coding:utf-8 -*-
from mysql import conn_mysql

def pro_sys_result(healthy_problem_str):
    '''
    根据生成的病情调查的结果，生成healthy_problem_str,根据这个字符串信息
    查询数据库，推断病情，数据库样例在专家系统.txt中
    :param healthy_problem_str: 字符串
    :return: 字符串，病的ID
    '''
    index = 0
    grade = 0
    ret = ""
    with conn_mysql(dict_or_tuple=1) as cursor:
        # 查询专家系统数据库 找到疾病ID
        rows_numbres = cursor.execute("select * from 专家系统")
        result = cursor.fetchall()
        ret = result[0][6] # ret 是返回值
        print(ret)
        # 比较那个得分最高，那个就最有可能
        for i in range(rows_numbres):
            row = result[i]
            grade_temp = 0
            healthy_think = row[1]+row[2]+row[3]+row[4]+row[5]

            for j in range(len(healthy_problem_str)):
                if((healthy_problem_str[j] == healthy_think[j])
                        or (healthy_problem_str[j] == "2")):
                    grade_temp += 1
            if(grade_temp > grade):
                ret = row[6]
                grade = grade_temp
                print(ret,"  ",grade_temp)

        # 查询数据库，根据疾病ID得到疾病名称，跟新ret
        rows_numbres = cursor.execute("select 疾病名称 from 疾病 where 疾病ID = "+ret)
        result = cursor.fetchall()
        ret = result[0][0]

        return ret


if __name__ == "__main__":
    if("012"[1] == "1"):
        print("run")
    result = pro_sys_result("011110000000000010000000122222222222122222222222001001110000")
    print(result)





