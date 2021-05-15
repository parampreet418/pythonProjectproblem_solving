def main():
    abc()
    a()

def abc():
    total = 0
    option = 'yes'
    with open('text.txt','w') as f:
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
    with open("text.txt") as f:
      while True:
        line = f.readline()
        if not line:
            break

        _, _, _, amt = [a.strip() for a in line.split(',')]
        amt = amt[1:]
        amt = float(amt)
        total = total + amt
        print(total)

main()