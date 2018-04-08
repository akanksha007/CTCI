class Stack():
    def __init__(self):
        self.stack_list = [None]*3
        self.s1 = -1
        self.s2 = 0
        self.s3 = 1

    def push(self, stack_number, data):
        if stack_number == 0:
            self.s1 += 1
            if self.stack_list[self.s1]:
                self.stack_list.insert(self.s1, data)
                self.s2 += 1
                self.s3 += 1
            else:
                self.stack_list[self.s1] = data
        elif stack_number == 1:
            self.s2 += 1
            if self.stack_list[self.s2]:
                self.stack_list.insert(self.s2, data)
                self.s3 += 1
            else:
                self.stack_list[self.s2] = data

        else:
            if self.stack_list[self.s3]:
                self.s3 += 1
                self.stack_list.append(data)
            else:
                self.stack_list[self.s3] = data


    def print_list(self):
        print(*self.stack_list)
        print(self.s1)
        print(self.s2)
        print(self.s3)




s1 = Stack()
# s1.push(1, 'a')
# s1.push(2, 'b')
# s1.push(0, 'c')
# s1.push(1, 'd')
# s1.push(2, 'e')
# s1.push(0, 'f')
# s1.push(1, 'g')
# s1.push(1, 'h')
# s1.push(1, 'i')
# s1.push(2, 'j')
# s1.push(2, 'k')
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.push(0,1)
s1.print_list()

