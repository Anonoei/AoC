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
    if char == "A":
        return Move.Rock
    elif char == "B":
        return Move.Paper
    elif char == "C":
        return Move.Scissors
    else:
        print(f"Unknown char: '{char}'!")
        exit(-1)
        
def GetOutcome(char: str):
    if char == "X":
        return Outcome.Lose
    elif char == "Y":
        return Outcome.Draw
    elif char == "Z":
        return Outcome.Win

def GetOutcomeMove(c1: Move, c2: Outcome):
    if c2 == Outcome.Draw:
        return c1
    if c1 is Move.Rock:
        if c2 is Outcome.Lose:
            return Move.Scissors
        elif c2 is Outcome.Win:
            return Move.Paper
    elif c1 is Move.Paper:
        if c2 is Outcome.Lose:
            return Move.Rock
        elif c2 is Outcome.Win:
            return Move.Scissors
    elif c1 is Move.Scissors:
        if c2 is Outcome.Lose:
            return Move.Paper
        elif c2 is Outcome.Win:
            return Move.Rock

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
            c2 = GetOutcome(line[1])
            move = GetOutcomeMove(c1, c2)
            result = c2.value + move.value
            #print(f"c1: {c1}, c2: {c2} = {move} ({result})")
            score += result
    print(f"Final score: {score}")


if __name__ == '__main__':
    main()