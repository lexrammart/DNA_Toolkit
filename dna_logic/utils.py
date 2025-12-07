from dna_logic.structures import NUCLEOTIDES_DNA

def validate_dna(dna_seq: str) -> str | bool:
    """
    Checks if DNA sequence is valid.
    :param dna_seq:
    :return: Upper case DNA sequence if valid, False otherwise.
    """
    dna_seq = dna_seq.upper()

    return dna_seq if all(nucleotide in NUCLEOTIDES_DNA for nucleotide in dna_seq) else False