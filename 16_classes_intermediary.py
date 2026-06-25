
# interiorul clasei
class BankAccount:
    bank = "ING"

    def __init__(self, owner, balance=0):
        self.owner = owner
        # proprietate privata.
        self.__balance = balance
        self.number_of_deposits = 0

    # getter:
    @property
    def balance(self):
        return self.__balance

    # setter:
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.number_of_deposits += 1
            self.__balance = value

    def __str__(self):
        return f"{self.owner} has {self.__balance} EURO"

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough funds!")
        else:
            self.__balance = self.__balance - amount

    @staticmethod
    def is_valid_amount(amount):
        # isinstance() checks if "amount" is of type "int" or "float".
        if not isinstance(amount, bool) and isinstance(amount, (int, float)) and amount > 0:
            return True
        else:
            return False

    @classmethod
    def construct_from_string(cls, account_data):
        # account_data = "John:300"
        # cls = BankAccount
        # obj1 = BankAccount() -> echivalent!
        # owner receives account_data.split(':')[0] and amount receives account_data.split(':')[1]
        owner, amount = account_data.split(":")
        obj1 = cls(owner, int(amount))
        return obj1

# @staticmethod. O metoda care are legatura cu conturi bancare, dar nu are legatura cu un cont anume sau informatii dintr-un "self" anume
# @classmethod. O metoda care opereaza pe clasa, si are o actiune la nivel de clasa.


# exteriorul clasei.
ing1 = BankAccount("adrian")
print(ing1)
print(ing1.balance)
# syntactic sugar.
ing1.balance += 300
ing1.balance += 600
ing1.balance += 900

new_amount = 1
print(BankAccount.is_valid_amount(new_amount))

print(ing1.number_of_deposits)
print(ing1.balance)

print(isinstance(True, float))

# __balance is a private property, cannot be accessed from the outside of the class.
# print(ing1.__balance)

v1 = BankAccount
print(v1)
