from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegre = [0]*numCourses
        for s,e in prerequisites:
            graph[e].append(s)
            indegre[s]+=1
        q = deque()
        for i in range(numCourses):
            if indegre[i]==0:
                q.append(i)
        ans = []

        while q:
            fn = q.popleft()
            ans.append(fn)

            for n in graph[fn]:
                indegre[n]-=1
                if indegre[n] == 0:
                    q.append(n)
        if len(ans) == numCourses:
            return ans

        return []

            
            