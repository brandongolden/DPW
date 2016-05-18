"""
Brandon Golden
DPW
Reusable Library
5/18/16
"""
class Simoleons(object):
    def __init__(self, simoleons):
        # Generate how many Simoleons the Sim has by multiplying the number the user entered by 100
        self._simoleons = int(simoleons) * int(100)

    @property
    def simoleons(self):
        return self._simoleons

    @simoleons.setter
    def simoleons(self, value):
        self._simoleons = value

class Sim(object):
    def __init__(self, name, hair, eyes):
        self._name = name
        self._hair = hair
        self._eyes = eyes

        # Generate hair color using number chosen by user
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

        # Generate eye color using number chosen by user
        if self._eyes == "1":
            self._eyes = "Dark Blue"
        elif self._eyes == "2":
            self._eyes = "Light Blue"
        elif self._eyes == "3":
            self._eyes = "Green"
        elif self._eyes == "4":
            self._eyes = "Grey"
        elif self._eyes == "5":
            self._eyes = "Brown"

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


    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value