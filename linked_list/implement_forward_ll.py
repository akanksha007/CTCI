class Node:
    def __init__(self, data, nextNode = None, previousNode = None):
        self.value = data
        self.next = nextNode
        self.previous = previousNode


class LinkeList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            n = Node(value, )
