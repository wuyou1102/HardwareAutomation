__author__ = 'wuyou'


class SCPIBase(object):
    @staticmethod
    def CLS():
        return '*CLS'

    @staticmethod
    def IDN():
        return '*IDN? '


class PowerSupplyBase(SCPIBase):
    @staticmethod
    def SYS_ERROR():
        raise NotImplementedError

    @staticmethod
    def SYS_VERSION():
        raise NotImplementedError

    @staticmethod
    def SYS_REMOTE():
        raise NotImplementedError

    @staticmethod
    def SYS_LOCAL():
        raise NotImplementedError

    @staticmethod
    def SYS_RWLOCK():
        raise NotImplementedError

    @staticmethod
    def SYS_BEEPER():
        raise NotImplementedError

    @staticmethod
    def POWER_ON():
        raise NotImplementedError

    @staticmethod
    def POWER_OFF():
        raise NotImplementedError

    @staticmethod
    def VOLTAGE():
        raise NotImplementedError

    @staticmethod
    def VOLTAGE_SET(value):
        raise NotImplementedError

    @staticmethod
    def AMPERE():
        raise NotImplementedError

    @staticmethod
    def AMPERE_SET(value):
        raise NotImplementedError


if __name__ == '__main__':
    pass
