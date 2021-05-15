'''class car:
    pass
c1=car()
c2=car()
c3=car()

print(hex(c1.__hash__()))
print(c1.__str__()) #__str__ its string representation of object
print('__str()__',c1.__str__())
print(c1)
print(c2)
print(c3)


class car:
    def __init__(self):
        self.colour = "red"
        self.manifact = "Lexus"
        self.price = 67000
        self.type = "SUV"


c1 = car()
c2 = car()
c3 = car()
print(c1.price)
print(c2.price)
class bankAccount:
    def __init__(self,balance,acc_holder,acc_number,type):
        self.balance =balance
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.type = type

    def withdraw(selfself,amount):


        def __str__(self):
            return f'Account-> Acc #:{self.acc_number},Acc holder:{self.acc_holder},'\
                    f'type:{self.type}, Balance:{self.balance}'


class BankAccount(object):
    pass


acc1 = BankAccount(1000,"parampreet",10,"checking")
print(acc1)
print(acc2)t
acc1.deposit(2000)
print(acc1)
acc1.withdraw(5000)
print(acc1)
#Lists to store the three columns
names = []
ids = []
tickets = []
with open("licenses.txt") as f:
    while True:
        line = f.readline()
        if not line:# end of file
            break
        
        name, id, ticket = [a.strip() for a in line.split(',')] 
        names.append(name)
        ids.append(id)
        tickets.append(int(ticket)) 

print("Enter license number")
s = input().strip() #ID to search

found = False 
for i in range(len(ids)):
    if s == ids[i]: 
        print("Name :", names[i], " Tickets :", tickets[i]) #Corresponding name and tickets
        found = True #Set flag
        break
if not found: 
    print("License number not found.")
Screenshot:

#Q1 #Lists to store the three columns names [] ids = [] tickets = [] with open(licenses.txt) as f: while True: line f.readl

Input (licenses.txt)

Monica Geller, D79347284, 1
Chandler Bing, D97254836, 4
Ross Geller, D57898765, 0
Phoebe Buffay, D07513445, 3
Joseph Tribianni, D29473644, 5
Rachel Green, D16735274, 19
Output:
Enter license number D29473644 Name : Joseph Tribianni Tickets : 18

Question 2

Code:

#Q2
total = 0 #stores total amount
with open("transactions.txt") as f:
    while True:
        line = f.readline() #read line by line
        if not line: #end of file
            break
        # Split line of commas, remove whitespaces
        _, _, _, amt = [a.strip() for a in line.split(',')] 
        amt = amt[1:] #ignore the $ sign
        amt = float(amt) #convert to float for addition
        total += amt #Total sum

print("Total amount spent: $" + str(round(total, 2)))
Input: (transactions.txt)

15/1/2021, Best Buy, TV, $1200.54
20/1/2021, Costco, Chair, $220.37
Screenshot:
#Q2 total = #stores total amount with open(transactions.txt) as f: while True: line = f.readline() #read line by line if no

Output :

Total amount spent: $1420.91
def main():
    abc()
    a()

def abc():
    total = 0
    option = 'yes'
    with open('tran.txt','w') as f:
        while option =='yes':
             date = input(f'Enter the date ')
             f.write(date+',')
             company = input(f'Enter the company Name ')
             f.write(company+',')
             product = input(f'Enter the Product ')
             f.write(product+',')
             amt = input(f'Enter the amount ')
             f.write(amt + '\n')
             option=input("u want to continue enter y for yes and n for no")
    f.close()

def a():
    with open("tran.txt") as f:
      while True:
        line = f.readline()
        if not line:
            break

        _, _, _, amt = [a.strip() for a in line.split(',')]
        amt = amt[1:]
        amt = float(amt)
        total = total + amt
        print(total)

main()'''
def add_user(user_db):

    uname = input('Please enter a username: ')

    while uname in user_db:
        uname = input('That username is already taken, please choose another: ')
    password = input("Please enter a password: ")
    user_db[uname] = password
    print('Added!')



def login(user_db):
    uname = input('Enter your username: ')
    if uname not in user_db:
        uname = input('Invalid username so try it again.')
        if uname not in user_db:
            print('Invalid data! please contact to your admin.')
            return
    for i in range(3):
        password = input("Enter your password: ")
        if user_db[uname] == password:
            print('Login successfully!')
            return
        else:
            print('Invalid password!')
    print('Temporarily blocked. Please try afterwards or contact to your admin.')



def main():
    user_db = {'param': "123", 'hesam': "1102", 'gagan': '2345', 'john': "a123", 'joe': '453'}
    print('Database:', user_db)
    print('Please add three new users:')
    add_user(user_db)
    print('Database:', user_db)
    add_user(user_db)
    print('Database:', user_db)
    add_user(user_db)
    print('Database:', user_db)
    # simulating login of three users
    print('Please logging-in two users to verify:')
    login(user_db)
    login(user_db)
    print('Database:', user_db)


main()