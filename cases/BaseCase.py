# -*- encoding:UTF-8 -*-
import inspect
import logging
from libs.Utility.TestPrint import TestPrint
from libs.Config import String
import time

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self):
        self.Print = TestPrint()
        self.count = 0

    def BeforeTest(self):
        self.Print.debug('Before Test.')

    def AfterTest(self):
        self.Print.debug('After Test.')

    def Test(self):
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

    @staticmethod
    def sleep(secs):
        time.sleep(secs)

    def run(self):
        self.count += 1
        try:
            self.BeforeTest()
            result = self.Test()
            self.AfterTest()
        except Exception:
            self.Print.traceback()
            return self.Error
        finally:
            return result

    def set_redirect(self, redirect):
        self.Print.set_redirect(redirect=redirect)

    def clear_redirect(self):
        self.Print.set_redirect(redirect=None)

    @property
    def Pass(self):
        self.Print.info(u"测试结果：Pass")
        return String.Pass

    @property
    def Fail(self):
        self.Print.info(u"测试结果：Fail")
        return String.Fail

    @property
    def Error(self):
        self.Print.error(u"测试结果：Error")
        return String.Error


class AndroidCase(Case):
    def __init__(self):
        Case.__init__(self)


class SerialCase(Case):
    def __init__(self):
        Case.__init__(self)


if __name__ == '__main__':
    print AndroidCase.get_configs()
