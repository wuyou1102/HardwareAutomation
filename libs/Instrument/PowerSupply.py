# -*- encoding:UTF-8 -*-
from libs import Utility
import logging
from InstrumentBase import SCPI
from SCPI_Command import Switch

logger = logging.getLogger(__name__)


def param_to_property(*props, **kwprops):
    if props and kwprops:
        raise SyntaxError("Can not set both props and kwprops at the same time.")

    class Wrapper(object):
        def __init__(self, func):
            self.func = func
            self.kwargs, self.args = {}, []

        def __getattr__(self, attr):
            if kwprops:
                for prop_name, prop_values in kwprops.items():
                    if attr in prop_values and prop_name not in self.kwargs:
                        self.kwargs[prop_name] = attr
                        return self
            elif attr in props:
                self.args.append(attr)
                return self
            raise AttributeError("%s parameter is duplicated or not allowed!" % attr)

        def __call__(self, *args, **kwargs):
            if kwprops:
                kwargs.update(self.kwargs)
                self.kwargs = {}
                return self.func(*args, **kwargs)
            else:
                new_args, self.args = self.args + list(args), []
                return self.func(*new_args, **kwargs)

    return Wrapper


class PowerSupply(SCPI):
    def __init__(self, port):
        SCPI.__init__(self, port=port)
        self.Command = Switch(self.model_name)
        self.send_command(self.Command.CLS())
        self.send_command(self.Command.SYS_REMOTE())

    @property
    def power(self):
        @param_to_property(action=["on", "off"])
        def _power(action='off'):
            if action == "on":
                return self.send_command(command=self.Command.POWER_ON())
            else:
                return self.send_command(command=self.Command.POWER_OFF())

        return _power

    @property
    def voltage(self):
        @param_to_property(action=["set", "query"])
        def _voltage(action='set', value='5'):
            if action == 'set':
                return self.send_command(command=self.Command.VOLTAGE_SET(value=value))
            elif action == 'query':
                return self.send_command(command=self.Command.VOLTAGE())

        return _voltage

    @property
    def ampere(self):
        @param_to_property(action=["set", "query"])
        def _ampere(action='set', value='2'):
            if action == 'set':
                return self.send_command(command=self.Command.AMPERE_SET(value=value))
            elif action == 'query':
                return self.send_command(command=self.Command.AMPERE())

        return _ampere

    @property
    def system(self):
        @param_to_property(action=["remote", "local", "version", "error", "beeper", "rwlock"])
        def _system(action='version'):
            if action == "remote":
                return self.send_command(command=self.Command.SYS_REMOTE())
            elif action == "local":
                return self.send_command(command=self.Command.SYS_LOCAL())
            elif action == "version":
                return self.send_command(command=self.Command.SYS_VERSION())
            elif action == "error":
                return self.send_command(command=self.Command.SYS_ERROR())
            elif action == "beeper":
                return self.send_command(command=self.Command.SYS_BEEPER())
            elif action == "rwlock":
                return self.send_command(command=self.Command.SYS_RWLOCK())

        return _system


if __name__ == '__main__':

    a = Utility.get_visa_resources()
    print a
    p = PowerSupply(a[2])
    # p.send_command(p.Command.SYS_ERROR())
    import time
    #
    # p.send_command(p.Command.SYS_REMOTE())
    # time.sleep(10)
    # p.send_command(p.Command.SYS_LOCAL())

    for x in range(10):
        p.power.on()
        time.sleep(1)
        p.power.off()
        time.sleep(1)
