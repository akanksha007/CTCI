def anagrams(a, b):
    flag = 1
    h = {}
    for i in a:
        if i in h:
            h[i] = h[i] + 1
        else:
            h[i] = 1
    for j in b:
        if j in h:
            h[j] = h[j] - 1
        else:
            flag = 0
    if flag == 1:
        for k, v in h.items():
            if(v != 0 ):
                flag = -1
                break;
    if flag == 1:
        return 1
    else:
        return - 1


def sorted_anagrams(str_list):
    sorted_anagram = list()
    temp = list()
    for i in range(len(str_list) - 1):
        v = anagrams(str[i], str[i+1])

def optimised_anagrams(a):
    t = len(a) - 1
    for i in range(t):
        for j in range(t-i):
            if (compare(a[j], a[j+1])):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print(a)

def sort_str(a):
    m = list(a)
    m.sort()
    k = "".join(m)
    return k


def compare(a, b):
    m = list(a)
    m.sort()
    k = "".join(m)
    n = list(b)
    n.sort()
    l = "".join(n)
    return k == l

def even_more_optimistion(a):
    h = {}
    for i in a:
        key = sort_str(i)
        if key in h:
            h[key].append(i)
        else:
            h[key] = [i]
    index = 0
    for k,v in h.items():
        for x in v:
            a[index] = x
            index = index+ 1
    print(a)




str = ['qap', 'yax', 'cab', 'bca', 'xay', 'pqa', 'apq', 'axy', 'abc']
str1 = ['qap', 'yax', 'cab', 'bca', 'xay', 'pqa']
even_more_optimistion(str1)
even_more_optimistion(str)
# optimised_anagrams(str)
# optimised_anagrams(str1)
# a = anagrams('abcd', 'dcab')
# b = anagrams('qewrewrewqr', 'fdsdsfdsfdsa')
# print("anagram value is", a, "'abcd', 'dcab'")
# print("anagram value is", b, "'qewrewrewqr', 'fdsdsfdsfdsa'")
