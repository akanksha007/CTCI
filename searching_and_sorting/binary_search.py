#iterative binary search
def iter_binary_search(a, search_element):
    flag = 0
    low = 0
    high = len(a) - 1
    mid = int((low + high) / 2)
    while(low <= high):
        if(a[mid] > search_element):
            high = mid - 1
            mid = int((low + high) / 2)
        elif(a[mid] < search_element):
            low = mid + 1
            mid = int((low + high) / 2)
        elif(a[mid] == search_element):
            flag = 1
            return mid + 1
    if(flag == 0):
        return 0

def recursive_binary_search(a, search_element):
    low = 0
    high = len(a) - 1
    mid = int((low + high) / 2)
    position = rr_binary_search(a,low, mid, high, search_element)
    print("search_element is", search_element, "position is", position)
    return position

def rr_binary_search(a,low, mid, high, search_element):
    if(low <= high):
        if(a[mid] == search_element):
            return mid + 1
        elif(a[mid] > search_element):
            high = mid - 1
            mid = int((low + high) / 2)
            return rr_binary_search(a,low,mid, high, search_element)
        elif(a[mid] < search_element):
            low = mid + 1
            mid = int((low + high) / 2)
            return rr_binary_search(a,low,mid, high, search_element)
    else:
        return 0


a = [2,4,6,8,10, 12, 14]
# output = iter_binary_search(a, 8)
# print(output)
# output1 = iter_binary_search(a, 18)
# print(output1)
# output2 = iter_binary_search(a,1)
# print(output2)
# output3 = iter_binary_search(a,14)
# print(output3)
# output4 = iter_binary_search(a,2)
# print(output4)
# output5 = iter_binary_search(a,4)
# print(output5)
############################################################
o1 = recursive_binary_search(a, 8)
o2 = recursive_binary_search(a, 18)
o3 = recursive_binary_search(a, 1)
o4 = recursive_binary_search(a, 14)
o5 = recursive_binary_search(a, 2)
o6 = recursive_binary_search(a, 4)
# print(o1)
# print(o2)
# print(o3)
# print(o4)
# print(o5)
# print(o6)
