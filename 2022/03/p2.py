import os
import string

def main():
    if not os.path.exists("list.txt"):
        print("Input list not found!")
        return
    valMap = [None]
    for char in string.ascii_lowercase:
        valMap.append(char)
    for char in string.ascii_uppercase:
        valMap.append(char)
    groups = [[]]
    with open("list.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if len(groups[-1]) == 3:
                groups.append([])
            line = line.strip()
            groups[-1].append(line)
    total = 0
    for group in groups:
        matching = None
        for item in group[0]:
            try:
                index = group[1].index(item)
                index = group[2].index(item)
                matching = item
            except ValueError:
                pass
        if matching is not None:
            total += valMap.index(matching)
        else:
            raise Exception("No badge found!")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()