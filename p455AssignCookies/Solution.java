import java.util.Arrays;


public class Solution{
    public static void main(String[] args) {
        int[] g = new int[]{1, 2};
        int[] s = new int[]{1, 2, 3};
        int ans = new Solution().findContentChildren(g,s);
        System.out.println(ans);
    }
    public int findContentChildren(int[] g, int[] s) {
        int res = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        int ind_s = 0;
        for(int i = 0; i < g.length;){
            if(ind_s >= s.length){
                break;
            }
            if(g[i] <= s[ind_s]){
                i ++;
            }
            res = i;
            ind_s ++;
        }
        return res;
    }
}