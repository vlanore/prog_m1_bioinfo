import read_fasta_correction

# print(read_fasta_correction.read_fasta("data/example.fasta"))


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

class Addable(ABC):
    @abstractmethod
    def add(self, other):
        pass
    
    @staticmethod
    @abstractmethod
    def zero():
        pass

    @abstractmethod
    def greater_or_equal(self, other):
        pass

class NumberPair(Addable):
    def __init__(self, a, b):
        self.value = (a, b)
    
    def add(self, other):
        self.value = (self.value[0] + other.value[0],
            self.value[1] + other.value[1])

    @staticmethod
    def zero():
        return NumberPair(0, 0)

    def greater_or_equal(self, other):
        if self.value[0] != other.value[0]:
            return self.value[0] >= other.value[0]
        else:
            return self.value[1] >= other.value[1]

class UnaryInt(Addable):
    def __init__(self, value):
        self.value = []
        for _ in range(value):
            self.value.append(None)

    def add(self, other):
        self.value += other.value

    @staticmethod
    def zero():
        return UnaryInt(0)

    def greater_or_equal(self, other):
        return len(self.value) >= len(other.value)

def sum_addable(l):
    assert type(l) == list
    assert len(l) > 0
    element_class = type(l[0])
    assert issubclass(element_class, Addable)
    result = element_class.zero()
    for element in l:
        result.add(element)
    return result

l = [UnaryInt(2), UnaryInt(5), UnaryInt(3)]
l2 = [NumberPair(2, 2), NumberPair(5, 2), NumberPair(3, 2)]
l3 = [4.2, 4.3, 4.5]
print(sum_addable(l).value)
print(sum_addable(l2).value)
# print(sum_addable(l3))


class Vehicle(ABC):
    @abstractmethod
    def terrain(self):
        pass

    @abstractmethod
    def speed(self):
        pass

class Car(Vehicle):
    def terrain(self):
        return "ground"

    @abstractmethod
    def nb_doors(self):
        pass

class Boat(Vehicle):
    def terrain(self):
        return "water"

class Beetle(Car):
    def __init__(self, color):
        self.color = color

    def nb_doors(self):
        return 3
        
    def speed(self):
        return 100

my_car = Beetle("blue")