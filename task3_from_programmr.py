#Write a Python program using inheritance to print the value of Counter.
#Create a class Counter with class variable 'i' and method called 'increment()'.
#Now write a subclass extending Counter class which calls the increment() function and displays the following output:


class Counter(object):
    def __init__(self, i):
        i = 0

def increment(self):
    print('i = 3')

class SubCounter(Counter):
    def __init__(self):
        super(SubCounter, self).__init__(i=0)


    def increment(self):
        print('i = 3')




result = SubCounter()
result.increment()

