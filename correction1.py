import logging, sys
logging.basicConfig(format='\033[1m\033[35m%(levelname)s\033[0m(%(asctime)s)  %(message)s',
    level=logging.DEBUG, datefmt='%H:%M:%S')

def read_fasta(fasta_filename):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    logging.info("Step 1: reading file")
    fasta_file = open(fasta_filename, 'r')
    lines = fasta_file.readlines()
    if (len(lines) == 0):
        logging.warning("File %s is empty", fasta_filename)
        return []

    logging.info("Step 2: going through the lines")
    result = [] 
    name_buffer = ""
    for line in lines:
        is_sequence_name = (line[0] == '>')
        logging.debug("Looking at line %r, is_sequence_name=%r", line.strip(), is_sequence_name)
        if is_sequence_name:
            if name_buffer == "":
                name_buffer = line[1:].strip()
            else:
                logging.error("Two lines starting with > in a row")
                sys.exit(1)
        else:  # otherwise it's a sequence line
            if name_buffer != "":
                result.append((name_buffer, line.strip()))
                name_buffer = ""
            else:
                logging.error("Sequence line does not follow a line with >")
                sys.exit(1)
    return result