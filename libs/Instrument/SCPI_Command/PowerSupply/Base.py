__author__ = 'wuyou'


class Command(object):
    @property
    def SYS_ERROR(self):
        raise NotImplementedError

    @property
    def SYS_VERSION(self):
        raise NotImplementedError

    @property
    def SYS_REMOTE(self):
        raise NotImplementedError

    @property
    def SYS_LOCAL(self):
        raise NotImplementedError

    @property
    def SYS_RWLOCK(self):
        raise NotImplementedError

    @property
    def SYS_BEEPER(self):
        raise NotImplementedError

    @property
    def POWER_ON(self):
        raise NotImplementedError

    @property
    def POWER_OFF(self):
        raise NotImplementedError

    @property
    def VOLTAGE(self):
        raise NotImplementedError

    def VOLTAGE_SET(self, value):
        raise NotImplementedError

    @property
    def AMPERE(self):
        raise NotImplementedError

    def AMPERE_SET(self, value):
        raise NotImplementedError


if __name__ == '__main__':
    pass
