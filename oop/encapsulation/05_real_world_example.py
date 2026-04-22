class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private

    # Getter
    def get_salary(self):
        return self.__salary

    # Method to increase salary
    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Invalid increment")

    # Method to decrease salary
    def decrease_salary(self, amount):
        if 0 < amount < self.__salary:
            self.__salary -= amount
        else:
            print("Invalid deduction")


emp = Employee("Mustafa", 5000)

print(emp.get_salary())   # 5000

emp.increase_salary(1000)
print(emp.get_salary())   # 6000

emp.decrease_salary(2000)
print(emp.get_salary())   # 4000

emp.decrease_salary(10000)  # invalid case