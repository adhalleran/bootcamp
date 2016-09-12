def reverseComplement(sequence):
    """Reverse complement function, this time lacking
    the 'reverse' function"""
    reversedList = []
    for base in range (0, len(sequence)):
        reversedList.insert(0, sequence[base])
    print(reversedList)
    
    rev_comp = []
    for base in reversedList:
        complementedBase = complementBase(base)
        rev_comp.append(complementedBase)

    reverseComplementSequence = ''.join(rev_comp)
    print reverseComplementSequence

def complementBase(base, material='DNA'):
    """Return the watson/crick complement of a base"""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid material.')
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'
