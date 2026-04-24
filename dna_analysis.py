# DNA Sequence Analysis Tool

def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    return ((g + c) / len(sequence)) * 100

def reverse_complement(sequence):
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join(complement[base] for base in reversed(sequence))

def analyze_dna(sequence):
    sequence = sequence.upper()
    
    print("DNA Sequence:", sequence)
    print("Length:", len(sequence))
    print("GC Content: {:.2f}%".format(gc_content(sequence)))
    print("Reverse Complement:", reverse_complement(sequence))

# Example sequence
dna = "ATGCGTACGTTAGC"
analyze_dna(dna)
