
creditLeft = int(input('creditLeft:'))
creditTaken = int(input('creditTaken'))
student_name = input('Student name is:')
degreeProgram = input('degreeProgram is:')
print('The student name is', student_name)
print('The degree program is', degreeProgram)
creditDegree = float(input('credit Degree:'))
print('Enter the number of credits taken so far:', creditDegree)
creditLeft = float(creditTaken-creditDegree)
print('The creditLeft is', creditLeft)
print("The student name is:", student_name,"This program requires" , creditDegree , "credits and they have taken ", creditTaken , "so far")