class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedList():
    def __init__(self, head= None):
        self.head = head


    def add_node(self, data):
        if(self.head):
            current = self.head
            n = Node(data)
            while(current.right):
                current = current.right
            current.right = n
        else:
            n = Node(data)
            self.head = n

    def print_node(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.right


    def create_binary_search_tree(self, *args):
        if(self.head):
            print("hi")
        else:
            mid = int((1 + len(args))/2)
            n = Node(args[mid])
            self.head = n

l = LinkedList()
l.add_node(5)
l.add_node(2)
l.add_node(3)
l.add_node(4)
l.print_node()
