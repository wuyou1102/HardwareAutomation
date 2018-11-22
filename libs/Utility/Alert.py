# -*- encoding:UTF-8 -*-
import wx


def Info(msg, title=None):
    title = u"消息" if title is None else u"来自%s的消息" % title
    dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_INFORMATION)
    dialog.ShowModal()
    dialog.Destroy()


def Warn(msg, title=None):
    title = u"警告" if title is None else u"来自%s的警告" % title
    dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_WARNING)
    dialog.ShowModal()
    dialog.Destroy()


def Error(msg, title=None):
    title = u"错误" if title is None else u"来自%s的错误" % title
    dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_ERROR)
    dialog.ShowModal()
    dialog.Destroy()
