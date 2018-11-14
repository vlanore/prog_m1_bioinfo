import read_fasta_correction

print(read_fasta_correction.read_fasta("data/example.fasta"))


class MyFloat:
    def __init__(self, value):
        self.real = value

    def is_integer(self):
        return (self.real - float(int(self.real))) == 0

class MySuperFloat(MyFloat):
    def is_positive(self):
        return self.real >= 0


def sum1(l):
    result = 0
    for element in l:
        result += element
    return result


def sum2(l):
    assert type(l) == list
    assert len(l) > 0
    if type(l[0]) == str:
        zero = ""
    elif type(l[0]) == int:
        zero = 0
    for element in l:
        zero += element
    return zero

zeros = {str:"", int:0, float:0, list:[]}

def sum3(l):
    assert type(l) == list
    assert len(l) > 0
    result = zeros[type(l[0])]
    for element in l:
        result += element
    return result

a = MyFloat(1.2)
b = MyFloat(1.0)

print("a.real = {}, b.real = {}, a.is_integer()={}, b.is_integer()={}".format(
    a.real, b.real, a.is_integer(), b.is_integer()))

c = MySuperFloat(1.3)
print("c.is_positive()={}, c.real={}".format(c.is_positive(), c.real))

print(sum3([1, 2.3]))
print(sum3(["a", "b", "c"]))
print(sum3([[1,2], [3, "a"], [4]]))


class List3:
    def __init__(self, a, b, c):
        self.value = [a, b, c]
    
    def count(self, value):
        result = 0
        for element in self.value:
            if value == element:
                result += 1
        return result

def count_list(l, value):
    result = 0
    for element in l:
        result += element.count(value)
    return result

l1 = [1, 2, 3, 4, 2]
l2 = List3(2, 3, 4)
a = count_list([l1, l2, (2, 3)], 2)
print(a)


from abc import ABC, abstractmethod, abstractproperty

class SequenceInterface(ABC):
    @abstractmethod
    def size(self):
        pass

def pretty_print_sequence(s):
    message = "Sequence {} with {} elements: {}.".format(
        s.name, s.size(), s.sequence)
    print(message)

class DNA(SequenceInterface):
    def __init__(self, name, seq):
        # self.name = name
        self.sequence = seq

    def size(self):
        return len(self.sequence)

s = DNA("seq1", "ATTGGCT")
pretty_print_sequence(s)