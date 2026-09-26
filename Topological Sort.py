
from collections import deque

class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(V)]
        indegree = [0] * V

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        result = []

        while q:
            fn = q.popleft()
            result.append(fn)

            for ne in graph[fn]:
                indegree[ne] -= 1

                if indegree[ne] == 0:
                    q.append(ne)

        if len(result) == V:
            return result

        return []