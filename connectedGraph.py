class Solution:
    def countConnected(self, V, edges):

        # Create adjacency list
        graph = [[] for _ in range(V)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V
        count = 0

        def dfs(node):
            visited[node] = True

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        # Find every disconnected component
        for i in range(V):
            if not visited[i]:
                count += 1
                dfs(i)

        return count