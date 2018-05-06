class SortStack:
    def __init__(self):
        self.primary_stack = list()
        self.tos = -1
        self.secondary_stack = list()
        self.stos = -1

    def push(self,data):
        self.primary_stack.append(data)
        self.tos += 1


    def sort(self):
        while self.tos != -1:
            if self.stos == -1:
                temp = self.primary_stack.pop()
                self.tos -= 1
                self.secondary_stack.append(temp)
                self.stos += 1
            else:
                temp = self.primary_stack.pop()
                while(self.stos != -1 and self.secondary_stack[self.stos] > temp):
                    data = self.secondary_stack.pop()
                    self.stos -= 1
                    self.primary_stack.append(data)
                    self.tos += 1
                self.secondary_stack.append(temp)
                self.stos += 1
                self.tos -= 1
            self.print_Stack()

    def print_Stack(self):
        print("primary_stack", self.primary_stack)
        print("secondary_stack", self.secondary_stack)

s = SortStack()
s.push(0)
s.push(5)
s.push(1)
s.push(8)
s.push(2)
s.print_Stack()
s.sort()
s.print_Stack()
