class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def details(self):
        print("Name: {0}, Age: {1:d}.".format(self.name, self.age))


class Speciality:
    def __init__(self, name: str, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}." % (self.__class__.__name__, ', '.join(items))


class Engineer(Person):
    def __init__(self, name: str, age: int, speciality: Speciality):
        super().__init__(name, age)
        self.speciality = speciality

    def details(self):
        super().details()
        print("Speciality: ", self.speciality)


piyo = Engineer("piyo", 65, Speciality("DB"))
piyo.details()




