import pymysql

#1-声明并初始化全部变量
#1.1-初始化概率矩阵
P_Level=[0.0,0.0,0.0,0.0,0.0]			#各个信用等级概率
P_Time_I_Level=	[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个开卡时间差概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_Change_I_Level=[[0.0,0.0,0.0,0.0,0.0],#已知信用等级，各个信用等级改变情况概率
				[0.0,0.0,0.0,0.0,0.0]]
P_Income_I_Level=[[0.0,0.0,0.0,0.0,0.0],#已知信用等级，各个年收入概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_Age_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个年龄概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_Sex_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个性别概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]				
P_Marry_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个婚姻概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_House_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个住房状况概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_Edu_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个教育程度概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_Last_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个上次账单余额概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
P_Work_I_Level=[[0.0,0.0,0.0,0.0,0.0],	#已知信用等级，各个工作年限概率
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0],
				[0.0,0.0,0.0,0.0,0.0]]
#1.2-初始化变量
Obs=0			#数据库条目ID
Time=0			#开卡时间差
Change=0		#信用等级改变情况
Income=0		#年收入
Age=0			#年龄
Sex=0			#性别
Marry=0			#婚姻
House=0			#住房情况
Edu=0			#教育程度
Last=0			#上次账单余额
Work=0			#工作年限
Level=0			#信用等级

NUMBER=0		#数据库条目总数
#1.3-初始化计算概率
P_Level_1=0.0	#信用等级为1/2/3/4的概率
P_Level_2=0.0
P_Level_3=0.0
P_Level_4=0.0
P_Level_Max=0.0	#目前最大可能性等级的概率

#1-声明并初始化全部变量-完成

#2-训练

#2.1-连接数据库
db = pymysql.connect("localhost","root","6880236","summer_school" )

#2.2-创建游标对象
cursor = db.cursor()			#采集数据游标
updatecursor = db.cursor()		#更新数据游标

#2.3-确定循环次数并取得训练样本数目

#确定循环次数，存入NUMBER
cursor.execute("SELECT COUNT(Obs) FROM data_t")
NUMBER=cursor.fetchone()[0]
#选取所有训练集，放入cursor
cursor.execute("SELECT * FROM data_t ORDER BY Obs")

#2.4-训练
for i in range(NUMBER):
	data = cursor.fetchone()
	#提取一条数据的各个成分，存入对应变量
	Time=data[1]
	Change=data[2]
	Income=data[3]
	Age=data[4]
	Sex=data[5]
	Marry=data[6]
	House=data[7]
	Edu=data[8]
	Last=data[9]
	Work=data[10]
	Level=data[11]
	P_Level[0]+=1			#总数+1（P_Level[0]存放总数
	P_Level[Level]+=1		#对应信用等级次数+1
	#根据当前条目的数据修改各个矩阵
	P_Time_I_Level[Time][Level]+=1
	P_Change_I_Level[Change][Level]+=1
	P_Income_I_Level[Income][Level]+=1
	P_Age_I_Level[Age][Level]+=1
	P_Sex_I_Level[Sex][Level]+=1
	P_Marry_I_Level[Marry][Level]+=1
	P_House_I_Level[House][Level]+=1
	P_Edu_I_Level[Edu][Level]+=1
	P_Last_I_Level[Last][Level]+=1
	P_Work_I_Level[Work][Level]+=1

#对目前矩阵进行转化，从出现次数转为出现概率
for i in range(1,5):
	P_Time_I_Level[0][i]/=P_Level[i]
	P_Time_I_Level[1][i]/=P_Level[i]
	P_Time_I_Level[2][i]/=P_Level[i]
	P_Time_I_Level[3][i]/=P_Level[i]
	P_Time_I_Level[4][i]/=P_Level[i]
	P_Change_I_Level[0][i]/=P_Level[i]
	P_Change_I_Level[1][i]/=P_Level[i]
	P_Income_I_Level[1][i]/=P_Level[i]
	P_Income_I_Level[2][i]/=P_Level[i]
	P_Income_I_Level[3][i]/=P_Level[i]
	P_Income_I_Level[4][i]/=P_Level[i]
	P_Age_I_Level[1][i]/=P_Level[i]
	P_Age_I_Level[2][i]/=P_Level[i]
	P_Age_I_Level[3][i]/=P_Level[i]
	P_Age_I_Level[4][i]/=P_Level[i]
	P_Sex_I_Level[1][i]/=P_Level[i]
	P_Sex_I_Level[2][i]/=P_Level[i]
	P_Marry_I_Level[0][i]/=P_Level[i]
	P_Marry_I_Level[1][i]/=P_Level[i]
	P_Marry_I_Level[2][i]/=P_Level[i]
	P_Marry_I_Level[3][i]/=P_Level[i]
	P_House_I_Level[0][i]/=P_Level[i]
	P_House_I_Level[1][i]/=P_Level[i]
	P_House_I_Level[2][i]/=P_Level[i]
	P_House_I_Level[3][i]/=P_Level[i]
	P_House_I_Level[4][i]/=P_Level[i]
	P_House_I_Level[5][i]/=P_Level[i]
	P_Edu_I_Level[0][i]/=P_Level[i]
	P_Edu_I_Level[1][i]/=P_Level[i]
	P_Edu_I_Level[2][i]/=P_Level[i]
	P_Edu_I_Level[3][i]/=P_Level[i]
	P_Edu_I_Level[4][i]/=P_Level[i]
	P_Edu_I_Level[5][i]/=P_Level[i]
	P_Edu_I_Level[6][i]/=P_Level[i]
	P_Last_I_Level[1][i]/=P_Level[i]
	P_Last_I_Level[2][i]/=P_Level[i]
	P_Last_I_Level[3][i]/=P_Level[i]
	P_Work_I_Level[1][i]/=P_Level[i]
	P_Work_I_Level[2][i]/=P_Level[i]
	P_Work_I_Level[3][i]/=P_Level[i]
	P_Work_I_Level[4][i]/=P_Level[i]
	P_Level[i]/=P_Level[0]
#概率矩阵转化完毕
#输出训练结果
	#print("训练结果如下：")
	



#2-训练-结束

#3-预测分析数据
#3.1-取得循环次数以及待分析数据
cursor.execute("SELECT COUNT(Obs) FROM data_a")
NUMBER=cursor.fetchone()[0]
cursor.execute("SELECT * FROM data_a ORDER BY Obs")
#3.2-循环训练每条数据
for i in range(NUMBER):
	data = cursor.fetchone()
	#提取一条数据的各个部分，存入相应变量
	Obs=data[0]
	Time=data[1]
	Change=data[2]
	Income=data[3]
	Age=data[4]
	Sex=data[5]
	Marry=data[6]
	House=data[7]
	Edu=data[8]
	Last=data[9]
	Work=data[10]
	Level=1			#默认为1，从1开始对比概率
	#计算各个信用等级概率
	P_Level_1=	P_Time_I_Level[Time][1]*\
				P_Change_I_Level[Change][1]*\
				P_Income_I_Level[Income][1]*\
				P_Age_I_Level[Age][1]*\
				P_Sex_I_Level[Sex][1]*\
				P_Marry_I_Level[Marry][1]*\
				P_House_I_Level[House][1]*\
				P_Edu_I_Level[Edu][1]*\
				P_Last_I_Level[Last][1]*\
				P_Work_I_Level[Work][1]*\
				P_Level[1]
	P_Level_2=	P_Time_I_Level[Time][2]*\
				P_Change_I_Level[Change][2]*\
				P_Income_I_Level[Income][2]*\
				P_Age_I_Level[Age][2]*\
				P_Sex_I_Level[Sex][2]*\
				P_Marry_I_Level[Marry][2]*\
				P_House_I_Level[House][2]*\
				P_Edu_I_Level[Edu][2]*\
				P_Last_I_Level[Last][2]*\
				P_Work_I_Level[Work][2]*\
				P_Level[2]
	P_Level_3=	P_Time_I_Level[Time][3]*\
				P_Change_I_Level[Change][3]*\
				P_Income_I_Level[Income][3]*\
				P_Age_I_Level[Age][3]*\
				P_Sex_I_Level[Sex][3]*\
				P_Marry_I_Level[Marry][3]*\
				P_House_I_Level[House][3]*\
				P_Edu_I_Level[Edu][3]*\
				P_Last_I_Level[Last][3]*\
				P_Work_I_Level[Work][3]*\
				P_Level[3]
	P_Level_4=	P_Time_I_Level[Time][4]*\
				P_Change_I_Level[Change][4]*\
				P_Income_I_Level[Income][4]*\
				P_Age_I_Level[Age][4]*\
				P_Sex_I_Level[Sex][4]*\
				P_Marry_I_Level[Marry][4]*\
				P_House_I_Level[House][4]*\
				P_Edu_I_Level[Edu][4]*\
				P_Last_I_Level[Last][4]*\
				P_Work_I_Level[Work][4]*\
				P_Level[4]

	#求出最大概率，确定等级
	P_Level_Max=P_Level_1
	if P_Level_2>P_Level_Max:
		P_Level_Max=P_Level_2
		Level=2
	if P_Level_3>P_Level_Max:
		P_Level_Max=P_Level_3
		Level=3
	if P_Level_4>P_Level_Max:
		P_Level_Max=P_Level_4
		Level=4
	#将最大可能的信用等级写回数据库
	ORDER="UPDATE data_a SET LEVEL = " + str(Level) + " WHERE Obs = "+ str(Obs)
	updatecursor.execute(ORDER)
	db.commit()		#提交
	###测试代码输出
	###print(data,Obs,Level)
	#3-预测分析数据-结束

#EX.断开数据库链接
db.close()