class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        for ch in s:
            if ch.isalnum():

                count[ch] = count.get(ch,0)+1
        count1 = {}
        for ch in t:
            if ch.isalnum():
                count1[ch] = count1.get(ch,0)+1

        return count1==count