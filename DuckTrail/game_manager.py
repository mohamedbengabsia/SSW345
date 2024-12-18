from event import Event
from stats_manager import StatsManager
from ui_manager import UIManager
from player_manager import PlayerManager

class GameManager:
    def __init__(self):
        print("Initializing GameManager...")
        self.stats_manager = StatsManager()
        self.ui_manager = UIManager()
        self.player_manager = PlayerManager("Player1", "Explorer", "In Progress")

    def storeEvents(self):
        print("Storing game events...")

    def sendBackendInfo(self):
        print("Sending backend information...")

    def interactWithUIManager(self):
        print("Interacting with UI Manager...")
        self.ui_manager.updateUI()

    def startGame(self):
        print("Starting the game...")
        event = Event("Intro Event")
        event.presentEvent()
        event.determineStatEffects()
        self.stats_manager.manageStats()
        self.ui_manager.updateUI()

    def loadGame(self):
        print("Loading game...")
        self.ui_manager.updateUI()

    def viewLeaderboard(self):
        print("Displaying leaderboard...")
        self.ui_manager.showLeaderboard()
