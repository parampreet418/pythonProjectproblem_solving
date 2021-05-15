square = []
def calcSquareroot():
  for i in range(0,100):
    square.append(i * i)
  print(square)
def searchSquareroot():
    guess = int(input("Enter the number to check square root: "))
    for i in range(len(square)):
        if(guess == square[i]):
            print(f'Number {guess} is perfect square.')
            break
def main():
    calcSquareroot()
    searchSquareroot()
main()