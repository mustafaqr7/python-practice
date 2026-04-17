class Student:
    def __init__(self, name, age):
        self._name = name    # protected
        self._age = age      # protected


s = Student("Mustafa", 31)

print(s._name)
print(s._age)