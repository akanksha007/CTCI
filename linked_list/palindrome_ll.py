class Node:
    def __init__(self, data, address):
        self.data = data
        self.address = address


class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def add_node(self, data):
        if self.head == self.tail == None:
            n = Node(data, None)
            self.tail = n
            self.head = n
        else:
            n = Node(data, None)
            self.tail.address = n
            self.tail = n

    def print_ll(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.address

    def reverse_ll(self):
        stack_list = list()
        current = self.head
        while(current):
            stack_list.append(current.data)
            current = current.address
        reverse_linked_list = LinkedList()
        for i in range(len(stack_list)):
            data = stack_list.pop()
            reverse_linked_list.add_node(data)
        self.compare_for_palindrome(reverse_linked_list)

    def compare_for_palindrome(self, reverse_linked_list):
        current1 = self.head
        current2 = reverse_linked_list.head
        while(current1):
            if(current1.data == current2.data):
                current1 = current1.address
                current2 = current2.address
            else:
                print("not a palindrome")
                break
        if(current1 == current2 == None):
            print("is a palindrome")

l = LinkedList()
l.add_node(1)
l.add_node(1)
l.add_node(3)
l.add_node(1)
l.add_node(1)
# l.print_ll()
l.reverse_ll()
