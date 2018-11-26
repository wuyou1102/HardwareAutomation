import Base


class Command(Base.Command):
    @property
    def SYS_ERROR(self):
        return 'SYST:ERR?'

    @property
    def SYS_VERSION(self):
        return 'SYST:VERS?'

    @property
    def SYS_REMOTE(self):
        return 'SYST:REM'

    @property
    def SYS_LOCAL(self):
        return 'SYST:LOC'

    @property
    def SYS_RWLOCK(self):
        return 'SYST:RWL'

    @property
    def SYS_BEEPER(self):
        return 'SYST:BEEP'

    @property
    def POWER_ON(self):
        return 'OUTP 1'

    @property
    def POWER_OFF(self):
        return 'OUTP 0'

    @property
    def VOLTAGE(self):
        return 'VOLT?'

    def VOLTAGE_SET(self, value):
        return 'VOLT %s' % value

    @property
    def AMPERE(self):
        return 'CURR?'

    def AMPERE_SET(self, value):
        return 'CURR %s' % value
