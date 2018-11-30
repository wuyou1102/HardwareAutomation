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
            self.Log.debug(u"执行第%s次检查" % (x + 1))
            result = Utility.execute_command(
                Command.adb.shell_command(cmd='dumpsys display | grep \\\"Logical Displays: size=\\\"',
                                          serial=self.device))
            self.Log.debug(u"获得输出: \"%s\"" % result.outputs)
            for output in result.outputs:
                if "Logical Displays: size=2" in output:
                    self.Log.info(u"找到输出Logical Displays: size=2")
                    return self.Pass
        self.Log.error(u'没有找到输出Logical Displays: size=2')
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


class test_AR8020_Node(BaseCase.AndroidCase):
    name = u"检查AR8020节点和UART"

    def __init__(self, device):
        BaseCase.AndroidCase.__init__(self)
        self.device = device
        Utility.execute_command(command=Command.adb.root(serial=self.device))
        self.sleep(0.5)
        Utility.execute_command(command=Command.adb.wait_for_device(serial=self.device))
        self.On_8020(on=False)

    def On_8020(self, on=True):
        on = '1' if on else '0'
        Utility.execute_command(
            Command.adb.shell_command(cmd='echo %s > /sys/bus/platform/drivers/artosyn_ar8020/soc:ar8020/enable' % on,
                                      serial=self.device))

    def On_CIT(self, on=True):
        on = '1' if on else '0'
        Utility.execute_command(
            Command.adb.shell_command(cmd='setprop persist.data.uartlog.cit %s' % on, serial=self.device))

    def AssertUart(self):
        self.Log.debug(u"打开UART CIT测试，并等待2秒")
        self.On_CIT(on=True)
        self.sleep(2)
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog', serial=self.device))
        self.Log.debug('getprop <uartlog> ---> %s' % (exec_rslt.outputs))
        if exec_rslt.exit_code == 0 and '1' in exec_rslt.outputs:
            return True
        self.Log.error("Uart测试失败:Except ['1'] , But was %s" % exec_rslt.outputs)
        return False

    def AssertNode(self):
        result = True
        self.Log.debug(u"打开AR8020，并等待4秒")
        self.On_8020(on=True)
        self.sleep(4)
        self.Log.debug(u"开始检查AR8020节点")
        for x in range(1, 21):
            exec_rslt = Utility.execute_command(
                command=Command.adb.shell_command('ls /dev/ |grep artosyn_port', serial=self.device))
            self.Log.debug(u"第%s次结果：%s" % (x, exec_rslt.outputs))
            if exec_rslt.exit_code == 0 and len(exec_rslt.outputs) == 4:
                break
            self.sleep(0.5)
        for x in range(4):
            if "artosyn_port%s" % x in exec_rslt.outputs:
                result = result and True
            else:
                self.Log.error(u"无法找到：artosyn_port%s node" % x)
                result = result and False
        return result

    def Test(self):
        node_result = self.AssertNode()
        uart_result = self.AssertUart()
        Utility.execute_command(Command.adb.shell_command('setprop persist.data.uartlog 0', serial=self.device))
        self.Log.debug('重新设置setprop <uartlog> <--- 0')
        exec_rslt = Utility.execute_command(
            Command.adb.shell_command(cmd='getprop persist.data.uartlog', serial=self.device))
        self.Log.debug('重新获取getprop <uartlog> ---> %s' % (exec_rslt.outputs))
        self.On_CIT(on=False)
        self.On_8020(on=False)
        self.Log.debug(u"关闭AR8020 和 UART CIT")
        if node_result and uart_result:
            return self.Pass
        return self.Fail


if __name__ == '__main__':
    import wx

    app = wx.App()
    a = test_AR8020_Node('4469e8e1')
    a.Test()
