# Technical exam with PYTHON

import sys

def jump_on_marsh(array):
    # The amount of numbers must be >=2, and <=100
    if not (len(array) >= 2 and len(array) <= 100):
        print("Enter an amount of numbers between 2 and 100")
        sys.exit()
    # The array must start and finish with 0
    if not (array[0] == 0 and array[len(array) - 1] == 0):
        print("The array must start and finish with 0")
        sys.exit()
    # Must contain only binary integers {0,1}
    for n in array:
        if n not in (0, 1):
            print("Only binary integers {0, 1}")
            sys.exit()

    jumps = 0
    while len(array) > 2:
        if array[0] == 0 and array[1] == 1 and array[2] == 0:
            jumps += 1
            del(array[0:2])
        elif array[0] == 0 and array[1] == 0 and array[2] == 0:
            jumps += 1
            del(array[0:2])
        elif array[0] == 0 and array[1] == 0 and array[2] == 1:
            jumps += 1
            del(array[0])       
    # In case there is a posibility of not winning the game [1, 1] 
        else:
           print("The stone is too far")
           sys.exit()

    if len(array) == 2:
            jumps += 1
            del(array[0])

    return jumps


################ PROGRAM ################
c = [0,1,0,0,1,0,0,0,1,0]    # 5 jumps example


print(jump_on_marsh(c))
