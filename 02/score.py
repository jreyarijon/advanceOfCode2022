import os, sys

if __name__ == "__main__":

    current_dir = os.getcwd()
    source = current_dir + "/02/rounds.txt"

    # hand points -- win/draw/lost points
    strategy1 = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3
    }

    strategy2 = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6
    }

    score1 = 0
    score2 = 0

    try:
        fr = open(source, "r")

        for line in fr:
            round = line.strip("\n")
            for key, value in strategy1.items():
                if key == round:
                    score1 += value
            for key, value in strategy2.items():
                if key == round:
                    score2 += value
        
        print(f"The maximum score I've got using the first strategy is {score1}")
        print(f"The maximum score I've got using the second strategy is {score2}")


    except IOError:
        print("Input/output issues")

    finally:
        if fr.closed != True:
            fr.close()


