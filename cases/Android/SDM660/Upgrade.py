# -*- encoding:UTF-8 -*-
from cases import BaseCase
from libs import Utility
from libs import Command
import os


class test_AR8020_Bootloader(BaseCase.AndroidCase):
    name = u"升级AR80200Bootloader"
    AR8020_SDK = "resource/AR8020Upgrade/AR8020_SDK"
    AR8020_UPGRADE = "resource/AR8020Upgrade/AR8020_UPGRADE"
    BOOT = "resource/AR8020Upgrade/boot.bin"
    BOOTLOADER = "resource/AR8020Upgrade/bootloader.bin"
    APP = "resource/AR8020Upgrade/app.bin"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device
        self.ar8020_serial_number = ""

    def Test(self):
        self.root_devices()
        self.push_files()
        self.read_serial_number()
        self.upgrade_boot()
        self.upgrade_bootloader()
        self.upgrade_app()
        self.write_serial_number()
        return self.ResultPass

    def push_files(self):
        for image in [self.BOOT, self.BOOTLOADER, self.APP]:
            Utility.execute_command(
                Command.adb.push(local=image, remote="/data/local/tmp/%s" % os.path.basename(image),
                                 serial=self.device))

        for binary in [self.AR8020_SDK, self.AR8020_UPGRADE]:
            Utility.execute_command(
                Command.adb.push(local=binary, remote="/data/local/tmp/%s" % os.path.basename(binary),
                                 serial=self.device))
            Utility.execute_command(
                Command.adb.shell_command(cmd="chmod +x /data/local/tmp/%s" % os.path.basename(binary),
                                          serial=self.device)
            )
        self.Info(u"Push文件成功。")

    def root_devices(self):
        Utility.execute_command(Command.adb.root(serial=self.device))

    def open_ar8020(self):
        self.Info(u"打开AR8020")
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo 1 > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable',
                                      serial=self.device))
        self.sleep(5)
        for x in range(20):
            exec_rslt = Utility.execute_command(
                command=Command.adb.shell_command('ls /dev/ |grep artosyn_port', serial=self.device))
            self.Debug(u"第%s次结果：%s" % (x, exec_rslt.outputs))
            if exec_rslt.exit_code == 0 and len(exec_rslt.outputs) == 4:
                return True
            self.sleep(0.5)
        self.Error(u"AR8020没有打开")
        raise AssertionError(u"AR8020没有打开")

    def close_ar8020(self):
        self.Info(u"关闭AR8020")
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo 0 > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable',
                                      serial=self.device))

    def read_serial_number(self):
        self.open_ar8020()
        for x in range(20):
            exec_rslt = Utility.execute_command(
                Command.adb.shell_command(cmd="/data/local/tmp/AR8020_SDK ReadSN", serial=self.device))
            if exec_rslt.exit_code == 0 and exec_rslt.outputs[0]:
                self.ar8020_serial_number = exec_rslt.outputs[0]
                self.Info(u"获取到AR8020的SN号:%s" % self.ar8020_serial_number)
                self.close_ar8020()
                return True
        self.Error(u"没有正常获取到AR8020的SN号")
        raise AssertionError(u"没有正常获取到AR8020的SN号")

    def write_serial_number(self):
        self.open_ar8020()
        for x in range(20):
            write_rslt = Utility.execute_command(
                Command.adb.shell_command(cmd="/data/local/tmp/AR8020_SDK WriteSN %s" % self.ar8020_serial_number,
                                          serial=self.device))
            print(repr(write_rslt.outputs))
            read_rslt = Utility.execute_command(
                Command.adb.shell_command(cmd="/data/local/tmp/AR8020_SDK ReadSN", serial=self.device))
            if read_rslt.exit_code == 0 and read_rslt.outputs[0] == self.ar8020_serial_number:
                self.Info(u"写入AR8020的SN号成功")
                self.close_ar8020()
                return True
        raise AssertionError(u"没有正常获取到AR8020的SN号")

    def upgrade_boot(self):
        self.__upgrade('/data/local/tmp/boot.bin')

    def upgrade_bootloader(self):
        self.__upgrade('/data/local/tmp/bootloader.bin')

    def upgrade_app(self):
        self.__upgrade('/data/local/tmp/app.bin')

    def __upgrade(self, image):
        self.open_ar8020()
        self.Info(u"开始升级 \"%s\"" % image)
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd="/data/local/tmp/AR8020_UPGRADE %s" % image, serial=self.device))
        print repr(exec_rslt.outputs[-2])
        if exec_rslt.exit_code == 0 and "upgrade successed" in exec_rslt.outputs[-2]:
            self.Info(u"升级 \"%s\" 成功" % image)
            self.close_ar8020()
            return True
        self.Error(u"升级 \"%s\" 失败" % image)
        for output in exec_rslt.outputs:
            self.Error(output)
        raise AssertionError(u"升级 \"%s\" 失败" % image)

class test_AR8020_Bootloader1(BaseCase.AndroidCase):
    name = u"测试AR80200Bootloader"
    AR8020_SDK = "resource/AR8020Upgrade/AR8020_SDK"
    AR8020_UPGRADE = "resource/AR8020Upgrade/AR8020_UPGRADE"
    BOOT = "resource/AR8020Upgrade/boot.bin"
    BOOTLOADER = "resource/AR8020Upgrade/bootloader.bin"
    APP = "resource/AR8020Upgrade/app.bin"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device
        self.ar8020_serial_number = ""
        self.root_devices()
        self.push_files()

    def Test(self):
        self.read_serial_number()
        self.upgrade_boot()
        self.upgrade_bootloader()
        # self.upgrade_app()
        self.write_serial_number()
        return self.ResultPass

    def push_files(self):
        for image in [self.BOOT, self.BOOTLOADER, self.APP]:
            Utility.execute_command(
                Command.adb.push(local=image, remote="/data/local/tmp/%s" % os.path.basename(image),
                                 serial=self.device))

        for binary in [self.AR8020_SDK, self.AR8020_UPGRADE]:
            Utility.execute_command(
                Command.adb.push(local=binary, remote="/data/local/tmp/%s" % os.path.basename(binary),
                                 serial=self.device))
            Utility.execute_command(
                Command.adb.shell_command(cmd="chmod +x /data/local/tmp/%s" % os.path.basename(binary),
                                          serial=self.device)
            )
        self.Info(u"Push文件成功。")

    def root_devices(self):
        Utility.execute_command(Command.adb.root(serial=self.device))

    def open_ar8020(self):
        self.Info(u"打开AR8020")
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo 1 > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable',
                                      serial=self.device))
        self.sleep(5)
        for x in range(20):
            exec_rslt = Utility.execute_command(
                command=Command.adb.shell_command('ls /dev/ |grep artosyn_port', serial=self.device))
            self.Debug(u"第%s次结果：%s" % (x, exec_rslt.outputs))
            if exec_rslt.exit_code == 0 and len(exec_rslt.outputs) == 4:
                return True
            self.sleep(0.5)
        self.Error(u"AR8020没有打开")
        raise AssertionError(u"AR8020没有打开")

    def close_ar8020(self):
        self.Info(u"关闭AR8020")
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo 0 > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable',
                                      serial=self.device))

    def read_serial_number(self):
        self.open_ar8020()
        for x in range(20):
            exec_rslt = Utility.execute_command(
                Command.adb.shell_command(cmd="/data/local/tmp/AR8020_SDK ReadSN", serial=self.device))
            if exec_rslt.exit_code == 0 and exec_rslt.outputs[0]:
                self.ar8020_serial_number = exec_rslt.outputs[0]
                self.Info(u"获取到AR8020的SN号:%s" % self.ar8020_serial_number)
                self.close_ar8020()
                return True
        self.Error(u"没有正常获取到AR8020的SN号")
        raise AssertionError(u"没有正常获取到AR8020的SN号")

    def write_serial_number(self):
        self.open_ar8020()
        for x in range(20):
            write_rslt = Utility.execute_command(
                Command.adb.shell_command(cmd="/data/local/tmp/AR8020_SDK WriteSN %s" % self.ar8020_serial_number,
                                          serial=self.device))
            print(repr(write_rslt.outputs))
            read_rslt = Utility.execute_command(
                Command.adb.shell_command(cmd="/data/local/tmp/AR8020_SDK ReadSN", serial=self.device))
            if read_rslt.exit_code == 0 and read_rslt.outputs[0] == self.ar8020_serial_number:
                self.Info(u"写入AR8020的SN号成功")
                self.close_ar8020()
                return True
        raise AssertionError(u"没有正常获取到AR8020的SN号")

    def upgrade_boot(self):
        self.__upgrade('/data/local/tmp/boot.bin')

    def upgrade_bootloader(self):
        self.__upgrade('/data/local/tmp/bootloader.bin')

    def upgrade_app(self):
        self.__upgrade('/data/local/tmp/app.bin')

    def __upgrade(self, image):
        self.open_ar8020()
        self.Info(u"开始升级 \"%s\"" % image)
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd="/data/local/tmp/AR8020_UPGRADE %s" % image, serial=self.device))
        print repr(exec_rslt.outputs[-2])
        if exec_rslt.exit_code == 0 and "upgrade successed" in exec_rslt.outputs[-2]:
            self.Info(u"升级 \"%s\" 成功" % image)
            self.close_ar8020()
            return True
        self.Error(u"升级 \"%s\" 失败" % image)
        for output in exec_rslt.outputs:
            self.Error(output)
        raise AssertionError(u"升级 \"%s\" 失败" % image)

if __name__ == '__main__':
    import wx

    os.chdir("C:\Users\OEMUSER\PycharmProjects\HardwareAutomation")
    app = wx.App()
    a = test_AR8020_Bootloader('4465f1bc')
    a.Test()
