# coding:utf-8
import serial
import logging
import re
from libs.Utility import Timeout

logger = logging.getLogger(__name__)

port_pattern = re.compile(r'(COM\d+)')


class Serial(object):
    def __init__(self, port, baudrate=115200, end_symbol='\r\n'):
        logger.debug('Serial| Init port.')
        port = re.findall(port_pattern, port)[0]
        self.port = serial.Serial(port=port, baudrate=baudrate, bytesize=8, parity='N', stopbits=1, timeout=2)
        self.end_symbol = end_symbol

    def read_line(self):
        data = ''
        while self.port.isOpen():
            char = self.port.read()
            data += char
            if data.endswith(self.end_symbol) and data.strip(self.end_symbol):
                return data.strip(self.end_symbol)

    @Timeout.timeout(1)
    def readline(self):
        data = ''
        while self.port.isOpen():
            char = self.port.read()
            data += char
            if data.endswith(self.end_symbol) and data.strip(self.end_symbol):
                return data.strip(self.end_symbol)

    def send_command(self, cmd):
        logger.debug('Serial| Send Command: %s ' % cmd)
        if self.port.isOpen():
            self.port.write(cmd + '\n')

    def close(self):
        self.port.close()


if __name__ == '__main__':
    s = Serial('COM16')
    # s.send_command('NvSetBbRcId 198 196 250 238 147')
    while True:
        print s.readline()
