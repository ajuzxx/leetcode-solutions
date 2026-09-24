from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        row = len(mat)
        col = len(mat[0])
        q = deque()
        visited = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    visited[i][j]= True
        direction = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        while q:
            
            i,j,distance =  q.popleft()
            for di,dj in direction:
                ni = i+di
                nj = j+dj

                if (0 <= ni < row and
                    0 <= nj < col and
                    not visited[ni][nj]):

                    visited[ni][nj] = True

                    mat[ni][nj] = distance + 1

                    q.append((ni, nj, distance + 1))

        return mat

        

        