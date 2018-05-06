def longest_sequence(num):
    number = list(map(int, str(num)))
    c1, c2 = 0, 0
    c = 0
    output = list()
    print(number)
    for i in number:
        if i == 1:
            if c > 0:
                c2 = c2 + 1
            else:
                c1 = c1 + 1
        else:
            if c == 0:
                c = c + 1
            elif c == 1 and c2 == 0:
                output.append(c1+ c2 + 1)
                c1,c2 = 0,0
                c = 1
            elif c == 1:
                output.append(c1+ c2 + 1)
                c1 = c2
                c2 = 0
    output.append(c1 + c2 + c)
    print(max(output))


longest_sequence(111111)
longest_sequence(0000000)
longest_sequence(101010)
longest_sequence(110110001111111)
longest_sequence(1111110)
longest_sequence(1111001111111111)
longest_sequence(11110000011)




