from string import ascii_letters
import os, sys

abc = dict([(c, i+1) for i, c in enumerate(ascii_letters)])
total = 0

trios = []
lines = []
auth_stickers = []

current_dir = os.getcwd()
source = current_dir + "/03/items.txt"
try:
    fr = open(source, "r")

    for line in fr:
        content = line.strip("\n")
        lines.append(content)
        i = int(len(content)/2)
        compartment1, compartment2 = list(content[:i]), list(content[i:])
        coincidences = list(filter(lambda x: x in compartment2, compartment1))
        values = abc[coincidences[0]]
        total += values
    print("Total: ", total)

    total = 0
    values = 0
    # Saves every three lines within a list of tuples
    for i in range(0, len(lines), 3):
        trios.append([x for x in lines[i:i + 3]])
    for triad in trios:
        auth_stickers.append(list(filter(lambda x: x in triad[1] and x in triad[2], triad[0]))[0])
    values = [abc[x] for x in auth_stickers]
    total = sum(values)
    print("Sum of priorities: ", total)

except IOError:
    print("Input/output issues")

finally:
    if not fr.closed: fr.close()