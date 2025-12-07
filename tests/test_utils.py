import unittest
from dna_logic.utils import validate_dna

class TestValidateDNA(unittest.TestCase):

    def test_validate_dna_valid(self):
        # case 1: DNA clean
        self.assertEqual(validate_dna("ATGC"), "ATGC")
        # case 2: DNA lowercase
        self.assertEqual(validate_dna("atgc"), "ATGC")
        #case 3: DNA repeated
        self.assertEqual(validate_dna("AAAA"), "AAAA")

    def tst_validate_dna_invalid(self):
        #case 4: invalid case
        self.assertFalse(validate_dna("ATGCZ"))
        #case 5: numbers
        self.assertFalse(validate_dna("1234"))
        #case 6: blank spaces
        self.assertFalse(validate_dna("A T G C"))

if __name__ == '__main__':
    unittest.main()
