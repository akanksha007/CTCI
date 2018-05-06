# f should be completed before a in first case
def find_build_order(args):
    temp = list()
    output = list()
    while(len(output) != len(args)):
        for k, v in args.items():
            if (not v) and (k not in output):
                temp.append(k)
        if temp:
            for k, v in args.items():
                for i in temp:
                    if i in v:
                        v.remove(i)
            for j in temp:
                output.append(j)
            temp = list()
        else:
            print("error")
            break
    print(output)
a = {'a': ['f'], 'b':['f'], 'c': ['d'], 'd': ['a', 'b'], 'e': [], 'f': []}
b = {'a': ['b'], 'b': ['a'], 'c': []}
# c = {'f': ['c', 'b', 'a'], 'c': ['a'], 'b': ['a', 'e'], 'a': ['e'], 'd': ['g']}
find_build_order(b)
find_build_order(a)
