import unittest
from dna_logic.operations import count_nucleotides

# noinspection SpellCheckingInspection
class TestCountNucleotides(unittest.TestCase):
    def test_count_nucleotides_standard(self):
        # case 1: a varied standard sequence
        dna = "ACGCGTTAC"
        expected = {
            'A': 2, 'C': 3, 'G': 2, 'T': 2
        }
        self.assertEqual(count_nucleotides(dna), expected)

    def test_count_nucleotides_empty(self):
        # case 2: empty sequence, i.e., all key valures equal 0
        dna = ''
        expected = {
            'A': 0, 'C': 0, 'G': 0, 'T': 0
        }
        self.assertEqual(count_nucleotides(dna), expected)

    def test_count_nucleotides_single(self):
        # case 3: all characters in the sequence are the same.
        dna = 'AAA'
        expected = {
            'A': 3, 'C': 0, 'G': 0, 'T': 0
        }
        self.assertEqual(count_nucleotides(dna), expected)

if __name__ == '__main__':
    unittest.main()
