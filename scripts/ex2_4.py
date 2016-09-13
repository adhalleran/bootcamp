import re

def identifyORF(sequence):
    """This function returns the five longest ORFs of a given DNA sequence."""
    starts = []
    stops = []

    # Find all occurences of the starts and stops and add them to an index
    for match in re.finditer('ATG', sequence):
        starts.append(match.start())

    for match in re.finditer('TGA', sequence):
        stops.append(match.start())

    for match in re.finditer('TAG', sequence):
        stops.append(match.start())

    for match in re.finditer('TAA', sequence):
        stops.append(match.start())

    # Sort the starts and stops by index of occurence
    starts.sort()
    stops.sort()

    # Let's find some ORFs!
    matchingPairs = []
    for i, x in enumerate(starts):
        for y, z in enumerate(stops):
            if x > z:
                pass
            elif (x-z)%3 == 0:
                toAppend = (x,z)
                matchingPairs.append(toAppend)
                break

    # Check to see if the pairs are three amino acids apart, and calculate length
    validatedPairs = []
    for i, x in enumerate(matchingPairs):
        ORFLength = x[1] - x[0]
        if ORFLength % 3 == 0:
            tupleToAppend = (x[0], x[1], ORFLength+3)
            validatedPairs.append(tupleToAppend)
        else:
            pass

    # This part of the code sorts the ORFs based on their lengths
    largestORF = []
    currentMax = 0
    for i,x in enumerate(validatedPairs):
        if x[2] > currentMax:
            largestORF.insert(0, x)
            currentMax = x[2]
        else:
            pass

    # Create a list of the five largest ORFs to return
    largestFiveORFS = list()
    largestFiveORFS.append(sequence[largestORF[0][0]:largestORF[0][1]])
    largestFiveORFS.append(sequence[largestORF[1][0]:largestORF[1][1]])
    largestFiveORFS.append(sequence[largestORF[2][0]:largestORF[2][1]])
    largestFiveORFS.append(sequence[largestORF[3][0]:largestORF[3][1]])
    largestFiveORFS.append(sequence[largestORF[4][0]:largestORF[4][1]])

    return(largestFiveORFS)

def main():
    """Executes the main instructions of the program."""

    with open('/Users/andrewhalleran/Documents/git/bootcamp/data/salmonella_spi1_region.fna', 'r') as inputFile:
        sequence = inputFile.readlines()

    # Remove the first entry
    headerSequence = sequence.pop(0)

    # Join the sequence stored in our list
    strSequence = ''.join(sequence)

    # Get rid of the new line characters by replacing them with empty
    cleanSequence = strSequence.replace('\n', '')

    ORF = identifyORF(cleanSequence)
    print('Longest ORF', ORF)

main()