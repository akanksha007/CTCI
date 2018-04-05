class Node:
    def __init__(self, data, address):
        self.data = data
        self.address = address


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def add_node(self, data):
        n = Node(data, self.head)
        self.head = n

    def partition_ll(self, pe):
        exact_list = list()
        less_list = list()
        greater_list = list()
        current = self.head
        while(current):
            if current.data > pe:
                greater_list.append(current.data)
            elif current.data < pe:
                less_list.append(current.data)
            else:
                exact_list.append(current.data)
            current = current.address
        print(exact_list)
        print(less_list)
        print(greater_list)
        self.head = None

        for j in greater_list:
            n = Node(j , self.head)
            self.head = n

        for j in exact_list:
            n = Node(j, self.head)
            self.head = n

        for j in less_list:
            n = Node(j, self.head)
            self.head = n



    def print_linklist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.address

l = LinkedList()
l.add_node(2)
l.add_node(4)
l.add_node(0)
l.add_node(11)
l.add_node(9)
l.add_node(4)
l.add_node(3)
l.add_node(8)
l.add_node(1)
l.add_node(7)
l.print_linklist()
l.partition_ll(9)
l.print_linklist()






