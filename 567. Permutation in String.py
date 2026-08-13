class Solution(object):
    def checkInclusion(self, s1, s2):
        search ={}
        for ch in s1:
            search[ch] = search.get(ch,0)+1
        valid = {}
        left = 0
        for right in range(len(s2)):
            ch = s2[right]
 
            valid[ch]= valid.get(ch,0)+1
            

            if right -left +1 > len(s1):
                remove= s2[left]
                left +=1
                valid[remove] -=1

                if valid[remove] == 0:
                    del valid[remove]
            if valid == search:
                return True
        return False

        




