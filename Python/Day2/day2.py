
def main():
   file = open('input.txt', 'r')
   score = 0
# Operates on assumption that X, Y, Z are Rock Paper Scisccors Respectivily
   for line in file:
    line = line.strip('\n')
    choices = line.split(" ")
    opponent = choices[0]
    player = choices[1]
# Add score for shape chosen
    match player:
        case 'X':
         score += 1
        case 'Y':
         score += 2
        case 'Z':
         score += 3
# Check for draws and wins
    match opponent:
        case 'A':
            match player:
                case 'X':
                    score += 3
                case 'Y':
                    score += 6
        case 'B':
            match player:
                case 'Y':
                    score += 3
                case 'Z':
                    score += 6
        case 'C':
            match player:
                case 'Z':
                    score += 3
                case 'X':
                    score += 6
   print(score)
# We now know that X, Y, Z says what needs to happen that round Lose, Draw, Win
   file.close()
   file = open('input.txt', 'r')
   score = 0
   for line in file:
    line = line.strip('\n')
    choices = line.split(' ')
    opponent = choices[0]
    outcome = choices[1]
    match outcome:
        case 'X':
            match opponent:
                case 'A':
                    # Player picked scicssors in order to lose
                    score += 3
                case 'B':
                    # Player picked rock to lose to paper
                    score += 1
                case 'C':
                    # Player picked paper to lose to scicssors
                    score += 2
        case 'Y':
            score += 3
            match opponent:
                case 'A':
                    score += 1
                case 'B':
                    score += 2
                case 'C':
                    score += 3
        case 'Z':
            score += 6
            match opponent:
                case 'A':
                    # Player picked paper to beat rock
                    score += 2
                case 'B':
                    # Player picked sciccsors to beat paper
                    score += 3
                case 'C':
                    # Player picked rock to beat scicssors
                    score += 1
   print(score)
    






if (__name__ == "__main__"):
        main()