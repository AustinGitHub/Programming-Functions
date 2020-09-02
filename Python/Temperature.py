def AllTemperature():
	one = "For all the following functions go to"
	two = "\nhttps://github.com/AustinGitHub/Programming-Functions/wiki/Temperature-Conversion"
	three = "\nRight click and open url"
	return one+two+three

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