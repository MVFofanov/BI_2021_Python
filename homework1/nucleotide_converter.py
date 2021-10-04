rna_dic = dict(zip('ACGUacgu', 'UGCAugca'))
dna_dic = dict(zip('ACGTacgt', 'TGCAtgca'))
transcribed_dic = dict(zip('Tt', 'Uu'))
reverse_transcribed_dic = dict(zip('Uu', 'Tt'))
extended_dna_dic = dict(zip('ACGTWSMKRYNBDHVacgtwsmkrynbdhv', 'TGCASWKMYRNVHDBtgcaswkmyrnvhdb'))
extended_rna_dic = dict(zip('ACGUWSMKRYNBDHVacguwsmkrynbdhv', 'UGCASWKMYRNVHDBugcaswkmyrnvhdb'))


def use_dna_or_rna_letters(sequence):
    if 'u' not in sequence.lower():
        return dna_dic
    else:
        return rna_dic


def is_invalid_alphabet(sequence):
    return set(sequence.lower()) - set(''.join(nucl_dic.keys()).lower())


def get_extended_alphabet(mode, dna_or_rna, input_file=''):
    extended = input('Do you want to use the extended nucleotide alphabet? Type yes or no: ').lower()
    if extended in {'yes', 'y'} and mode in {'m', 'manually', 'f', 'file'} and dna_or_rna == dna_dic:
        return extended, extended_dna_dic
    elif extended in {'yes', 'y'} and mode in {'m', 'manually', 'f', 'file'} and dna_or_rna == rna_dic:
        return extended, extended_rna_dic
    elif extended not in {'yes', 'y'} and mode in {'f', 'file'}:
        return extended, use_dna_or_rna_letters(get_sequence_example_from_file(input_file))
    else:
        return extended, use_dna_or_rna_letters(sequence)


def get_print(sequence):
    return sequence


def get_reversed(sequence):
    return sequence[::-1]


def get_transcribed(sequence, extended=''):
    rna_error = 'Try to transcribe a DNA sequence instead of RNA'
    if 'u' in sequence.lower():
        return rna_error
    else:
        return ''.join([c if c not in {'T', 't'} else transcribed_dic[c] for c in sequence])


def get_reverse_transcribed(sequence, extended=''):
    dna_error = 'Try to reverse transcribe a RNA sequence instead of DNA'
    if 't' in sequence.lower():
        return dna_error
    else:
        return ''.join([c if c not in {'U', 'u'} else reverse_transcribed_dic[c] for c in sequence])


def get_complemented(sequence):
    return ''.join([nucl_dic[c] for c in sequence])


def get_reverse_complemented(sequence):
    return get_complemented(get_reversed(sequence))


def get_example(example):
    example = example.lower()
    if example == 'dna example' or example == 'dna':
        return 'ACGTacgtAATtggcgcg'
    elif example == 'rna example' or example == 'rna':
        return 'ACGUacguAAUuggcgcg'


def get_file_example(example):
    example = example.lower()
    if example in {'viruses extended', 've'}:
        return 'viruses_extended_alphabet_examples.txt', 'viruses_extended_alphabet_examples_result.txt'
    elif example in {'viruses default', 'vd'}:
        return 'viruses_default_alphabet_examples.txt', 'viruses_default_alphabet_examples_result.txt'


def get_sequence_example_from_file(input_file):
    with open(input_file) as r:
        lines = r.read().splitlines()
        fasta = ''
        for line in lines:
            if not line.startswith('>'):
                fasta += line
        return fasta


def get_converted_sequence(command, sequence, extended=''):
    if command in {'reverse', 'r'}:
        return get_reversed(sequence)
    elif command in {'transcribe', 't'}:
        return get_transcribed(sequence)
    elif command in {'reverse transcribe', 'rt'}:
        return get_reverse_transcribed(sequence)
    elif command in {'complement', 'c'}:
        return get_complemented(sequence)
    elif command in {'reverse complement', 'rc'}:
        return get_reverse_complemented(sequence)
    elif command in {'print', 'p'}:
        return get_print(sequence)


def get_converted_header(command, header):
    if command in {'reverse', 'r'}:
        return header + '_sequence_was_reversed'
    elif command in {'transcribe', 't'}:
        return header + '_sequence_was_transcribed'
    elif command in {'reverse transcribe', 'rt'}:
        return header + '_sequence_was_reverse_transcribed'
    elif command in {'complement', 'c'}:
        return header + '_sequence_was_complemented'
    elif command in {'reverse complement', 'rc'}:
        return header + '_sequence_was_reverse_complemented'
    elif command in {'print', 'p'}:
        return header + '_sequence_was_printed'


def get_sequences_from_file(command, input_file, output_file):
    with open(input_file) as r, open(output_file, 'w') as w:
        lines = r.read().splitlines()
        fasta = ''
        for line in lines:
            if line.startswith('>'):
                if len(fasta) > 0:
                    w.write(get_converted_sequence(command, fasta) + '\n')
                    fasta = ''
                    w.write(get_converted_header(command, line) + '\n')
                else:
                    w.write(get_converted_header(command, line) + '\n')
            else:
                fasta += line
        w.write(get_converted_sequence(command, fasta) + '\n')


def get_help():
    help_message = f'''
    Program: nucleotide_converter.py
    Version: 1.0

    Currently available commands:
    c or complement             converts a DNA/RNA sequence into its complement conterpart
    e or exit                   quit the programm
    q or quit                   quit the programm
    h or help                   get this help page
    p or print                  print a DNA/RNA sequence itself. It may be usefull to check if your sequence has
                                suitable format (dna or rna) with valid alphabet or convert multi-line fasta
                                from input file into single line fasta per sequence format in output file
    r or reverse                converts a DNA/RNA sequence into its reverse conterpart
    rc or reverse complement    converts a DNA/RNA sequence into its reverse complement conterpart
    rt or reverse transcribe    converts a RNA sequence into its DNA conterpart
    t or transcribe             converts a DNA sequence into its RNA conterpart

    Available fasta sequences sources:
    m or manually               type the sequence in the command line manually
    f or file                   type input fasta file and output file where converted sequences will be placed,
                                file name format: file.txt, file.fasta, etc

    You can type the sequence of your interest or use some examples by typing this:

    example sequences:
    dna or dna example          use example dna sequence {get_example('dna example')}
    rna or rna example          use example rna sequence {get_example('rna example')}

    input example files:
    vd or viruses default       use example viruses genome sequences with a default nucleotide alphabet
                                input file:     viruses_default_alphabet_examples.txt
                                output file:    viruses_default_alphabet_examples_result.txt

    ve or viruses extended      use example viruses genome sequences with an extended nucleotide alphabet
                                input file:     viruses_extended_alphabet_examples.txt
                                output file:    viruses_extended_alphabet_examples_result.txt

    If you want to use the extended nucleotide alphabet type 'yes' or 'y' when program asks about it
    Default nucleotide alphabet includes 'ACGTUacgtu'.
    Extended nucleotide alphabet supports 'ACGTUWSMKRYNBDHVacgtuwsmkrynbdhv'

    Fasta sequences are case sensitive unlike commands:
    'ACGT' and 'acgt' are different sequences.
    'COMPLEMENT' and 'complement' performs equally

    Contacts:
    Mikhail Fofanov             mikhail.v.fofanov@gmail.com
    '''
    return help_message


print('''
    Frequently used commands: complement, exit, help, reverse, reverse complement, transcribe.
    Commands can be used not only by their full names, but also by its first letters, for example,
    such command as 'c' or 'complement' and 'rc' or 'reverse complement' performs equally
    Full list of commands, examples and details of use you can find by entering 'h' or 'help'
    ''')


while True:
    command = input('Enter command: ').lower()
    if command in {'exit', 'e', 'q', 'quit'}:
        print('Good luck\n')
        break
    elif command in {'help', 'h'}:
        print(get_help())
    elif command not in {'reverse', 'transcribe', 'reverse transcribe', 'complement',
                         'reverse complement', 'print', 'r', 't', 'c', 'rc', 'p', 'rt'}:
        print('Invalid command. Try again!\n')
    else:
        mode = input("Type 'm' to insert the sequence manually or 'f' to download sequences from file: ").lower()
        if mode in {'f', 'file'}:
            input_file = input('Enter input file: ')
            if input_file in {'viruses extended', 've', 'viruses default', 'vd'}:
                input_file, output_file = get_file_example(input_file)
                try:
                    f = open(input_file)
                    f.close()
                except FileNotFoundError:
                    print(f'File {input_file} is not found in the working directory. \
                            Please, place it here and try again!\n')
                    continue
            else:
                try:
                    f = open(input_file)
                    f.close()
                except FileNotFoundError:
                    print(f'File {input_file} is not found\n')
                    continue
                else:
                    output_file = input('Enter output file: ')
            dna_or_rna = use_dna_or_rna_letters(get_sequence_example_from_file(input_file))
            extended, nucl_dic = get_extended_alphabet(mode, dna_or_rna, input_file)
            if is_invalid_alphabet(get_sequence_example_from_file(input_file)):
                mes = ''.join(set(get_sequence_example_from_file(input_file)) - set(''.join(nucl_dic.keys())))
                print(f"Invalid alphabet: {mes}. Try again!\n")
            else:
                get_sequences_from_file(command, input_file, output_file)
                print()
        elif mode in {'m', 'manually'}:
            sequence = input('Enter sequence: ')
            if sequence in {'dna example', 'rna example', 'dna', 'rna'}:
                sequence = get_example(sequence)
            dna_or_rna = use_dna_or_rna_letters(sequence)
            extended, nucl_dic = get_extended_alphabet(mode, dna_or_rna)
            if is_invalid_alphabet(sequence):
                print(f"Invalid alphabet: {''.join(set(sequence) - set(''.join(nucl_dic.keys())))}. Try again!\n")
            else:
                print(f'Result sequence: {get_converted_sequence(command, sequence)}\n')
        else:
            print('Invalid source of sequences. Try again!\n')
