from test2 import PeopleContainer, Person, PeopleSet
from abc import ABC, abstractmethod


class DeclarationDisplay:
    def __init__(self, declarations):
        self.declarations = declarations

    def display(self):
        for i in range(len(self.declarations)):
            print("Declaration {}: {}".format(
                i, self.declarations[i].to_string()))


class Declarations:
    def __init__(self):
        self.declarations = []

    def new_person(self, name):
        self.declarations.append(Person(name))

    def new_container(self, container_type):
        self.declarations.append(PeopleContainer([], container_type))

    def add_person(self, name):
        assert type(self.declarations[-1]) == PeopleContainer
        self.declarations[-1].subsets.append(Person(name))


class DeclarationInterface:
    def __init__(self):
        self.model = Declarations()
        self.display = DeclarationDisplay(self.model.declarations)

    def run(self):
        while True:
            command = input("Enter command (q to quit): ")
            if command == "q":
                break
            elif command == "new person":
                self.get_name_and_declare(self.model.new_person)
            elif command == "new container":
                self.get_name_and_declare(self.model.new_container)
            elif command == "add person":
                self.get_name_and_declare(self.model.add_person)
            else:
                print("Existing commands are:\n*new person\n*add person\n*new container")
            self.display.display()

    def get_name_and_declare(self, method):
        name = input("Enter name: ")
        method(name)


interface = DeclarationInterface()
interface.run()
