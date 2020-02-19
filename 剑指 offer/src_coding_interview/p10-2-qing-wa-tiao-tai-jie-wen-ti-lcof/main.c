int numWays(int n){
	int *a = (int *)malloc((n + 1) * sizeof(int));
	int i,
		ans;

	a[1] = 1;
	a[2] = 2;
	for(i = 3; i <= n; i ++){
		a[i] = a[i - 1] + a[i - 2];
	}
	ans = a[n];
	free(a);
	a = NULL;
	return ans;
}