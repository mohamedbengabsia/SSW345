class PlayerManager:
    def __init__(self, name: str, role: str, progress: str):
        self.name = name
        self.role = role
        self.progress = progress

    def makeDecisions(self):
        print(f"{self.name} is making decisions as a {self.role}.")

    def updateStats(self):
        print(f"{self.name}'s stats are being updated.")
