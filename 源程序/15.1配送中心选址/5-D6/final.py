import wx,socket
import matplotlib.pyplot as plt
from main import *
from useroutput import *

sshuzu=[0,0,0,0,0]
        #此序列存5个参数

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(600, 300))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(panel, -1, "配送中心数量（ <12）")
        hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1 = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER)
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1.Bind(wx.EVT_TEXT, self.OnEnterPressed1)
        vbox.Add(hbox1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "种群数量( >100)")
        hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2 = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER)
        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)
        self.t2.Bind(wx.EVT_TEXT, self.OnEnterPressed2)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        l3 = wx.StaticText(panel, -1, "交叉概率( <1)")
        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3 = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER)
        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)
        self.t3.Bind(wx.EVT_TEXT, self.OnEnterPressed3)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        l4 = wx.StaticText(panel, -1, "变异概率( <1)")
        hbox4.Add(l4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t4 = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER)
        hbox4.Add(self.t4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox4)
        self.t4.Bind(wx.EVT_TEXT,self.OnEnterPressed4)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        l5 = wx.StaticText(panel, -1, "最大迭代次数")
        hbox5.Add(l5, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t5 = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER)          #wx.TE_PROCESS_ENTER*****
        hbox5.Add(self.t5, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox5)
        self.t5.Bind(wx.EVT_TEXT, self.OnEnterPressed5)

        hbox6=wx.BoxSizer(wx.HORIZONTAL)
        btn=wx.Button(panel,label="next")
        hbox6.Add(btn,1,wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        btn.Bind(wx.EVT_BUTTON,self.GoToNext)
        vbox.Add(hbox6)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()
        self.Fit()


    def OnEnterPressed1(self, event):
        print("Enter pressed")
        s1=event.GetString()
        sshuzu[0]=int(s1)
        print(s1)

    def OnEnterPressed2(self, event):
        print("Enter pressed")
        s2=event.GetString()
        sshuzu[1]=int(s2)
        print(s2)
    def OnEnterPressed3(self, event):
        print("Enter pressed")
        s3=event.GetString()
        sshuzu[2]=float(s3)
        print(s3)
    def OnEnterPressed4(self, event):
        print("Enter pressed")
        s4=event.GetString()
        sshuzu[3]=float(s4)
        print(s4)
    def OnEnterPressed5(self, event):
        print("Enter pressed")
        s5=event.GetString()
        sshuzu[4]=int(s5)
        print(s5)

    def GoToNext(self,event):
        print("OK")
        (cos, shu1, picture) = fengzhang(sshuzu[0], sshuzu[1], sshuzu[2], sshuzu[3], sshuzu[4])
        print(cos)
        print(shu1)
        print(picture)
        for i in range(sshuzu[0]):
            for j in range(14):
                if j == 0:
                    GridData._data[i][j] = shu1[i][j] + 1
                else:
                    GridData._data[i][j] = shu1[i][j]

        GridData._picture=picture

        dlg=Test(cos)

        dlg.Show()

app=wx.App()
Mywin(None,"user input")
app.MainLoop()
'''
(cos,shu1)=fengzhang(sshuzu[0],sshuzu[1],sshuzu[2],sshuzu[3],sshuzu[4])
print(cos)
print(shu1)
'''
