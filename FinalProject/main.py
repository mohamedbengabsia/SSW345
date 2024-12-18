from core_menu import MainMenu
from menu_decorator import LoggingMenuDecorator

if __name__ == "__main__":
    print("----- Basic Duck Trail Menu -----")
    menu = MainMenu()
    menu.startGame()
    menu.loadGame()
    menu.viewLeaderboard()

    print("\n----- Duck Trail Menu with Logging -----")
    logged_menu = LoggingMenuDecorator(menu)
    logged_menu.startGame()
    logged_menu.loadGame()
    logged_menu.viewLeaderboard()
