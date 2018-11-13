from abc import ABC, abstractmethod

class DataInterface(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def sum(self):
        pass

class DataPoint(DataInterface):
    def __init__(self, value):
        self.value = value

    def size(self):
        return 1

    def sum(self):
        return self.value


class DataCollection(DataInterface):
    def __init__(self, value_list):
        self.value_list = []
        for element in value_list:
            if issubclass(type(element), DataInterface):
                self.value_list.append(element)
            else:
                self.value_list.append(DataPoint(element))

    def size(self):
        return len(self.value_list)

    def sum(self):
        acc = 0
        for element in self.value_list:
            acc += element.sum()
        return acc


if __name__ == "__main__":
    my_list = DataCollection([DataPoint(3), DataPoint(5), DataCollection(
        [DataCollection([2, 7, 2.3]), 3, 5]), DataPoint(7)])
    print("Collection has size {} and sum {}".format(
        my_list.size(), my_list.sum()))
