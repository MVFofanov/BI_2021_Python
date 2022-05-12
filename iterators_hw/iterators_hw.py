import random


def fasta_reader(fasta_file_path):
    """get fasta file path, read fasta file and return its header and sequence in pairs"""
    with open(fasta_file_path) as fasta_file:
        seq_id = None
        sequence = []

        for line in fasta_file:
            if line.startswith('>'):
                if sequence:
                    yield seq_id, ''.join(sequence)
                    sequence = []
                seq_id = line.strip().lstrip('>')
            else:
                sequence.append(line.strip())
        else:
            yield seq_id, ''.join(sequence)


class AminoAcidSequenceMutator:
    """get fasta file path, read fasta file and randomly mutate each sequence"""
    amino_acid_list = list('ACDEFHIGKLMNPRSTQVWY')

    def __init__(self, path_to_file):
        """class instance initialization"""
        self.path_to_file = path_to_file
        self.make_random_change_probability = random.uniform(0.5, 1)
        self.max_mutation_length = random.randint(50, 250)
        self.max_change_number = random.randint(50, 250)
        self.fasta_generator = fasta_reader(path_to_file)

    def __iter__(self):
        return self

    def __next__(self):
        """get fasta file path, read fasta file and return every next sequence endlessly"""
        try:
            idx, sequence = next(self.fasta_generator)
        except StopIteration:
            self.fasta_generator = fasta_reader(self.path_to_file)
            idx, sequence = next(self.fasta_generator)
        return self.make_random_change(sequence)

    def make_random_change(self, sequence):
        """make several random mutations and return mutated sequence"""
        functions = (
            self.make_inversion,
            self.make_deletion,
            self.make_insertion,
            self.make_substitution
        )

        if random.random() <= self.make_random_change_probability:
            functions_order = random.choices(functions, k=random.randint(1, self.max_change_number))
            for function in functions_order:
                sequence = function(sequence)
            return sequence
        else:
            return sequence

    def make_inversion(self, sequence):
        """get sequence and return mutated sequence with inversion"""
        sequence_length = len(sequence)
        inversion_start = random.randint(0, sequence_length - 1)
        inversion_length = random.randint(0, self.max_mutation_length)

        result_sequence = ''.join([sequence[: inversion_start],
                                   sequence[inversion_start: inversion_start + inversion_length][::-1],
                                   sequence[inversion_start + inversion_length:]])
        return result_sequence

    def make_deletion(self, sequence):
        """get sequence and return mutated sequence with deletion"""
        sequence_length = len(sequence)
        deletion_start = random.randint(0, sequence_length - 1)
        deletion_end = random.randint(deletion_start, sequence_length - 1)

        result_sequence = ''.join([sequence[: deletion_start],
                                   sequence[deletion_end:]])

        return result_sequence

    def make_insertion(self, sequence):
        """get sequence and return mutated sequence with insertion"""
        sequence_length = len(sequence)
        insertion_start = random.randint(0, sequence_length - 1)
        insertion_length = random.randint(0, self.max_mutation_length)
        random_sequence = ''.join(random.choices(self.amino_acid_list, k=insertion_length))

        result_sequence = ''.join([sequence[: insertion_start],
                                   random_sequence,
                                   sequence[insertion_start + 1:]])

        return result_sequence

    def make_substitution(self, sequence):
        """get sequence and return mutated sequence with substitution"""
        sequence_length = len(sequence)
        substitution_start = random.randint(0, sequence_length - 1)
        substitution_length = random.randint(0, self.max_mutation_length)
        substitution_sequence = ''.join(random.choices(self.amino_acid_list, k=substitution_length))

        result_sequence = ''.join([sequence[: substitution_start],
                                   substitution_sequence,
                                   sequence[substitution_start + substitution_length:]])
        return result_sequence


def iter_append(iterable, item):
    yield from iterable
    yield item


def unpack_nested_list(my_list):
    for element in my_list:
        if type(element) is list:
            yield from unpack_nested_list(element)
        else:
            yield element


def nested_list_unpacker(my_list):
    return list(unpack_nested_list(my_list))


if __name__ == "__main__":
    # checking the performance of functions above
    fasta_file_path = 'sequences.fasta'

    print('Task1\n')

    reader = fasta_reader(fasta_file_path)
    print(type(reader))
    for id_, seq in reader:
        print(id_, seq[:50])

    print('\nTask2')

    sequence_mutated = AminoAcidSequenceMutator(fasta_file_path)
    print(f'\nRandom mutated amino acid sequences:\n\n{next(sequence_mutated)}')
    for i in range(10):
        print(f'{next(sequence_mutated)}\n')

    print('Task3\n')

    generator = iter_append([1, 2, 3, 4], 'ABCD')
    print(type(generator))
    for i in generator:
        print(i)

    filt = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    generator = iter_append(filt, [5, 6, 7, 8])
    print(type(generator))
    for i in generator:
        print(i)

    print('\nTask4\n')

    packed_list = [1, 2, 3, [1, 2, [3, 4, []], [1], [], 12, 3], [1, [5, 6]]]
    print(f'Unpacked list is {nested_list_unpacker(packed_list)}')

