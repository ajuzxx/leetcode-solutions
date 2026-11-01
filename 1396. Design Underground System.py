class UndergroundSystem(object):

    def __init__(self):
        self.h1= {}
        self.h2 = {}
        

    def checkIn(self, id, stationName, t):
        
        self.h1[id] = (stationName,t)
    def checkOut(self, id, stationName, t):

        es,et = self.h1[id]

        travelTime = t - et
        key = (es,stationName)
        if key not in self.h2:
            self.h2[key] = [0,0]
        self.h2[key][0]+=travelTime
        self.h2[key][1]+=1
        del self.h1[id]


        

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)
        total,count = self.h2[key]

        return float(total)/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)