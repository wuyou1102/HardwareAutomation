from libs.Instrument.SCPI_Command import CommandBase


class Command(CommandBase.PowerSupplyBase):
    @staticmethod
    def SYS_ERROR():
        return 'SYST:ERR?'

    @staticmethod
    def SYS_VERSION():
        return 'SYST:VERS?'

    @staticmethod
    def SYS_REMOTE():
        return 'SYST:REM'

    @staticmethod
    def SYS_LOCAL():
        return 'SYST:LOC'

    @staticmethod
    def SYS_RWLOCK():
        return 'SYST:RWL'

    @staticmethod
    def SYS_BEEPER():
        return 'SYST:BEEP'

    @staticmethod
    def POWER_ON():
        return 'OUTP 1'

    @staticmethod
    def POWER_OFF():
        return 'OUTP 0'

    @staticmethod
    def VOLTAGE():
        return 'VOLT?'

    @staticmethod
    def VOLTAGE_SET(value):
        return 'VOLT %s' % value

    @staticmethod
    def AMPERE():
        return 'CURR?'

    @staticmethod
    def AMPERE_SET(value):
        return 'CURR %s' % value
