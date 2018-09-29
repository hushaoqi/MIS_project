import wx, wx.grid
import matplotlib.pyplot as plt
import numpy as np

'''
f=open(r'D:\111\datafile.txt')
ineed=f.read()
print(ineed[0])
f.close()
'''


class GridData(wx.grid.PyGridTableBase):
    _cols = "配送中心 1 2 3 4 5 6 7 8 9 10 11 12 容量".split()
    _data = [
        "1 0 0 0 0 0 0 0 0 0 0 0 0 17".split(),
        "4 0 0 0 0 0 0 0 0 0 0 0 0 7 ".split(),
        "8 0 0 0 0 0 0 0 0 0 0 0 0 15".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 ".split(),
    ]
    _picture = []

    _highlighted = set()

    def GetColLabelValue(self, col):
        return self._cols[col]

    def GetNumberRows(self):
        return len(self._data)

    def GetNumberCols(self):
        return len(self._cols)

    def GetValue(self, row, col):
        return self._data[row][col]

    def SetValue(self, row, col, val):
        self._data[row][col] = val

    def GetAttr(self, row, col, kind):
        attr = wx.grid.GridCellAttr()
        attr.SetBackgroundColour(wx.GREEN if row in self._highlighted else wx.WHITE)
        return attr

    def set_value(self, row, col, val):
        self._highlighted.add(row)
        self.SetValue(row, col, val)


class Test(wx.Frame):
    def __init__(self, num):
        wx.Frame.__init__(self, None)

        self.data = GridData()
        self.picture = GridData._picture
        self.grid = wx.grid.Grid(self)
        self.grid.SetTable(self.data)

        hbox10 = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, label="查看收敛曲线")
        btn.Bind(wx.EVT_BUTTON,self.Show_Picture)
        # vbox.Add(hbox10)

        texta = wx.StaticText(self, -1, "最优结果费用:%s" % num)

        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.grid, 1, wx.EXPAND)
        self.Sizer.Add(btn, 0, wx.EXPAND)
        self.Sizer.Add(texta, 0, wx.EXPAND)

    def Show_Picture(self, event):
        # def f(picture):
        #     return self.picture

        # t1 = np.arange(0.0, 5.0, 0.1)
        # t2 = np.arange(0.0, 5.0, 0.02)
        #
        # # plt.figure(100)
        # plt.subplot(211)
        # plt.plot(t1, self.picture, 'bo', t2, self.picture, 'k')
        #
        # plt.subplot(212)
        # plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
        # plt.show()
        plt.plot(self.picture)
        plt.plot(self.picture, 'ro')
        plt.show()
    # def OnTest(self, event):
    #     self.data.show_picture(_picture)
    #     self.grid.Refresh()


'''
app = wx.PySimpleApp()
app.TopWindow = Test()
app.TopWindow.Show()
app.MainLoop()

'''
