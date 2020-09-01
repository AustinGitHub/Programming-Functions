def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return round(a/b,4)
def Square(a,b):
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
def Acre2SqM(a):
    return (round(a/640),4)


def ARectangle(a,b):
    return (a*b)
def ASquare(a):
    return (a**2)
def ACircle(a):
    return round(3.145192*(a**2),4)
def AEllipse(a,b):
    return round(3.141592*a*b,4)
def ATriangle(a,b):
    return round(.5*(a*b),3)

def Square4Root(n, i, j): 
    mid = (i + j) / 2; 
    mul = mid * mid; 
    if ((mul == n) or (abs(mul - n) < 0.00001)): 
        return mid; 
    elif (mul < n): 
        return Square4Root(n, mid, j); 
    else: 
        return Square4Root(n, i, mid); 
def SquareRoot(a):
    i = 1; 
    found = False; 
    while(found == False): 
         if (i * i == a): 
            return i
            found = True;       
         elif(i * i > a): 
            res = Square4Root(a, i - 1, i); 
            return round(res,4)
            found = True;
         i += 1;
    











    
