# -*- encoding:UTF-8 -*-
from cases import BaseCase
from libs import Utility


class test_PingIpAddress(BaseCase.Case):
    name = u"通过PingIP检查连接情况"

    def __init__(self, ip):
        BaseCase.Case.__init__(self)
        self.ip = ip
        self.command = 'ping %s -n 1' % self.ip

    def Test(self):
        self.sleep(1)
        result = Utility.execute_command(self.command, encoding='gb2312')
        line = result.outputs[2]
        if "TTL=" in line:
            self.Debug("%-14s>> %s" % (self.ip, line))
            return self.ResultPass
        else:
            self.Error("%-14s>> %s" % (self.ip, line))
            return self.ResultFail
