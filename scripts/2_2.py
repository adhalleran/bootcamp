import os

os.path.isfile('/Users/andrewhalleran/Documents/git/bootcamp/scripts/thresholdedSequence.txt')
def writeOutput(seq, header, outputFilename):
    with open(outputFilename, 'w') as output:
        output.write(header)
        sequences = seq[::60]
        sequences = [seq[i:i+60] for i in range (0, len(seq), 60)]
        for entry in sequences:
            entry = entry + '\n'
            output.write(entry)

def gc_blocks(seq, blockSize):
    blocks = [seq[i:i+blockSize] for i in range (0, len(seq), blockSize)]
    if len(blocks[-1]) != blockSize:
        blocks.pop()
    else:
        pass

    gcContent = []
    for entry in blocks:
        gc = (entry.count('G') + entry.count('C')) / blockSize
        gcContent.append(gc)
    return tuple(gcContent), tuple(blocks)

def gc_map(seq, block_size, gc_thresh):
    blockContent = gc_blocks(seq, block_size)

    #print(type(blockContent))
    #print('Hi', blockContent, 'Hi')
    toOutput = []

    print(len(blockContent))
    for i in range(0, len(blockContent[0])):
        if blockContent[0][i] > gc_thresh:
            toOutput.append(blockContent[1][i].upper())
        else:
            toOutput.append(blockContent[1][i].lower())

    outputString = ''.join(toOutput)
    return outputString

import re
from operator import itemgetter

def identifyORF(sequence):
    """Doc string here... fill me out"""
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

    # Now, are they actually valid?
    validatedPairs = []
    for i, x in enumerate(matchingPairs):
        ORFLength = x[1] - x[0]
        if ORFLength % 3 == 0:
            tupleToAppend = (x[0], x[1], ORFLength+3)
            validatedPairs.append(tupleToAppend)
        else:
            pass

    # Can we sort things based on their length
    largestORF = []
    currentMax = 0
    for i,x in enumerate(validatedPairs):
        if x[2] > currentMax:
            largestORF.append(x)
            currentMax = x[2]
        else:
            pass

    print(sequence[largestORF[0][0]:largestORF[0][1]])

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

    # Get our thresholded sequence
    thresholdedSequence = gc_map(cleanSequence, 1000, 0.45)

    # Write the sequence to a text file
    writeOutput(thresholdedSequence, headerSequence, 'thresholdedSequence.fasta')

    longestORF = identifyORF(cleanSequence)
    print(cleanSequence[0:1000])
    print('Longest ORF', longestORF)

main()
