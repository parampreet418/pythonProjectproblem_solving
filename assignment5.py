def input_Marks():
    global quiz, ass, test1, test2
    quiz = float(input("Quiz overall marks out of 100: "))
    ass = float(input("Assignment overall mark out of 100: "))
    test1 = float(input("Test 1 mark out of 100: "))
    test2 = float(input("Test 2 mark out of 100: "))


def cal_Grade():
    final_Grade = (quiz * 0.2) + (ass * 0.2) + (test1 * 0.3) + (test2 * 0.3)

    if final_Grade >= 94 and final_Grade <= 100:
        print("Your grade point is 4.0 , Your grade is A+")
    elif final_Grade >= 87 and final_Grade <= 93:
        print("Your grade point is 3.7, Your grade is A")
    elif final_Grade >= 80 and final_Grade <= 86:
        print("Your grade point is 3.5, Your grade is A-")
    elif final_Grade >= 77 and final_Grade <= 79:
        print("Your grade point is 3.2, Your grade is B+")
    elif final_Grade >= 73 and final_Grade <= 76:
        print("Your grade point is 3.0, Your grade is B")
    elif final_Grade >= 70 and final_Grade <= 72:
        print("Your grade point is 2.7, Your grade is B-")
    elif final_Grade >= 67 and final_Grade <= 69:
        print("Your grade point is 2.3, Your grade is C+")
    elif final_Grade >= 63 and final_Grade <= 66:
        print("Your grade point is 2.0, Your grade is C")
    elif final_Grade >= 60 and final_Grade <= 62:
        print("Your grade point is 1.7, Your grade is C-")
    elif final_Grade >= 50 and final_Grade <= 59:
        print("Your grade point is 1.0, Your grade is D")
    elif final_Grade >= 0 and final_Grade <= 49:
        print("Your grade point is 0.0, Your grade is F")
    else:
        print("Bad input")


def main():
    input_Marks()
    cal_Grade()
main()