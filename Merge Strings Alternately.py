class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3 = []
        i = 0
        j = 0 

 
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                word3.append(word1[i])
                i += 1
            if j < len(word2):
                word3.append(word2[j])
                j += 1
        
        return "".join(word3)