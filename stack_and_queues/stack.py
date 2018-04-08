class Stack:
    def __init__(self):
        self.stk = list()

    def push(self, data):
        self.stk.append(data)

    def pop(self):
        if not self.stk:
            print("cannot delete stack is empty")
        else:
            n = self.stk[-1]
            del self.stk[-1]
            print(n)

    def peek(self):
        print(self.stk[-1])

    def isEmpty(self):
        if not self.stk:
            print("stack is empty")
        else:
            print("stack is not empty")


s = Stack()
s.pop()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.pop()
s.peek()
s.pop()
s.isEmpty()
s.pop()
s.isEmpty()
