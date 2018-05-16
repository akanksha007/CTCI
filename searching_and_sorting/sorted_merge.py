def sorted_merge(a, b):
    j = 0
    for i in range(len(a) + len(b)):
        print(*a)
        if(a[i] > b[j]):
            a.insert(i, b[j])
            j = j + 1
    # for k in range(j, len(b)):
    #     a.append(b[k])
    print(*a)
a = [1,3,5,7,9]
b = [2,4,6,8,10,12, 14]
sorted_merge(a, b)
