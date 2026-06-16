print("========== Classes Course Start ===========")


class Cat:
    # constructor:
    def __init__(self, name, owner, temperament="Loving"):
        self.name = name
        self.owner = owner
        self.temperament = temperament

    def __str__(self):
        return f"Cat: name = {self.name}, owner is {self.owner}, and its temperament is {self.temperament}"

    def __repr__(self):
        return f"Cat('{self.name}', '{self.owner}', '{self.temperament}')"

    def speak(self):
        print(f'{self.name} says: "Meow"')

    def eat(self, food):
        print(f'{self.name} takes a bite out of {food}!')


cat1 = Cat("Shadow", "Mark")
cat2 = Cat("Spot", "John", "Shy")
# cat1 = Cat.__init__(cat1)

print(cat1)
cat2.name = "Ouroborus"
print(cat2)
cat2.speak()
cat2.eat(cat1)

cats = [cat1, cat2]
print(cats)

stray_cats = [Cat('Shadow', 'Mark', 'Loving'), Cat('Ouroborus', 'John', 'Shy')]

print(stray_cats)
# cat1.name = "Shadow"
# cat2.name = "Spot"
# cat1.owner = "Mark"

# str(10) -> "10"

print("====== Complex functionality  ======")


class BankAccount:
    bank = "ING"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has {self.balance} EURO"

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds!")
        else:
            self.balance = self.balance - amount


acc1 = BankAccount("Adrian", 10)
# acc1.balance = acc1.balance + 100
acc1.deposit(200)
acc1.withdraw(300)
print(acc1)

acc2 = BankAccount("Mark", 3000)
print(acc2)

acc1.bank = "BNR"

print(acc1.bank)
print(acc2.bank)


# creati o clasa Rectangle care are doua atribute interne, x si y. initiati-le din constructor.
# creati doua metode, area() si perimeter() care calculeaza aria si perimetrul acelui Rectangle, si returneaza acea valoare., folosind formulele:
# area: x * y
# perimeter: 2 * x + 2 * y


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return self.x * 2 + self.y * 2


# https://peps.python.org/pep-0008/