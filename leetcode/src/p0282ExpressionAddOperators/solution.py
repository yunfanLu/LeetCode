class Solution:
    def addOperators(self, num, target):
        def dfs(ops):
            res = []
            for op in ops:
                res.append(op + ['-'])
                res.append(op + ['+'])
                res.append(op + ['*'])
                res.append(op + [''])
            return res

        def check(ops, num):
            s = ''
            for i in range(0, len(num) - 1):
                if num[i] == '0' and ops[i] == '':
                    return None, None
                s += num[i]
                s += ops[i]
            s += num[-1]
            return eval(s), s

        ops = [['-'], ['+'], ['*'], ['']]
        for i in range(1, len(num) - 1, 1):
            ops = dfs(ops)
        ans = []
        for op in ops:
            r, s = check(op, num)
            if r == target:
                ans.append(s)
        return ans

if __name__ == '__main__':
    print(Solution().addOperators("123456789", 45))