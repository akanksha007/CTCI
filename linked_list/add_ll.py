class Node:
    def __init__(self, data, address):
        self.data = data
        self.address = address

class LinkList:
    def __init__(self, head = None):
        self.head = head

    def add_node(self, data):
        n = Node(data, self.head)
        self.head = n

    def display_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.address

    def find_number(self):
        current = self.head
        count, temp = 0, 0
        while current:
            temp = temp + (current.data * 10**count)
            count = count + 1
            current = current.address
        return temp





l = LinkList()
l.add_node(6)
l.add_node(1)
l.add_node(7)
l.display_ll()
l1 = LinkList()
l1.add_node(2)
l1.add_node(9)
l1.add_node(5)
l1.display_ll()
n1 = l.find_number()
n2 = l1.find_number()
print(n1 + n2)
