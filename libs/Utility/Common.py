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
    try:
        for line in iter(p.stdout.readline, b''):
            __logger.info(line)
            outputs.append(line)
    finally:
        exit_code = p.wait()
        __logger.info('Executed command:\"%s\" and exit code is : \"%s\"' % (command, exit_code))
        return ExecuteResult(exit_code=exit_code, outputs=outputs)


def get_adb_devices():
    devices = list()
    result = execute_command(Command.adb.devices())
    for line in result.outputs:
        if 'device' in line and 'List of' not in line:
            devices.append(line[:line.index('\t')])
    return devices


if __name__ == '__main__':
    print get_adb_devices()
