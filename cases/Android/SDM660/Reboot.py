# -*- encoding:UTF-8 -*-
from cases import BaseCase
from libs import Utility
from libs import Command


class test_LogicalDisplays(BaseCase.AndroidCase):
    name = u"开机上下屏检测"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device

    def Test(self):
        self.Log.info(u"重启设备:%s,并等待设备重启完成" % self.device)
        Utility.execute_command(Command.adb.reboot(serial=self.device))
        Utility.execute_command(Command.adb.wait_for_device(serial=self.device))
        self.Log.info(u"设备已启动,继续等待4秒后检查")
        self.sleep(3)
        for x in range(20):
            self.sleep(1)
            self.Log.info(u"执行第%s次检查" % (x + 1))
            result = Utility.execute_command(
                Command.adb.shell_command(cmd='dumpsys display | grep \\\"Logical Displays: size=\\\"',
                                          serial=self.device))
            self.Log.info(u"获得输出: \"%s\"" % result.outputs)
            for output in result.outputs:
                if "Logical Displays: size=2" in output:
                    return self.Pass
        return self.Fail


class test_DeviceExist(BaseCase.AndroidCase):
    name = u"检查设备是否存在"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device

    def Test(self):
        result = Utility.execute_command(Command.adb.devices())
        for line in result.outputs:
            if self.device in line:
                return self.Pass
        return self.Fail


if __name__ == '__main__':
    a = test_DeviceExist('8f5d878')
    a.test()
