class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            
            # 1. Current interval is completely before newInterval
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])

            # 2. Current interval is completely after newInterval
            elif intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            # 3. Current interval overlaps with newInterval
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)
        return result
        