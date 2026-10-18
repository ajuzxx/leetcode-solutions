
class Solution:
    def memo(self, sr, sc, dr, dc, arr, dp):
        if sr > dr or sc > dc:
            return 0

        if arr[sr][sc] == 1:
            return 0

        if sr == dr and sc == dc:
            return 1

        if dp[sr][sc] != -1:
            return dp[sr][sc]

        rightway = self.memo(sr, sc + 1, dr, dc, arr, dp)
        downway = self.memo(sr + 1, sc, dr, dc, arr, dp)

        dp[sr][sc] = rightway + downway
        return dp[sr][sc]

    def uniquePathsWithObstacles(self, obstacleGrid):
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[r-1][c-1] == 1:
            return 0

        dp = [[-1] * c for _ in range(r)]

        return self.memo(0, 0, r-1, c-1, obstacleGrid, dp)
