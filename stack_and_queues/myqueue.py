class MyQueue:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()
        self.tos = -1

    def add(self, data):
        self.s1.append(data)
        self.tos += 1

    def remove(self):
        if self.tos == -1:
            print("stack is empty")
        else:
            while self.s1:
                temp = self.s1.pop()
                self.s2.append(temp)
            print(self.s2.pop())
            self.tos = -1
            while self.s2:
                temp = self.s2.pop()
                self.s1.append(temp)
                self.tos += 1


    def print_stack(self):
        print(*self.s1)
        print(*self.s2)


q = MyQueue()
for i in range(11):
    q.add(i)
q.print_stack()
for i in range(9):
    q.remove()
