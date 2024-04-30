import pickle

from characters import Character, Warrior, Mage, Rogue, Paladin
from npc import Bot
from equipment import Helmet, LWeapon, RWeapon, Shoes, Shield, Ring
from game import Game

players = dict()
file_name: str = 'players.pkl'


def open_file() -> None:
    global players

    try:
        with open(file_name, 'rb') as file:
            players = pickle.load(file)
    except FileNotFoundError:
        print("Creating a new file...")


def save_file() -> None:
    with open(file_name, 'wb') as file:
        pickle.dump(players, file)


def choose_character(name) -> Character:
    characters = Warrior(), Paladin(), Mage(), Rogue()
    equipment = {
        'helmet': Helmet(),
        'sword': LWeapon(),
        'axe': RWeapon(),
        'shield': Shield(),
        'shoes': Shoes(),
        'ring': Ring()
    }
    result = "\n".join([f"{i + 1}: {c.char_class}" for i, c in enumerate(characters)])

    print(result)

    while True:
        index = input(f"{name}, choose a type for your character. Enter number: ")

        try:
            player = characters[int(index) - 1]
            break
        except (ValueError, IndexError):
            print("Incorrect index. Try again.")

    player.name = name

    for item in equipment.values():
        player.inventory.add_item(item)

    return player


def training(player, game) -> None:
    go_train = input(f"{player.name}, do you want to train? (type 'y' or 'n')")

    if go_train == "y":
        while True:
            new_bot = next(Bot.generate_bot())

            while True:
                game.training_arena(player, new_bot)

                if game.arena_winner(player, new_bot):
                    break

            cont = input("Do you want to continue (type 'y' or 'n'): ")
            if cont == "n":
                break


def main() -> None:
    while True:
        open_file()
        player1_name = input("Enter the name of the first player: ")

        if not players.get(player1_name):
            player1 = choose_character(player1_name)
            players[player1.name] = player1

        player1 = players[player1_name]

        player2_name = input("Enter the name of the second player: ")

        if not players.get(player2_name):
            player2 = choose_character(player2_name)
            players[player2.name] = player2

        player2 = players[player2_name]

        player1.check_inventory()
        player1.check_armory()

        player2.check_inventory()
        player2.check_armory()

        new_game = Game(player1, player2)
        new_game.save_health_defence_damage()

        training(player1, new_game)
        training(player2, new_game)

        new_game.restore_health_defence()
        new_game.boost_char_damage()

        while True:

            new_game.take_a_strike()
            if new_game.check_winner():
                break

        save_file()

        another_round = input("One more round? (type 'y' or 'n') ")

        if another_round == "n":
            break


if __name__ == "__main__":
    main()
