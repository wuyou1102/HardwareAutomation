class Case(object):
    name = None

    def __init__(self):
        pass

    def _check(self):
        print self.__class__


class AndroidCase(Case):
    def __init__(self):
        Case.__init__(self)


class Serial(Case):
    def __init__(self):
        Case.__init__(self)
