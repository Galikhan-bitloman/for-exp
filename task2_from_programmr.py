class Pet:
    def __init__(self, name, eats):
        self.name = name
        self.eats = eats


class Cat(Pet):
    def __init__(self, name, eats):
        super(Cat, self).__init__(name, eats)

    def iny(self):
        print(self.name)
        print(self.eats)


cat = Cat(input("Cat Name: "), input("Cat food: "))
cat.iny()


class Dog(Pet):
    def __init__(self, name, eats):
        super(Dog, self).__init__(name, eats)

    def ini(self):
        print(self.name)
        print(self.eats)

    def eat_cat(self):
        print(self.name + " has eaten " + cat)


dog = Dog(input("Dog Name: "), input("Dog food: "))
dog.ini()
dog.eat_cat(cat)
