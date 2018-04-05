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

    def displayLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.address

    def find_duplicate(self):
        current = self.head
        mapper = dict()
        while current:
            if current.data in mapper:
                mapper[current.data] = mapper[current.data] + 1
            else:
                mapper[current.data] = 1
            current = current.address
        print(mapper)
        self.remove_duplicate(mapper)

    def remove_duplicate(self,mapper):
        for key, value in mapper.items():
            while value > 1:
                current = self.head
                previous = current
                while current:
                    if current.data == key and current == self.head:
                        self.head = current.address
                        value = value - 1
                        break
                    elif current.data == key:
                        if current.address:
                            previous.address = current.address
                        else:
                            previous.address = None
                        break
                    previous = current
                    current = current.address
                value = value - 1
        self.displayLinkedList()

    def improvised_remove_duplicate(self):
        current = self.head
        previous = current
        unique_value = set()
        while current:
            if current.data in unique_value:
                previous.address = current.address
                current = previous.address
            else:
                unique_value.add(current.data)
                previous = current
                current = current.address

    def remove_duplicate_without_buffer(self):
        current = self.head
        previous = current
        while current:
            temp = current.data
            p1 = current.address
            p2 = current
            while p1:
                if p1.data == temp:
                    p2.address = p1.address
                    p1 = p2.address
                else:
                    p2 = p1
                    p1 = p1.address
            current = current.address

    def remove_duplicate_with_buffer_improvised(self):



l = LinkedList()
# l.addNode(1)
# l.addNode(1)
# l.addNode(1)
l.addNode(1)
l.addNode(1)
l.addNode(1)
l.addNode(1)
l.addNode(7)
l.displayLinkedList()
l.remove_duplicate_without_buffer()
l.displayLinkedList()
# l.displayLinkedList()
# l.find_duplicate()



