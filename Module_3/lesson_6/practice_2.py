import random


class MyList:
    class _MyListIterator:
        def __iter__(self):
            print("GET ITERATOR OBJECT")
            return self

        def __init__(self, list_obj):
            print("INIT ITERATOR")

            self._list_obj = list_obj
            self._next_node = list_obj._head

        def __next__(self):
            # print("CALL NEXT")
            if self._next_node is None:
                raise StopIteration
            value = self._next_node.value
            # print(f"CURRENT NODE = {self._next_node}")
            self._next_node = self._next_node.next
            # if self._next_node is not None:
            #     self._next_node = self._next_node.next
            # print(f"SET CURRENT NODE: {self._next_node}")
            return value

    class _MyListElement:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = None
            self.next = None

        def __repr__(self):
            return f"ListElement({self.value}) - {id(self)}"

    def __init__(self):
        print("INIT MY LIST")
        self._length = 0
        self._head: MyList._MyListElement | None = None
        self._tail: MyList._MyListElement | None = None

    def __getitem__(self, index):
        print(f"GET ELEMENT AT {index}")
        if not 0 <= index < len(self):
            raise IndexError("Index cant be less then Zero or more then amount of elements")
        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def append(self, element_value):
        print()
        print("ADD NEW ELEMENT TO LIST")
        new_element = MyList._MyListElement(element_value)

        if self._tail is None:
            print("ITS THE FIRST EL IN LIST")
            self._head = new_element
            self._tail = new_element
        else:
            self._tail.next = new_element  # Вкажемо що праворуч від останнього елементу з'явився новий
            new_element.prev = self._tail  # Вкажемо що в нового елемента є сусід ліворуч

            self._tail = new_element  # Останнім елементом списку є новий елемент

        self._length += 1

    def __len__(self):
        return self._length

    def __iter__(self):
        return MyList._MyListIterator(self)


my_list = MyList()

for _ in range(10):
    new_value = random.randint(1, 100)
    my_list.append(new_value)

print(my_list)

x = my_list[3]
# print(x)

for i in my_list:
    print(f">>> {i}")


class NewListClass(list):
    class _MyListIterator:
        def __iter__(self):
            print("GET ITERATOR OBJECT")
            return self

        def __init__(self, list_obj):
            print("INIT ITERATOR")
            self.counter = 0
            self._list_obj = list_obj

        def __next__(self):
            if self.counter > len(self._list_obj):
                raise StopIteration
            value = self._list_obj[self.counter]
            self.counter += 1
            return value

    def __iter__(self):
        return NewListClass._MyListIterator(self)


l = NewListClass()
for _ in range(10):
    new_value = random.randint(1, 100)
    l.append(new_value)

print(l)

for i in l:
    print(i)
