# -*- encoding:UTF-8 -*-
from cases import BaseCase
from libs.Instrument.PowerSupply import PowerSupply
from libs.Instrument.Serial import Serial
from libs import Utility
from libs.Utility import Timeout


class test_RebootAfterBoot(BaseCase.SerialCase):
    name = u"开机完成后重启"

    def __init__(self, device, power_supply):
        BaseCase.SerialCase.__init__(self)
        self.power_supply = PowerSupply(port=power_supply)
        self.serial = Serial(port=device)
        self.power_supply.power.off()
        self.power_supply.voltage.set(value=12)

    def Test(self):
        self.power_supply.power.on()
        self.Info(u"开启电源。")
        try:
            wait_for_boot_success(self)
            return self.ResultPass
        except Timeout.Timeout:
            return self.ResultFail
        finally:
            for x in range(60):
                self.Info(u"重启等待：%s" % x)
                self.sleep(1)
            self.Info(u"关闭电源并等待3秒")
            self.power_supply.power.off()
            self.sleep(3)


class test_RebootDuringBootProcess(BaseCase.SerialCase):
    name = u"开机过程中重启"

    def __init__(self, device, power_supply):
        BaseCase.SerialCase.__init__(self)
        self.power_supply = PowerSupply(port=power_supply)
        self.serial = Serial(port=device)
        self.power_supply.power.off()
        self.power_supply.voltage.set(value=12)

    def Test(self):
        self.power_supply.power.on()
        self.Info(u"开启电源。")
        self.sleep(Utility.Random.integer(5, 15))
        self.Info(u"关闭电源并等待3秒")
        self.power_supply.power.off()
        self.sleep(3)
        self.power_supply.power.on()
        self.Info(u"重新开启电源。")
        try:
            wait_for_boot_success(self)
            return self.ResultPass
        except Timeout.Timeout:
            return self.ResultFail
        finally:
            self.Info(u"关闭电源并等待3秒")
            self.power_supply.power.off()
            self.sleep(3)


class test_RebootToConfigMode(BaseCase.SerialCase):
    name = u"开机到配置模式"

    def __init__(self, device, SW16_device, SW16_button1, SW16_button2):
        BaseCase.SerialCase.__init__(self)
        self.serial = Serial(port=device)
        self.SW16_device = SW16_device
        self.SW16_power = SW16_button1
        self.SW16_switch = SW16_button2
        self.SW16_device.OFF()
        self.SW16_switch.OFF()

    def Test(self):
        self.SW16_switch.ON()
        self.sleep(1)
        self.SW16_power.ON()
        self.Info(u"开启电源。")
        self.sleep(5)
        self.SW16_switch.OFF()
        try:
            wait_for_boot_success(self)
            return self.ResultPass
        except Timeout.Timeout:
            return self.ResultFail
        finally:

            self.Info(u"关闭电源并等待3秒")
            self.SW16_power.OFF()
            self.sleep(3)


@Timeout.timeout(40)
def wait_for_boot_success(obj):
    while True:
        line = obj.serial.read_line()
        obj.Debug(repr(line))
        if "A7 boot up successfully." in line or "A7 boot up succe[" in line:
            obj.Info(u"AR9201已经完成开机")
            break
