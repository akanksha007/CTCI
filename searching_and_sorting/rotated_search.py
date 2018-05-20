def sorted_search(a, search_element):
    low = a.index(min(a))
    high = len(a) - 1 + low
    flag = 0
    while(low <= high):
        mid = int((low + high) / 2)
        mid_without_mod = mid
        if (mid > len(a) - 1):
            mid_without_mod = mid
            mid = mid % len(a)
        if(a[mid] == search_element):
            flag = 1
            return mid + 1
        elif(a[mid] < search_element):
            low = mid_without_mod + 1
        elif(a[mid] > search_element):
            high = mid_without_mod - 1
    if(flag == 0):
        return -1
a = [15,16,19,20,25,1,3,4,5,7,10,14]
b = [19,20,25,1,3,4,5,7,10,14,15,16]
c = [25,1,3,4,5,7,10,14,15,16,19,20]
t1 =  sorted_search(a, 27)
t2 = sorted_search(a, 14)
t3 = sorted_search(a, 25)
t4 = sorted_search(a, 10)
t5 = sorted_search(a, 1)
t6 = sorted_search(a,3)
t7 = sorted_search(a,19)
print("a is", a)
print("search_element is", 27, "t1 is", t1)
print("search_element is", 14, "t2 is", t2)
print("search_element is", 25, "t3 is", t3)
print("search_element is", 10, "t4 is", t4)
print("search_element is", 1, "t5 is", t5)
print("search_element is", 3, "t6 is", t6)
print("search_element is", 19, "t7 is", t7)
