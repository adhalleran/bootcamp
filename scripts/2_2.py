import os

def writeOutput(seq, header, outputFilename):
    with open(outputFilename, 'w') as output:
        output.write(header)
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

    toOutput = []

    for i in range(0, len(blockContent[0])):
        if blockContent[0][i] > gc_thresh:
            toOutput.append(blockContent[1][i].upper())
        else:
            toOutput.append(blockContent[1][i].lower())

    outputString = ''.join(toOutput)
    return outputString

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
    print(len(thresholdedS))

    # Write the sequence to a text file
    writeOutput(thresholdedSequence, headerSequence, 'thresholdedSequence.fasta')

    writeOutput()
    longestORF = identifyORF(cleanSequence)
    print(cleanSequence[0:1000])
    print('Longest ORF', longestORF)

main()
