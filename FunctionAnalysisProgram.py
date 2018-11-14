#Claire Yegian
#11/6/18
#Function Analysis Program

from math import log10, sin

function = input('Enter a function: ')
IntervalBeg = float(input('Enter the begining of the interval: '))
IntervalEnd = float(input('Enter the end of the interval: '))
step = float(input('Enter the step: '))

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
ExtremaList.append(IntervalBeg)
loc = 0
def FindX(loc):
    return(IntervalBeg + (step*(loc)+step*(loc+1))/2)
while loc <= (NumXVals - 2):
    if SlopeList[loc] < 0:
        if SlopeList[loc+1] > 0:
            print('There is a local minimum around x='+ str(FindX(loc)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] < 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] > 0:
        if SlopeList[loc+1] < 0:
            print('There is a local maximum around x='+ str(FindX(loc)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] > 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] == 0:
        if SlopeList[loc+1] > 0:
            print('There is a local minimum around x='+ str(FindX(loc)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] < 0:
            print('There is a local maxiumum around x='+ str(FindX(loc)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] == 0:
            pass
    loc += 1
print('There is an extreme around x='+str(IntervalEnd))
ExtremaList.append(IntervalEnd)

#Finds increasing/decreasing
NumExtrema = len(ExtremaList)
IncDecList = []
if SlopeList[0] > 0:
    Runs = 1
    while Runs <= (NumExtrema-1):
        if Runs%2 != 0:
            IncDecList.append('increasing')
        elif Runs%2 == 0:
            IncDecList.append('decreasing')
        Runs += 1
elif SlopeList[0] < 0:
    Runs = 1
    while Runs <= (NumExtrema-1):
        if Runs%2 != 0:
            IncDecList.append('decreasing')
        elif Runs%2 == 0:
            IncDecList.append('increasing')
        Runs += 1
def IncDecIntervals(IncDecList, ExtremaList):
    IncDecListLen = len(IncDecList)
    index = 0
    while index < (IncDecListLen):
        print('The function is '+IncDecList[index]+' on the interval ['+str(ExtremaList[index])+', '+str(ExtremaList[index+1])+'].')
        index += 1
IncDecIntervals(IncDecList, ExtremaList)

#Takes the second derivative at each x value
SlopeList2 = []
a2 = IntervalBeg + 0.001
while a2 <= IntervalEnd:
    x = a2 + h
    f1 = eval(function)
    x = a2 - h
    f2 = eval(function)
    SymDif = (f1 - f2)/(2*h)
    SlopeList2.append(SymDif)
    a2 += 1
SecondDeriv = []
i = 0
while i < NumXVals:
    slope = (SlopeList2[0]-SlopeList[0])/0.001
    SecondDeriv.append(slope)
    i += 1
print(SlopeList)
print(SlopeList2)
print(SecondDeriv)
print(len(SecondDeriv))

#Finds inflection points
"""Num2DerivVals = len(SecondDeriv)
InflecList = []
k = 0
def Find2DX(k):
    return(IntervalBeg + (step*(k)+step*(k+1))/2)
while k <= (Num2DerivVals - 2):
    if SecondDeriv[k] < 0:
        if SecondDeriv[k+1] > 0:
            InflecList.append(Find2DX(k))
        elif SecondDeriv[k+1] < 0:
            pass
        elif SecondDeriv[k+1] == 0:
            pass
    elif SecondDeriv[k] > 0:
        if SecondDeriv[k+1] < 0:
            InflecList.append(Find2DX(k))
        elif SecondDeriv[k+1] > 0:
            pass
        elif SecondDeriv[k+1] == 0:
            pass
    elif SecondDeriv[k] == 0:
        if SecondDeriv[k+1] > 0:
            InflecList.append(Find2DX(k))
        elif SecondDeriv[k+1] < 0:
            InflecList.append(Find2DX(k))
        elif SecondDeriv[k+1] == 0:
            pass
    k += 1
print(InflecList)"""

    
    
    
    
    
    
    
    