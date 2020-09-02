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
def SqK2SqM(a):
    return round(a/2.59,4)
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

def Km2Yard(a):
    return a*1093.61
def Km2Meter(a):
    return a*1000
def Km2Cm(a):
    return a*100000
def Km2mm(a):
    return a*1000000
def Km2Microm(a):
    return a*1000000000
def Km2Nm(a):
    return a*1000000000000
def Km2Mile(a):
    return round(a/1.609,5)
def Km2Ft(a):
    return a*3280.84
def Km2In(a):
    return a*39370
def Km2NauMile(a):
    return round(a/1.852,5)

def MetTon2kg(a):
    return a*1000
def MetTon2g(a):
    return a*1000000
def MetTon2mg(a):
    return a*1000000000
def MetTon2Microg(a):
    return a*1000000000000
def MetTon2ImpTon(a):
    return round(a/1.016,4)
def MetTon2UsTon(a):
    return round(a*1.102,4)
def MetTon2Stone(a):
    return round(a*157.46,4)
def MetTon2lb(a):
    return round(a*2205,4)
def MetTon2oz(a):
    return a*35274

def Kg2MetTon(a):
    return round(a/1000,5)
def Kg2g(a):
    return a*1000
def Kg2mg(a):
    return a*1000000
def Kg2Microg(a):
    return a*1000000000
def Kg2ImpTon(a):
    return round(a/1016,5)
def Kg2UsTon(a):
    return round(a/907,5)
def Kg2Stone(a):
    return round(a/6.35,4)
def Kg2lb(a):
    return round(a*2.205,4)
def Kg2oz(a):
    return round(a*35.274,4)

def Gram2MetTon(a):
    return a/1000000
def Gram2kg(a):
    return a/1000
def Gram2mg(a):
    return a*1000
def Gram2Microg(a):
    return a*1000000
def Gram2ImpTon(a):
    return a/1016046.91
def Gram2UsTon(a):
    return a/907185
def Gram2Stone(a):
    return round(a/6350,8)
def Gram2lb(a):
    return round(a/454,6)
def Gram2oz(a):
    return round(a/28.35,5)

def Miph2Kph(a):
    return round(a*1.609,4)
def Miph2Mps(a):
    return round(a/2.237,4)
def Miph2Knot(a):
    return round(a/1.151,4)
def Miph2Fps(a):
    return round(a*1.467,4)

def Mps2Miph(a):
    return round(a*2.237,4)
def Mps2Knot(a):
    return round(a*1.944,4)
def Mps2Fps(a):
    return round(a*3.281,4)
def Mps2Kph(a):
    return round(a*3.6,4)

def Knot2Mps(a):
    return round(a/1.944,4)
def Knot2Fps(a):
    return round(a*1.688,4)
def Knot2Miph(a):
    return round(a*1.151,4)
def Knot2Kph(a):
    return round(a*1.852,4)

def Fps2Knot(a):
    return round(a/1.688,4)
def Fps2Miph(a):
    return round(a/1.467,4)
def Fps2Mps(a):
    return round(a/3.281,4)
def Fps2Kph(a):
    return round(a*1.097,4)

def Kph2Knot(a):
    return round(a/1.852,4)
def Kph2Miph(a):
    return round(a/1.609,4)
def Kph2Mps(a):
    return round(a/3.6,4)
def Kph2Fps(a):
    return round(a/1.097,4)

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