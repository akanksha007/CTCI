class StackList:
    def __init__(self):
        self.stack_list = [None]* 10
        self.t1 = -1
        self.t2 = 2
        self.t3 = 5

    def push(self,stack_number, data):
        if(stack_number == 0 and self.t1 == 2):
            print("stack 0 is full")
        elif(stack_number == 1 and self.t2 == 5):
            print("stack 1 is full")
        elif(stack_number == 2 and self.t3 == 9):
            print("stack 2 is full")
        else:
            if(stack_number == 0):
                self.t1 += 1
                self.stack_list[self.t1] = data
            elif(stack_number == 1):
                self.t2 += 1
                self.stack_list[self.t2] = data
            elif(stack_number == 2):
                self.t3 += 1
                self.stack_list[self.t3] = data

    def pop(self, stack_number):
        if(stack_number == 0 and self.t1 == -1):
            print("stack 0 is empty")
        elif(stack_number == 1 and self.t2 == 2):
            print("stack 1 is empty")
        elif(stack_number == 2 and self.t3 == 5):
            print("stack 2 is empty")
        else:
            if(stack_number == 0):
                print(self.stack_list[self.t1])
                del self.stack_list[self.t1]
                self.t1 = self.t1 - 1
            elif(stack_number == 1):
                print(self.stack_list[self.t2])
                del self.stack_list[self.t2]
                self.t2 = self.t2 - 1
            elif(stack_number == 2):
                print(self.stack_list[self.t2])
                del self.stack_list[self.t2]
                self.t2 = self.t2 - 1

    def print_stack(self):
        print(*self.stack_list)
s1 = StackList()
s1.push(1, 'a')
s1.push(2, 'b')
s1.push(0, 'c')
s1.push(1, 'd')
s1.push(2, 'e')
s1.push(0, 'f')
s1.push(1, 'g')
s1.push(1, 'i')
s1.push(2, 'j')
s1.push(2, 'k')
s1.print_stack()

