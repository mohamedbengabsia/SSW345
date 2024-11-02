class PairGame:
    def __init__(self):
        self.m_players = [None, None]

    def SetPlayerOne(self, player):
        self.m_players[0] = player

    def SetPlayerTwo(self, player):
        if player != self.m_players[0]:
            self.m_players[1] = player
        else:
            raise ValueError("Player One and Player Two cannot be the same.")

    def Play(self):
        raise NotImplementedError("Play method must be defined in subclasses.")
