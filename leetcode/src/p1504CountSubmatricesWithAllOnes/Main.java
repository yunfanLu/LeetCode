package p1504CountSubmatricesWithAllOnes;


class Solution {
    private void print_2d_array(int[][] a, int i, int j, int p, int q) {
        for (int x = i; i <= p; i++) {
            for (int y = j; j <= q; j++) {
                System.out.print(a[x][y] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    private void print_2d_array(int[][] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private int get(int[][] a, int i, int j) {
        if (i < 0 || j < 0) {
            return 0;
        }
        return a[i][j];
    }

    public int numSubmat(int[][] mat) {
        if (mat.length == 0 || mat[0].length == 0) {
            return 0;
        }
        int n = mat.length;
        int m = mat[0].length;
        int[][] sum = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0) {
                    sum[i][j] = mat[i][j];
                } else if (i == 0) {
                    sum[i][j] = sum[i][j - 1] + mat[i][j];
                } else if (j == 0) {
                    sum[i][j] = sum[i - 1][j] + mat[i][j];
                } else {
                    sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + mat[i][j];
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int p = i; p < n; p++) {
                    for (int q = j; q < m; q++) {
                        if (mat[p][q] == 0) {
                            break;
                        }
                        int pq = get(sum, p, q);
                        int pj1 = get(sum, p, j - 1);
                        int i1q = get(sum, i - 1, q);
                        int i1j1 = get(sum, i - 1, j - 1);
                        if (pq + i1j1 - pj1 - i1q == (p - i + 1) * (q - j + 1)) {
                            ans += 1;
                        }
                    }
                }
            }
        }
        return ans;
    }
}

public class Main {
    public static void main(String[] args){
        Solution s = new Solution();
        int[][] a = {
            {1,0,1},
            {1,1,0},
            {1,1,0},
        };
        System.out.println(s.numSubmat(a));
    }
}
