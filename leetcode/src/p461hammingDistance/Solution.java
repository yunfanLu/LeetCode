package p461hammingDistance;

class Solution {
    public int hammingDistance(int x, int y) {
//        int ans = 0;
//        while (x > 0 || y > 0) {
//            if (x % 2 != y % 2) {
//                ans++;
//            }
//            x /= 2;
//            y /= 2;
//        }
//        return ans;
        return Integer.bitCount(x ^ y);
    }

    public static void main(String[] args){
        System.out.println(new Solution().hammingDistance(1,4));
    }
}