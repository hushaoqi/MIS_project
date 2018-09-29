import sys
import time
import pymysql
from PyQt5 import QtCore,QtWidgets
from TotalInterface import Ui_TotalInterface
from Result import Ui_NegoResult
from Sure import Ui_Sure

class Found(Exception):
    pass
class TotalInterface(QtWidgets.QMainWindow,Ui_TotalInterface):
    def __init__(self):
        super(TotalInterface,self).__init__()
        self.setupUi(self)
        self.Start.clicked.connect(self.System)
        self.Quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def System(self):
        #数据读取及企业实例化
        self.A = AProduce(self.Expect_A.text(),self.RelaxValue_A.text(),self.Priority_A.text())
        self.B = BBuyer(self.Expect_B.text(),self.RelaxValue_B.text(),self.Priority_B.text())
        self.C = CSupply(self.Expect_C_total.text(),self.RelaxValue_C_total.text(),self.Priority_C_total.text(),self.Expect_C_unit.text(),self.RelaxValue_C_unit.text(),self.Priority_C_unit.text())
        self.D = DTrains(self.Expect_D.text(),self.RelaxValue_D.text(),self.Priority_D.text())

        #初始化其他谈判信息
        self.B.setNum(20)
        self.A.setProNum(self.B.pur_num)
        self.C.setMaterialNum(self.A.pro_num)
        self.D.setMaterialNum(self.C.material_num)

        self.db = pymysql.connect(host="localhost", user="root",password="root", db="nego_db", port=3306)  # 数据库连接
        self.cur = self.db.cursor()
        # SQL更新语句
        sql_A = "update product_sup set priority = '%s',profit_expect = '%s',profit_relax_value = '%s',profit_final = '%s' where Id = 'A'"
        sql_B = "update product_pur set priority = '%s',unit_price_expect = '%s',unit_price_relax_value = '%s',unit_price_final = '%s' where Id = 'B'"
        sql_C = "update r_material_sup set total_cost_priority = '%s',total_cost_expect = '%s',total_cost_relax_value = '%s',unit_cost_priority = '%s',unit_cost_expect = '%s',unit_cost_relax_value = '%s' where Id = 'C'"
        sql_D = "update r_material_trans set priority = '%s',trans_profit_expect = '%s',trans_profit_relax_value = '%s' where Id = 'D'"
        try:
            # SQL执行
            self.cur.execute(sql_A % (self.A.priority, self.A.profit_expect, self.A.profit_relax_value, self.A.profit_final))
            self.cur.execute(sql_B % (self.B.priority, self.B.mean, self.B.relax, self.B.unit_price_final))
            self.cur.execute(sql_C % (self.C.total_cost_priority, self.C.total_cost_expect,self.C.total_cost_relax_value,self.C.unit_cost_priority, self.C.unit_cost_expect, self.C.unit_cost_relax_value))
            self.cur.execute(sql_D % (self.D.priority, self.D.trans_profit_expect, self.D.trans_profit_relax_value))
            # 提交到数据库执行
            self.db.commit()
        # except Exception as e:
        #     self.db.rollback()
        finally:
            self.db.close()

        #弹出Sure(确认)窗口
        self.MySure = SureWin()
        self.MySure.show()
        #谈判并在Result窗口显示谈判过程及结果
        self.NegoTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        NegoResult.Start_txt.append("谈判初始化：")
        NegoResult.Start_txt.append("核心企业(企业A:产品制造商)：<利润>期望值："+self.A.profit_expect+",可放松值："+self.A.profit_relax_value+",优先级："+self.A.priority)
        NegoResult.Start_txt.append("下游企业(企业B:产品购买商)：<产品单价>期望值："+self.B.mean+",可放松值："+self.B.relax+",优先级："+self.B.priority)
        NegoResult.Start_txt.append("上游企业(企业C:原料供应商)：<原料固定总费用>期望值："+self.C.total_cost_expect+",可放松值："+self.C.total_cost_relax_value+",优先级："+self.C.total_cost_priority)
        NegoResult.Start_txt.append("上游企业(企业C:原料供应商)：<原料变动单位费用>期望值："+self.C.unit_cost_expect+",可放松值："+self.C.unit_cost_relax_value+",优先级："+self.C.unit_cost_priority)
        NegoResult.Start_txt.append("上游企业(企业D:运输服务商)：<原料运输单位费用>期望值："+self.D.trans_profit_expect+",可放松值："+self.D.trans_profit_relax_value+",优先级："+self.D.priority)
        #谈判逻辑
        NegoResult.Start_txt.append("计算当前各企业收入或支出，计算当前冲突值：")
        try:
            for w in range(int(self.C.total_cost_relax_value)):
                for x in range(int(self.C.unit_cost_relax_value)):
                    for y in range(int(self.D.trans_profit_relax_value)):
                        for z in range(int(self.B.relax)):
                            self.C.fin = int(self.C.total_cost_expect) + int(self.C.unit_cost_expect) * int(self.C.material_num)
                            self.D.fin = int(self.D.trans_profit_expect) * int(self.D.material_num)
                            self.B.fin = int(self.B.mean) * int(self.B.pur_num)
                            self.A.profit_final = self.B.fin - self.D.fin - self.C.fin
                            conflict = int(self.A.profit_final) - int(self.A.profit_expect)
                            NegoResult.Start_txt.append("上游企业（企业C:原料供应商）：<收入合计>："+str(self.C.fin))
                            NegoResult.Start_txt.append("上游企业（企业B:产品购买商）：<支出合计>："+str(self.B.fin))
                            NegoResult.Start_txt.append("上游企业（企业D:原料供应商）：<收入合计>："+str(self.D.fin))
                            NegoResult.Start_txt.append("上游企业（企业A:原料供应商）：<收入合计>："+str(self.A.profit_final))
                            NegoResult.Start_txt.append("当前冲突值："+str(conflict))
                            if int(conflict) >= -int(self.A.profit_relax_value ):
                                raise  Found
                            self.B.mean = int(self.B.mean) + 1
                        self.D.trans_profit_expect = int(self.D.trans_profit_expect) - 1
                    self.C.unit_cost_expect = int(self.C.unit_cost_expect) - 1
                self.C.total_cost_expect = int(self.C.total_cost_expect) - 1
        except Found:
            pass
        NegoResult.Start_txt.append("谈判结束")
        if conflict >= -int(self.A.profit_relax_value ):
            NegoResult.Result_txt.append("谈判冲突消除！谈判成功！")
            NegoResult.Result_txt.append("谈判结果为：")
        else:
            NegoResult.Result_txt.append("谈判冲突不能消除！谈判失败！")
            NegoResult.Result_txt.append("此时的谈判局面为：")
            self.B.mean = int(self.B.mean) - 1
            self.D.trans_profit_expect = int(self.D.trans_profit_expect) + 1
            self.C.unit_cost_expect = int(self.C.unit_cost_expect) + 1
            self.C.total_cost_expect = int(self.C.total_cost_expect) + 1
        # NegoResult.Start_txt.append("" + "\n") #追加显示
        NegoResult.Result_txt.append("上游企业（企业C：原料供应商）：<原料固定费用>："+str(self.C.total_cost_expect))
        NegoResult.Result_txt.append("上游企业（企业C：原料供应商）：<原料变动单位费用>："+str(self.C.unit_cost_expect))
        NegoResult.Result_txt.append("上游企业（企业D：运输服务商）：<原料运输单位费用>："+str(self.D.trans_profit_expect))
        NegoResult.Result_txt.append("下游企业（企业B：产品购买商）：<商品单价>："+str(self.B.mean))
        NegoResult.Result_txt.append("上游企业（企业C：原料供应商）：<收入合计>："+str(self.C.fin))
        NegoResult.Result_txt.append("上游企业（企业D：运输服务商）：<收入合计>："+str(self.D.fin))
        NegoResult.Result_txt.append("下游企业（企业B：产品购买商）：<费用合计>："+str(self.B.fin))
        NegoResult.Result_txt.append("核心企业（企业A：产品生产商）：<最终利润>："+str(self.A.profit_final))
class SureWin(QtWidgets.QMainWindow,Ui_Sure):
    def __init__(self, parent = None):
        super(SureWin,self).__init__()
        self.setupUi(self)
        self.Sure.clicked.connect(self.NegoResultShow)

    def NegoResultShow(self):
        Total.MySure.close()
        NegoResult.show()

class Result(QtWidgets.QMainWindow,Ui_NegoResult):
    def __init__(self, parent = None):
        super(Result,self).__init__()
        self.setupUi(self)
        self.InforSave.clicked.connect(self.SaveResult)
        self.Quit.clicked.connect(self.Quit_ReturnTotal)

    def SaveResult(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", db="nego_db", port=3306)  # 数据库连接
        self.cur = self.db.cursor()
        sql_A = "update finally set unit_price_expect = '%s',unit_prices = '%s',profit_final = '%s',trans_profit_expect = '%s',total_cost_expect = '%s',unit_cost_expect = '%s',trans_final = '%s',material_final = '%s' where id = '1'"
        try:
            # SQL执行
            self.cur.execute(sql_A % (Total.B.mean,Total.B.fin,Total.A.profit_final,Total.D.trans_profit_expect,Total.C.total_cost_expect,Total.C.unit_cost_expect,Total.D.fin,Total.C.fin))
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            self.db.rollback()
        finally:
            self.db.close()

        #将谈判过程和结果分别追加存储到NegoProcess.txt和NegoResult.txt文件夹中
        Start = self.Start_txt.toPlainText()
        Result = self.Result_txt.toPlainText()
        file = open("NegoProcess.txt", "a+")
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if not file.readline():
            file.write("\r\n")
        file.write("开始谈判：\n")
        file.write("谈判时间：" + Total.NegoTime + "\n")
        file.write("信息记录时间：" + Time + "\n")
        file.write(Start)
        file.close()

        file = open("NegoResult.txt", "a+")
        if not file.readline():
            file.write("\r\n")
        file.write("谈判结果：\n")
        file.write("谈判时间：" + Total.NegoTime + "\n")
        file.write("信息记录时间：" + Time + "\n")
        file.write(Result)
        file.close()

    def Quit_ReturnTotal(self):
        self.close()


class AProduce(object):
    def __init__(self, profit_expect, profit_relax_value, priority):
        self.profit_expect = profit_expect
        self.profit_relax_value = profit_relax_value
        self.priority = priority
        self.pro_num = 0
        self.profit_final = 0

    def setProNum(self,pro_num):
        self.pro_num = pro_num

    def setProfit_final(self,finalProfit):
        self.profit_final = finalProfit

class BBuyer(object):
    def __init__(self, unit_price_except, unit_price_relax_value , priority):
        self.priority = priority
        self.mean = unit_price_except
        self.relax = unit_price_relax_value
        self.pur_num = 0
        self.total_price = 0
        self.unit_price_final = 0
        self.fin = 0
    def setNum(self, Num):
        self.pur_num = Num

    def setUnit_price_final(self, finalPrice):
        self.unit_price_final = finalPrice

    def calculate_total_price(self,unit_price_final,pur_num):
        self.total_price = unit_price_final * pur_num
        return self.total_price

class CSupply(object):
    def __init__(self, total_cost_expect, total_cost_relax_value, total_cost_priority, unit_cost_expect, unit_cost_relax_value, unit_cost_priority ):
        self.material_num = 0
        self.total_cost_expect = total_cost_expect
        self.total_cost_relax_value = total_cost_relax_value
        self.total_cost_priority = total_cost_priority
        self.unit_cost_expect = unit_cost_expect
        self.unit_cost_relax_value = unit_cost_relax_value
        self.unit_cost_priority = unit_cost_priority
        self.stable_price = 0
        self.pur_price = 0
        self.fin = 0
    def setMaterialNum(self,mNum):
        self.material_num = mNum

    def setStablePrice(self,stablePrice):
        self.stable_price = stablePrice

    def setPurprice(self,purPrice):
        self.pur_price = purPrice

class DTrains(object):
    def __init__(self, trans_profit_expect, trans_profit_relax_value, priority):
        self.material_num = 0
        self.trans_profit_expect = trans_profit_expect
        self.trans_profit_relax_value = trans_profit_relax_value
        self.priority = priority
        self.fin = 0
    def setMaterialNum(self,materialNum):
        self.material_num = materialNum

# class RelationRaw(object):
#     def __init__(self, trans_id, r_sup_id, p_sup_id):
#         self.trans_id = trans_id
#         self.r_sup_id = r_sup_id
#         self.p_sup_id = p_sup_id
#
#
# class RelationProduct(object):
#     def __init__(self, trans_id, p_sup_id, p_pur_id):
#         self.trans_id = trans_id
#         self.p_sup_id = p_sup_id
#         self.p_pur_id = p_pur_id

# def true_profit( ):
#     true_profit = B.pur_num * B.price - C.stable_price - B.pur_num * C.pur_price - D.pur_price * B.pur_num
#     return true_profit
#
# def c_result( ):
#     c_result = true_profit( ) - A.profit_expect
#     return c_result


def DB_init():
    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="nego_db", port=3306)  # 数据库连接
    cur = db.cursor()
    # SQL初始化语句
    sql_A = "insert into product_sup(id,profit_expect,profit_relax_value,profit_final,priority) values('A',0,0,0,1)"
    sql_B = "insert into product_pur(id,pur_num,unit_price_expect,unit_price_relax_value,unit_price_final,priority) values('B',20,0,0,0,1)"
    sql_C = "insert into r_material_sup(id,total_cost_expect,total_cost_relax_value,total_cost_priority,unit_cost_expect,unit_cost_relax_value,unit_cost_priority) values('C',0,0,1,0,0,1)"
    sql_D = "insert into r_material_trans(id,r_material_num,trans_profit_expect,trans_profit_relax_value,priority) values('D',20,0,0,1)"
    sql_A_to_B = "insert into product_dis(trans_id,p_sup_id,p_pur_id) values(1,'A','B')"
    sql_C_to_A = "insert into r_material_dis(trans_id,r_sup_id,p_sup_id) values(1,'C','A')"
    sql_fin = "insert into finally(id,unit_price_expect,unit_prices,profit_final,trans_profit_expect,total_cost_expect,unit_cost_expect,trans_final,material_final) values('1',0,0,0,0,0,0,0,0) "
    try:
        # SQL执行
        cur.execute(sql_A)
        cur.execute(sql_B)
        cur.execute(sql_C)
        cur.execute(sql_D)
        cur.execute(sql_A_to_B)
        cur.execute(sql_C_to_A)
        cur.execute(sql_fin)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        cur.close()
        db.close()
if __name__ == "__main__":
    # print("System Strat:")
    DB_init()#数据库初始化
    app = QtWidgets.QApplication(sys.argv)
    Total = TotalInterface()
    NegoResult = Result()
    Total.Negotiation_txt.setPlainText(open("Information.txt","r",encoding="utf-8").read())
    Total.show()
    sys.exit(app.exec_())