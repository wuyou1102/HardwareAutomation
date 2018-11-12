# -*- encoding:UTF-8 -*-
from cases import BaseCase


class test_hello(BaseCase.AndroidCase):
    name = u"测试hello world"

    def __init__(self):
        BaseCase.AndroidCase(self)


if __name__ == '__main__':
    print test_hello.name
