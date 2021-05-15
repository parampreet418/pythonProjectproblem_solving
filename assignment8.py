import random
def Name():
    name = input("Enter Student Name: ")
    return name

def getNum():
    num1 = random.randrange(1, 500)
    num2 = random.randrange(1, 500)
    return num1, num2

def getAns(num1, num2, ans):
    print("What is the answer to the following equation")
    print(str(num1) + "\n+\n" + str(num2))
    print("What is the sum", sep=': ')
    ans = int(input())
    return ans

def checkAns(num1, num2, ans, right):
    if ans == num1 + num2:
        print("Right")
        right = right + 1
    else:
        print("Wrong")
    return right

def res(right, avgRight):
    avgRight = right / 10
    return avgRight

def infoDisplay(right, avgRight, stdName):
    print("Information for student: " + stdName)
    print("The number right: " + str(right))
    print("The average right is " + str(avgRight) + " or " + str(avgRight * 100) + " %")

def main():
    c = 0
    stdName = "NO NAME"
    avgRight = 0.0
    right = 0
    num1 = 0
    num2 = 0
    ans = 0
    stdName = Name()

    while c < 10:
        num1, num2 = getNum()
        ans = getAns(num1, num2, ans)
        right = checkAns(num1, num2, ans, right)
        c = c + 1
    avgRight = res(right, avgRight)
    infoDisplay(right, avgRight, stdName)

main()