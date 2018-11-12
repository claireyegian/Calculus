#Claire Yegian
#11/6/18
#Function Analysis Program

from math import log10

function = input('Enter a function')
IntervalBeg = float(input('Enter the begining of the interval'))
IntervalEnd = float(input('Enter the end of the interval'))

#FIX VOCAB!!!
tick = input('Enter the distance between ticks')
SymDifXList = []
a = IntervalBeg
h = 0.001
while a <= IntervalEnd:
    x = a + h
    f1 = eval(function)
    x = a - h
    f2 = eval(function)
    SymDif = (f1 - f2)/(2*h)
    print(SymDif)

    SymDifXList.append(SymDif)
    
    

"""x = a + h
f1 = eval(function)
x = a - h
f2 = eval(function)
SymDif = (f1 - f2)/(2*h)
print(SymDif)"""
