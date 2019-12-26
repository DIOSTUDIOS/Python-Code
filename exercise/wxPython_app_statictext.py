# coding=utf-8

import wx


app = wx.App()
frame = wx.Frame(None, id=-1, title=r"Hello wxPython", pos=(-1, -1), size=(-1, -1))

panel = wx.Panel(frame, id=-1)

wx.StaticText(panel, label=r"Python 之禅", pos=(100, 20))
wx.StaticText(panel, label=r"优美胜于丑陋", pos=(50, 50))
wx.StaticText(panel, label=r"明了胜于晦涩", pos=(50, 70))
wx.StaticText(panel, label=r"简介胜于复杂", pos=(50, 90))
wx.StaticText(panel, label=r"复杂胜于凌乱", pos=(50, 110))
wx.StaticText(panel, label=r"扁平胜于嵌套", pos=(50, 130))
wx.StaticText(panel, label=r"间隔胜于紧凑", pos=(50, 150))
wx.StaticText(panel, label=r"可读性很重要", pos=(50, 170))

frame.Show()
app.MainLoop()