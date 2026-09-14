class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key = lambda x:x [1])

        arrow_used = 1
        end_point = points [0] [1]

        for i in range(1, len(points)):
            if points[i] [0]> end_point:
                arrow_used+=1
                end_point = points [i] [1]
        return arrow_used
        