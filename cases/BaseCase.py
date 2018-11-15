import inspect
import logging
from libs.Utility.TestPrint import TestPrint

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self, device, loop):
        self.Print = TestPrint()

    def setUp(self):
        self.Print.debug('sss')

    def tearDown(self):
        self.Print.info('sss')

    def prcess(self):
        self

    @classmethod
    def get_configs(cls):
        args = inspect.getargspec(cls.__init__).args
        ignore_list = ['self', 'device']
        configs = list()
        for arg in args:
            if arg not in ignore_list:
                configs.append(arg)
        return configs

    def _check(self):
        print self.__class__

    def run(self):
        NotImplementedError


class AndroidCase(Case):
    def __init__(self, device, loop):
        Case.__init__(self, device=device, loop=loop)


class SerialCase(Case):
    def __init__(self, device, loop):
        Case.__init__(self, device=device, loop=loop)


if __name__ == '__main__':
    print AndroidCase.get_configs()
