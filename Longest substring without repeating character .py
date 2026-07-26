class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        duplicate = False
        anslen = float('-inf')
        freq = [0]*256

        while i < len(s):
            ch = ord(s[i])

            if freq[ch] == 1:
                duplicate = True
            freq[ch]+=1
            i+=1

            while duplicate:
                ch2 = ord(s[j])
                if freq[ch2] == 2:
                    duplicate = False
                freq[ch2]-=1
                j+=1
            cur = i-j
            anslen = max(cur,anslen)
        return anslen
        





        

        