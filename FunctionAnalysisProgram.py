#Claire Yegian
#11/6/18
#Function Analysis Program

from math import log10

"""FuncType = input('What kind of function: ')
Interval = input('Enter the interval: ')

if FuncType == 'polynomial':
    NumTerm = int(input("How many terms does your function have? "))
    r = 1
    while r <= NumTerm:
        print(r)
        r += 1
    Coef1 = int(input("Enter the coefficient of the first term: "))
    Pow1 = int(input("Enter the power of the first term: "))
    Coef2
elif FuncType == 'logorithmic':

function = input('Enter a function')


def getValue(x):
    Locfunction = function.lower()
    y = eval(Locfunction)

    return y"""
a = float(input("coefficient 1: "))
b = int(input("power 1: "))
c = int(input("coefficient 2: "))
d = int(input("power 2: "))

x=3
print(eval('a*(x**b)+c*(x**d)'))
