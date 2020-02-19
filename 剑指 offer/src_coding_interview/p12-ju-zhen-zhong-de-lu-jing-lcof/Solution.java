class Solution {
    public boolean exist(char[][] board, String word) {
    	if(board == null || board.length == 0 || board[0].length == 0 || word.length() == 0){
    		return false;
    	}

 		int w = board.length;
 		int h = board[0].length;
 		boolean[][] used = new boolean[w][h];


 		for (int i = 0; i < w; i ++){
 			for (int j = 0; j < h; j ++){
 				if(board[i][j] == word.charAt(0)){
 					init_bool_mat(used);
 					if (dfs(board, w, h, i, j, word, 0, used)){
 						return true;
 					}
 				}
 			}
 		}   
 		return false;
    }

    private void init_bool_mat(boolean[][] b){
    	for(int i = 0; i < b.length; i ++){
    		for(int j = 0; j < b[0].length; j ++){
    			b[i][j] = true;
    		}
    	}
    }

    private int[] dx = new int[]{1, 0, -1, 0};
    private int[] dy = new int[]{0, 1, 0, -1};

    private boolean dfs(char[][] board, int w, int h, int i, int j, String word, int ind, boolean[][] used){
    	if (board[i][j] == word.charAt(ind)){
    		if (ind == word.length() - 1){
    			return true;
    		}
    		used[i][j] = false;
    		for(int k = 0; k < 4; k ++){
    			int tx = i + dx[k];
    			int ty = j + dy[k];
    			if (tx >= 0 && tx < w && ty >= 0 && ty < h && used[tx][ty] == true){
    				if (dfs(board, w, h, tx, ty, word, ind + 1, used)){
    					return true;
    				}
    			}
    		}
    		used[i][j] = true;
    		return false;
    	}else{
    		return false;
    	}
    }
}














