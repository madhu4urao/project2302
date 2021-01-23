# Banking System
#parent class user
#Holds details about user
# Has a function to show user details
#child class:bank
#stores details about the account balance
#stores details about the amount
#allows deposits, withdraw and view balance
class User():
    def __init__(self, name, age, gender, ano):
        self.name =name
        self.age =age
        self.gender =gender
        self.Accountno =ano
    def show_details(self):
        print("your account details are")
        print("  ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Account No:", self.Accountno)
# amit =User("amit", 20,"Male",123456789)
# amit.show_details()
class Bank(User):
    def __init__(self, name, age, gender, ano):
        super().__init__(name, age, gender, ano)
        self.balance=0
    def deposit(self, amount):
        self.amount =amount
        self.balance =self.balance+amount
        print("Your Account balance has been updated: Rs", self.balance)

# amit =Bank("amit",20,"Male",123456)
# amit.deposit(10000)
    def withdraw(self, amount):
        self.amount =amount
        if self.amount>self.balance:
            print("insufficient funds in your account:balance available:Rs", self.balance)
        else:
            self.balance =self.balance-self.amount
            print("balance updated is :Rs", self.balance)
    def view_balance(self):
        self.show_details()
        print("Your Account balance has been updated: Rs", self.balance)

amit = Bank("amit", 20, "Male", 123456)
amit.deposit(15000)
amit.withdraw(10000)
amit.view_balance()












