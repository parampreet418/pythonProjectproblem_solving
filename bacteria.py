def main():
    InputData()
def InputData():
    BacteriaPresent = input("Enter the number of bacteria present at the beginning: ")
    if BacteriaPresent > 0:
        BacteriaPresent = int(BacteriaPresent)
    else:
        print("The input that you entered is invalid.")
        exit()
    calculateBacteria(BacteriaPresent)
def calculateBacteria(BacteriaCount):
    global res
    count = 1
    print("Day" + "         " + "Number of bacteria")
    while count <= 10:
        res = BacteriaCount * 2 ^ count
        print(f'{count}          {res}')
        count = count+1
main()



