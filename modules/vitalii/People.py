class Person:
    def __init__(self, name):
        self.name = name


class PeopleFacade:
    def __init__(self):
        self.people = []

    def add_person(self, name):
        person = Person(name)
        self.people.append(person)

    def get_people_names(self):
        return [person.name for person in self.people]
