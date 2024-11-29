from pair_game import PairGame  # Import directly from `pair_game.py` within the same folder

class Checkers(PairGame):
    def Play(self):
        if self.m_players[0] and self.m_players[1]:
            print(f"{self.m_players[0].GetProfession()} and {self.m_players[1].GetProfession()} are playing Checkers.")
        else:
            print("Both players must be set before playing the game.")
