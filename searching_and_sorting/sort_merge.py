# def sorted_merge(a, b):
#     m = len(a) + len(b)
#     i, j = 0, 0
#     while(j != len(b)):
#         if (i + j <= m and i < len(a)):
#             if(a[i] > b[j]):
#                 a.insert(i, b[j])
#                 i = i + 1
#                 j = j + 1
#             else:
#                 i = i+1
#         else:
#             for j in range(j, len(b)):
#                 a.append(b[j])
#     print(*a)


def sorted_merge(a, b):
    indexA = len(a) - 1
    indexB = len(b) - 1
    indexMerge = len(a) + len(b) - 1
    for i in range(len(b)):
        a.append(None)
    while(indexB >= 0):
        if (indexA >= 0 and a[indexA] > b[indexB]):
            a[indexMerge] = a[indexA]
            indexA = indexA - 1
        else:
            a[indexMerge] = b[indexB]
            indexB = indexB - 1
        indexMerge = indexMerge - 1
    print(*a)



a = [1,3,5,7,9]
b = [2,4,6,8,10,12,14]
sorted_merge(a, b)
c = list(range(1,4))
d = list(range(5,10))
sorted_merge(c, d)
e = list(range(5,10))
f = list(range(1,4))
sorted_merge(e, f)
