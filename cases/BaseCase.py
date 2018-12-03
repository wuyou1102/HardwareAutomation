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

    def BeforeTest(self):
        pass

    def AfterTest(self):
        pass

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
        result = None
        try:
            self.BeforeTest()
            result = self.Test()
            self.AfterTest()
        except Exception as e:
            print e.message
            self.Log.traceback()
            result = self.ResultError
        finally:
            return result

    def Show(self, show=True):
        self.LogMonitor.Show(show=show)

    def IsShown(self):
        return self.LogMonitor.IsShown()

    def SetTitle(self, title):
        self.LogMonitor.SetTitle(title)

    def Finished(self):
        self.LogMonitor.Destroy()

    def Debug(self, msg):
        self.LogMonitor.Debug(index=self.count, msg=msg)

    def Info(self, msg):
        self.LogMonitor.Info(index=self.count, msg=msg)

    def Error(self, msg):
        self.LogMonitor.Error(index=self.count, msg=msg)

    def Warm(self, msg):
        self.LogMonitor.Warm(index=self.count, msg=msg)

    def Traceback(self):
        self.LogMonitor.Error(index=self.get_count(), msg='Exception')
        tmp = traceback.format_exc()
        if tmp != 'None\n':
            self.LogMonitor.Error(index=self.get_count(), msg=tmp.strip('\n'))

    @property
    def ResultPass(self):
        self.LogMonitor.Result(index=self.count, msg=u"测试成功")
        return String.Pass

    @property
    def ResultFail(self):
        self.LogMonitor.Result(index=self.count, msg=u"测试失败")
        return String.Fail

    @property
    def ResultError(self):
        self.LogMonitor.Result(index=self.count, msg=u"测试异常")
        return String.Error


class AndroidCase(Case):
    def __init__(self):
        Case.__init__(self)


class SerialCase(Case):
    def __init__(self):
        Case.__init__(self)


if __name__ == '__main__':
    print AndroidCase.get_configs()
