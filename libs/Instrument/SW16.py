# -*- encoding:UTF-8 -*-
import serial
import threading
import time
from InstrumentBase import SharedBaseInstrument


def generator_index():
    while True:
        for _idx in range(60, 144):
            yield chr(_idx)


class SW16(SharedBaseInstrument):
    @classmethod
    def create(cls, port):
        cls.pool[port] = _Equipment(port=port)


class _Equipment(object):
    def __init__(self, port, bandrate=115200):
        self.port = serial.Serial(port=port, baudrate=bandrate, bytesize=8, parity='N', stopbits=1, timeout=2)
        self.lock = threading.Lock()
        self.__buttons = dict()
        self.idx = generator_index()
        self.__init_button()
        time.sleep(1)

    def get_button(self, _id):
        return self.__buttons[_id]

    def get_buttons(self):
        return self.__buttons.keys()

    def __init_button(self):
        btns = {
            'Button0': '\x00',
            'Button1': '\x01',
            'Button2': '\x02',
            'Button3': '\x03',
            'Button4': '\x04',
            'Button5': '\x05',
            'Button6': '\x06',
            'Button7': '\x07',
            'Button8': '\x08',
            'Button9': '\x09',
            'ButtonA': '\x0A',
            'ButtonB': '\x0B',
            'ButtonC': '\x0C',
            'ButtonD': '\x0D',
            'ButtonE': '\x0E',
            'ButtonF': '\x0F',
        }
        for k, v in btns.items():
            self.__buttons[k] = _Button(_id=v, idx=self.idx, send=self.send_command)

    def __read(self):
        line = ''
        while self.port.isOpen():
            char = self.port.read()
            line += char
            if char == '\xdd':
                return line

    def send_command(self, cmd):
        if self.lock.acquire():
            try:
                if self.port.isOpen():
                    self.port.write(cmd)
                    self.port.flush()
                    return self.__read()
            finally:
                time.sleep(0.15)
                self.lock.release()

    def close(self):
        self.port.close()

    def ON(self):
        command = '\xAA\x0A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{idx}\xBB'.format(
            idx=self.idx.next())
        self.send_command(cmd=command)

    def OFF(self):
        command = '\xAA\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{idx}\xBB'.format(
            idx=self.idx.next())
        self.send_command(cmd=command)


class _Button(object):
    def __init__(self, _id, idx, send):
        self._id = _id
        self._send = send
        self._idx = idx

    def ON(self):
        command = '\xAA\x0F{id}\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{idx}\xBB'.format(
            id=self._id, idx=self._idx.next())
        self._send(cmd=command)

    def OFF(self):
        command = '\xAA\x0F{id}\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{idx}\xBB'.format(
            id=self._id, idx=self._idx.next())
        self._send(cmd=command)


if __name__ == '__main__':
    a = _Equipment('COM10')
    a.OFF()
    btn = a.get_button('Button0')
    btn.ON()
    btn.OFF()
