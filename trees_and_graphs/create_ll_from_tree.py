class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue = list()
        self.l_queue = list()

    def create_node(self, data):
        if self.head:
            while(self.queue):
                temp = self.queue.pop(0)
                if(temp.left):
                    self.queue.append(temp.left)
                else:
                    n = Node(data)
                    temp.left = n
                    self.queue = [self.head]
                    break
                if(temp.right):
                    self.queue.append(temp.right)
                else:
                    n = Node(data)
                    temp.right = n
                    self.queue = [self.head]
                    break
        else:
            n = Node(data)
            self.head = n
            self.tail = n
            self.queue.append(n)

    def inorder_traversal(self, root):
        if(root):
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

    def create_linked_list(self):
        count = 1
        queue = list()
        queue.append(self.head)
        while(queue):
            if(len(queue) == count):
                l = LinkedList()
                self.l_queue.append(l)
                temp_count = count
                for i in range(temp_count):
                    temp = queue.pop(0)
                    count = count - 1
                    l.create_node(temp.data)
                    if (temp.left):
                        queue.append(temp.left)
                        count += 1
                    if(temp.right):
                        queue.append(temp.right)
                        count += 1
        for i in self.l_queue:
            print("linked list is")
            i.print_ll()

class Node_LL:
    def __init__(self, data= None, address = None):
        self.data = data
        self.address = address

class LinkedList:
    def __init__(self):
        self.ll_head = None
        self.ll_tail = None

    def create_node(self, data):
        if(self.ll_head):
            n = Node_LL(data)
            self.ll_tail.address = n
            self.ll_tail = n
        else:
            n = Node_LL(data)
            self.ll_head = n
            self.ll_tail = n

    def print_ll(self):
        current = self.ll_head
        while(current):
            print(current.data),
            current = current.address


t = Tree()
for i in range(100):
    t.create_node(i)
# root = t.head
# l = LinkedList()
# l.create_node(5)
# l.create_node(10)
# l.print_ll()
# t.inorder_traversal(root)
t.create_linked_list()
