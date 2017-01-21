package p005LongestPalindromicSubstring;

import java.util.Scanner;

class Manacher {
	private char[] Ma ;
	private int[] Mp ;
	
	public Manacher(String str) {
		int len = str.length() ;
		Ma = new char[len * 2 + 3] ;
		Mp = new int[len * 2 + 3] ;
		run(str.toCharArray() , len) ;
	}

	private void run(char[] s, int len) {
		int l = 0 ;
		Ma[l++] = '$' ;
		Ma[l++] = '#' ;
		for(int i = 0 ; i < len ; i ++){
			Ma[l++] = s[i] ;
			Ma[l++] = '#' ;
		}
		int mx = 0 , id = 0 ;
		for(int i = 0 ; i < l ; i ++){
			Mp[i] = mx > i ? Math.min( Mp[2 * id - i], mx - i ) : 1 ;
			while( i >= Mp[i] && Ma[i + Mp[i]] == Ma[i - Mp[i]]) {
				Mp[i] ++ ;
			}
			if(i + Mp[i] > mx){
				mx = i + Mp[i] ;
				id = i ;
			}
		}
	}

	private int[] getMp(){
		return Mp;
	}

	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in) ;
		String s = cin.next() ;
		Manacher manacher = new Manacher(s) ;
		int[] r = manacher.getMp() ;
		int ans = 0 ;
		for(int i = 0 ; i < r.length ; i ++){
			ans = Math.max(ans, r[i] - 1) ;
		}
		System.out.println(ans);
		cin.close();
	}
}

public class Solution {
    public String longestPalindrome(String s) {
    	String res = "";
    	
    	return res;
    }
}
