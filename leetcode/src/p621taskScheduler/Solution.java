package p621taskScheduler;

/**
 * Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent
 * different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval,
 * CPU could finish one task or just be idle.
 * However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals
 * that CPU are doing different tasks or just be idle.
 * You need to return the least number of intervals the CPU will take to finish all the given tasks.
 * Example:
 * Input: tasks = ["A","A","A","B","B","B"], n = 2
 * Output: 8
 * Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 *  
 * Note:
 * The number of tasks is in the range [1, 10000].
 * The integer n is in the range [0, 100].
 */


class Solution {
    private int alphabate = 26;

    public static void main(String[] args) {
        char[] tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
        int n = 2;
        System.out.print(new Solution().leastInterval(tasks, n));
    }

    private int select(int[] task, int[] wait) {
        int id = -1;
        for (int i = 0; i < alphabate; i++) {
            if (wait[i] > 0) {
                continue;
            }
            if ((task[i] > 0) && ((id == -1) || (task[i] > task[id]))) {
                id = i;
            }
        }
        return id;
    }

    private int sum(int[] arr) {
        int ans = 0;
        for (int a : arr) {
            ans += a;
        }
        return ans;
    }

    public int leastInterval(char[] tasks, int n) {
        int[] task = new int[alphabate];
        int[] wait = new int[alphabate];
        for (int i = 0; i < alphabate; i++) {
            task[i] = 0;
            wait[i] = 0;
        }
        for (char c : tasks) {
            task[(int) (c - 'A')] += 1;
        }

        int ans = 0;
        int task_count = sum(task);
        while (task_count > 0) {
            int id = select(task, wait);
            for (int i = 0; i < alphabate; i++) {
                if (wait[i] > 0) {
                    wait[i] -= 1;
                }
            }
            if (id >= 0) {
                task_count -= 1;
                task[id] -= 1;
                wait[id] = n;
            }
            ans += 1;
//            if (id >=0){
//                System.out.print(id + ",");
//            }else{
//                System.out.print("#,");
//            }
        }

        return ans;
    }
}