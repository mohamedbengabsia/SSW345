class Human:
    def __init__(self, profession=None):
        self.__profession = profession  # Private attribute

    def __SetProfession(self, profession):  # Private method
        self.__profession = profession

    def GetProfession(self):
        return self.__profession
