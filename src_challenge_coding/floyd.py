
# 每次更新的这个点是放在最外面这个循环的。
def floyd(d, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

