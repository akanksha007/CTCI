class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def add_node(self, data):
        if(self.head):
            temp = self.head
            if temp.left:

        else:
            n = Node(data)
            self.head, self.tail = n

