from interfaces import IGameMenu

class MenuDecorator(IGameMenu):
    def __init__(self, menu: IGameMenu):
        self._menu = menu

    def startGame(self):
        self._menu.startGame()

    def loadGame(self):
        self._menu.loadGame()

    def viewLeaderboard(self):
        self._menu.viewLeaderboard()

class LoggingMenuDecorator(MenuDecorator):
    def startGame(self):
        print("[LOG] Starting game...")
        super().startGame()
        print("[LOG] Game started.")

    def loadGame(self):
        print("[LOG] Loading game...")
        super().loadGame()
        print("[LOG] Game loaded.")

    def viewLeaderboard(self):
        print("[LOG] Viewing leaderboard...")
        super().viewLeaderboard()
        print("[LOG] Leaderboard displayed.")
