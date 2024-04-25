
class Player:
    # class attributes
    number_of_players = 0

    def __init__(self, nickname, age, character):
        # instance/object attributes
        self.name = nickname
        self.age = age
        self.character = character
        self.level = 1
        self.lives = 3

        # Player.number_of_players += 1
        self.__class__.number_of_players += 1
        self.who_am_i()

    # instance/object method
    def who_am_i(self):
        print(f"I am Player, my name is {self.name} {self.age} y.o. Now I play for {self.character}, I am on level {self.level}")

    @classmethod
    def reset_players_counter(cls):
        cls.number_of_players = 0

    @staticmethod
    def independent_method(current_level, amount_of_xp):
        plus_levels = amount_of_xp / 100
        new_level = current_level + plus_levels
        return new_level




my_player = Player("sdnask", 32, "asjdnasda")
print(Player.number_of_players)
Player.reset_players_counter()
print(Player.number_of_players)
my_player.independent_method(10, 20000)

Player.independent_method(10, 20000)




