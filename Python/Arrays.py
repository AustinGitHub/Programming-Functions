def AddAll(a):
    total = 0
    for x in a:
        total += x
    return total
def Highest(a):
    highest = 0;
    for x in a:
        if(x > highest):
            highest = x
    return highest;
def Lowest(a):
    lowest = 0;
    for x in a:
        if(x < lowest):
            lowest = x
    return lowest;