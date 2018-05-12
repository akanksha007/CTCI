def bubble_sort(a):
    swap = False
    for i in range(len(a) - 1):
        if swap:
            break;
        for j in range(len(a) - i -1):
            if(a[j] > a[j+1]):
                swap = False
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
            else:
                swap = True
    print(*a)

bubble_sort([5,1,4,2,8])
bubble_sort(list(range(20,30)))
bubble_sort([9,8,1,2,3])
