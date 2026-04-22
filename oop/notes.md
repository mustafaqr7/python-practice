# OOP Notes

## Constructor (__init__) Important Note

Common mistake:

```python
class Student:
    def __init___(self, name, age):  # ❌ Wrong (3 underscores)
        self.name = name
        self.age = age


In your file:

```python
class Student:
    # ⚠️ Important:
    # __init__ must have exactly 2 underscores on each side
    # __init___ (3 underscores) will NOT work

    def __init__(self, name, age):
        self.name = name
        self.age = age


## Encapsulation Summary

Encapsulation = Data Hiding + Controlled Access

Types:
- Public
- Protected (_)
- Private (__)

Key:
- Use private variables
- Access via methods (get/set)
- Add validation logic


## Java vs Python – Constructor Behavior (super)

### Java:
- Parent constructor is automatically called
- If not written, compiler inserts:
  super()

### Python:
- Parent constructor is NOT called automatically
- Must explicitly call:
  super().__init__()

### Example:

#### ❌ Without super()
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

d = Dog("Tommy", "Labrador")

# print(d.name) → AttributeError