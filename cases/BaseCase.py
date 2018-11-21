import inspect
import logging
from libs.Utility.TestPrint import TestPrint

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self, loop):
        self.Print = TestPrint()
        self._pass = 0
        self._fail = 0
        self._total = 0
        self._stop_flag = False
        self._pause_flag = False

    def tearDown(self):
        self.Print.info('sss')

    def setUp(self):
        self.Print.info('dddd')

    @classmethod
    def get_configs(cls):
        args = inspect.getargspec(cls.__init__).args
        ignore_list = ['self']
        configs = list()
        for arg in args:
            if arg not in ignore_list:
                configs.append(arg)
        return configs

    @classmethod
    def convert_dict_to_tuple(cls, **kwargs):
        args_name = inspect.getargspec(cls.__init__).args
        args_value = list()
        for arg_name in args_name:
            if arg_name != "self":
                args_value.append(kwargs.get(arg_name))
        return tuple(args_value)

    def run(self):
        NotImplementedError

    def stop(self):
        self.stop_flag = True

    def pause(self):
        self.pause_flag = not self.pause_flag


class AndroidCase(Case):
    def __init__(self, loop):
        Case.__init__(self, loop=loop)


class SerialCase(Case):
    def __init__(self, loop):
        Case.__init__(self, loop=loop)


if __name__ == '__main__':
    print AndroidCase.get_configs()
