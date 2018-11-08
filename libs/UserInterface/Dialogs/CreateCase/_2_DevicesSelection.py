# -*- encoding:UTF-8 -*-
import Base


class DeviceSelection(Base.DialogWindow):
    def __init__(self):
        Base.DialogWindow.__init__(self, size=(50, 60), name=u"请选择设备")
