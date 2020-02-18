package p1086HighFive;

//1086. 前五科的均分
//用户通过次数 162
//用户尝试次数 166
//通过次数 162
//提交次数 243
//题目难度 Easy
//给你一个不同学生的分数列表，请按 学生的 id 顺序 返回每个学生 最高的五科 成绩的 平均分。
//
//对于每条 items[i] 记录， items[i][0] 为学生的 id，items[i][1] 为学生的分数。平均分请采用整数除法计算。
//
//
//
//示例：
//
//输入：[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
//输出：[[1,87],[2,88]]
//解释：
//id = 1 的学生平均分为 87。
//id = 2 的学生平均分为 88.6。但由于整数除法的缘故，平均分会被转换为 88。
//
//
//提示：
//
//1 <= items.length <= 1000
//items[i].length == 2
//学生的 ID 在 1 到 1000 之间
//学生的分数在 1 到 100 之间
//每个学生至少有五个分数

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Solution {

    public int[][] highFive(int[][] items) {
        TreeMap<Integer, List<Integer>> map = new TreeMap<>();
        for (int i = 0; i < items.length; i ++){
            int key = items[i][0];
            int val = items[i][1];
            if (map.containsKey(key)){
                map.get(key).add(val);
            }else{
                List<Integer> l = new ArrayList<>();
                l.add(val);
                map.put(key, l);
            }
        }

        int[][] ans = new int[map.keySet().size()][2];
        for (Map.Entry<Integer, List<Integer>> it: map.entrySet()){
            it.getValue().sort(Integer::compareTo);
            int count = 0;
            for(int i =0; i < 5; i ++) {
                count += it.getValue().get(it.getValue().size() - i - 1);
            }
            ans[it.getKey() - 1][0] = it.getKey();
            ans[it.getKey() - 1][1] = count / 5;
        }
        return ans;
    }


}
