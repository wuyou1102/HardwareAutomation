# -*- encoding:UTF-8 -*-
import pyvisa
import logging

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


class ExecuteResult(object):
    def __init__(self, exit_code, outputs):
        self._exit_code = exit_code
        self._outputs = outputs

    @property
    def exit_code(self):
        return self._exit_code

    @property
    def outputs(self):
        return self._outputs


class PowerSupply(object):
    def __init__(self, port):
        self.__port = port
        self.__session = None
        self.__init_session()

    @property
    def power(self):
        @param_to_property(action=["on", "off"])
        def _power(action='off'):
            if action == "on":
                return self._send_command(cmd=output_on)
            else:
                return self._send_command(cmd=output_off)

        return _power

    @property
    def voltage(self):
        @param_to_property(action=["set", "query"])
        def _voltage(action='set', val='5'):
            if action == 'set':
                return self._send_command(voltage_value_set % val)
            elif action == 'query':
                return self._send_command(voltage_query)

        return _voltage

    @property
    def ampere(self):
        @param_to_property(action=["set", "query"])
        def _ampere(action='set', val='2'):
            if action == 'set':
                return self._send_command(ampere_value_set % val)
            elif action == 'query':
                return self._send_command(ampere_query)

        return _ampere

    @property
    def system(self):
        @param_to_property(action=["remote", "local", "version", "error", "beeper", "rwlock"])
        def _system(action='version'):
            if action == "remote":
                return self._send_command(cmd=sys_remote)
            elif action == "local":
                return self._send_command(cmd=sys_local)
            elif action == "version":
                return self._send_command(cmd=sys_version)
            elif action == "error":
                return self._send_command(cmd=sys_error)
            elif action == "beeper":
                return self._send_command(cmd=sys_beeper)
            elif action == "rwlock":
                return self._send_command(cmd=sys_rwlock)

        return _system

    def __init_session(self):
        try:
            rm = pyvisa.ResourceManager()
            self.__session = rm.open_resource(self.__port)
            self.__session.timeout = 5000
        except pyvisa.errors.VisaIOError:
            self.__session = None
            logger.error('SCPI|Initialization serial instrument failure')

    def _send_command(self, cmd):
        if self.__session is None:
            return False, 'Session has not been established'
        if cmd.endswith('?'):
            logger.debug("SCPI|Query:%s" % cmd)
            exec_result = self.__query(cmd)
        else:
            logger.debug("SCPI|Write:%s" % cmd)
            exec_result = self.__write(cmd)
        error_msg = self.__query(sys_error)
        logger.debug("SCPI|Error msg:%s" % error_msg)
        if error_msg == '0, \"No error\"':
            return True, exec_result
        else:
            return False, error_msg

    def __query(self, cmd):
        try:
            return self.__session.query(cmd).strip('\r\n')
        except pyvisa.errors.VisaIOError:
            return 'ERROR'

    def __write(self, cmd):
        return self.__session.write(cmd)
