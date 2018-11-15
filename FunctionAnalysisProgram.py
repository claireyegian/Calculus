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
            print('There is a local minimum around x='+ str(round(FindX(loc),4)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] < 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] > 0:
        if SlopeList[loc+1] < 0:
            print('There is a local maximum around x='+ str(round(FindX(loc),4)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] > 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] == 0:
        if SlopeList[loc+1] > 0:
            print('There is a local minimum around x='+ str(round(FindX(loc),4)))
            ExtremaList.append(FindX(loc))
        elif SlopeList[loc+1] < 0:
            print('There is a local maxiumum around x='+ str(round(FindX(loc),4)))
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
        print('The function is '+IncDecList[index]+' on the interval ['+str(round(ExtremaList[index],4))+', '+str(round(ExtremaList[index+1],4))+'].')
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
    a2 += step
SecondDeriv = []
i = 0
while i < (NumXVals-1):
    slope = (SlopeList2[i]-SlopeList[i])/0.001
    SecondDeriv.append(slope)
    i += 1

#Finds inflection points
def Find2DX(k):
    return(IntervalBeg + (step*(k)+step*(k+1))/2)
Num2DerivVals = len(SecondDeriv)
InflecList = []
k = 0
while k < (Num2DerivVals - 1):
    if SecondDeriv[k] < 0:
        if SecondDeriv[k+1] > 0:
            InflecList.append(Find2DX(k))
            print('There is an inflection point at x='+str(round(Find2DX(k),4)))
        elif SecondDeriv[k+1] < 0:
            pass
        elif SecondDeriv[k+1] == 0:
            pass
    elif SecondDeriv[k] > 0:
        if SecondDeriv[k+1] < 0:
            InflecList.append(Find2DX(k))
            print('There is an inflection point at x='+str(round(Find2DX(k),4)))
        elif SecondDeriv[k+1] > 0:
            pass
        elif SecondDeriv[k+1] == 0:
            pass
    elif SecondDeriv[k] == 0:
        if SecondDeriv[k+1] > 0:
            InflecList.append(Find2DX(k))
            print('There is an inflection point at x='+str(round(Find2DX(k),4)))
        elif SecondDeriv[k+1] < 0:
            InflecList.append(Find2DX(k))
            print('There is an inflection point at x='+str(round(Find2DX(k),4)))
        elif SecondDeriv[k+1] == 0:
            pass
    k += 1

print(SecondDeriv)

#Finds concave up/concave down
NumInflec = len(InflecList)
ConUpDownList = []
if SecondDeriv[0] > 0:
    Runs = 1
    while Runs <= (NumInflec-1):
        if Runs%2 != 0:
            ConUpDownList.append('concave up')
        elif Runs%2 == 0:
            ConUpDownList.append('concave down')
        Runs += 1
elif SecondDeriv[0] < 0:
    Runs = 1
    while Runs <= (NumInflec-1):
        if Runs%2 != 0:
            ConUpDownList.append('concave up')
        elif Runs%2 == 0:
            ConUpDownList.append('concave down')
        Runs += 1
if SecondDeriv[0] > 0:
    print('!!!The function is concave up on the interval ['+str(round(IntervalBeg,4))+','+str(round(InflecList[0],4))+'].')
elif SecondDeriv[0] > 0:
    print('!!!The function is concave down on the interval ['+str(round(IntervalBeg,4))+','+str(round(InflecList[0],4))+'].')
def ConIntervals(ConUpDownList, InflecList):
    CUDLLen = len(ConUpDownList)
    index = 0
    while index < (CUDLLen):
        print('The function is '+ConUpDownList[index]+' on the interval ['+str(round(InflecList[index],4))+', '+str(round(InflecList[index+1],4))+'].')
        index += 1
ConIntervals(ConUpDownList, InflecList)
if SecondDeriv[-1] > 0:
    print('!!!The function is concave up on the interval ['+str(round(InflecList[-1],4))+','+str(round(IntervalEnd,4))+'].')
elif SecondDeriv[-1] < 0:
    print('!!!The function is concave down on the interval ['+str(round(InflecList[-1],4))+','+str(round(IntervalEnd,4))+'].')
    
    
    
    
    
    