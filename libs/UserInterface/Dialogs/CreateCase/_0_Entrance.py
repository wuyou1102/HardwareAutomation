# -*- encoding:UTF-8 -*-
import wx
from _1_DevicesType import DeviceType
from _2_DevicesSelection import DeviceSelection
from _3_CaseSelection import CaseSelection


def entrance():
    try:
        case = dict()
        device_type = __get_device_type()
        device_name = __get_device_name(device_type=device_type)
        test_case = __get_test_case(device_type=device_type)
        test_config = __get_test_config(test_case=test_case)
        case['device_type'] = device_type
        case['device_name'] = device_name
        case['test_case'] = test_case
        case['test_config'] = test_config
        return case
    except UserWarning:
        return {}


def __get_device_type():
    dlg = DeviceType()
    if dlg.ShowModal() == wx.ID_OK:
        return dlg.get_type()
    else:
        raise UserWarning(u"用户手动中断创建测试")


def __get_device_name(device_type):
    return ""


def __get_test_case(device_type):
    return ""


def __get_test_config(test_case):
    return ""


if __name__ == '__main__':
    entrance()
