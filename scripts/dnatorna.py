"""
Convert DNA sequences to RNA.
"""
def rna(seq):
    """Convert a DNA sequence to RNA"""

    #convert sequence to uppercase
    seq = seq.upper()

    #return the sequence with Ts replaced with Us
    return seq.replace('T', 'U')
