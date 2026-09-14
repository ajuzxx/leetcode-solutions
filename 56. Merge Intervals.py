class Solution(object):
    def merge(self, intervals):
        ans = []
        intervals.sort(key = lambda x:x[0])
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if ans[-1][1]>=intervals[i][0]:
                if ans[-1][1]<intervals[i][1]:
                    ans[-1][1]=intervals[i][1]
                
            else:
                ans.append(intervals[i])
        return ans

        