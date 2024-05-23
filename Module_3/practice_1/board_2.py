# getter setter

class Item:
    def __init__(self, size, color, name):
        self.__my_secret = size
        self.color = color
        self.name = name

    @property
    def size(self):
        print("You GET size of Item")
        return str(self.__my_secret) + " meters"

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("Item.size can by only <type 'int'> ")
        print("You SET size of Item")
        self.__my_secret = new_size

    @size.deleter
    def size(self):
        print("You delete size of Item")
        del self.__my_secret


my_item = Item(10, "red", "ball")
print(my_item.size)
print(my_item.color)
my_item.size = 5.2
print(my_item.size)
del my_item.size

print("End of Code")
