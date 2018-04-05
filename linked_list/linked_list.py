class Node:
    def __init__(self, data, address):
        self.data = data
        self.address = address

    def getNextNode(self):
        return self.address


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        return True

    def printLinkList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.getNextNode()



    def removeNode(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.address = current.address
                else:
                    self.head = current.getNextNode()
            previous = current
            current = current.getNextNode()



l = LinkedList()
print(l.addNode(5))
print(l.addNode(10))
print(l.addNode(15))
print(l.addNode(20))
l.printLinkList()
print(l.removeNode(15))
l.printLinkList()




