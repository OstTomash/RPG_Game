from characters import Character
from npc import Bot
from .constants import characters_boosts


class Game:
    def __init__(self, character_1: Character, character_2: Character) -> None:
        self.character_1 = character_1
        self.character_2 = character_2
        self.initial_state = {}

    def save_health_defence_damage(self) -> None:
        self.initial_state = {
            "character_1": self.get_character_state(self.character_1),
            "character_2": self.get_character_state(self.character_2)
        }

    def restore_health_defence(self) -> None:
        self.set_character_state(self.character_1, self.initial_state["character_1"])
        self.set_character_state(self.character_2, self.initial_state["character_2"])

    @staticmethod
    def get_character_state(character: Character) -> dict:
        return {
            "health": character.health,
            "defence": character.defence,
            "damage": character.damage
        }

    @staticmethod
    def set_character_state(character: Character, state: dict) -> None:
        for attr, value in state.items():
            setattr(character, attr, value)

    @staticmethod
    def training_arena(character: Character, bot: Bot) -> None:
        char_strike_damage = character.strike
        bot.boost_bot(character.level)
        bot_strike_damage = bot.attack

        if character.fatal_prop:
            char_strike_damage += character.fatal_damage

        if bot_strike_damage < character.defence:
            character.reduce_defence(bot_strike_damage)
        elif bot_strike_damage >= character.defence:
            bot_strike_damage -= character.defence
            character.defence_off()
            character.reduce_health(bot_strike_damage)

        bot.reduce_health(char_strike_damage)

    @staticmethod
    def arena_winner(character: Character, bot: Bot):
        if character.health > 0 >= bot.health:
            character.experience_add(bot.level)
            character.level_up()
            prize = bot.drop_item()
            if prize:
                character.inventory.add_item(prize)
            return "Congrats! You kicked bot's ass!"

        if character.health <= 0 < bot.health:
            character.experience_drop()
            return "You lost to the bot. Loser."

        if character.health <= 0 and bot.health <= 0:
            character.experience_drop()
            return "Both characters lost."

    def boost_char_damage(self) -> None:
        char_1_type = self.character_1.char_class
        char_2_type = self.character_2.char_class

        if char_1_type == char_2_type:
            return

        if char_2_type in characters_boosts.get(char_1_type, []):
            self.character_1.type_boost_damage()
        elif char_1_type in characters_boosts.get(char_2_type, []):
            self.character_2.type_boost_damage()

    def check_winner(self) -> None | str:
        player_1 = self.character_1.health
        player_2 = self.character_2.health

        if player_1 > 0 > player_2:
            winner = self.character_1
            loser = self.character_2
        elif player_1 <= 0 < player_2:
            winner = self.character_2
            loser = self.character_1
        elif player_1 <= 0 and player_2 <= 0:
            self.restore_health_defence()
            self.character_1.experience_drop()
            self.character_2.experience_drop()
            return "Both characters lost."
        else:
            return None

        winner.experience_add(loser.level)
        winner.level_up()
        winner.level_dependent_boost()
        loser.experience_drop()

        print(f"\nThe winner:\n{winner}")
        return f"The winner:\n{winner}"

    def take_a_strike(self) -> None:
        player_1_strike = self.character_1.strike
        player_2_strike = self.character_2.strike

        if self.character_1.fatal_prop:
            player_1_strike += self.character_1.fatal_damage
        if self.character_2.fatal_prop:
            player_2_strike += self.character_2.fatal_damage

        for attacker, defender in ((self.character_1, self.character_2), (self.character_2, self.character_1)):
            damage = player_1_strike if attacker == self.character_1 else player_2_strike
            print('ERRROOOOR', damage)
            if damage < defender.defence:
                defender.reduce_defence(damage)
            else:
                damage -= defender.defence
                defender.defence_off()
                defender.reduce_health(damage)
                print(f"{attacker.name} strikes {defender.name} for {damage} damage.")
