class Solution {

    private int gao(int n, int m){
        int a = n / m;
        int b = n % m;
        int ans = 1;
        for(int i = 0; i < b; i ++){
            ans *= a + 1;
        }
        for(int i = 0; i < m - b; i ++){
            ans *= a;
        }
        return ans;
    }

    private int max(int a, int b){
        return a > b ? a : b;
    }

    public int cuttingRope(int n) {
        int ans = -1;
        for(int i = 2; i <= n; i ++){
            ans = max(ans, gao(n, i));
        }
        return ans;
    }
}
