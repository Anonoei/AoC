import os
import string

def main():
    valMap = [None]
    for char in string.ascii_lowercase:
        valMap.append(char)
    for char in string.ascii_uppercase:
        valMap.append(char)
    if not os.path.exists("list.txt"):
        print("Input list not found!")
        return
    rucksacks = []
    with open("list.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            compartments = []
            compartment = int(len(line) / 2)
            compartments.append(line[:compartment])
            compartments.append(line[compartment:])
            rucksacks.append(compartments)
    total = 0
    for rucksack in rucksacks:
        matching = None
        for item in rucksack[0]:
            try:
                index = rucksack[1].index(item)
                matching = item
                break
            except ValueError:
                pass
        if matching is None:
            print(f"Matching: {matching}")
            input("Pause")
        else:
            total += valMap.index(matching)
    print(f"Total: {total}")

if __name__ == '__main__':
    main()