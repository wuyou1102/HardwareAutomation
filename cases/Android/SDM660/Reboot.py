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
        self.Info(u"重启设备:%s,并等待设备重启完成" % self.device)
        Utility.execute_command(Command.adb.reboot(serial=self.device))
        Utility.execute_command(Command.adb.wait_for_device(serial=self.device))
        self.Info(u"设备已启动,继续等待4秒后检查")
        self.sleep(3)
        for x in range(20):
            self.sleep(1)
            self.Debug(u"执行第%s次检查" % (x + 1))
            result = Utility.execute_command(
                Command.adb.shell_command(cmd='dumpsys display | grep \\\"Logical Displays: size=\\\"',
                                          serial=self.device))
            self.Debug(u"获得输出: \"%s\"" % result.outputs)
            for output in result.outputs:
                if "Logical Displays: size=2" in output:
                    self.Info(u"找到输出Logical Displays: size=2")
                    return self.ResultPass
        self.Error(u'没有找到输出Logical Displays: size=2')
        return self.ResultFail


class test_DeviceExist(BaseCase.AndroidCase):
    name = u"检查设备是否存在"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device

    def Test(self):
        result = Utility.execute_command(Command.adb.devices())
        for line in result.outputs:
            if self.device in line:
                return self.ResultPass
        return self.ResultFail


class test_AR8020_Node(BaseCase.AndroidCase):
    name = u"检查AR8020节点和UART"

    def __init__(self, device, storage):
        BaseCase.AndroidCase.__init__(self)
        self.device = device
        self.storage = storage
        Utility.execute_command(command=Command.adb.root(serial=self.device))
        self.sleep(0.5)
        Utility.execute_command(command=Command.adb.wait_for_device(serial=self.device))
        self.On_8020(on=False)

    def BeforeTest(self):
        Utility.execute_command(Command.adb.shell_command(cmd="logcat -c", serial=self.device))
        exec_rslt = Utility.execute_command(
            command=Command.adb.shell_command('ls /dev/ |grep artosyn_port', serial=self.device))
        if exec_rslt.outputs:
            self.Error("检查是否AR8020已经关闭： %s" % exec_rslt.outputs)
        else:
            self.Debug("检查是否AR8020已经关闭： %s" % exec_rslt.outputs)

    def On_8020(self, on=True):
        on = '1' if on else '0'
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo %s > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable' % on,
                                      serial=self.device))

    def On_CIT(self, on=True):
        on = '1' if on else '0'
        Utility.execute_command(
            Command.adb.shell_command(cmd='setprop persist.data.uartlog.cit %s' % on, serial=self.device))
        result = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog.cit', serial=self.device))
        self.Debug(u"检查UART CIT打开情况：%s" % result.outputs)

    def AssertUart(self):
        self.Debug(u"打开UART CIT测试，并等待2秒")
        self.On_CIT(on=True)
        self.sleep(2)
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog', serial=self.device))
        self.Debug('getprop <uartlog> ---> %s' % (exec_rslt.outputs))
        if exec_rslt.exit_code == 0 and '1' in exec_rslt.outputs:
            return True
        self.Error("Uart测试失败:Expect ['1'] , But was %s" % exec_rslt.outputs)
        t = Utility.execute_command(command=Command.adb.shell_command("logcat -d", serial=self.device))
        for line in t.outputs:
            self.Info(line)
        return False

    def AssertNode(self):
        result = True
        self.Debug(u"打开AR8020，并等待4秒")
        self.On_8020(on=True)
        self.sleep(4)
        self.Debug(u"开始检查AR8020节点")
        for x in range(1, 21):
            exec_rslt = Utility.execute_command(
                command=Command.adb.shell_command('ls /dev/ |grep artosyn_port', serial=self.device))
            self.Debug(u"第%s次结果：%s" % (x, exec_rslt.outputs))
            if exec_rslt.exit_code == 0 and len(exec_rslt.outputs) == 4:
                break
            self.sleep(0.5)
        for x in range(4):
            if "artosyn_port%s" % x in exec_rslt.outputs:
                result = result and True
            else:
                self.Error(u"无法找到：artosyn_port%s node" % x)
                result = result and False
        return result

    def Test(self):
        node_result = self.AssertNode()
        uart_result = self.AssertUart()
        Utility.execute_command(Command.adb.shell_command('setprop persist.data.uartlog 0', serial=self.device))
        self.Debug('重新设置setprop <uartlog> <--- 0')
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog', serial=self.device))
        self.Debug('重新获取getprop <uartlog> ---> %s' % (exec_rslt.outputs))
        self.On_CIT(on=False)
        self.On_8020(on=False)
        self.Debug(u"关闭AR8020 和 UART CIT")
        if node_result and uart_result:
            return self.ResultPass
        return self.ResultFail


class test_AR8020_Node_For_DVT(BaseCase.AndroidCase):
    name = u"检查AR8020节点和UART(660为DVT)"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device
        Utility.execute_command(command=Command.adb.root(serial=self.device))
        self.sleep(0.5)
        Utility.execute_command(command=Command.adb.wait_for_device(serial=self.device))
        self.On_8020(on=False)

    def BeforeTest(self):
        Utility.execute_command(Command.adb.shell_command(cmd="logcat -c", serial=self.device))

    def On_8020(self, on=True):
        on = '1' if on else '0'
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo %s > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable' % on,
                                      serial=self.device))

    def On_CIT(self, on=True):
        on = '1' if on else '0'
        Utility.execute_command(
            Command.adb.shell_command(cmd='setprop persist.data.uartlog.cit %s' % on, serial=self.device))
        result = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog.cit', serial=self.device))
        self.Debug(u"检查UART CIT打开情况：%s" % result.outputs)

    def AssertUart(self):
        self.Debug(u"打开UART CIT测试，并等待2秒")
        self.On_CIT(on=True)
        self.sleep(2)
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog', serial=self.device))
        self.Debug('getprop <uartlog> ---> %s' % (exec_rslt.outputs))
        if exec_rslt.exit_code == 0 and '1' in exec_rslt.outputs:
            return True
        self.Error("Uart测试失败:Expect ['1'] , But was %s" % exec_rslt.outputs)
        t = Utility.execute_command(command=Command.adb.shell_command("logcat -d", serial=self.device))
        for line in t.outputs:
            self.Info(line)
        return False

    def AssertNode(self):
        result = True
        self.Debug(u"打开AR8020，并等待4秒")
        self.On_8020(on=True)
        self.sleep(4)
        self.Debug(u"开始检查AR8020节点")
        for x in range(1, 21):
            exec_rslt = Utility.execute_command(
                command=Command.adb.shell_command(
                    'ls /sys/devices/soc/c200000.hsusb/c200000.dwc3/xhci-hcd.0.auto/usb1/1-1/ | grep 1-1 ',
                    serial=self.device))
            self.Debug(u"第%s次结果：%s" % (x, exec_rslt.outputs))
            if exec_rslt.exit_code == 0 and len(exec_rslt.outputs) == 4:
                break
            self.sleep(0.5)
        for x in range(4):
            if "1-1:1.%s" % x in exec_rslt.outputs:
                result = result and True
            else:
                self.Error(u"无法找到：1.%s" % x)
                result = result and False
        return result

    def Test(self):
        node_result = self.AssertNode()
        uart_result = True #self.AssertUart()
        Utility.execute_command(Command.adb.shell_command('setprop persist.data.uartlog 0', serial=self.device))
        self.Debug('重新设置setprop <uartlog> <--- 0')
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog', serial=self.device))
        self.Debug('重新获取getprop <uartlog> ---> %s' % (exec_rslt.outputs))
        self.On_CIT(on=False)
        self.Debug(u"关闭AR8020 和 UART CIT")
        if node_result and uart_result:

            self.On_8020(on=False)
            return self.ResultPass
        while True:
            self.sleep(10)
        return self.ResultFail


if __name__ == '__main__':
    import wx

    app = wx.App()
    a = test_AR8020_Node('4469e8e1')
    a.Test()
