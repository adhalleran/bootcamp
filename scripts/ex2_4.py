import re
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


"""
find each occurence of ATG, append that index to a list of "starts"

find each occurence of TGA, TAG or TAA (treat them identically), append that index to a list of "stops"

Check to find all ORFs

So, pop the first entry of the ATG
pop the first stop

If the first stop follows the ATG, assign those to a pair
Check if the pair is valid (aka the distance between the indices is a multiple of three)
if it is, add the pair and the distance between them to a list of things

Then, how are we storing this list of things? Actually. Key being the distance and then
the positions between the value wouldn't be bad.

Then, search for the largest Key
Get it's value

def dnaToProtein(DNASequence):
    pass"""
