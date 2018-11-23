# -*- encoding:UTF-8 -*-
import wx
import logging

logger = logging.getLogger(__name__)


def Info(msg, title=None):
    title = u"消息" if title is None else u"来自 \"%s\" 的消息" % title
    logger.info('{title}:{msg}'.format(title=title, msg=msg))
    dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_INFORMATION)
    dialog.ShowModal()
    dialog.Center()
    dialog.Destroy()


def Warn(msg, title=None):
    title = u"警告" if title is None else u"来自 \"%s\" 的警告" % title
    logger.warn('{title}:{msg}'.format(title=title, msg=msg))
    dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_WARNING)
    dialog.ShowModal()
    dialog.Center()
    dialog.Destroy()


def Error(msg, title=None):
    title = u"错误" if title is None else u"来自 \"%s\" 的错误" % title
    logger.error('{title}:{msg}'.format(title=title, msg=msg))
    dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_ERROR)
    dialog.ShowModal()
    dialog.Center()
    dialog.Destroy()
