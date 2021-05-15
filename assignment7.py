def calc_price():
    global totalprice
    totalprice = 0
    if(item == 1):
        itemprice = (.99 * itemcount) * 6 / 100

    if (item == 2):
        itemprice = (.79 * itemcount) * 6 / 100

    if (item == 3):
        itemprice = (1.09 * itemcount) * 6 / 100
    totalprice = totalprice + itemprice
    print("The total price of items are $ ", totalprice)

def menu():
    global item, itemcount
    item = int(input("Enter 1 for Yum Yum Burger")
    item = int(input("Enter 2 for Grease Yum Fries"))
    item = int(input("Enter 3 for Soda Yum"))
    item = input("Enter now -")
    itemcount = int(input("Enter the number of burgers you want"))
    result = input("Do you want to end your order? (Enter YES or NO)")
    if (result == "YES"):
        calc_price()

def menu_item_reset():
        item, itemcount = 0
menu()