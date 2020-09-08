def AllArrays():
    one = "For all the following functions go to"
    two = "\nhttps://github.com/AustinGitHub/Programming-Functions/wiki/Array-Elements"
    three = "\nRight click and open url"
    return one+two+three
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
    lowest = Highest(a);
    for x in a:
        if(x < lowest):
            lowest = x
    return lowest;