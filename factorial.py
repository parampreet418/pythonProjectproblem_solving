def main():
    InputData()
    res()
def InputData():
    number = int(input("Enter any positive number: "))
    if int(number) > 0:
        number = int(number)
        calcFactorial(number)
    else:
        print("The number that you entered is invalid.")
        exit()
#abcd------------2345
def calcFactorial(number):
    global Factorial
    Factorial = 1
    while number > 0:
        Factorial = Factorial * number
        number = number - 1
def res():
    print(f' Factorial of the number is  { Factorial }')
main()
