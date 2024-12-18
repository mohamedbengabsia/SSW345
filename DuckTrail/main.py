from game_manager import GameManager

if __name__ == "__main__":
    print("----- Starting Duck Trail -----")
    game_manager = GameManager()

    # Game actions
    game_manager.startGame()
    game_manager.loadGame()
    game_manager.viewLeaderboard()
