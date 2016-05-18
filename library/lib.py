class Simoleons(object):
    def __init__(self, simoleons):
        self._simoleons = simoleons * 2

    @property
    def simoleons(self):
        return self._simoleons

    @simoleons.setter
    def simoleons(self, simoleons):
        self._simoleons = simoleons
