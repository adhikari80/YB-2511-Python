# Animal is the base (parent) class
# All other animal types inherit from this class
class Animal:
    def __init__(self, name):
        # store the name of the animal
        self.name = name


# Mammal class inherits from Animal
class Mammal(Animal):
    def __init__(self, name, feature):
        # call the constructor of Animal class
        super().__init__(name)
        # store mammal specific feature
        self.feature = feature


# Bird class inherits from Animal
class Bird(Animal):
    def __init__(self, name, feature):
        # call parent class constructor
        super().__init__(name)
        # store bird specific feature
        self.feature = feature


# Fish class inherits from Animal
class Fish(Animal):
    def __init__(self, name, feature):
        # call parent class constructor
        super().__init__(name)
        # store fish specific feature
        self.feature = feature


# Dog class inherits from Mammal
class Dog(Mammal):
    # dog has its own behaviour
    def walk(self):
        print(f"{self.name} is walking")


# Cat class inherits from Mammal
class Cat(Mammal):
    # cat has its own behaviour
    def walk(self):
        print(f"{self.name} is walking calmly")


# Eagle class inherits from Bird
class Eagle(Bird):
    # eagle can fly
    def fly(self):
        print(f"{self.name} is flying")


# Penguin class inherits from Bird
class Penguin(Bird):
    # penguin cannot fly, it can swim
    def swim(self):
        print(f"{self.name} is swimming")


# Salmon class inherits from Fish
class Salmon(Fish):
    # salmon swimming behaviour
    def swim(self):
        print(f"{self.name} is swimming")


# Shark class inherits from Fish
class Shark(Fish):
    # shark swimming behaviour
    def swim(self):
        print(f"{self.name} is swimming fast")


# main execution starts here
if __name__ == "__main__":

    # creating Mammal objects
    dog = Dog("Buddy", "Warm-blooded")
    cat = Cat("Kitty", "Fur-covered")

    dog.walk()
    cat.walk()

    # creating Bird objects
    eagle = Eagle("Rocky", "Sharp vision")
    penguin = Penguin("Pingo", "Flightless bird")

    eagle.fly()
    penguin.swim()

    # creating Fish objects
    salmon = Salmon("Salmo", "Gills")
    shark = Shark("Jaws", "Sharp teeth")

    salmon.swim()
    shark.swim()
