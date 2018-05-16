def radix_sort(a):
    j = 0
    m = len(str(max(a)))
    hash_list = {}

    for i in range(10):
        queue_name = "q" + str(i)
        hash_list[queue_name] = list()

    while(j < m):
        if (j == 0):
            for k in a:
                temp = k % 10
                queue = "q" + str(temp)
                hash_list[queue].append(k)
            output = []
            for k, v in hash_list.items():
                output = output + v
                v.clear()
            a = output
            j = j + 1

        if j == 1:
            for k in a:
                temp = int(k/10)
                temp = temp % 10
                queue = "q" + str(temp)
                hash_list[queue].append(k)
            output = []
            for k, v in hash_list.items():
                output = output + v
                v.clear()
            a = output
            j = j + 1

        if j == 2:
            for k in a:
                temp = int(k/100)
                queue = "q" + str(temp)
                hash_list[queue].append(k)
            output = []
            for k, v in hash_list.items():
                output = output + v
                v.clear()
            a = output
            j = j + 1
    print(a)
a = [170,45,75,90,802,24,2,66]
radix_sort(a)




