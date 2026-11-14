class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.TtoU = {}
        for userId,taskId,priority in tasks:
            heapq.heappush(self.pq,(-priority,-taskId,userId))
            self.TtoU[taskId]=[userId,priority]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.pq,(-priority,-taskId,userId))
        self.TtoU[taskId]=[userId,priority]

    def edit(self, taskId: int, newPriority: int) -> None:
        self.TtoU[taskId][1] = newPriority
        heapq.heappush(self.pq,(-newPriority,-taskId,self.TtoU[taskId][0]))

        

    def rmv(self, taskId: int) -> None:
        del self.TtoU[taskId]
        

    def execTop(self) -> int:
        while self.pq:
            priority,taskId,userId = heapq.heappop(self.pq)
            taskId = -taskId
            priority = -priority
            if taskId  not in self.TtoU:
                continue

            if self.TtoU[taskId][1] == priority and self.TtoU[taskId][0] == userId:
                
                del self.TtoU[taskId]
                return userId
            
        return -1

        


        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()