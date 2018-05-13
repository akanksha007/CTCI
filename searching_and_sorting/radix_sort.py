def radix_sort(a):
    j = 0

    for i in range(10):
        queue_name = "q" + str(i)
        queue_name = list()

    while(j < 3):
        if (j == 0):
            for k in a:
                temp = k % 10
                queue = "q" + str(temp)
                queue.append(temp)
            output = []
            for x in range(10):
                queue_name = "q" + str(x)
                output = output + queue_name
                queue_name.clear()
            a = output
            j = j + 1

        if j == 1:
            for k in a:
                temp = int(k/10)
                temp = temp % 10
                queue = "q" + str(temp)
                queue.append(temp)
            output = []
            for x in range(10):
                queue_name = "q" + str(x)
                output = output + queue_name
                queue_name.clear()
            a = output
            j = j + 1

        if j == 2:
            for k in a:
                temp = k / 100
                queue = "q" + str(temp)
                queue.append(temp)
            output = []
            for x in range(10):
                queue_name = "q" + str(x)
                output = output + queue_name
                queue_name.clear()
            a = output
            j = j + 1
a = [170,45,75,90,802,24,2,66]
radix_sort(a)




