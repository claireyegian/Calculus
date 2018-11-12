#Claire Yegian
#11/6/18
#Function Analysis Program

from math import log10

function = input('Enter a function')
IntervalBeg = float(input('Enter the begining of the interval'))
IntervalEnd = float(input('Enter the end of the interval'))

#FIX VOCAB!!!
tick = float(input('Enter the distance between ticks'))

#Takes symmetric difference quotient to take the derivative at each designated x value
SlopeList = []
h = 0.001
a = IntervalBeg
while a <= IntervalEnd:
    x = a + h
    f1 = eval(function)
    x = a - h
    f2 = eval(function)
    SymDif = (f1 - f2)/(2*h)
    SlopeList.append(SymDif)
    a += tick

#Finds extreme values
NumXVals = len(SlopeList)
loc = 0
while loc <= (NumXVals - 2):
    if SlopeList[loc+1] =! 0:
        Quotient = SlopeList[loc]/SlopeList[loc+1]
        if Quotient > 0:
            pass
        elif Quotient <= 0:
            print('There is an extreme around x='+ str(IntervalBeg + (tick*(loc)+tick*(loc+1))/2))
    loc += 1

"""x = a + h
f1 = eval(function)
x = a - h
f2 = eval(function)
SymDif = (f1 - f2)/(2*h)
print(SymDif)"""
