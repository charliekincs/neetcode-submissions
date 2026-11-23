class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                up_nei = obstacleGrid[i - 1][j]
                left_nei = obstacleGrid[i][j - 1]
                if up_nei != 1 and left_nei != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif up_nei != 1 and left_nei == 1:
                    dp[i][j] = dp[i - 1][j] 
                elif up_nei == 1 and left_nei != 1:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]


                    
                