class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

    def show_breed(self):
        print(f"Breed: {self.breed}")


d = Dog("Tommy", "Labrador")

d.show()        # from parent
d.show_breed()  # from child