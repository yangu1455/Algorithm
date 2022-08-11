# 1076번 저항

# 색	값	곱
# black	0	1
# brown	1	10
# red	2	100
# orange	3	1,000
# yellow	4	10,000
# green	5	100,000
# blue	6	1,000,000
# violet	7	10,000,000
# grey	8	100,000,000
# white	9	1,000,000,000

import sys

color_dict = {
    0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'violet', 8: 'grey', 9: 'white'
    }

multi_list = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

one = input()
two = input()
multiply = input()

def dict():

    for i in range(len(color_dict)):
        if color_dict[i] == one:
            one = i
            continue
        elif color_dict[i] == two:
            two = i
            continue
        elif color_dict[i] == multiply:
            multiply = multi_list[i]

print(((one * 10) + two) * multiply)
