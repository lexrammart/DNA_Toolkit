import random
from dna_logic.structures import NUCLEOTIDES_DNA

def generate_random_dna_sequence(length: int) -> str:
    """
    Generates a random DNA sequence with the specified length.
    :param length: The length of the DNA sequence.
    :return: A string with a random DNA sequence.
    """
    return ''.join(random.choice(NUCLEOTIDES_DNA) for _ in range(length))

def validate_dna(dna_seq: str) -> str | bool:
    """
    Checks if DNA sequence is valid.
    :param dna_seq:
    :return: Upper case DNA sequence if valid, False otherwise.
    """
    dna_seq = dna_seq.upper()

    return dna_seq if all(nucleotide in NUCLEOTIDES_DNA for nucleotide in dna_seq) else False