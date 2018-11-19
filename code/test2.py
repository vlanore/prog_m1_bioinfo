from abc import ABC, abstractmethod

class Stringable(ABC):
    @abstractmethod
    def to_string(self): # returns a string
        pass


class Countable(ABC):
    @abstractmethod
    def count(self): # returns an int
        pass

class PeopleSet(Stringable, Countable):
    pass

class Person(PeopleSet):
    def __init__(self, name):
        self.name = name
    
    def to_string(self):
        return self.name

    def count(self):
        return 1


class PeopleContainer(PeopleSet):
    def __init__(self, subsets, set_type):
        assert type(subsets) == list
        self.subsets = subsets
        self.set_type = set_type

    def count(self):
        result = 0
        for subset in self.subsets:
            result += subset.count()
        return result

    def to_string(self):
        result = self.set_type + "{ "
        for subset in self.subsets:
            result += subset.to_string() + " "
        return result + "}"


if __name__ == "__main__":
    john, jenny, betty = Person("john"), Person("jenny"), Person("betty")
    appartment1 = PeopleContainer([john], "appartment")
    appartment2 = PeopleContainer([jenny, betty], "appartment")
    building = PeopleContainer([appartment1, appartment2], "building")
    print(building.count())
    print(building.to_string())