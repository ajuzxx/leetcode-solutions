class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1

        while left< right:
            su = numbers[left]+numbers[right]
            if su < target:
                left+=1
            elif su> target:
                right -= 1
            elif target == su:
                return[left+1,right+1]