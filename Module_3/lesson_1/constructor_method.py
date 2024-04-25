# Dunder (magic) method - double underscored method

# print(dir(list))

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


print(Player.number_of_players)
my_player = Player("NoobName", 13, "Warrior")
print(Player.number_of_players)
second_player = Player("ProName", 31, "Mage")
print(Player.number_of_players)
# my_player.who_am_i()
# second_player.who_am_i()



