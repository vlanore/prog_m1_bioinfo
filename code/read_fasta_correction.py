import logging
import sys
logging.basicConfig(format='\033[1m%(asctime)s -\033[0m \033[1m\033[32m%(levelname)s\033[0m in file \033[1m%(filename)s\033[0m, line \033[1m%(lineno)d\033[0m (function \033[1m%(funcName)s\033[0m)\n\t%(message)s\n',
    level=logging.DEBUG, datefmt='%H:%M:%S')


def read_fasta(fasta_filename):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    # Step 1: reading file
    fasta_file = open(fasta_filename, 'r')
    line_list = fasta_file.readlines()
    if (len(line_list) == 0):
        print("Warning: File " + fasta_filename + " is empty!")

    # Step 2: going through the sequences
    result = []
    nb_sequences = int(len(line_list) / 2)
    for sequence_index in range(nb_sequences):
        first_line_index = 2 * sequence_index
        assert line_list[first_line_index][0] == '>'
        assert line_list[first_line_index + 1][0] != '>'
        sequence_name = line_list[first_line_index][1:].strip()
        sequence_data = line_list[first_line_index + 1].strip()
        result.append((sequence_name, sequence_data))
    return result


def read_fasta3(fasta_filename):
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
            assert name_buffer == "", "Two lines with > in a row"
            name_buffer = line[1:].strip()
        else: # otherwise it's sequence data
            assert name_buffer != "", "Data without sequence name"
            result.append((name_buffer, line.strip()))
            name_buffer = ""
    return result


def read_fasta2(fasta_filename):
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
        logging.debug("Looking at line %r", line.strip())
        if line[0] == '>':
            logging.debug("Line is a sequence name")
            if name_buffer == "":
                name_buffer = line[1:].strip()
            else:
                logging.error("Two lines starting with > in a row")
                sys.exit(1)
        else:
            logging.debug("Line is sequence data")
            if name_buffer != "":
                result.append((name_buffer, line.strip()))
                name_buffer = ""
            else:
                logging.error("Sequence line does not follow a line with >")
                sys.exit(1)

    logging.info("Step 3: everything went fine; returning result")
    return result

if __name__ == "__main__":
    print(read_fasta("data/example.fasta"))
    print(read_fasta("data/example2.fasta"))
