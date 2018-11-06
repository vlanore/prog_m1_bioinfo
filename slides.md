---
theme: white
---

<!--=================================================================================================== -->
<!-- INTRO -->
<!--=================================================================================================== -->

<link href='custom.css' rel='stylesheet' type='text/css'>

## <h2 style="color:white;">Good software <br/> engineering practices</h2>
<!-- .slide: style="color:white" -->
<!-- .slide: data-background="code.png" -->

UE programmation

Master bioinfo

Automne 2018


---

### Who am I?

_Vincent Lanore_

Send questions at:

[vincent.lanore@univ-lyon1.fr](mailto:vincent.lanore@univ-lyon1.fr)


---

### Software engineering courses

* today
* next monday afternoon


---

<!--=================================================================================================== -->
<!-- EXAMPLE: parsing fasta files -->
<!--=================================================================================================== -->

## <h2 style="color:white;">Example:<br/>parsing FASTA files</h2>
<!-- .slide: style="color:white" -->
<!-- .slide: data-background="code.png" -->

---

### FASTA files

This is a FASTA file:

```fasta
>SEQUENCE_1
MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEGLVSVKVSDDFTIAAMRPSYLSYEDLDMTFVENEYKALVAELEKENEERR
>SEQUENCE_2
SATVSEINSETDFVAKNDQFIALTKDTTAHIQSNSLQSVEELHSSTINGVKFEEYLKSQIATIGENLVVRRFATLKAGANGVVNGYIHTNGRVGVVIAAACDSAEVASKSRDLLRQICMH
```

Lines starting with `>` are sequence names<br/>
they are followed by the sequence in plain text

---

### A fasta parser in python

__Goal:__ write a function that<br/>
takes the path to a fasta file
```path
~/data/example.fasta```
and returns a list of sequences
```python
[
    ('SEQUENCE1', 'AGMMD...'),
    ('SEQUENCE2', 'MMDGGAA...')
]
```

----

```python
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
```

What's wrong with this code?
<!-- .element: class="fragment" -->

---

<!--=================================================================================================== -->
<!-- Improving code readability -->
<!--=================================================================================================== -->

## <h2 style="color:white;"> Improving code readability </h2>
<!-- .slide: style="color:white" -->
<!-- .slide: data-background="code.png" -->

---

#### Adding comments

```python
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
```

---

#### Better variable names

```python
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
```

---

#### Self-documenting code

```python
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
```