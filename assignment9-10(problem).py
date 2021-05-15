'''driver_name = []
license_number = []
ticket_number = []


def output_data():
    global driver_name
    global license_number
    global ticket_number
    fileObject = open('detail.txt', 'r')
    line = fileObject.readlines()
    for a in line:

        data = a.split(",")
        driver_name.append(data[0])
        license_number.append(data[1])
        ticket_number.append(data[2])
    fileObject.close()


def printDetails():
    user = input("Enter license number")
    flag = False
    for i in range(len(license_number)):
        if (license_number[i] == user):
            print("Name :", driver_name[i], " Ticket :", ticket_number[i])
            flag = True
            break
    if flag is not True:
        print("License number not found.")

def main():
    output_data()
    printDetails()

main()

'''
