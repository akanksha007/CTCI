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

    def create_link_list(self):


t = Tree()
for i in range(15):
    t.create_node(i)
root = t.head
t.inorder_traversal(root)
