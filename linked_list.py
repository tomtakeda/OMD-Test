class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self, *args):
        self.head = None
        self.last = None
        self.len = 0
        for arg in args:
            self.append(arg)

    @property
    def _value(self):
        if self.head:
            return self.head.data

    @_value.setter
    def _value(self, value):
        if self.head:
            self.head.data = value

    def append(self, item):
        node = ListNode(item)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.len += 1
        return True

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def print_reversed(self):
        for el in reversed(self):
            print(el)

    def __len__(self):
        return self.len

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key < 0:
            raise IndexError
        tmp = self.head
        for i in range(key):
            tmp = tmp.next
            if tmp is None:
                raise IndexError
        return tmp.data

    def __iter__(self):
        self._pointer = self.head
        return self

    def __next__(self):
        tmp = self._pointer
        if tmp is None:
            raise StopIteration
        self._pointer = tmp.next
        return tmp.data

    def __add__(self, data):
        for item in data:
            self.append(item)
        return self

    def __eq__(self, other):
        if len(other) != len(self):
            return False
        for my_item, other_item in zip(self, other):
            if my_item != other_item:
                return False
        return True


if __name__ == "__main__":
    list_ = List(1, 2, 3)
    list_.print()
    print("---------------------------------")
    list_.append(4)
    list_.print()
    print("---------------------------------")
    tail = List(5, 6)
    list_ += tail
    list_.print()
    print("---------------------------------")
    tail._value = 0
    tail.print()
    list_.print()
    print("---------------------------------")
    list_ += [7, 8]
    list_.print()
    print("---------------------------------")
    list_ += ()
    list_.print()
    print("---------------------------------")

    for elem in list_:
        print(2 ** elem)

    print("---------------------------------")
    list_.print_reversed()

    print("---------------------------------")
    empty_list = List()
    empty_list.print()

    print("---------------------------------")
    list_with_single_none_element = List(None)
    list_with_single_none_element.print()
