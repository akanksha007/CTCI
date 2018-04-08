class StackList:
    def __init__(self):
        self.tos = -1
        self.stack_list = list()
        self.min = 100000000000

    def push(self, data):
        if self.min > data:
            self.min = data
        self.stack_list.append({data: self.min})
        self.tos += 1


    def pop(self):
        if self.tos == -1:
            print("stack empty")
        else:
            a = self.stack_list[self.tos]
            del self.stack_list[-1]
            self.tos = self.tos - 1

    def isEmpty(self):
        if self.tos == -1:
            print("stack empty")
        else:
            print("stack full")

    def seek(self):
        print(self.stack_list[self.tos])

    def print_stack(self):
        print(*self.stack_list)

s = StackList()
s.pop()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()
s.pop()
s.pop()
s.isEmpty()
s.seek()
s.pop()
s.pop()
s.print_stack()
s.isEmpty()

