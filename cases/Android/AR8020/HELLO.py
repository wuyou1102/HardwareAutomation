from cases import BaseCase


class test_hello(BaseCase.AndroidCase):
    def __init__(self):
        BaseCase.AndroidCase(self, name=u"测试hello world")
