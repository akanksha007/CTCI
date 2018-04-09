class SetofStack:
    def __init__(self, n):
        self.stack_size = n
        self.s1 = list()
        self.s2 = list()
        self.s3 = list()
        self.s4 = list()
        self.tos = -1

    def push(self, data):
        if self.tos >= self.stack_size * 4 - 1:
            print("stack full")
        else:
            if -1 <= self.tos < (self.stack_size - 1):
                self.s1.append(data)
                self.tos += 1
            elif (self.stack_size - 1) <= self.tos < (2*self.stack_size - 1):
                self.s2.append(data)
                self.tos += 1
            elif (2*self.stack_size - 1) <= self.tos < (3*self.stack_size - 1):
                self.s3.append(data)
                self.tos += 1
            elif (3*self.stack_size - 1) <= self.tos < (4*self.stack_size - 1):
                self.s4.append(data)
                self.tos += 1

    def print_stack(self):
        print(*self.s1)
        print(*self.s2)
        print(*self.s3)
        print(*self.s4)
        # print(self.tos)

    def pop(self):
        stack_number = int(self.tos / self.stack_size) + 1
        if (self.tos == -1):
            print("stack empty")
        elif stack_number == 1:
            temp = self.tos % self.stack_size
            print(self.s1[temp])
            del self.s1[temp]
            self.tos -= 1
        elif stack_number == 2:
            temp = self.tos % self.stack_size
            print(self.s2[temp])
            del self.s2[temp]
            self.tos -= 1
        elif stack_number == 3:
            temp = self.tos % self.stack_size
            print(self.s3[temp])
            del self.s3[temp]
            self.tos -= 1
        elif stack_number == 4:
            temp = self.tos % self.stack_size
            print(self.s4[temp])
            del self.s4[temp]
            self.tos -= 1
    def seek(self):
        if(self.tos == -1)

s = SetofStack(4)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
s.push(15)
s.push(16)
s.push(17)
s.print_stack()
for i in range(18):
    s.pop()
s.print_stack()
