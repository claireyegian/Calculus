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
print(LRAM)