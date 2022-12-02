import os

# Using list.txt, find elf with most calories

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
    print(max(elves))

if __name__ == '__main__':
    main()