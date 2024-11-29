from human import Human  # Import directly from `human.py` within the same folder

class Teacher(Human):
    def __init__(self):
        super().__init__()
        self._Human__SetProfession("Teacher")  # Access private method in Human class
