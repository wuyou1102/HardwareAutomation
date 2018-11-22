# -*- encoding:UTF-8 -*-

from libs.UserInterface.Dialogs.CreateCase import Base
from libs.Config import String


class LoopSelection(Base.IntSettingPage):
    def __init__(self, parent):
        Base.IntSettingPage.__init__(self, parent=parent, attr_name=String.CaseLoop, min=0, max=10000, initial=100,
                                     title=u"请输入循环次数(0为无穷): ")
