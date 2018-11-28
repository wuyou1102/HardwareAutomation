# -*- encoding:UTF-8 -*-
import inspect
import logging
import time
import traceback
from libs.Config import String
from libs.UserInterface.LogMonitor import LogMonitor

logger = logging.getLogger(__name__)


class Case(object):
    name = None

    def __init__(self):
        self.LogMonitor = LogMonitor()
        self.count = 0
        self.Log = Log(self)

    def BeforeTest(self):
        self.Log.debug(u'Before Test.')

    def AfterTest(self):
        self.Log.debug(u'After Test.')

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
        result = String.NotTest
        try:
            self.BeforeTest()
            result = self.Test()
            self.AfterTest()
        except Exception as e:
            print e.message
            self.Log.traceback()
            result = self.Error
        finally:
            return result

    @property
    def Pass(self):
        self.Log.result(String.Pass)
        return String.Pass

    @property
    def Fail(self):
        self.Log.result(String.Fail)
        return String.Fail

    @property
    def Error(self):
        self.Log.error(String.Error)
        return String.Error

    def Show(self, show=True):
        self.LogMonitor.Show(show=show)

    def IsShown(self):
        return self.LogMonitor.IsShown()

    def SetTitle(self, title):
        self.LogMonitor.SetTitle(title)

    def get_count(self):
        return self.count

    def Finished(self):
        self.LogMonitor.Destroy()


class Log(object):
    def __init__(self, parent):
        self.LogMonitor = parent.LogMonitor
        self.get_count = parent.get_count

    def debug(self, msg):
        self.LogMonitor.Debug(index=self.get_count(), msg=msg)

    def info(self, msg):
        self.LogMonitor.Info(index=self.get_count(), msg=msg)

    def error(self, msg):
        self.LogMonitor.Error(index=self.get_count(), msg=msg)

    def result(self, msg):
        self.LogMonitor.Result(index=self.get_count(), msg=msg)

    def warm(self, msg):
        self.LogMonitor.Warm(index=self.get_count(), msg=msg)

    def traceback(self):
        self.LogMonitor.Error(index=self.get_count(), msg='Exception')
        tmp = traceback.format_exc()
        if tmp != 'None\n':
            self.LogMonitor.Error(index=self.get_count(), msg=tmp.strip('\n'))


class AndroidCase(Case):
    def __init__(self):
        Case.__init__(self)


class SerialCase(Case):
    def __init__(self):
        Case.__init__(self)


if __name__ == '__main__':
    print AndroidCase.get_configs()
