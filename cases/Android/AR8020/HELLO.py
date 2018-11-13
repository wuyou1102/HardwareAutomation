# -*- encoding:UTF-8 -*-
from cases import BaseCase


class test_hello(BaseCase.AndroidCase):
    name = u"测试hello world"

    def __init__(self, loop, device, **kwargs):
        BaseCase.AndroidCase(self, loop=loop, device=device)


if __name__ == '__main__':
    print test_hello.name
