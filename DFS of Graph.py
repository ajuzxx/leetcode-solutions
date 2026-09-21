class Solution:
    def dfsofgraph(self,node, adj,visited,result):
        visited[node] = True
        result.append(node)
        
        for neighbour in adj[node]:
                    if not visited[neighbour]:
                        self.dfsofgraph(neighbour, adj, visited, result)
    def dfs(self,adj):
        v = len(adj)
        visited = [False]*v
        result = []
        
        self.dfsofgraph(0,adj,visited,result)
        return result
        
