def main():
    while True:
        menu()
        select = input("Select 1,2,3: ")
        if select == '1':
            std_data()
        elif select == '2':
            display()
        elif select == '3':
            record_ID()
        elif select == '4':
            break
        else:
            print('bad input!')

def menu():
    print('Menu:')
    print('Press 1 to Add student data into file')
    print('Press 2 to Print student Record')
    print('Press 3 to print specific student data of particular student id')
    print('Press 4 Exit program')


def std_data():
    stu_data = open('studentinfo.txt', 'a')
    stu_ID = input("Enter the studentID: ")
    stu_data.write(stu_ID + '\n')
    first_Name = input("Enter the firstName: ")
    stu_data.write(first_Name + '\n')
    last_Name = input("Enter the lastName: ")
    stu_data.write(last_Name + '\n')
    major = input("Enter the major: ")
    stu_data.write(major + '\n')
    phone = input("Enter the phone: ")
    stu_data.write(phone + '\n')
    GPA = input("Enter the GPA: ")
    stu_data.write(GPA + '\n')
    dob = input("Enter the date of Birth: ")
    stu_data.write(dob + '\n')
    stu_data.close()


def display():
    stu_data = open('studentinfo.txt', 'r')
    counter = 1
    stu_gpa = 0
    avg_counter = 1
    for data in stu_data:
        print(data.strip('\n'))
        counter = counter + 1
        if counter == 7:
            students_gpa = stu_gpa + str(data.strip('\n'))
            avg_counter = avg_counter + 1

    print("Total GPA", students_gpa)
    print("Average GPA", students_gpa / avg_counter)


def record_ID():
    stu_Id = input("Enter the studentID: ")
    stu_data = open('studentinfo.txt', 'r')
    counter = 0
    for data in stu_data:
        if stu_Id == data.strip('\n'):
            for counter in range(0, 8):
                if counter != 8:
                    print(stu_data.readline().strip('\n'))
        else:
            print("No data found")





main()



