double myPow(double x, int n){
	if (n < 0){
		return 1.0 / ((myPow(x, - (n + 1))) * x);
	}
	if (n == 0){
		return 1.0;
	}else if (n == 1){
		return x;
	}else{
		double t = myPow(x, n / 2);
		t *= t;
		if (n % 2 == 0){
			return t;
		}else{
			return t * x;
		}
	}
}