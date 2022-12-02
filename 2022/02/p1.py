import os
from enum import Enum

# Rock = 1, Paper = 2, Scissors = 3
# Lose = 0, Draw = 3, Win = 6

class Move(Enum):
    Rock = 1        # A . X
    Paper = 2       # B . Y
    Scissors = 3    # C . Z

class Outcome(Enum):
    Lose = 0
    Draw = 3
    Win = 6

def GetMove(char: str):
    if char == "A" or char == "X":
        return Move.Rock
    elif char == "B" or char == "Y":
        return Move.Paper
    elif char == "C" or char == "Z":
        return Move.Scissors
    else:
        print(f"Unknown char: '{char}'!")
        exit(-1)
def GetOutcome(c1: Move, c2: Move):
    if c1 == c2:
        return Outcome.Draw
    if c1 is Move.Rock:
        if c2 is Move.Paper:
            return Outcome.Win
        elif c2 is Move.Scissors:
            return Outcome.Lose
    elif c1 is Move.Paper:
        if c2 is Move.Rock:
            return Outcome.Lose
        elif c2 is Move.Scissors:
            return Outcome.Win
    elif c1 is Move.Scissors:
        if c2 is Move.Rock:
            return Outcome.Win
        elif c2 is Move.Paper:
            return Outcome.Lose

def main():
    if not os.path.exists("list.txt"):
        print("Input list not found!")
        return
    score = 0
    with open("list.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")
            c1 = GetMove(line[0])
            c2 = GetMove(line[1])
            outcome = GetOutcome(c1, c2)
            result = outcome.value + c2.value
            #print(f"c1: {c1.name}, c2: {c2.name} = {outcome} ({result})")
            score += result
    print(f"Final score: {score}")


if __name__ == '__main__':
    main()