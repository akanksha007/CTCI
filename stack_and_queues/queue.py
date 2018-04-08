class Queue:
    def __init__(self):
        self.q = list()

    def add(self, data):
        self.q.append(data)

    def remove(self):
        del self.q[0]

    def peek(self):
        print(self.q[0])

    def isEmpty(self):
        if not self.q:
            print("q is empty")
        else:
            print("q is not empty")



q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.remove()
q.peek()
q.isEmpty()
q.remove()

