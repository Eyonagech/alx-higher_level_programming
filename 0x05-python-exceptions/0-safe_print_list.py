#!/usr/bin/python3
def safe_print_list (my_list=[], x=0):
    b = 0
    while True:
        try:
            if b < x:
                print(my_list[b], end='')
                b += 1
            else:
                print()
                return b
        except IndexError:
            print()
            return b