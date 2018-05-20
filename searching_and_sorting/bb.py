def bb(a):
    t = len(a) - 1
    for i in range(t):
        for j in range(t-i):
            if (a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print(a)
a = [9,1,7,2,6,11,13,15,5,3]
bb(a)
