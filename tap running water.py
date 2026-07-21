class Solution(object):
    def trap(self, height):
        n = len(height)
        prefix = [0]*n
        prefix[0] = height[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])
        sufix = [0]*n
        sufix[n-1]= height[n-1]
        for i in range(n-2,-1,-1):
            sufix[i] = max(sufix[i+1],height[i])
        water = 0
        for i in range(n):
            potentialwater = min(prefix[i],sufix[i])
            water+= potentialwater-height[i]
        return water

        



        