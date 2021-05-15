class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return True

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return True
    def getName(self):
        return self.owner

    def getBalance(self):
        return self.balance


class MoneyMarketAccount(BankAccount):
    def __init__(self, owner, balance, numWithdraws):
        self.owner = owner
        self.balance = balance
        self.numWithdraws = numWithdraws


class CDAccount(BankAccount):
    def __init__(self, owner, balance, interestRate):
        self.owner = owner
        self.balance = balance
        self.interestRate = interestRate

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("You are getting money with " + str(self.interestRate) + "% interest rate.")
        print("So, your withdrawal amount is: " + str(amount * (self.interestRate + 100) / 100))
        return True



cust1 = MoneyMarketAccount("Hesam", 10000, 1)
print("The account balance of " + str(cust1.getName()) + " is: " + str(cust1.getBalance()))
if cust1.withdraw(100):
    print("Withdraw is successful")
    print("The account balance of " + str(cust1.getName()) + " after this withdrawal is: " + str(cust1.getBalance()))
else:
    print("Sorry! Withdraw is unsuccessful")


cust2 = CDAccount("Param", 20000, 1)
print("\nThe account balance of " + str(cust2.getName()) + " is: " + str(cust2.getBalance()))
if cust2.withdraw(200):
    print("Withdraw is successful")
    print("The account balance of " + str(cust2.getName()) + " after this withdrawal is: " + str(cust2.getBalance()))
else:
    print("Sorry! Withdraw is unsuccessful")


if cust1.deposit(5000):
    print("\nDeposit is successful")
    print("The account balance of " + str(cust1.getName()) + " after this deposit is: " + str(cust1.getBalance()))
else:
    print("Sorry! Deposit is unsuccessful")


if cust2.deposit(8000):
    print("\nDeposit is successful")
    print("The account balance of " + str(cust2.getName()) + " after this deposit is: " + str(cust2.getBalance()))
else:
    print("Sorry! Deposit is unsuccessful")