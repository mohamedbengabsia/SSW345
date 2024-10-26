# Define the base class Human with private profession setting
class Human:
    def __init__(self, profession=None):
        self.__profession = profession  # Private attribute
    
    def __SetProfession(self, profession):  # Private method
        self.__profession = profession
    
    def GetProfession(self):
        return self.__profession

# Define the Student class, inheriting from Human
class Student(Human):
    def __init__(self):
        super().__init__()
        self._Human__SetProfession("Student")  # Access private method in Human class

# Define the Teacher class, inheriting from Human
class Teacher(Human):
    def __init__(self):
        super().__init__()
        self._Human__SetProfession("Teacher")  # Access private method in Human class

# Define the PairGame class
class PairGame:
    def __init__(self):
        self.m_players = [None, None]
    
    def SetPlayerOne(self, player):
        self.m_players[0] = player
    
    def SetPlayerTwo(self, player):
        # Ensure that Player Two is distinct from Player One
        if player != self.m_players[0]:
            self.m_players[1] = player
        else:
            raise ValueError("Player One and Player Two cannot be the same.")

    def Play(self):
        raise NotImplementedError("Play method must be defined in subclasses.")

# Define the Chess class, inheriting from PairGame
class Chess(PairGame):
    def Play(self):
        if self.m_players[0] and self.m_players[1]:
            print(f"{self.m_players[0].GetProfession()} and {self.m_players[1].GetProfession()} are playing Chess.")
        else:
            print("Both players must be set before playing the game.")

# Define the Checkers class, inheriting from PairGame
class Checkers(PairGame):
    def Play(self):
        if self.m_players[0] and self.m_players[1]:
            print(f"{self.m_players[0].GetProfession()} and {self.m_players[1].GetProfession()} are playing Checkers.")
        else:
            print("Both players must be set before playing the game.")

# Now let's instantiate the objects as per the requirement
student = Student()
teacher = Teacher()

# Instantiate games
chess_game = Chess()
checkers_game = Checkers()

# Set players for both games
chess_game.SetPlayerOne(student)
chess_game.SetPlayerTwo(teacher)

checkers_game.SetPlayerOne(student)
checkers_game.SetPlayerTwo(teacher)

# Play both games
chess_game.Play()
checkers_game.Play()
