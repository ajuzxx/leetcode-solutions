import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        # Step 1: Create an empty adjacency list for V nodes
        adj = [[] for _ in range(V)]
        
        # Step 2: Convert the edges list into an undirected adjacency list
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # Step 3: Set all initial distances to infinity, and start node to 0
        dist = [float('inf')] * V
        dist[src] = 0
        
        # Step 4: Create the priority queue with (distance, node)
        pq = [(0, src)]
        
        # Step 5: Process nodes until the queue is empty
        while pq:
            d, u = heapq.heappop(pq)
            
            # Step 6: Ignore outdated distance values
            if d > dist[u]:
                continue
                
            # Step 7: Check all connected neighbors of node u
            for v, weight in adj[u]:
                # Step 8: Update distance if a shorter path is found
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
                    
        # Step 9: Return the final shortest distances
        return dist