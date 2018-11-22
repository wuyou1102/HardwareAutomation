from DevicePanel import DeviceSelection

__panels = {
    u'device': DeviceSelection,
}


def switch(_type):
    _type = _type.lower()
    if _type in __panels.keys():
        return __panels[_type]
    return None
