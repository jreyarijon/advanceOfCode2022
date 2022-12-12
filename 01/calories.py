import os, sys

if __name__ == "__main__":
    
    current_dir = os.getcwd()
    source = current_dir + "/01/inventory.txt"

    total_calories = 0
    calories_per_elf = 0
    elves = []

    try:
        fr = open(source, "r")
        for line in fr:
            if line == "\n":
                elves.append(total_calories)
                total_calories = 0
            else:
                total_calories += int(line)
    except IOError:
        print("Input/output issues")

    finally:
        if  fr.closed != True:
            fr.close()
    copy = elves
    elves.sort()
    elf = copy.index(elves[-1])
    print(f"The elf with the biggest amount of calories is nº{elf}: {elves[-1]} calories")
    calories_3_elves = sum(elves[-3:])
    print(f"The top 3 elves carry the amount of {calories_3_elves} calories")

