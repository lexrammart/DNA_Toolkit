import random
from dna_logic.structures import NUCLEOTIDES_DNA

def generate_random_dna_sequence(length: int) -> str:
    """
    Generates a random DNA sequence with the specified length.
    :param length: The length of the DNA sequence.
    :return: A string with a random DNA sequence.
    """
    return ''.join(random.choice(NUCLEOTIDES_DNA) for _ in range(length))

def count_nucleotides(sequence):
    pass
