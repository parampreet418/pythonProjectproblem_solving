'''a = 4
b = 2
c = a+b
#c = a*b
#c = a**b
#a = a**b
print(a)
name = input("What is your name?:")
last_name = input("What is your last name:")
print(input)
full_name = input(name + ' ' + last_name)
print(' full_name')
age = input("tell me your age i'll double it")
print(age*2)

num1 = float(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
num3 = int(input('Enter the third number:'))
avg = float(num1 + num2 + num3)/ 3   #use// for int res even use float
print(f'The average number is {avg:.2f}')

def message():
    print('1')
    print('2')
    print('3')
print('4')
message()
print('5')
print('-------')
value = 15
print(value*2)


def collect_3inputs():
      global num1, num2 , num3
      num1= int(input('Enter the first number:'))
      num2 = int(input('Enter the second number:'))
      num3 = int(input('Enter the third number:'))
def cal_sum():
      result = num1+num2+num3
      return result
def cal_avg():
      avg = cal_sum/3
def display_results():
      print(f'the sum of{num1},{num2},{num3} is {cal_sum()}')
      print(f'the averagee sum is{cal_avg}')
def main():
    collect_3inputs()
 # summ=cal_sum[data0],[data1],[data2]   avg=cal_avg(summ)
    display_results()
main()
'''
'''''
a=5
b=6
c= a==b
print(c)
age = int(input("age: "))
height = int(input('height:'))
ans = (age == 27  or height > 185)
print(ans)
'''''
''''
a = int(input("enter no:"))
b = int(input("enter n0:"))
if a > b:
    print(f'{a} is bigger than {b}')
else:
    print(f'{b} is bigger then {a}')
    if a < b:
        print(f'{a} is not bigger than {b}')
    else:
        print(f'{a} is smaller than {b}')
'''''
'''''
for i in [45,0,1,2,3]:
    print("A")
for i in range(10,20):
    print('B',i)
'''''

for i in range(10,101,-10):
    print('C',i)
#------------------------------------
import random
print('---------------random library-------------------')
for i in range(20):
    num = random.randint(1,5)
    print('num')
    n1 = random.randrange(0,100,10)
    print('n1')
    float_num = random.randint(4,6) + random.random()
    print('float_num')
    float_num = random.randrange(4,40,10) + random.random()
    print('float_num')