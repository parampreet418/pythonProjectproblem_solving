class Car:
    def __init__(self, model, company, price, size):
        self.__model = model
        self.__company = company
        self.__price = price
        self.__size = size

    def str(self):
        info = ''
        info += 'Model Name : ' + self.__model + '\n'
        info += 'Company : ' + self.__company + '\n'
        info += 'Price : ' + str(self.__price) + '\n'
        info += 'Size :' + str(self.__size) + '\n'
        return info

    def discount(self, percent: float) -> float:
        return (1 - percent / 100) * self.__price


L1 = Car(
    model='k-10',
    company='Honda',
    price=51560,
    size=148.3
)

L2 = Car(
    model='Vdi',
    company='Maruti Sazuki',
    price=442600,
    size=285
)

L3 = Car(
    model='Go',
    company='Hyundi',
    price=745030,
    size=531.3
)
L4 = Car(
    model='Zdi',
    company='Toyota',
    price=1040050,
    size=569.4
)

print(L1.str())
print(L2.str())
print(L3.str())
print(L4.str())
