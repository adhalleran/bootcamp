def reverseComplement(sequence):
    """Reverse complement program this time using a while loop instead
    of the for loop used previously."""

    # take the input sequence and use string comprehension to
    # reverse it. 

    reverseSequence = sequence[::-1]

    # Perform reverse complementation. Note how A and G are first
    # transofmed into lowercase a and g - this is to prevent them
    # being converted twice (from A to T and then in the T operation)
    reverseSequence.replace('A', 'a')
    reverseSequence.replace('T', 'A')
    reverseSequence.replace('a', 'T')
    reverseSequence.replace('G', 'g')
    reverseSequence.replace('C', 'G')
    reverseSequence.replace('g', 'C')
    
    return reverseSequence