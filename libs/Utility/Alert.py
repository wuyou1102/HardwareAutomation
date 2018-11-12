# -*- encoding:UTF-8 -*-
import wx


def Info(msg):
    dialog = wx.MessageDialog(None, msg, u"消息", wx.OK | wx.ICON_INFORMATION)
    dialog.ShowModal()
    dialog.Destroy()


def Warn(msg):
    dialog = wx.MessageDialog(None, msg, u"警告", wx.OK | wx.ICON_WARNING)
    dialog.ShowModal()
    dialog.Destroy()


def Error(msg):
    dialog = wx.MessageDialog(None, msg, u"错误", wx.OK | wx.ICON_ERROR)
    dialog.ShowModal()
    dialog.Destroy()
