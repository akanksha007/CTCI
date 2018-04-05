class Node:
    def __init__(self, data, address=None):
        self.data = data
        self.address = address

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_node(self, data):
        if self.head == self.tail == None:
            n = Node(data)
            self.head = self.tail = n
        else:
            n = Node(data)
            self.tail.address = n
            self.tail = n

    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.address

    def create_circular_ll(self):
        current = self.head
        while current:
            if(current.data == 'c'):
                break;
            current = current.address

        self.tail.address = current

    def print_circular_loop_element(self):
        print(self.tail.address.data)

    def loop_detection(self):
        current = self.head
        temp = list()
        while(current):
            temp.append(current)
            if(current.address in temp):
                print("loop exist")
                print(current.address.data)
                break
            else:
                current = current.address



l = LinkedList()
l.add_node('a')
l.add_node('b')
l.add_node('c')
l.add_node('d')
l.add_node('e')
l.print_ll()
l.create_circular_ll()
l.loop_detection()
# l.print_circular_loop_element()
