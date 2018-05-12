#last element as pivout.
def call_quick_sort(a):
    low = 0
    high = len(a) - 1
    quick_sort(a, low, high)
    print(a)

def quick_sort(a, low, high):
    if(low <= high):
        partition_position = partition(a, low, high)
        quick_sort(a, low, partition_position - 1)
        quick_sort(a, partition_position+1, high)

def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low,high):
        if(a[j] < pivot):
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return (i + 1)


a = [15,5,25,35,1,6,2,20]
b = [10,80,30,90,40,50,70]
call_quick_sort(a)
call_quick_sort(b)
