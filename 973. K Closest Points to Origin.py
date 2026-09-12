class Solution(object):
    def kClosest(self, points, k):
        pq = []

        for point in points:
            dis = point[0]**2+point[1]**2
            heapq.heappush(pq,(-dis,point[0],point[1]))
            if len(pq)>k :
                heapq.heappop(pq)
        ans= []
        while pq:
            dis,x,y=heapq.heappop(pq)
            ans.append([x,y])
        return ans

        
        

        