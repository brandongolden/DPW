class Simoleons(object):
    def __init__(self, simoleons):
        self._simoleons = int(simoleons) + int(2)

    @property
    def simoleons(self):
        return self._simoleons

    @simoleons.setter
    def simoleons(self, value):
        self._simoleons = value

class Sim(object):
    def __init__(self, name, hair):
        self._name = name
        self._hair = hair

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hair(self):
        return self._hair

    @hair.setter
    def hair(self, value):
        self._hair = value