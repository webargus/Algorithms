
import Node


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        node = Node.DoubleNode(data)
        if self.__is_empty():
            self.head = self.tail = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node

    def add_tail(self, data):
        if self.__is_empty():
            self.add_head(data)
        else:
            node = Node.DoubleNode(data)
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node

    def remove_head(self):
        if self.__is_empty():
            print("Can't remove from head: list is empty!")
            return None
        ret = self.head.get_data()
        if self.head is self.tail:
            self.head = self.tail = None
            return ret
        self.head = self.head.get_next()
        self.head.set_prev(None)          # unref pointer to prev node (header) and make it garbage collectible
        return ret

    def remove_tail(self):
        if self.__is_empty():
            print("Can't remove from tail: list is empty!")
            return None
        ret = self.tail.get_data()
        if self.head is self.tail:
            self.tail = self.head = None
            return ret
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)
        return ret

    def __str__(self, reverse=False):
        s = ""
        if reverse:
            node = self.tail
        else:
            node = self.head
        while 1:
            if node is None:
                break
            s += node.get_data() + " -> "
            if reverse:
                node = node.get_prev()
            else:
                node = node.get_next()
        return "[" + s[:-4] + "]"

    def __is_empty(self):
        return self.head is None


"""
dbl_linked = DoubleLinkedList()
dbl_linked.add_head("abc")
dbl_linked.add_tail("xyz")
dbl_linked.add_tail("123")
print(dbl_linked)
print(dbl_linked.__str__(True))
dbl_linked.remove_head()
dbl_linked.remove_tail()
print(dbl_linked)
dbl_linked.remove_tail()
print(dbl_linked)
"""
