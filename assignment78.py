def calc_price():
    global totalprice
    totalprice = 0
    if (item == 1):
        itemprice = (.99 * itemcount) * 6 / 100
    if (item == 2):
        itemprice = (.79 * itemcount) * 6 / 100
    if (item == 3):
        itemprice = (1.09 * itemcount) * 6 / 100
    totalprice = totalprice + itemprice
    print("The total price of items are $ ", totalprice)

def main():
    global item, itemcount
    item = int(input("Enter 1 for Yum Yum Burger \n Enter 2 for Grease Yum Fries \n Enter 3 for Soda Yum \n Enter now -"))
    itemcount = int(input("Enter the total number of burgers you want: "))
    result = str(input("Enter YES if you want to end your order,otherwise NO): "))
    if (result == "YES"):
        calc_price()

def menu():
       global item
       itemcount = 0

main()
menu()