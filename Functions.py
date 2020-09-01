def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return a/b
def SquareRoot(a,b):
    return a**b
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
def F2C(a):
    return round((a-32)*5/9,3)
def C2F(a):
    return round((a * 9/5)+32,3)
def C2K(a):
    return round((a+273.15),3)
def F2K(a):
    return round((a-32)*5/9+273.15,3)
def K2C(a):
    return round((a-273.15),3)
def K2F(a):
    return round((a-273.15)*9/5+32,3)
def SqK2SqM(a):
    return round(a/2.59,4)















    
