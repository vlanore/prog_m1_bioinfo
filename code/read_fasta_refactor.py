def read_fasta(fasta_filename):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    # Step 1: reading file
    fasta_file = open(fasta_filename, 'r')
    line_list = fasta_file.readlines()

    # Step 2: going through the sequences
    result = []
    nb_sequences = int(len(line_list) / 2)
    for sequence_index in range(nb_sequences):
        sequence_name = line_list[2 * sequence_index][1:].strip()
        sequence_data = line_list[2 * sequence_index + 1].strip()
        result.append((sequence_name, sequence_data))
    return result

print(read_fasta("data/example.fasta"))