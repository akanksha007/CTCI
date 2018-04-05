class Node:
    def __init__(self, data, address):
        self.data = data
        self.address = address

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def addNode(self, data):
        n = Node(data, self.head)
        self.head = n
        return self.head

    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.address


    def add_two_link_list(self, l1, l2):
        l1_num = 0
        l2_num = 0
        current1 = l1
        c1 = 0
        current2 = l2
        c2 = 0

        while current1:
            print(current1.data)
            l1_num = l1_num + current1.data * (10 ** c1)
            c1 = c1 + 1
            current1 = current1.address

        while current2:
            l2_num = l2_num + current2.data * ( 10 ** c2)
            c2 = c2 + 1
            current2 = current2.address
        print(l1_num)

        print(l2_num + l1_num)



l1 = LinkedList()
h1 = l1.addNode(6)
h1 = l1.addNode(1)
h1 = l1.addNode(7)
l2 = LinkedList()
h2 = l2.addNode(5)
h2 = l2.addNode(9)
h2 = l2.addNode(2)
l3 = LinkedList()
print(l1)
print(l2)
l3.add_two_link_list(h1, h2)
