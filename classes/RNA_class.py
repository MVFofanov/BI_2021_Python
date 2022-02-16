class Rna(str):
    """Rna class documentation"""

    reverse_transcribed_dic = dict(zip('Uu', 'Tt'))
    genetic_code_table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'U', 'ACC': 'U', 'ACG': 'U', 'ACU': 'U',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': '*', 'UAG': '*',
        'UGC': 'C', 'UGU': 'C', 'UGA': '*', 'UGG': 'W',
    }

    def __init__(self, sequence): 
        """constructor"""
        self.sequence = sequence

    def get_reverse_transcribed(self):
        """return DNA sequence obtained from RNA sequence submitted after its reverse transcription"""
        dna_error = 'Try to reverse transcribe a RNA sequence instead of DNA'
        if 't' in self.sequence.lower():
            return dna_error
        else:
            return ''.join([char if char not in {'U', 'u'}
                            else self.reverse_transcribed_dic[char] for char in self.sequence])

    def translate(self):
        self.sequence = self.sequence.upper()
        protein = []
        if len(self.sequence) % 3 == 0:
            for i in range(0, len(self.sequence), 3):
                codon = self.sequence[i: i + 3]
                protein.append(self.genetic_code_table[codon])
        return ''.join(protein)


if __name__ == "__main__":
    sequence = Rna("GUCAUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAGUUG")
    print(sequence)
    print(type(sequence))
    sequence_translated = sequence.translate()
    print(sequence_translated)
    print()
    print(sequence.get_reverse_transcribed())
    print(Rna("ACGGTACGUUUU").get_reverse_transcribed())
