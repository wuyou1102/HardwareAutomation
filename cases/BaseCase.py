import inspect
import logging

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self, device, loop):
        pass

    def setUp(self):
        logging.debug()

    @classmethod
    def get_config(cls):
        print inspect.getargspec(cls.__init__).args

    def _check(self):
        print self.__class__


class AndroidCase(Case):
    def __init__(self, device, loop):
        Case.__init__(self, device=device, loop=loop)


class SerialCase(Case):
    def __init__(self, device, loop):
        Case.__init__(self, device=device, loop=loop)


if __name__ == '__main__':
    AndroidCase.get_config()
