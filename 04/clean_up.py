import os, sys


def is_inside(my_list1, my_list2):
    bools1 = list(map(lambda x: x in my_list2, my_list1))
    bools2 = list(map(lambda x: x in my_list1, my_list2))
    if False not in bools1 or  False not in bools2: return 1
    else:                                           return 0


current_dir = os.getcwd()
source = current_dir + "/04/assignment_pairs.txt"

fr = open(source, "r")

i = 0

try:
    for line in fr:
        assignment = line.strip("\n").split(",")
        pair1 = list(map(lambda x: int(x), assignment[0].split("-")))
        pair2 = list(map(lambda x: int(x), assignment[1].split("-")))
        i += is_inside(range(int(pair1[0]), pair1[1]), range(pair2[0],pair2[1]))
    print(i)
except IOError:
    print("Input/output issues")

finally: 
    if not fr.closed: fr.close()