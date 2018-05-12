def selection_sort(a):
    for i in range(len(a)):
        counter = -1
        temp = 10000000000
        for j in range(i, len(a)):
            if(a[j] < temp):
                temp = a[j]
                counter = j
        if counter != -1:
            a[counter] = a[i]
            a[i] = temp
    print(*a)
selection_sort([64,25,12,22,11])
selection_sort(list(range(1,6)))


