class EventManager:

    def __init__(self, events: list[list[int]]):
        self.eventtoprio = {}
        self.pq = []

        for event in events:
            id,prio = event
            self.eventtoprio[id] = prio
            heapq.heappush(self.pq,(-prio,id))
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId not in self.eventtoprio:
            return
        self.eventtoprio[eventId] = newPriority
        heapq.heappush(self.pq,(-newPriority,eventId))

        

    def pollHighest(self) -> int:
        while self.pq:
            prio,id = heapq.heappop(self.pq)
            prio = - prio

            if id not in self.eventtoprio:
                continue
            

            if self.eventtoprio[id] == prio:
                del self.eventtoprio[id]
                return id

        return -1

        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()