import asyncio
# from justcard.poker.game import play_game
from .poker.game import main


if __name__ == "__main__":
    # num_players = int(input("Enter the number of players (2-4): "))
    # while not (2 <= num_players <= 4):
    #     num_players = int(input("Enter a valid number of players (2-4): "))
    # asyncio.run(play_game(num_players))

    main()
