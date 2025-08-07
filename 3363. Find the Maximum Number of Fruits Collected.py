"""

3363. Find the Maximum Number of Fruits Collected
https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected

"""

fmax = lambda x, y: x if x > y else y


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        INF = 10**20

        diagonal = 0
        for i in range(N):
            diagonal += fruits[i][i]
            fruits[i][i] = -INF
        fruits[N - 1][N - 1] = 0

        dp = [[-INF] * N for _ in range(N)]
        dp[0][N - 1] = fruits[0][N - 1]
        for i in range(1, N):
            for j in range(N):
                for dj in [-1, 0, 1]:
                    if 0 <= j + dj < N:
                        dp[i][j] = fmax(dp[i - 1][j + dj] + fruits[i][j], dp[i][j])
        besta = dp[N - 1][N - 1]

        dp = [[-INF] * N for _ in range(N)]
        dp[N - 1][0] = fruits[N - 1][0]
        for j in range(1, N):
            for i in range(N):
                for di in [-1, 0, 1]:
                    if 0 <= i + di < N:
                        dp[i][j] = fmax(dp[i][j], dp[i + di][j - 1] + fruits[i][j])
        bestb = dp[N - 1][N - 1]

        return diagonal + besta + bestb
