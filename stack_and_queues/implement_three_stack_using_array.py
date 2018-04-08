class StacktoArray:
    def __init__(self):
        self.stack_list = [None]*3
        self.s1 = -1
        self.tos_s1 = -1
        self.s2 = 0
        self.tos_s2 = 0
        self.s3 = 1
        self.tos_s3 = 1

    def push(self, stack_number, data):
        if stack_number == 0:
            if (self.tos_s1 == self.s1):
                self.tos_s1 += 1
                self.s1 += 1
                if self.stack_list[self.tos_s1]:
                    self.stack_list.insert(self.tos_s1, data)
                    self.tos_s2 += 1
                    self.tos_s3 += 1
                else:
                    self.stack_list[self.tos_s1] = data
            else:
                self.tos_s1 += 1
                self.stack_list.insert(self.tos_s1, data)

        elif stack_number == 1:
            if (self.tos_s2 == self.s2):
                self.tos_s2 += 1
                self.s2 += 1
                if self.stack_list[self.tos_s2]:
                    self.stack_list.insert(self.tos_s2, data)
                    self.tos_s3 += 1
                else:
                    self.stack_list[self.tos_s2] = data
            else:
                self.tos_s2 += 1
                self.stack_list.insert(self.tos_s2, data)

        else:
            if (self.tos_s3 == self.s3):
                self.tos_s3 += 1
                self.s3 += 1
                if self.stack_list[self.tos_s3]:
                    self.stack_list.insert(self.tos_s3, data)
                else:
                    self.stack_list[self.tos_s3] = data
            else:
                self.tos_s3 += 1
                self.stack_list.insert(self.tos_s3, data)
        self.print_list()


    def print_list(self):
        print(*self.stack_list)




s1 = StacktoArray()
s1.push(1, 'a')
s1.push(2, 'b')
s1.push(0, 'c')
s1.push(1, 'd')
s1.push(2, 'e')
s1.push(0, 'f')
s1.push(1, 'g')
s1.push(1, 'h')
s1.push(1, 'i')
s1.push(2, 'j')
s1.push(2, 'k')
s1.print_list()
