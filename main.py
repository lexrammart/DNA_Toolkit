from dna_logic.operations import generate_dna_sequence

if __name__ == '__main__':
    print("\n--- DNA Toolkit Starting ---\n")

    dna_string = generate_dna_sequence(90)
    print(f"DNA string: {dna_string}")
    print(f"Length of DNA string: {len(dna_string):,.0f}")