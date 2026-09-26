from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegre = [0]*numCourses
        for s,e in prerequisites:
            graph[e].append(s)
            indegre[s]+=1
        q = deque()
        for i in range(numCourses):
            if indegre[i]==0:
                q.append(i)
        count = 0

        while q:
            fn = q.popleft()
            count+=1

            for n in graph[fn]:
                indegre[n]-=1
                if indegre[n] == 0:
                    q.append(n)
        return count == numCourses

        