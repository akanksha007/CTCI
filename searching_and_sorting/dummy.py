def recursive(a):
    if(a <= 0):
        a = a- 1
        recursive(a)
    else:
        return 0

temp = recursive(5)
print("temp is", temp)
