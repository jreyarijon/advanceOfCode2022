import os, sys

current_dir = os.getcwd()
source = current_dir + "/04/assignment_pairs.txt"

fr = open(source, "r")

i = 0

try:
    for line in fr:
        assignment = line.strip("\n").split(",")
        pair1, pair2 = assignment[0].split("-"), assignment[1].split("-")
        elf_assignment_range1 = [n for n in range(int(pair1[0]), int(pair1[1]))]
        elf_assignment_range2 = [n for n in range(int(pair2[0]), int(pair2[1]))]
        coincidences = list(map(lambda x : x in elf_assignment_range2, elf_assignment_range1))
        if False not in coincidences and len(coincidences) == len(elf_assignment_range2): i += 1

    print(i)
except IOError:
    print("Input/output issues")

finally: 
    if not fr.closed: fr.close()