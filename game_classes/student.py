from human import Human  # Import directly from `human.py` within the same folder

class Student(Human):
    def __init__(self):
        super().__init__()
        self._Human__SetProfession("Student")  # Access private method in Human class
