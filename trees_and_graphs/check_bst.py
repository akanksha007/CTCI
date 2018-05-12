class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, head= None):
        self.head = head

    def add_node(self, data):
        if self.head:
            current = self.head
            while(current):
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        n = Node(data)
                        current.left = n
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        n = Node(data)
                        current.right = n
                        break
        else:
            n = Node(data)
            self.head = n


    def inorder(self, n):
        if(n):
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)

    # def check_bst(self, root, max, min, parent=None):
    #     if root.left:
    #         if parent:
    #         check_bst(root.left, root.data, parent.data])

    def check_bst_optimised(self, root, max=None, min = None):
        if not root:
            return True
        else:
            if(min and root.data <= min) or (max and root.data > max):
                return False
            elif (not self.check_bst_optimised(root.left, root.data, min)) or (not self.check_bst_optimised(root.right, max, root.data)):
                return False
            else:
                return True





t = Tree()
t.add_node(40)
t.add_node(120)
t.add_node(60)
t.add_node(10)
t.add_node(30)
t.add_node(50)
t.add_node(170)
t.add_node(5)
t.add_node(15)
t.add_node(25)
t.add_node(35)
t.add_node(435)
t.add_node(55)
t.add_node(65)
t.add_node(75)
t.inorder(t.head)
n = t.check_bst_optimised(t.head)
print(n)

