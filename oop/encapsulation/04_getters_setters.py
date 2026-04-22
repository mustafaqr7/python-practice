class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    # Getter → read value
    def get_balance(self):
        return self.__balance

    # Setter → update value with control
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount")


acc = BankAccount(1000)

print(acc.get_balance())   # 1000

acc.set_balance(2000)
print(acc.get_balance())   # 2000

acc.set_balance(-500)      # invalid case