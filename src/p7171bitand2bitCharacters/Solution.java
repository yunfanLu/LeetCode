package p7171bitand2bitCharacters;

public class Solution {
    public static void main(String[] args) {
        Solution slt = new Solution();
        System.out.println(slt.isOneBitCharacter(
                new int[]{1,1,1,1,1,1,1}
        ));
    }

    public boolean isOneBitCharacter(int[] bits) {
        if(bits == null || bits.length == 0){
            return false;
        }
        for (int i = 0; i < bits.length; ) {
            if (bits[i] == 1) {
                i += 2;
            } else {
                if (i == bits.length - 1) {
                    return true;
                }
                i += 1;
            }
        }
        return false;
    }
}