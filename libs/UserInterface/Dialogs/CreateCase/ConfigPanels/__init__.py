from DevicePanel import DeviceSelection
from PowerSupplyPanel import InstrumentSelection
from IpAddressPanel import IpAddressSetting
from StoragePanel import StorageSetting

__panels = {
    u'device': DeviceSelection,
    u'power_supply': InstrumentSelection,
    u'ip': IpAddressSetting,
    u'storage': StorageSetting,
}


def Switch(_type):
    _type = _type.lower()
    if _type in __panels.keys():
        return __panels[_type]
    return None
