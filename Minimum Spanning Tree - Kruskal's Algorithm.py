from typing import List

class Solution:
    def find(self,parent,x):
        if parent[x] != x:
            parent[x] = self.find(parent,parent[x])
            
        return parent[x]
        
    def union(self,parent,rank,a,b) :
        rootA = self.find(parent,a)
        rootB = self.find(parent,b)
        if rootA == rootB:
            return False
        
        
        if rank[rootA]>rank[rootB]:
            parent[rootB]=rootA
        elif rank[rootA]<rank[rootB]:
            parent[rootA]=rootB
        else :
            parent[rootB]=rootA
            rank[rootA]+=1
        return True
            
        
        
        
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        edges.sort(key = lambda x:x[2])
        parent = [i for i in range(V)]
        rank = [1]*V
        
        totalWeight = 0
        edges_used = 0
        
        for u,v,weight in edges:
            if self.union(parent,rank,u,v):
                totalWeight+=weight
                edges_used +=1
            if edges_used == V-1:
                break
        return totalWeight
            
        
        
        
        
        
        
        
        
        