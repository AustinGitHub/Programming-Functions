function AllTemperature(){
	return "For all the following functions go to https://github.com/AustinGitHub/Programming-Functions/wiki/Temperature-Conversion";
}

function F2C(a){
	return ((a-32)*5/9).toPrecision(3);
}
function C2F(a){
	return ((a*9/5)+32).toPrecision(3);
}
function C2K(a){
	return ((a+273.15)).toPrecision(3);
}
function F2K(a){
	return ((a-32)*5/9+273.15).toPrecision(3);
}
function K2C(a){
	return ((a-273.15)).toPrecision(3);
}
function K2F(a){
	return ((a-273.15)*9/5+32).toPrecision(3);
}