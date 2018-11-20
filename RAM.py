#Claire Yegian
#11/19/18
#RAM program - calculates LRAM, RRAM, and MRAM for an interval of a function

function = input('Enter your function: ')
IntervalBeg = float(input('Enter the begining of your interval: '))
IntervalEnd = float(input('Enter the end of your interval: '))
Width = float(input('Enter the width of the rectangles: '))

LRAM = 0
XVal =  IntervalBeg
while XVal < IntervalEnd:
    x = XVal
    y = eval(function)
    LRAM += y*Width
    XVal += Width
print('LRAM=' + str(LRAM))

RRAM = 0
XVal1 =  IntervalEnd
while XVal1 > IntervalBeg:
    x = XVal1
    y = eval(function)
    RRAM += y*Width
    XVal1 -= Width
print('RRAM=' + str(RRAM))

MRAM = 0
XVal2 =  IntervalBeg + (0.5*Width)
while XVal2 < IntervalEnd:
    x = XVal2
    y = eval(function)
    MRAM += y*Width
    XVal2 += Width
print('MRAM=' + str(MRAM))
