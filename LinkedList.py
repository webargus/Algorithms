
import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        node = Node.Node(data)
        if self.__is_empty():
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head = node

    def add_tail(self, data):
        if self.__is_empty():
            self.add_head(data)
        else:
            node = Node.Node(data)      # constructor of Node already points node to None as next node
            self.tail.set_next(node)
            self.tail = node

    def remove_head(self):
        if self.__is_empty():
            print("Can't remove from head: list is empty!")
            return None
        ret = self.head.get_data()
        if self.head is self.tail:              # list has only one element left
            self.head = self.tail = None        # make list empty
            return ret
        self.head = self.head.get_next()
        return ret

    def remove_tail(self):
        if self.__is_empty():
            print("Can't remove from tail: list is empty!")
            return None
        ret = self.tail.get_data()
        if self.head is self.tail:
            self.head = self.tail = None
            return ret
        node = self.head
        while node.get_next() is not self.tail:
            node = node.get_next()
        node.set_next(None)
        self.tail = node
        return ret

    def __is_empty(self):
        return self.head is None

    def __str__(self):
        node = self.head
        s = ""
        while 1:
            if node is None:
                break
            s += node.get_data() + " -> "
            node = node.get_next()
        return "[" + s[:-4] + "]"

"""
linked = LinkedList()
linked.add_head("abc")
linked.add_head("xyz")
linked.add_tail("mno")
print(linked)
linked.remove_head()
linked.remove_tail()
print(linked)
"""












