def inputResult():
    global OrderTotal
    OrderTotal = float(input("Enter the Total amount:$"))
def performCalculation():
    global ShipWithinUSA, ShipToCanada
    if OrderTotal <= 0:
        print("Amount can not be zero or negative")
    elif(OrderTotal <= 50 ):
        ShipWithinUSA = 6.00
        ShipToCanada = 8.00
    elif(50.01 <= OrderTotal <= 100.00):
        ShipWithinUSA = 9.00
        ShipToCanada = 12.00
    elif(100.01 < OrderTotal <= 150.00):
        ShipWithinUSA = 12.00
        ShipToCanada = 15.00
    else:
        ShipWithinUSA = "Free"
        ShipToCanada = "Free"
def outputResult():
        if OrderTotal > 0:
            print("The ship cost within USA is" ,ShipWithinUSA)
            print("The ship cost to Canada is" , ShipToCanada)
def main():
    inputResult()
    performCalculation()
    outputResult()
main()