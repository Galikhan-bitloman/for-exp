class Animal(object):
    def __init__(self, behavior):
        self.behavior = behavior
        print("Animal constructor")

    def getbehavior(self):
        for i in self.behavior:
            print(i)



class Dog(Animal):
    def __init__(self, behavior):
        super(Dog, self).__init__(behavior)
        print("Dog constructor")
        print("Animal run")
        print("Dog barks")

    def getbehavior1(self):
        for i in self.behavior:
            print(i)




my1 = Dog(behavior='')
my1.getbehavior1()


class Dog1(Animal):
    def __init__(self, behavior):
        super(Dog1, self).__init__(behavior)
        print("Dog constructor")
        print("Animal talks")
        print("Dog chase cat")


    def getbehavior2(self):
        for i in self.behavior:
            print(i)
my2 = Dog1(behavior='')
my2.getbehavior2()



