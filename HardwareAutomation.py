# -*- encoding:UTF-8 -*-
__author__ = 'wuyou'
from libs.Utility import Logger
import sys
import wx
from libs import Frame
import logging

logger = logging.getLogger(__name__)
print 's'
logger.info("ssss")
print 'd'
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    app = wx.App()
    f = Frame()
    f.Show()
    app.MainLoop()
