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


a = MyFloat(1.2)
b = MyFloat(1.0)

print("a.real = {}, b.real = {}, a.is_integer()={}, b.is_integer()={}".format(
    a.real, b.real, a.is_integer(), b.is_integer()))

c = MySuperFloat(1.3)
print("c.is_positive()={}, c.real={}".format(c.is_positive(), c.real))