package p1079LetterTilePossibilities;


import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        System.out.println(new Solution().numTilePossibilities("AAB"));
        System.out.println(new Solution().numTilePossibilities("AAABBC"));
    }


    private int dfs(int[] map){
        int res = 0;
        for (int i = 0; i < map.length; i ++){
            if(map[i] >= 1){
                map[i] -= 1;
                res += dfs(map);
                map[i] += 1;
            }
        }
        return res;
    }

    public int numTilePossibilities(String tiles) {

        int[] map = new int[26];
        for (int i = 0; i < tiles.length(); i ++){
            map[tiles.charAt(i) - 'A'] += 1;
        }

        return dfs(map);
    }
}