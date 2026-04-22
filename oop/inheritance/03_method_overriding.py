class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):   # overriding parent method
        print("Dog barks")


a = Animal()
d = Dog()

a.speak()
d.speak()