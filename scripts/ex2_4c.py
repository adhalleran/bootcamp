import bioinfo_dicts

def translate(seq):
    sequences = [seq[i:i+3] for i in range (0, len(seq), 3)]
    print(sequences)
    proteinSequence = []
    for i, x in enumerate(sequences):
        proteinSequence.append(biodict_info.codons[x])
    outputString = ''.join(proteinSequence)

    return outputString