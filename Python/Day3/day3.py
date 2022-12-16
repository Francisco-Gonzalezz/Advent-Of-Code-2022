from string import ascii_lowercase
from string import ascii_uppercase

def main():
    #part1()
    part2()

def part2():
    letterValues = giveLettersValues()
    file = open('input.txt', 'r')
    lines = file.readlines()
    tmp = []
    for line in lines:
        tmp.append(line.strip('\n'))
    lines = tmp
    
    sum = 0
    index = 0
    while (index < len(lines) - 2):
        line1 = lines[index]
        line1 = placeLettersInList(line1)
        index += 1
        line2 = lines[index]
        line2 = placeLettersInList(line2)
        index += 1
        line3 = lines[index]
        line3 = placeLettersInList(line3)
        sameLetters = getSimilarLetters(line1, line2, line3)
        index += 1
        sum += letterValues[sameLetters[0]]
    print(sum)

def getSimilarLetters(line1, line2, line3):
    similar = []
    for letter in line1:
        if letter in line2 and letter in line3:
            similar.append(letter)
    return similar
def placeLettersInList(stringOfLetters):
    letterList = []
    for letter in stringOfLetters:
        letterList.append(letter)
    return letterList

def part1():
    letterValues = giveLettersValues()
    file = open('input.txt', 'r')
    similar = []
    for line in file:
        line = line.strip('\n')
        dict1 = {}
        dict2 = {}
        firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]
        placeLettersInDictionary(dict1, firsthalf)
        placeLettersInDictionary(dict2, secondhalf)
        for key in dict1.keys():
            if key in dict2.keys():
                similar.append(key)
    file.close()
    sum = getSums(letterValues, similar)
    print(sum)
    
def getSums(letterValues, similarLetters):
    sum = 0
    for letter in similarLetters:
        sum += letterValues[letter]
    return sum

def placeLettersInDictionary(dict, stringOfLetters):
    for letter in stringOfLetters:
        if letter in dict.keys():
            value = dict[letter] + 1
            dict[letter] = value
        else:
            dict[letter] = 1

def giveLettersValues():
    dict = {}
    letterValue = 1
    for letter in ascii_lowercase:
        dict[letter] = letterValue
        letterValue += 1
    for letter in ascii_uppercase:
        dict[letter] = letterValue
        letterValue += 1
    return dict

if (__name__ == "__main__"):
        main()