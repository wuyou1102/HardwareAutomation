# -*- encoding:UTF-8 -*-

import Base
import cases
from libs import Utility


class CaseNameSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name="case_name", need_refresh=False)
        self._case = dict()

    def get_choices(self):
        self._case = dict()
        _type = self._get_value("device_type")
        _group_name = self._get_value("case_group")
        _case_groups = getattr(cases, _type)
        _group_attr = getattr(_case_groups, _group_name)
        __test_case_names = [x for x in dir(_group_attr) if x.startswith('test_')]
        for case_name in __test_case_names:
            case = getattr(_group_attr, case_name)
            try:
                if case.name:
                    self._case[case.name] = case
                else:
                    self._case[case_name] = case
            except AttributeError:
                self._case[case_name] = case_name
        return self._case.keys()

    def update(self):
        attr_value = self.wx_list.GetStringSelection()
        if attr_value:
            case = self._case[attr_value]
            self._set_value('case_name', attr_value)
            self._set_value('case_class', case)
            self.parent.add_config_page(case.get_config())
        else:
            Utility.Alert.Error(u"请选择选项")
            raise AttributeError