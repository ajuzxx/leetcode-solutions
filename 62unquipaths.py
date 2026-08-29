class Solution(object):
    def noofwayhelper(self,sr,sc,dr,dc):
        if sr>dr or sc > dc:
            return 0 

        if sr == dr and sc == dc:
            return 1

        ra1 = self.noofwayhelper(sr+1,sc,dr,dc)
        ra2 = self.noofwayhelper(sr,sc + 1,dr,dc)
        masn =ra1+ra2
        return masn 
    def uniquePaths(self, m, n):
        return self.noofwayhelper(0,0,m-1,n-1) 

        
        
        