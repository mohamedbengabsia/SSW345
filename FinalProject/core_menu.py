from interfaces import IGameMenu
from game_starter import GameStarter
from game_loader import GameLoader
from leaderboard_viewer import LeaderboardViewer

class MainMenu(IGameMenu):
    def __init__(self):
        print("Welcome to Duck Trail!")
        self.starter = GameStarter()
        self.loader = GameLoader()
        self.viewer = LeaderboardViewer()

    def startGame(self):
        self.starter.start()

    def loadGame(self):
        self.loader.load()

    def viewLeaderboard(self):
        self.viewer.view()
