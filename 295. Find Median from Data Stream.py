class MedianFinder(object):

    def __init__(self,):
        self.lmax =[]
        self.rmin = []
        self.count = 0
    
        
        

    def addNum(self, num):
        if len(self.lmax)==0 or num< -self.lmax[0]:
            heapq.heappush(self.lmax,-num)
        else:
            heapq.heappush(self.rmin,num)

        if len(self.rmin)>len(self.lmax):
            n = heapq.heappop(self.rmin)
            heapq.heappush(self.lmax,-n)
        elif len(self.lmax)>len(self.rmin)+1:
            n = heapq.heappop(self.lmax)
            heapq.heappush(self.rmin,-n)
        self.count+=1

    def findMedian(self):
        if self.count %2==0:
            left_max = -self.lmax[0]
            right_min = self.rmin[0]
            return (left_max+right_min)/2.0
        else:
            return -self.lmax[0]



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()