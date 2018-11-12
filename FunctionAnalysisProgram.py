#Claire Yegian
#11/6/18
#Function Analysis Program

from math import log10

function = input('Enter a function')
IntervalBeg = float(input('Enter the begining of the interval'))
IntervalEnd = float(input('Enter the end of the interval'))

#FIX VOCAB!!!
tick = input('Enter the distance between ticks')
TickList = []
a = IntervalBeg
while a <= IntervalEnd:
    
a = 2
h = 0.001
x = a + h
f1 = eval(function)
x = a - h
f2 = eval(function)
SymDif = (f1 - f2)/(2*h)
print(SymDif)
