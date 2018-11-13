
from abc import ABC, abstractmethod, abstractclassmethod
import re
from enum import Enum, unique


# ===================================================================================
class Serializable(ABC):
    # ===============================================================================
    @abstractmethod
    def serialize(self):
        "Encodes object state to string"
        pass

    @staticmethod
    @abstractmethod
    def unserialize(string):
        "Restore object state from string"
        pass


@unique
# ===================================================================================
class DNA(Enum):
    # ===============================================================================
    A, T, G, C = range(4)


@unique
# ===================================================================================
class AminoAcid(Enum):
    # ===============================================================================
    A, R, N, D, B, C, E, Q, Z, G, H, I, L, K, M, F, P, S, T, W, Y, V = range(
        22)


@unique
# ===================================================================================
class BaseTypes(Enum):
    # ===============================================================================
    dna, aminoacid = range(2)


corresponding_types = {BaseTypes.dna: DNA, BaseTypes.aminoacid: AminoAcid}


# ===================================================================================
class Base(Serializable):
    # ===============================================================================
    def __init__(self, base_type, value):
        assert isinstance(base_type, BaseTypes)
        assert isinstance(value, corresponding_types[base_type])
        self.type = base_type
        self.value = value

    def serialize(self):
        return "{}:{}".format(self.type.name, self.value.name)

    @staticmethod
    def unserialize(string):
        parsing = re.search(r"(.+):(.+)", string)
        base_type = BaseTypes[parsing.group(1)]
        value_type = corresponding_types[base_type]
        assert parsing.group(2) in [t.name for t in value_type], \
            "Base {} not valid for type {}".format(
            parsing.group(2), value_type.__name__)
        value = value_type[parsing.group(2)]
        return Base(base_type, value)


# ===================================================================================
class Pair(Serializable):
    # ===============================================================================
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def serialize(self):
        return "({},{})".format(self.a, self.b)

    @staticmethod
    def unserialize(string):
        parsing = re.search(r"\((.+),(.+)\)", string)
        return Pair(parsing.group(1), parsing.group(2))


if __name__ == "__main__":
    a = Pair(1, "a")
    print(a.serialize())
    b = Pair.unserialize("(2,3)")
    print(b.serialize())

    c = Base(BaseTypes.dna, DNA.A)
    d = Base.unserialize("dna:Y")
    print(c.serialize())
    print(d.serialize())
