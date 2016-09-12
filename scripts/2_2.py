inputFile = open('/Users/andrewhalleran/Documents/git/bootcamp/data/salmonella_spi1_region.fna', 'r')

sequence = inputFile.readlines()
print(sequence[0])
