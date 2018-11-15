# -*- encoding:UTF-8 -*-
from cases import BaseCase


class test_LogicalDisplays(BaseCase.AndroidCase):
    name = u"开机上下屏检测"

    def __init__(self, device, loop):
        BaseCase.AndroidCase.__init__(self, device=device, loop=loop)



