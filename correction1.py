import logging
import sys
logging.basicConfig(format='\033[1m%(asctime)s -\033[0m \033[1m\033[32m%(levelname)s\033[0m in file \033[1m%(filename)s\033[0m, line \033[1m%(lineno)d\033[0m (function \033[1m%(funcName)s\033[0m)\n\t%(message)s\n',
    level=logging.DEBUG, datefmt='%H:%M:%S')


def read_fasta(fasta_filename):
    """A function that reads the fasta file located at fn
    and outputs a list of (name, sequence)"""

    # Step 1: reading file
    fasta_file = open(fasta_filename, 'r')
    lines = fasta_file.readlines()
    if (len(lines) == 0):
        print("WARNING: File " + fasta_filename + " is empty!")
        return []

    # Step 2: going through the lines
    result = [] 
    name_buffer = ""
    for line in lines:
        is_sequence_name = (line[0] == '>')
        if is_sequence_name:
            if name_buffer == "":
                name_buffer = line[1:].strip()
            else:
                print("ERROR: Two lines starting with > in a row")
                sys.exit(1)
        else: # otherwise it's sequence data
            if name_buffer != "":
                result.append((name_buffer, line.strip()))
                name_buffer = ""
            else:
                print("ERROR: Sequence data does not follow a line with >")
                sys.exit(1)
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
