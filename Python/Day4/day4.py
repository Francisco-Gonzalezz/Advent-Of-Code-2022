import os
import sys
import PyUtil as Util


def main():
    # part1()
    lines = Util.readInputLinesIntoList(os.getcwd() + '/input.txt')
    count = 0
    for line in lines:
        line = line.strip('\n')
        line = line.split(",")
        firstElf = line[0]
        secondElf = line[1]
        count += determinePartialOverlaps(firstElf, secondElf)
    print(count)

def determinePartialOverlaps(firstElf, secondElf):
    firstElf = firstElf.split('-')
    firstElfStart = int(firstElf[0])
    firstElfEnd = int(firstElf[1])
    
    secondElf = secondElf.split('-')
    secondElfStart = int(secondElf[0])
    secondElfEnd = int(secondElf[1])

    if (firstElfStart in range(secondElfStart, secondElfEnd + 1) or firstElfEnd in range(secondElfStart, secondElfEnd + 1) or secondElfStart in range(firstElfStart,  firstElfEnd + 1) or secondElfEnd in range(firstElfStart, secondElfEnd)):
        return 1
    return 0

def part1():
    lines = Util.readInputLinesIntoList(os.getcwd() + '/input.txt')
    count = 0
    for line in lines:
        line = line.split(',')
        firstElf = line[0]
        secondElf = line[1]
        count += determineFullOverLap(firstElf, secondElf)
    print(count)

def determineFullOverLap(firstElf, secondElf):
    firstElf = firstElf.split('-')
    firstElfStart = int(firstElf[0])
    firstElfEnd = int(firstElf[1])
    
    secondElf = secondElf.split('-')
    secondElfStart = int(secondElf[0])
    secondElfEnd = int(secondElf[1])
    if (firstElfStart >= secondElfStart and firstElfEnd <= secondElfEnd):
        return 1
    elif (secondElfStart >= firstElfStart and secondElfEnd <= firstElfEnd):
        return 1
    else:
        return 0

if (__name__ == "__main__"):
    main()
