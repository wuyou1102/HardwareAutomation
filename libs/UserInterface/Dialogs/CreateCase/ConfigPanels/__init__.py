def Switch(_type):
    print _type
    if _type == u'device':
        from DevicePanel import DeviceSelection
        return DeviceSelection
    elif _type == u'power_supply':
        from PowerSupplyPanel import InstrumentSelection
        return InstrumentSelection
    elif _type == u'ip':
        from IpAddressPanel import IpAddressSetting
        return IpAddressSetting
    elif _type == u'storage':
        from StoragePanel import StorageSetting
        return StorageSetting
    elif _type == u"SW16_device":
        from InstrSw16Panel import SW16DeviceSetting
        return SW16DeviceSetting
    elif _type.startswith(u'SW16_button'):
        from InstrSw16Panel import SW16ButtonSetting
        return SW16ButtonSetting
    return None
