package p1087BraceExpansion;

/*
我们用一个特殊的字符串 S 来表示一份单词列表，之所以能展开成为一个列表，是因为这个字符串 S 中存在一个叫做「选项」的概念：

单词中的每个字母可能只有一个选项或存在多个备选项。如果只有一个选项，那么该字母按原样表示。

如果存在多个选项，就会以花括号包裹来表示这些选项（使它们与其他字母分隔开），例如 "{a,b,c}" 表示 ["a", "b", "c"]。

例子："{a,b,c}d{e,f}" 可以表示单词列表 ["ade", "adf", "bde", "bdf", "cde", "cdf"]。

请你按字典顺序，返回所有以这种方式形成的单词。



示例 1：

输入："{a,b}c{d,e}f"
输出：["acdf","acef","bcdf","bcef"]
示例 2：

输入："abcd"
输出：["abcd"]


提示：

1 <= S.length <= 50
你可以假设题目中不存在嵌套的花括号
在一对连续的花括号（开花括号与闭花括号）之间的所有字母都不会相同
 */

import java.util.ArrayList;
import java.util.List;

public class Soultion {

    private List<String> comp(String s){
        List<String> ans =  new ArrayList<>();
        for (int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);
            if(c == ','){
                continue;
            }else{
                ans.add("" + c);
            }
        }
        return ans;
    }

    public String[] permute(String S) {
        List<List<String>> ls = new ArrayList<>();
        for (int i = 0; i < S.length(); i ++){
            if (S.charAt(i) == '{'){
                int start = i;
                int end = i + 1;
                for (; end < S.length(); end ++){
                    if (S.charAt(end) == '}'){
                        break;
                    }
                }
                String ss = S.substring(start + 1, end);
                ls.add(comp(ss));
            }
        }

//        TODO
        return null;
    }
}
