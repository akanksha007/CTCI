class MyQueue:
    def __init__(self):
        self.stack_new = list()
        self.stack_old = list()

    def add(self, data):
        self.stack_new.append(data)

    def remove(self):
        if not self.stack_old and not self.stack_new:
            print("stack is empty")
        elif not self.stack_old:
            while self.stack_new:
                temp = self.stack_new.pop()
                self.stack_old.append(temp)
            print(self.stack_old.pop())
        else:
            print(self.stack_old.pop())

    def print_stack(self):
        print("stack new",*self.stack_new)
        print("stack old",*self.stack_old)


q = MyQueue()
for i in range(11):
    q.add(i)
q.print_stack()
for i in range(12):
    q.remove()
