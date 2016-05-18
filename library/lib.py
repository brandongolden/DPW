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

        if self._hair == "1":
            self._hair = "Blonde"
        elif self._hair == "2":
            self._hair = "Chestnut"
        elif self._hair == "3":
            self._hair = "Brown"
        elif self._hair == "4":
            self._hair = "Red"
        elif self._hair == "5":
            self._hair = "Black"
        elif self._hair == "6":
            self._hair = "Light Blonde"
        elif self._hair == "7":
            self._hair = "Grey"

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