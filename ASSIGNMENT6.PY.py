f_name = [0]*2
l_name = [0]*2
e_adr = [0]*2
def Input_Data():
    global f_name, l_name
    for i in range(len(f_name)):
        fStr = input("Enter the first name: ")
        lStr = input("Enter the last name: ")
        if(fStr.isnumeric() or lStr.isnumeric()):
            print("Invalid input")
            break;
        else:
            f_name[i] = fStr
            l_name[i] = lStr
        if(i < len(f_name)-1):
            flag = input("Press Y for adding more name \nPress N for end \n Choice: ")
        if(flag.lower() == "N"):
            return
def email_id():
    global e_adr
    for i in range(len(e_adr)):
        if( f_name[i] != 0 and l_name[i] != 0):
             e_adr[i] = f_name[i]  +  "."  +  l_name[i]  +"@mycollege.edu"
def email_adr():
   for i in range(len(e_adr)):
        if (e_adr[i] != 0):
            print(e_adr[i])
def main():
    Input_Data()
    email_id()
    email_adr()
main()
