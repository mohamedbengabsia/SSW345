class StatsManager:
    def __init__(self):
        self.mental_health = 100
        self.physical_health = 100
        self.grades = 100

    def manageStats(self):
        print("Managing stats... Mental Health:", self.mental_health)
        print("Physical Health:", self.physical_health)
        print("Grades:", self.grades)

    def interactWithEvents(self, event):
        print(f"Updating stats based on the event: {event.event_type}")
