import sys
import os

# Add the specific directory to the Python path
sys.path.append(r"C:\Users\mbeng\OneDrive\Desktop\School Files\Year 3\2024 Fall Semester\ssw345\midterm1ExtraCredit\game_classes")

# Now import the classes
from student import Student
from teacher import Teacher
from chess import Chess
from checkers import Checkers

# Instantiate players
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
