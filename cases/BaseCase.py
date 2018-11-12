class Case(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self.name

    def _check(self):
        print self.__class__


class AndroidCase(Case):
    def __init__(self, name):
        Case.__init__(self, name=name)


class Serial(Case):
    def __init__(self, name):
        Case.__init__(self, name=name)
