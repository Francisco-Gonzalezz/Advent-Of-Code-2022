# This class is used to do various things that are required over and over

# Returns a list of each line from input file
def readInputLinesIntoList(fileName):
    file = open(fileName, 'r')
    list = []
    for line in file:
        line = line.strip('\n')
        list.append(line)
    return list