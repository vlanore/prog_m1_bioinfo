def read(fn):
    f = open(fn, 'r')
    ls = f.readlines()
    r, n = [], ""
    for l in ls:
        if l[0] == '>':
            n = l[1:].strip()
        else:
            r.append((n, l.strip()))
    return r


def read2(fn):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    # Step 1: reading file
    f = open(fn, 'r')
    ls = f.readlines()

    # Step 2: going through the lines
    r = []  # result (a list)
    n = ""  # buffer for sequence names
    for l in ls:
        # if the line starts by > this is a sequence name
        if l[0] == '>':
            n = l[1:].strip()  # store in the n buffer
        else:  # otherwise it's a sequence line
            # add tuple (name, sequence) to result
            r.append((n, l.strip()))
    return r

def read_fasta(fasta_filename):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    # Step 1: reading file
    fasta_file = open(fasta_filename, 'r')
    lines = fasta_file.readlines()

    # Step 2: going through the lines
    result = []  # result (a list)
    name_buffer = ""  # buffer for sequence names
    for line in lines:
        # if the line starts by > this is a sequence name
        if line[0] == '>':
            # store in the name buffer
            name_buffer = line[1:].strip()
        else:  # otherwise it's a sequence line
            # add tuple (name, sequence) to result
            result.append((name_buffer, line.strip()))
    return result

def read_fasta2(fasta_filename):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    # Step 1: reading file
    fasta_file = open(fasta_filename, 'r')
    lines = fasta_file.readlines()

    # Step 2: going through the lines
    result = [] 
    name_buffer = ""
    for line in lines:
        is_sequence_name = (line[0] == '>')
        if is_sequence_name:
            name_buffer = line[1:].strip()
        else:  # otherwise it's a sequence line
            result.append((name_buffer, line.strip()))
    return result


print(read_fasta2("example.fasta"))
