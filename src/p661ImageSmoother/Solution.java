import java.util.Arrays;

class Solution {
    public int[][] imageSmoother(int[][] M) {
        if(M.length == 0) return null;
        if(M[0].length == 0) return new int[M.length][0];
        int L = M.length;
        int R = M[0].length;
        int[][] res = new int[L][R];
        for(int i = 0; i < L; i ++){
            for(int j = 0; j < R; j ++){
                int countN = 0;
                int countV = 0;
                for(int r = -1; r <= 1; r ++){
                    for(int k = -1; k <= 1; k ++){
                        int tx = i + r;
                        int ty = j + k;
                        if( tx >= 0 && tx < L && ty >= 0 && ty < R){
                            countN ++;
                            countV += M[tx][ty];
                        }
                    }
                }
                res[i][j] = countV / countN;
            }
        }
        return res;
    }
    public static void main(String[] args) {
        int[][] M = new int[][]{
            {1,1,1},
            {1,0,1},
        };
        int[][] res = new Solution().imageSmoother(M);
        for(int i = 0; i < res.length; i ++){
            for(int j = 0; j < res[0].length; j ++){
                System.out.print(res[i][j] + " ");
            }
            System.out.println();
        }
    }
}