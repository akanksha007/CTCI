def find_project_order(args):
    length = len(args)
    output = list()
    count = 0
    keys = list(args.keys())
    while(len(output) != length):
        for t in range(len(args)):
            k = keys[t]
            value = args[k]
            if len(output) == 5:
                print("k is ", k)
                print("value is ", value)
                print("args is", args)
            if (not value) and (k not in output):
                count = count + 1
                if k in output:
                    next
                else:
                    print(args)
                    output.append(k)
                    for m, n in args.items():
                        if k in n:
                            print("output", output)
                            print("args", args)
                            n.remove(k)
                            print(" after args", args)
                    t = 0
            else:
                count = 0
        if count == 0:
            print(output)
            print("no path exist")
            break;
    print(output)

a = {'a': ['f'], 'b':['f'], 'c': ['d'], 'd': ['a', 'b'], 'e': [], 'f': []}
b = {'a': ['b'], 'b': ['a'], 'c': []}
find_project_order(b)
find_project_order(a)
