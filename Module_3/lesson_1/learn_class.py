# class definition
class Player:
    nickname = "Player1"
    lives = 3
    level = 1

    def who_am_i(self):
        print(f"I am Player, my name is {self.nickname} I have {self.lives} lives. Now I am on level {self.level}")

    def change_name(self):
        new_name = input("Type new name here: ")
        self.nickname = new_name

    def attack(self):
        print("Attack!")

    def defend(self):
        print("Defend")

# how to create class instance/object/екземпляр
my_player = Player()

new_list = list()
print(list)
print(new_list)

print(Player)
print(my_player)

#
# new_list.reverse()
# my_player.attack()
# my_player.defend()
# print(my_player.nickname)
print("\nWho am I:")
my_player.who_am_i()
my_player.change_name()
my_player.who_am_i()

second_player = Player()
print("P2: ", second_player.nickname)