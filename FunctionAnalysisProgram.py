#Claire Yegian
#11/6/18
#Function Analysis Program

from math import log10, sin

function = input('Enter a function')
IntervalBeg = float(input('Enter the begining of the interval'))
IntervalEnd = float(input('Enter the end of the interval'))

#FIX VOCAB!!!
step = float(input('Enter the step'))

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
    a += step

#Finds extreme values
NumXVals = len(SlopeList)
ExtremaList = []
print('There is an extreme around x='+str(IntervalBeg))
loc = 0
while loc <= (NumXVals - 2):
    if SlopeList[loc] < 0:
        if SlopeList[loc+1] > 0:
            print('There is a local maxiumum around x='+ str(SlopeList[loc]))
        elif SlopeList[loc+1] < 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] > 0:
        if SlopeList[loc+1] < 0:
            print('max')
        elif SlopeList[loc+1] > 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] == 0:
        if SlopeList[loc+1] > 0:
            print('min')
        elif SlopeList[loc+1] < 0:
            print('max')
        elif SlopeList[loc+1] == 0:
            pass
    """if SlopeList[loc+1] != 0:
        Quotient = SlopeList[loc]/SlopeList[loc+1]
        if Quotient > 0:
            pass
        elif Quotient <= 0:
            Extrema = (IntervalBeg + (step*(loc)+step*(loc+1))/2)
            ExtremaList.append(Extrema)
            print('There is an extreme around x='+ str(Extrema))"""
    loc += 1
print('There is an extreme around x='+str(IntervalEnd))

#Finds increasing/decreasing
if SlopeList[0] > 0:
    pass