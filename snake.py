
        # code here
class Solution:

    def mazePath_helper(self, sr, sc, dr, dc, cans, fans, arr):
        if sr > dr or sc > dc or sr < 0 or sc < 0 or arr[sr][sc] == 0:
            return

        if sr == dr and sc == dc:
            fans.append(cans)
            return

            # VIS
        arr[sr][sc] = 0

            # Recursive calls
        self.mazePath_helper(sr + 1, sc, dr, dc, cans + "D", fans, arr)
        self.mazePath_helper(sr, sc - 1, dr, dc, cans + "L", fans, arr)
        self.mazePath_helper(sr, sc + 1, dr, dc, cans + "R", fans, arr)
        self.mazePath_helper(sr - 1, sc, dr, dc, cans + "U", fans, arr)


            # UNVIS
        arr[sr][sc] = 1

    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        fans = []

        sr = 0
        sc = 0

        dr = len(maze) - 1
        dc = len(maze[0]) - 1

        self.mazePath_helper(sr, sc, dr, dc, "", fans, maze)

        return fans