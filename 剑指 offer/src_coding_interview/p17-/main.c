/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int ten_pow(int n){
	int ans = 1;
	int i;
	for(i = 0; i < n; i ++){
		ans *= 10;
	}
	return ans;
}

int* printNumbers(int n, int* returnSize){
	int tp,
	    i;
	tp = ten_pow(n);
	int *ans = (int *)malloc((tp - 1)*(sizeof(int)));
	for(i = 1; i < ten_pow(n); i ++){
		ans[i - 1] = i;
	}
	(* returnSize) = tp - 1;
	return ans;
}