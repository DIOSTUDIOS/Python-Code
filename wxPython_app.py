# coding=utf-8

# import wx


# class App(wx.App):
# 	def OnInit(self):
# 		frame = wx.Frame(parent=None, title=r"Hello wxPython")
# 		frame.Show()

# 		return True


# if __name__ == "__main__":
# 	app = App()
# 	app.MainLoop()

import wx


app = wx.App()
frame = wx.Frame(None, title=r"Hello wxPython")
frame.Show()
app.MainLoop()