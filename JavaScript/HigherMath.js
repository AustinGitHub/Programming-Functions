function AllMaths(){
return "For all the following functions go to https://github.com/AustinGitHub/Programming-Functions/wiki/Maths";
}
function Add(a,b){
	return a+b;
}
function Subtract(a,b){
	return a-b;
}
function Multiply(a,b){
	return a*b;
}
function Divide(a,b){
	return (a/b).toPrecision(4)
}
function Square(a,b){
	return a**b;
}
function Square4Root(n,i,j){
	var mid = (i + j) / 2; 
    var mul = mid * mid; 
    if ((mul == n) || (abs(mul - n) < 0.00001)){
        return mid; 
    }else if(mul < n){
        return Square4Root(n, mid, j); 
    }else{
        return Square4Root(n, i, mid); 
    }
}
function SquareRoot(a){
	 var i = 1; 
    var found = false; 
    while(found == false){ 
         if (i * i == a){
            return i;
            found = true;       
         }else if(i * i > a){ 
            var res = Square4Root(a, i - 1, i); 
            return (res).toPrecision(4);
            found = true;
        }
         i += 1;
     }
}