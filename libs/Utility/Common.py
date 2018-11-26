# -*- encoding:UTF-8 -*-
import subprocess
import logging
from libs import Command

__logger = logging.getLogger(__name__)


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


def execute_command(command):
    outputs = list()
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    __logger.debug('********************************************************')
    __logger.debug('* EXECUTED COMMAND:\"%s\"' % command)
    try:
        for line in iter(p.stdout.readline, b''):
            line = line.strip('\r\n')
            __logger.debug("* STDOUT: {line}".format(line=line))
            outputs.append(line)
    finally:
        exit_code = p.wait()
        p.kill()
        __logger.debug('* EXIT CODE: \"%s\"' % exit_code)
        __logger.debug('********************************************************')
        return ExecuteResult(exit_code=exit_code, outputs=outputs)


def get_adb_devices():
    devices = list()
    result = execute_command(Command.adb.devices())
    for line in result.outputs:
        if 'device' in line and 'List of' not in line:
            devices.append(line[:line.index('\t')])
    return devices


def get_visa_resources():
    import pyvisa
    resource_manager = pyvisa.ResourceManager()
    return resource_manager.list_resources()


def get_serial_ports():
    import serial.tools.list_ports
    ports = list()
    port_list = serial.tools.list_ports.comports()
    if len(port_list) == 0:
        __logger.info(u'Can not find ports.')
        return ports
    else:
        for port in list(port_list):
            port_name = port[1]
            ports.append(port_name)
        return sorted(ports, reverse=True)


if __name__ == '__main__':
    res = execute_command(Command.adb.shell_command('ps |grep \"ddd\"'))
    print res.outputs
    print res.exit_code
