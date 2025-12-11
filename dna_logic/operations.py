
def count_nucleotides(dna_sequence: str) -> dict:
    """
    Counts the number of nucleotides in a DNA sequence.
    :param dna_sequence: DNA sequence
    :return: count: number of nucleotides
    """
    dna_sequence = dna_sequence.upper()
    count = {
        "A": dna_sequence.count("A"),
        "G": dna_sequence.count("G"),
        "C": dna_sequence.count("C"),
        "T": dna_sequence.count("T"),
    }

    return count

def dna_transcription (dna_sequence: str) -> str:
    """
    Converts a DNA strand into an RNA transcription.
    :param dna_sequence: DNA strand
    :return: RNA transcription
    """
    return dna_sequence.upper().replace("T", "U")
