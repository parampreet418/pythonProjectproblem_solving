'''
student = 1
while student<= 3:
    total = 0
    for score in range(1,4):
      score = int(input("Enter test score:"))
      total += score
      average = total/3
      print("Student ", student, "average: ", average)
      student+= 1

def pass_it(x,y):
    z=y**x
    return(z)
num1 = 3
num2 = 4
answer = pass_it(num1,num2)
print(answer)

total = 0
for count in range(4,6):
    total += count
    print(total)

for num in range(0,20,5):
    num += num
print(num)

count = 4
while count < 12:
    print('counting')
    count = count+2

for num in range(0,20,5):
    num += num
print(num)
print('The path is D:\\sample\\test.')
def main():
  print("The answer is", magic(5))
def magic(num):
  answer = num + 2 * 10
  return answer
main()
def pass_it(x, y):
  z = x + ", " + y
  return(z)
name2 = "Tony"
name1 = "Gaddis"
fullname = pass_it(name1, name2)
print(fullname)

def pass_it(x, y):
  z = x , ", " , y
num1 = 4
num2 = 8
answer = pass_it(num1, num2)
print(answer)

print('I\'m rady to begin')
count = 4
while count < 12:
  print("counting")
count = count + 2

value1 = 2.0
value2 = 12
print(value1 * value2)
def pass_it(x, y):
  z = y**x
  return(z)
num1 = 3
num2 = 4
answer = pass_it(num1, num2)
print(answer)
for num in range(4):
'''
even_number=[2,3,4,5]
print(even_number)
even_number[2]=12
print(even_number)
print('the length of list:',len (even_number))
print(f'the first item is{even_number[0]}')
print(f'the last item is{even_number[3]}')

alist2D=[[1,2],[1,2,3,4],[2,3,4,5,6]]
m_liat =['a','b',29,56,True,1.2,[3.4,10,'hesam'],[20,56,'f']]
for item in m_liat:
    print(item.isnumeric())
