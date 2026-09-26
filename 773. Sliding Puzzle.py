from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        start = ""
        for row in board:
            for num in row:
                start+=str(num)
        target = "123450"

        queue = deque()
        queue.append((start,0))
        visited = set()

        directions = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [1,3,5],
            [2,4],
        ]
        while queue:
            config,moves = queue.popleft()

            if config in visited:
                continue
            visited.add(config)

            if config == target:
                return moves
            zeroidx = config.index('0')

            for newidx in directions[zeroidx]:
                newconfig = list(config)
                temp = newconfig[newidx]
                newconfig[newidx] = newconfig[zeroidx]
                newconfig[zeroidx] = temp

                newst = "".join(newconfig)
                if newst not in visited:
                    queue.append((newst,moves+1))
        return -1

            



        