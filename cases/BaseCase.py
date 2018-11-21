import inspect
import logging
from libs.Utility.TestPrint import TestPrint

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self, loop):
        self.Print = TestPrint()
        self.init_variable()

    def init_variable(self):
        self.Pass = 0
        self.Fail = 0
        self.Total = 0

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

    def _check(self):
        print self.__class__

    def run(self):
        NotImplementedError


class AndroidCase(Case):
    def __init__(self, loop):
        Case.__init__(self, loop=loop)


class SerialCase(Case):
    def __init__(self, loop):
        Case.__init__(self, loop=loop)


if __name__ == '__main__':
    print AndroidCase.get_configs()
