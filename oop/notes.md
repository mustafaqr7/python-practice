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