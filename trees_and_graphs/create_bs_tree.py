class Node:
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self, head = None):
        self.head = head

    def create_bs_tree(self, args):
        print(args)
        if len(args) == 1 or len(args) == 0:
            return
        else:
            mid = int((0 + len(args)) / 2)
            n = Node(args[mid])
            n.left = self.create_bs_tree(args[0:mid])
            n.right = self.create_bs_tree(args[mid+1:len(args)])

b = BST()
b.create_bs_tree([1,2,3,4,5,6,7,8,9,10])
