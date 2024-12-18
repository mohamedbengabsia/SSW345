class Event:
    def __init__(self, event_type: str):
        self.event_type = event_type

    def presentEvent(self):
        print(f"Presenting event: {self.event_type}")

    def determineStatEffects(self):
        print(f"Determining the effects of {self.event_type} on stats.")
