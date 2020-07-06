package p63UniquePathsII;


public class Solution {
    public static void main(String[] args) {
        int[][] c = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};
        new Solution().uniquePathsWithObstacles(c);
    }

    private int get(int[][] a, int i, int j) {
        if (i < 0 || j < 0) {
            return 0;
        }
        return a[i][j];
    }

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid.length == 0 || obstacleGrid[0].length == 0 || obstacleGrid[0][0] == 1) {
            return 0;
        }
        int n = obstacleGrid.length;
        int m = obstacleGrid[0].length;
        int[][] c = new int[n][m];
        c[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }
                if (obstacleGrid[i][j] == 1) {
                    c[i][j] = 0;
                    continue;
                }
                int a = get(c, i - 1, j);
                int b = get(c, i, j - 1);
                c[i][j] = a + b;
            }
        }
        return c[n - 1][m - 1];
    }
}