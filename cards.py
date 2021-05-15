import random
clubs = 1
diamonds = 1
hearts = 1
spades = 1
def calc():
    global clubs
    global diamonds
    global hearts
    global spades
    for i in range(0,1000) :
        num = random.randrange(1,53)
        if(0 < num <= 13):
            clubs = clubs+1
        elif(13 < num <= 26):
            diamonds = diamonds + 1
        elif(26 < num <= 39):
            hearts = hearts + 1
        else:
            spades = spades + 1
def Output_result():
    print("Display the number of times each suit occurred in the 1,000 deals are as follows:- ")
    print(f'1.              {clubs}')
    print(f'2.              {diamonds}')
    print(f'3.              {hearts}')
    print(f'4.              {spades}')
def cards():
    calc()
    Output_result()
cards()