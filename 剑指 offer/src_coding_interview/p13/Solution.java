class Solution {
    private int bitSum(int n){
        int ans = 0;
        while(n > 0){
            ans += n % 10;
            n /= 10;
        }
        return ans;
    }
    private int[] dx = {0, 0, 1, -1};
    private int[] dy = {1, -1, 0, 0};
    
    private void dfs(boolean[][] used, int x, int y, int m, int n, int k){
        if (used[x][y] == false){
            used[x][y] = true;
            for(int i = 0; i < 4; i ++){
                int tx = dx[i] + x;
                int ty = dy[i] + y;
                if(tx >= 0 && tx < m && ty >= 0 && ty < n && used[tx][ty] == false){
                    if(bitSum(tx) + bitSum(ty) <= k){
                        dfs(used, tx, ty, m, n, k);
                    }
                }
            }
        }
    }

    public int movingCount(int m, int n, int k) {
        boolean[][] used = new boolean[m][n];
        for(int i = 0; i < m; i ++) for(int j = 0; j < n; j ++) used[i][j] = false;
        dfs(used, 0, 0, m, n, k);
        int ans = 0;
        for(int i = 0; i < m; i ++) for(int j = 0; j < n; j ++) if (used[i][j]) ans ++;
        return ans;
    }
}