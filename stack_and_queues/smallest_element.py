class SmallestElement:


    def sort_stack(self, *args):
        original_stack = list(args)
        original_stack = sum(original_stack, [])
        temp_stack = list()
        sort_stack = list()
        min = 1000000000000
        for i in range(len(original_stack)):
            j = 0
            while original_stack:
                if min > original_stack[j]:
                    min = original_stack[j]
                    temp_stack.append(min)
                else:
                    t = temp_stack.pop()
                    temp_stack.append(t)
                    temp_stack.append(min)
                original_stack.pop()
                j = j+1
            print("temp_stack", temp_stack)
            temp = temp_stack.pop()
            sort_stack.append(temp)
            original_stack = temp_stack[:]
            temp_stack = list()

        print(sort_stack)
s = SmallestElement()
s.sort_stack([6,1,7,4,0,9,2,8,3])




