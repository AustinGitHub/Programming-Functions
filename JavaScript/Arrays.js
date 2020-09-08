function AllArrays(){
	return "For all the following functions go to https://github.com/AustinGitHub/Programming-Functions/wiki/Array-Elements";
}
function AddAll(a){
	var total = 0;
	for(var x=0;x<a.length;x++){
		total += a[x];
	}
	
	return total;
}
function Highest(a){
	var Highest = 0;
	for(var x=0;x<a.length;x++){
		if(a[x] > Highest){
			Highest = a[x];
		}
	}
	return Highest;
}
function Lowest(a){
	var Lowest = Highest(a);
	for(var x=0;x<a.length;x++){
		if(a[x] < Lowest){
			Lowest = a[x];
		}
	}
	return Lowest;

}