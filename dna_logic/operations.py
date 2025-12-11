
def count_nucleotides(dna_sequence: str) -> dict:
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
    :param dna_sequence:
    :return:
    """
    return dna_sequence.upper().replace("T", "U")
