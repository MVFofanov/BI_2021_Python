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
