"""
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    def clear(self):
        self._head = self._tail = None
        self._length = 0

    def insert(self, index, element):
        if not 0 <= index <= self._length:
            raise IndexError('list index out of range')

        new_node = MyList._ListNode(element)
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev.next = new_node
        current_node.prev = new_node

        self._length += 1

    def pop(self, index=None):
        if index is None:
            if self._tail is None:
                raise IndexError('pop from empty list')
            value = self._tail.value
            if self._length == 1:
                self._head = self._tail = None
            else:
                self._tail = self._tail.prev
                self._tail.next = None
            self._length -= 1
            return value

        if not 0 <= index < self._length:
            raise IndexError('list index out of range')

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        value = current_node.value
        if current_node.prev is None:
            self._head = current_node.next
        else:
            current_node.prev.next = current_node.next

        if current_node.next is None:
            self._tail = current_node.prev
        else:
            current_node.next.prev = current_node.prev

        self._length -= 1
        return value


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # # Обход списка
    # for element in my_list:
    #     print(element)
    #
    # print()
    #
    # # Повторный обход списка
    # for element in my_list:
    #     print(element)

    my_list.append(9)
    print(my_list)
    my_list.insert(2, 88)
    print(my_list)
    my_list.pop()
    print(my_list)
    my_list.pop(2)
    print(my_list)
    my_list.clear()
    print(my_list)


if __name__ == '__main__':
    main()
