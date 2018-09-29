import xlrd
from xlutils.copy import copy
import xlwt
import sys
from PyQt5.QtCore import QProcess
# TFILE_AD="E:\\D9训练样本数据.xls"
# AFILE_AD="E:\\D9待分析数据.xls"
TFILE_AD="D9训练样本数据.xls"
AFILE_AD="D9待分析数据.xls"


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

#2.1-打开表格文档
TFile = xlrd.open_workbook(TFILE_AD,formatting_info=True)
Tsheet = TFile.sheet_by_index(0)


#2.2-确定循环次数并取得训练样本数目

#确定循环次数，存入NUMBER
NUMBER=Tsheet.nrows

#2.3-训练
for i in range(1,NUMBER):
	row = Tsheet.row_values(i)		#获取第i行数据
	#提取一条数据的各个成分，存入对应变量
	Time=int(Tsheet.cell_value(i,1))
	Change=int(Tsheet.cell_value(i,2))
	Income=int(Tsheet.cell_value(i,4))
	Age=int(Tsheet.cell_value(i,5))
	Sex=int(Tsheet.cell_value(i,6))
	Marry=int(Tsheet.cell_value(i,7))
	House=int(Tsheet.cell_value(i,8))
	Edu=int(Tsheet.cell_value(i,9))
	Last=int(Tsheet.cell_value(i,10))
	Work=int(Tsheet.cell_value(i,11))
	Level=int(Tsheet.cell_value(i,3))
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

	
#2-训练-结束

#3-预测分析数据
#3.1-取得循环次数以及待分析数据
AFile = xlrd.open_workbook(AFILE_AD,formatting_info=True)
Asheet = AFile.sheet_by_index(0)
NUMBER=Asheet.nrows
Level_Set=[0 for i in range(NUMBER)]

#3.2-循环训练每条数据
for i in range(1,NUMBER):
	row = Asheet.row_values(i)
	#提取一条数据的各个部分，存入相应变量
	Time=int(Asheet.cell_value(i,1))
	Change=int(Asheet.cell_value(i,2))
	Income=int(Asheet.cell_value(i,3))
	Age=int(Asheet.cell_value(i,4))
	Sex=int(Asheet.cell_value(i,5))
	Marry=int(Asheet.cell_value(i,6))
	House=int(Asheet.cell_value(i,7))
	Edu=int(Asheet.cell_value(i,8))
	Last=int(Asheet.cell_value(i,9))
	Work=int(Asheet.cell_value(i,11))
	Obs=int(Asheet.cell_value(i,0))
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
	Level_Set[i]=Level


#将最大可能的信用等级写回待分析文件
Wxlsx=copy(AFile)
Wsheet=Wxlsx.get_sheet(0)
for i in range(1,NUMBER):
	Wsheet.write(i,10,Level_Set[i])
Wxlsx.save(AFILE_AD)
	#3-预测分析数据-结束
code = QProcess.execute("explorer D9待分析数据.xls")
