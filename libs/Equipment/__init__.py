# -*- encoding:UTF-8 -*-
__author__ = 'wuyou'


class BaseEquipment(object):
    def __init__(self):
        self.__pool = list()

    def create(self):
        raise NotImplementedError

    def get(self):
        return self.__pool


class SW16(BaseEquipment):
    def __init__(self):
        BaseEquipment.__init__(self)


class Oscillograph(BaseEquipment):
    def __init__(self):
        BaseEquipment.__init__(self)

