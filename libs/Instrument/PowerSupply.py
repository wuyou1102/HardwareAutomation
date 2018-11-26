# -*- encoding:UTF-8 -*-
import logging
from Base import SCPI
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
        SCPI.__init__(port=port)
        self.Command = Switch(self.model_name)

    @property
    def power(self):
        @param_to_property(action=["on", "off"])
        def _power(action='off'):
            if action == "on":
                return self.send_command(cmd=self.Command.POWER_ON)
            else:
                return self.send_command(cmd=self.Command.POWER_OFF)

        return _power

    @property
    def voltage(self):
        @param_to_property(action=["set", "query"])
        def _voltage(action='set', val='5'):
            if action == 'set':
                return self.send_command(cmd=self.Command.VOLTAGE_SET(value=val))
            elif action == 'query':
                return self.send_command(cmd=self.Command.VOLTAGE)

        return _voltage

    @property
    def ampere(self):
        @param_to_property(action=["set", "query"])
        def _ampere(action='set', val='2'):
            if action == 'set':
                return self.send_command(cmd=self.Command.AMPERE_SET(value=val))
            elif action == 'query':
                return self.send_command(cmd=self.Command.AMPERE)

        return _ampere

    @property
    def system(self):
        @param_to_property(action=["remote", "local", "version", "error", "beeper", "rwlock"])
        def _system(action='version'):
            if action == "remote":
                return self.send_command(cmd=self.Command.SYS_REMOTE)
            elif action == "local":
                return self.send_command(cmd=self.Command.SYS_LOCAL)
            elif action == "version":
                return self.send_command(cmd=self.Command.SYS_VERSION)
            elif action == "error":
                return self.send_command(cmd=self.Command.SYS_ERROR)
            elif action == "beeper":
                return self.send_command(cmd=self.Command.SYS_BEEPER)
            elif action == "rwlock":
                return self.send_command(cmd=self.Command.SYS_RWLOCK)

        return _system
