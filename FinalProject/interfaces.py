from abc import ABC, abstractmethod

class IGameMenu(ABC):
    @abstractmethod
    def startGame(self):
        pass

    @abstractmethod
    def loadGame(self):
        pass

    @abstractmethod
    def viewLeaderboard(self):
        pass

