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
    


