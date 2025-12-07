import random

def generate_dna_sequence(length):
    """
    Generates a random DNA sequence with the specified length.
    """
    bases = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(bases) for _ in range(length))