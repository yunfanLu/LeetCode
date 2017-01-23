package p200NumberOfIslands;

public class Solution {
	public int numIslands(char[][] grid) {
		int res = 0;
		if(grid == null || grid.length == 0) return res;
		int l = grid.length;
		int m = grid[0].length;
		for(int i = 0; i < l; i ++){
			for(int j = 0; j < m; j ++){
				if(grid[i][j] == '1') {
					res++;
					dfs(grid, i, j, l, m);
				}
			}
		}
		return res;
	}

	final int[] dx = new int[]{ 0, 1, 0,-1};
	final int[] dy = new int[]{-1, 0, 1, 0};
	private void dfs(char[][] grid, int i, int j, int l, int m) {
		if(i < 0 || i >= l || j < 0 || j >= m) return;
		if(grid[i][j] == '0') return;
		grid[i][j] = '0';
		for(int t = 0; t < 4; t ++){
			dfs(grid, i + dx[t], j + dy[t], l, m);
		}
	}
	public static void main(String[] args) {
		char[][] ch = new char[4][5];
		ch[0] = "11110".toCharArray();
		ch[1] = "10010".toCharArray();
		ch[2] = "10000".toCharArray();
		ch[3] = "01110".toCharArray();
		System.out.println(new Solution().numIslands(ch));
	}
}
