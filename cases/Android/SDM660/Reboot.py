# -*- encoding:UTF-8 -*-
from cases import BaseCase
from libs import Utility
from libs import Command
import time


class test_LogicalDisplays(BaseCase.AndroidCase):
    name = u"开机上下屏检测"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device

    def test(self):
        Utility.execute_command(Command.adb.reboot(serial=self.device))
        Utility.execute_command(Command.adb.wait_for_device(serial=self.device))
        return self.Pass


class test_DeviceExist(BaseCase.AndroidCase):
    name = u"检查设备是否存在"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device
        print self.device

    def test(self):
        time.sleep(10)
        result = Utility.execute_command(Command.adb.devices())
        for line in result.outputs:
            if self.device in line:
                return self.Pass
        return self.Fail


if __name__ == '__main__':
    a = test_DeviceExist('8f5d878')
    a.test()
