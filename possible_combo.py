def count_combination(n):
    if(n > 3):
        return(count_combination(n-1) + count_combination(n-2) + count_combination(n-3))
    else:
        if(n == 3):
            return 4
        elif(n == 2):
            return 2
        elif(n == 1):
            return 1


a = count_combination(20)
print(a)
