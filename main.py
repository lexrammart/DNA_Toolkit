from dna_logic.operations import count_nucleotides
from dna_logic.utils import validate_dna, generate_random_dna_sequence

if __name__ == '__main__':
    print("\n--- DNA Toolkit Starting ---\n")

    dna_string = generate_random_dna_sequence(50)
    print(f"DNA string: {dna_string}")
    print(f"Length of DNA string: {len(dna_string):,.0f}")

    dna_string_manual = input("Input the DNA strand manually: ")
    if validate_dna(dna_string_manual):
        nucleotide_amounts = count_nucleotides(dna_string_manual)
        print(f"Total number of nucleotides: {sum(nucleotide_amounts.values())}")
        for nucleotide, count in nucleotide_amounts.items():
            print(f"{nucleotide}: {count}")
    else:
        print("Error")