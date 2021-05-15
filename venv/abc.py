import math
def input_value():
    global A, B
    A = float(input("Enter the value of A:"))
    B = float(input("Enter the value of B:"))
def calc():
    global X1, X2
    if not A == 0:

        if B / A < 0:
            X1 = math.sqrt(-B / A)
            X2 = -(math.sqrt(-B / A))
            print(A*X1**2 + B)
            print(A * X2 ** 2 + B)
        if B / A == 0:
            X1, X2 = 0
            print(A * X1 ** 2 + B)
            print(A * X2 ** 2 + B)
        if B / A > 0:
            print("This equation has no real number solutions.")
    else:
        exit()
def main():
    input_value()
    calc()
main()