# -*- encoding:UTF-8 -*-
from cases import BaseCase
from libs.Instrument.PowerSupply import PowerSupply
from libs.Instrument.Serial import Serial
from libs.Utility import Timeout

import random


class test_RebootAfterBoot(BaseCase.SerialCase):
    name = u"开机完成后重启"

    def __init__(self, device, power_supply):
        BaseCase.SerialCase.__init__(self)
        self.power_supply = PowerSupply(port=power_supply)
        self.serial = Serial(port=device)
        self.power_supply.power.off()
        self.power_supply.voltage.set(value=4.2)

    def Test(self):
        # self.Debug(time.time())
        self.power_supply.power.on()
        self.Info(u"开启电源。")
        try:
            wait_for_boot_success(self)
            # self.Debug(time.time())
            return self.ResultPass
        except Timeout.Timeout:
            return self.ResultFail
        finally:
            self.power_supply.power.off()
            self.Info(u"关闭电源。")
            self.sleep(1)


@Timeout.timeout(6)
def wait_for_boot_success(obj):
    while True:
        line = obj.serial.read_line()
        obj.Debug(repr(line))
        if "CPU2: main\tmain ground function start" in line:
            obj.Info(u"AR8020已经开机完成")
            break


class test_RebootAfterBoot_SW16(BaseCase.SerialCase):
    name = u"开机完成后重启_SW16"

    def __init__(self, device, SW16_device, SW16_button_1, SW16_button_2):
        BaseCase.SerialCase.__init__(self)
        self.device = device
        self.SW16_device = SW16_device
        self.SW16_button_1 = SW16_button_1
        self.SW16_button_2 = SW16_button_2
        # self.power_supply = PowerSupply(port=power_supply)
        # self.serial = Serial(port=device)
        # self.power_supply.power.off()
        # self.power_supply.voltage.set(value=4.2)

    def Test(self):
        self.SW16_button_1.ON()
        self.sleep(0.5)
        self.SW16_button_2.ON()
        self.sleep(0.5)
        self.SW16_button_1.OFF()
        self.sleep(0.5)
        self.SW16_button_2.OFF()
        self.sleep(0.5)
