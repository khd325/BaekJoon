import sys

sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if graph[x][y] == 0:
        return False

    else:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx,ny)
        return True



for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1

    print(count)
