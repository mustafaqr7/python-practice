class Student:
    def __init__(self, name, age):
        self.__name = name   # private
        self.__age = age     # private


s = Student("Mustafa", 31)

# ❌ This will give error
# print(s.__name)

# ✅ Access using name mangling
print(s._Student__name)
print(s._Student__age)