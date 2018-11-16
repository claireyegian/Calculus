#Claire Yegian and Romaney Granizo-Mackenzie
#11/6/18
#Function Analysis Program

from math import sin,cos, tan, acos, asin, atan, e, pi, log, log10, sqrt

function = input('Enter a function: ')
IntervalBeg = float(input('Enter the begining of an interval on which the function is continuous: '))
IntervalEnd = float(input('Enter the end of the interval: '))
step = 0.1
print(' ')




#Takes symmetric difference quotient to calculate the derivative at each designated x value
SlopeList = []
h = 0.001
a = IntervalBeg
while a <= IntervalEnd:
    x = a + h
    f1 = eval(function)
    x = a - h
    f2 = eval(function)
    SymDif = (f1 - f2)/(2*h)
    SlopeList.append(SymDif) #Adds all numerical derivatives to a list so they can be kept track of
    a += step




#Finds extreme values
x = IntervalBeg #Dermines if the first endpoint is a maximum or a minium. If the second y value is higher than the endpoint, it is a min. If the second is lower, it's a max.
y1 = eval(function)
x = IntervalBeg + step
y2 = eval(function)
if y1 > y2:
    print('There is a local maxiumum at x='+str(IntervalBeg))
elif y1 < y2:
    print('There is a local minimum at x='+str(IntervalBeg))

NumXVals = len(SlopeList)
ExtremaList = [IntervalBeg]
yList = [y1]
loc = 0
def FindX(loc):
    return(IntervalBeg + (step*(loc)+step*(loc+1))/2)
while loc <= (NumXVals - 2): #Runs through all of the recorded numerical derivatives
    if SlopeList[loc] < 0: #If the a given numerical derivative is negative, and the next recorded derivative is positive, there is an extreme.
        if SlopeList[loc+1] > 0:
            print('There is a local minimum around x='+ str(round(FindX(loc),4)))
            ExtremaList.append(FindX(loc))
            x = FindX(loc)
            yList.append(eval(function))
        elif SlopeList[loc+1] < 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    elif SlopeList[loc] > 0: #If the a given numerical derivative is positive, and the next recorded derivative is negative, there is an extreme.
        if SlopeList[loc+1] < 0:
            print('There is a local maximum around x='+ str(round(FindX(loc),4)))
            ExtremaList.append(FindX(loc))
            x = FindX(loc)
            yList.append(eval(function))
        elif SlopeList[loc+1] > 0:
            pass
        elif SlopeList[loc+1] == 0:
            pass
    loc += 1

x = IntervalEnd - step #Dermines if the last endpoint is a maximum or a minium. If the y value before it is higher than the endpoint, it is a min. If the y value is lower, it's a max.
y3 = eval(function)
x = IntervalEnd
y4 = eval(function)
if y3 > y4:
    print('There is a local minimum at x='+str(IntervalEnd))
elif y3 < y4:
    print('There is a local maxiumum at x='+str(IntervalEnd))
ExtremaList.append(IntervalEnd)
yList.append(y4)

print('The absolute maxiumum is y='+str(round(max(yList),4))) #Determines the highest and lowest y values in the list of extrema and prints that they are the absolute maxium and minimum.
print('The absolute minimum is y='+str(round(min(yList),4)))




#Finds increasing/decreasing
NumExtrema = len(ExtremaList)
IncDecList = [] #Creates a list of increasing/decreasing intervals
if SlopeList[0] > 0: #If the first numerical derivative is positive, the first object in the list is 'increasing', and then it alternates increasing and decreasing for the remainder of places in the extrema list.
    Runs = 1
    while Runs <= (NumExtrema-1):
        if Runs%2 != 0:
            IncDecList.append('increasing')
        elif Runs%2 == 0:
            IncDecList.append('decreasing')
        Runs += 1
elif SlopeList[0] < 0: #If the first numerical derivative is negative, the first object in the list is 'decreasing', and then it alternates increasing and decreasing for the remainder of places in the extrema list.
    Runs = 1
    while Runs <= (NumExtrema-1):
        if Runs%2 != 0:
            IncDecList.append('decreasing')
        elif Runs%2 == 0:
            IncDecList.append('increasing')
        Runs += 1

def IncDecIntervals(IncDecList, ExtremaList): #This function uses the list created above (alternating increasing and decreasing) and the list of x values for the extrema to print the increasing and decreasing intervals.
    IncDecListLen = len(IncDecList)
    index = 0
    while index < (IncDecListLen):
        print('The function is '+IncDecList[index]+' on the interval ['+str(round(ExtremaList[index],4))+', '+str(round(ExtremaList[index+1],4))+'].')
        index += 1

IncDecIntervals(IncDecList, ExtremaList) #This calls the function above




#Takes the second derivative at each x value
SlopeList2 = [] #This a list of numerical derivatives at each of the x values from the first SlopeList transfered 0.001 units to the right.
a2 = IntervalBeg + 0.001
while a2 <= IntervalEnd: #This loop uses the symetric difference quotient to determine the numerical derivative at each of the adjusted x values.
    x = a2 + h
    f1 = eval(function)
    x = a2 - h
    f2 = eval(function)
    SymDif = (f1 - f2)/(2*h)
    SlopeList2.append(SymDif)
    a2 += step

SecondDeriv = [] #This is a list of the numerical second derivative at each step on the function.
i = 0
while i < (NumXVals-1): #The loop uses (y-y1)/(x-x1) to determine the slope using the symetric difference quotients from SlopeList and SlopeList2 as y values and 0.001 as the difference in x values.
    slope = (SlopeList2[i]-SlopeList[i])/0.001
    SecondDeriv.append(slope)
    i += 1





#Finds inflection points
def Find2DX(k): #This function finds the second derivative x value that coresponds to the number of times that the computer has run through the while loop below.
    return(IntervalBeg + (step*(k)+step*(k+1))/2)

Num2DerivVals = len(SecondDeriv)
InflecList = [] #This a list of the function's inflection points.
k = 0
while k < (Num2DerivVals - 1):
    if SecondDeriv[k] < 0: #If a given numerical second derivative is negative and the following second derivative is positive, the value is added to the list of inflection points.
        if SecondDeriv[k+1] > 0:
            InflecList.append(Find2DX(k))
            print('There is an inflection point at x='+str(round(Find2DX(k),4)))
        elif SecondDeriv[k+1] < 0:
            pass
        elif SecondDeriv[k+1] == 0:
            pass
    elif SecondDeriv[k] > 0: #If a given numerical second derivative is positive and the following second derivative is negative, the value is added to the list of inflection points.
        if SecondDeriv[k+1] < 0:
            InflecList.append(Find2DX(k))
            print('There is an inflection point at x='+str(round(Find2DX(k),4)))
        elif SecondDeriv[k+1] > 0:
            pass
        elif SecondDeriv[k+1] == 0:
            pass
    k += 1

if len(InflecList) == 0: #If there are no values added to the list of inflection points, the function has no inflection points.
    print('There are no points of inflection')





#Finds concave up/concave down
NumInflec = len(InflecList)
if NumInflec != 0: #If there are inflection points, the following if statements determine concavity.
    ConUpDownList = [] #This creates a list similar to the increasing/decreasing one that records alternating intervals of concavity.
    if SecondDeriv[0] > 0: #If the first numerical second derivative value is positive, than the next interval will be negative, the next positive, and so on.
        Runs = 1
        while Runs <= (NumInflec-1):
            if Runs%2 != 0:
                ConUpDownList.append('concave up')
            elif Runs%2 == 0:
                ConUpDownList.append('concave down')
            Runs += 1
    elif SecondDeriv[0] < 0: #If the first numerical second derivative value is negative, than the next interval will be positive, the next negative, and so on.
        Runs = 1
        while Runs <= (NumInflec-1):
            if Runs%2 != 0:
                ConUpDownList.append('concave up')
            elif Runs%2 == 0:
                ConUpDownList.append('concave down')
            Runs += 1
    
    def ConIntervals(ConUpDownList, InflecList): #This function takes the concavity list and the list of inflection points as arguments and prints a statement of the intervals on which the function is concave up or concave down.
        CUDLLen = len(ConUpDownList)
        index = 0
        while index < (CUDLLen):
            print('The function is '+ConUpDownList[index]+' on the interval ['+str(round(InflecList[index],4))+', '+str(round(InflecList[index+1],4))+'].')
            index += 1
    
    if SecondDeriv[0] > 0: #If the first numerical second derivative is positive, then the first interval will be concave up.
        print('The function is concave up on the interval ['+str(round(IntervalBeg,4))+','+str(round(InflecList[0],4))+'].')
    elif SecondDeriv[0] < 0: #If the first numerical second derivative is negative, then the first interval will be concave down.
        print('The function is concave down on the interval ['+str(round(IntervalBeg,4))+','+str(round(InflecList[0],4))+'].')
    
    ConIntervals(ConUpDownList, InflecList) #This calls the function above.
    
    if SecondDeriv[-1] > 0: #If the last numerical second derivative is positive, then the last interval is concave up.
        print('The function is concave up on the interval ['+str(round(InflecList[-1],4))+','+str(round(IntervalEnd,4))+'].')
    elif SecondDeriv[-1] < 0: #If the last numerical second derivative is negative, then the last interval is concave down.
        print('The function is concave down on the interval ['+str(round(InflecList[-1],4))+','+str(round(IntervalEnd,4))+'].')
elif NumInflec == 0: #If there are no inflection points, the following if statements decide concavity.
    if SecondDeriv[0] > 0: #If the first numerical second derivative is positive,
        print('The function is concave up on the interval ['+str(round(IntervalBeg,4))+','+str(round(IntervalEnd,4))+'].')
    elif SecondDeriv[0] < 0:
        print('The function is concave down on the interval ['+str(round(IntervalBeg,4))+','+str(round(IntervalEnd,4))+'].')
    elif SecondDeriv[0] == 0:
        print('The function has no concavity.')











