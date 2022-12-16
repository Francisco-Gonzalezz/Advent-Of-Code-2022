def main():
    elfNum = 1
    elves = {}
    file = open("input.txt", "r")
    for line in file:
        if (line == "\n"):
            elfNum += 1
            continue
        if (elfNum in elves.keys()):
            val = elves[elfNum] + int(line)
            elves[elfNum] = val
        else:
            elves[elfNum] = int(line)
    topThree = 0
    for i in range(3):
        elf = max(elves, key=elves.get)
        max_value = max(elves.values())
        topThree += max_value
        del elves[elf]
    file.close()
    print(topThree)
       
    
        


if (__name__ == "__main__"):
    main()