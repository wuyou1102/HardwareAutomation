# -*- encoding:UTF-8 -*-

from libs.UserInterface.Dialogs.CreateCase import Base


class LoopPanel(Base.IntSettingPage):
    def __init__(self, parent):
        Base.IntSettingPage.__init__(self, parent=parent, attr_name='loop', title=u"请输入循环次数")
