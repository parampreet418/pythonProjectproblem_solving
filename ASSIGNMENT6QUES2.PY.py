def insert_data():
    global Item_Name, Cost, Number_in_Stock
    Item_Name = []
    Cost = []
    Number_in_Stock = []
    choice = "y"
    while choice == 'y':
        Item_Name.append(input("Enter the item: "))
        Cost.append(input("Enter the cost of item: "))
        Number_in_Stock.append(input("Enter the quantity of item: "))
        choice = input("Enter y for adding more data \nPress any key to exit \n Choice: ")

def display_data():
    print("Item_Name     Cost      Number_in_Stock")
    for i in range(len(Item_Name)):
        print(f'{Item_Name[i]}         {Cost[i]}         {Number_in_Stock[i]}')

def main():
   insert_data()
   display_data()

main()