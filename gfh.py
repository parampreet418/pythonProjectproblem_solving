def main():
    InputData()
    res()
def InputData():
    number = input("Enter any positive number: ")
    calcFactorial(number)


def calcFactorial(number):
    global Factorial
    Factorial = 1
    num = 1
    if number < 0:
        print("The number that you entered is invalid.")
    elif number == 0:
        print("The factorial of number 0 is 1. ")
    else:
       while num <= number:
        Factorial = Factorial * num
        number = num + 1
def res():
    print(f' Factorial of the number is  { Factorial }')
main()
