

def count_nucleotides(dna_sequence: str) -> dict:
    dna_sequence = dna_sequence.upper()
    count = {
        "A": dna_sequence.count("A"),
        "G": dna_sequence.count("G"),
        "C": dna_sequence.count("C"),
        "T": dna_sequence.count("T"),
    }

    return count
