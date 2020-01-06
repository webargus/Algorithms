

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data


class DoubleNode(Node):

    def __init__(self, data=None):
        super(DoubleNode, self).__init__(data)
        self.prev = None

    def set_prev(self, node):
        self.prev = node

    def get_prev(self):
        return self.prev






