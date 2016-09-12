import re 
def checkParens(sequence):
    if sequence.count('(') == sequence.count(')') and sequence.count('(') > 0:
        return True
    else:
        return False

def findall(parens, sequence):
    numberToDo = sequence.count(parens)
    positions = []
    foundPosition = 0
    for i in range (0, numberToDo):
        location = sequence.find(parens, foundPosition)
        foundPosition = location+1
        positions.append(location)

    return positions

def checkDotLength(sequence):

    sequence = sequence.lstrip('.')
    sequence = sequence.rstrip('.')

    splitString = sequence.split('(')

    counts = []
    for i in range(0, len(splitString)):
        count = splitString[i].count('.')
        counts.append(count)

    maximumEntry = max(counts)
    print(maximumEntry)

    if maximumEntry > 2:
        print('do we get here?')
        return True
    else:
        return False



def dotparen_to_bp(sequence):
    openPositions = findall('(', sequence)
    closedPositions = findall(')', sequence)
    closedPositions = closedPositions[::-1]
 
    pairedPositions = []
    for openParens, closedParens in zip(openPositions, closedPositions):
        pair = (openParens, closedParens)
        pairedPositions.append(pair)
    pairedPositions = tuple(pairedPositions)

    return(pairedPositions)

    for i in range(0, len(tuple)):
        firstBase = pairedPositions[i][0]
        firstBase = sequence(firstBase)
        secondBase = pairedPositions[i][1]
        secondBase = sequence(secondBase)

        pairedBases = firstBase + secondBase

        if A in pairedBases and U in pairedBases:
            its okay
        elif G in pairedBases and C in pairedBases:
            its okay
        elif (only when wobble is okay) G in pairedBases and U in pairedBases:
            its okay
        else:
            not a valid pairing!
        if 
        access first and access second
        make sure either has both A and U or both G and C

    """for each pair
    check if they are either an AU or a GC"""

def rna_ss_validator(empty, sequence): 
    parensOutput = checkParens(sequence)
    if parensOutput == False:
        return False
    else:
        dotSequence = dotparen_to_bp(sequence)
        validStructure = checkDotLength(sequence)
        return validStructure
#print(checkDotLength('.(..).'))

x = rna_ss_validator('GCCCUUGGCA', '(.((..))).')
print(x)
