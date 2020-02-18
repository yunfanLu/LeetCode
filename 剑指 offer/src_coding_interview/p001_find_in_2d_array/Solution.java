/**
 * 题目描述
 * 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
 * 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 * 例如
 * [
 * [1,2,3,4],
 * [2,3,4,5],
 * [3,4,5,6],
 * [6,7,8,9]
 * ]
 */
public class Solution {
    public boolean Find(int target, int[][] array) {
        if (array == null || array.length == 0 || array[0].length == 0) {
            return false;
        }
        int h = array.length;
        int w = array[0].length;
        return _find_in_2d_array(array, target, 0, 0, h - 1, w - 1);
    }

    private boolean findIn2DArray(int[][] array, int target, int x1, int y1, int x2, int y2) {
        int x = (x1 + x2) / 2;
        int y = (y1 + y2) / 2;
        if ((x > x2) || (y > y2)) {
            return false;
        }
        if (array[x][y] == target) {
            return true;
        }
        if ((x1 == x2) && (y1 == y2)) {
            return false;
        }
        if (array[x][y] > target) {
            return findIn2DArray(array, target, 0, 0, x - 1, y) ||
                    findIn2DArray(array, target, x - 1, 0, x, y - 1)
        }
    }
}