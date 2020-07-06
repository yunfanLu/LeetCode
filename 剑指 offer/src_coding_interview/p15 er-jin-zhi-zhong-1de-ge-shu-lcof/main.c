int hammingWeight(uint32_t n) {
	int ans;
	ans = 0;
	while(n > 0){
		ans += n % 2;
		n /= 2;
	}   
	return ans;
}