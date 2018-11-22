import inspect
import logging
from libs.Utility.TestPrint import TestPrint
from libs.Config import String

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self):
        self.Print = TestPrint()
        self.Pass = String.Pass
        self.Fail = String.Fail
        self.Error = String.Error

    def teardown(self):
        self.Print.info('Teardown')

    def setup(self):
        self.Print.info('Setup')

    def test(self):
        raise NotImplementedError

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
        result = String.Error
        try:
            self.setup()
            result = self.test()
            self.teardown()
        except Exception:
            self.Print.traceback()
            result = self.Error
        finally:
            return result


class AndroidCase(Case):
    def __init__(self):
        Case.__init__(self)


class SerialCase(Case):
    def __init__(self):
        Case.__init__(self)


if __name__ == '__main__':
    print AndroidCase.get_configs()
