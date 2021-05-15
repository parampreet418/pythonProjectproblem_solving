import random
clubs = 0
diamonds = 0
hearts = 0
spades = 0
def main():
    generateRandom()
    printResult()

def generateRandom():
            spades += 1

    global clubs
    global diamonds
    global hearts
    global spades
    for i in range(0,1000) :
        num = random.randrange(1,53)
        if(0 < num <= 13):
            clubs = clubs+1
        elif(13 < num <= 26):
            diamonds += 1
        elif(26 < num <= 39):
            hearts += 1
        else:

def printResult():

    print(f'a. Clubs         {clubs}')
    print(f'b. Diamonds      {diamonds}')
    print(f'c. Hearts        {hearts}')
    print(f'd. Spades        {spades}')

main()