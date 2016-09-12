def indexes(seq, start=0):
    return (i for i,_ in enumerate(seq, start=start))
def gen_all_substrings(s):
    return (s[i:j] for i in indexes(s) for j in indexes(s[i:], i+1))
def get_all_substrings(string):
    return list(gen_all_substrings(string))

def longestSub(sequence1, sequence2):
    if len(sequence1) > len(sequence2): 
    	larger = sequence1
    	smaller = sequence2
    else:
    	larger = sequence2
    	smaller = sequence1

    substrings = get_all_substrings(smaller)

    substringsInBoth = []
    for i in substrings:
    	if i in larger:
    		substringsInBoth.append(i)
    	else:
    		pass

    return(max(substringsInBoth, key=len))


