'''
Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different. For instance, Dog’s can be to print
‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and 
performs talk method on input parameter.

'''


def print_talk(animal):
    print(animal.talk())


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError(f'Define talk for {self.__class__.__name__}')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        return "woof woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        return "meow"


if __name__ == '__main__':
    cat = Cat("Masha")
    print_talk(cat)
    dog = Dog("Sharik")
    print_talk(dog)
