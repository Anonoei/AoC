import os

# Using list.txt, find top 3 elves with most calories

def main():
    if not os.path.exists("list.txt"):
        print("Calorie list does not exist")
        return
    elves: list = [0]
    with open("list.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                elves.append(0)
                continue
            elves[-1] += int(line.strip())
    elves.sort(reverse=True) # Sort highest to lowest
    print(f"{elves[0]}, {elves[1]}, {elves[2]}")
    top3 = elves[0] + elves[1] + elves[2]
    print(f"Total: {top3}")

if __name__ == '__main__':
    main()