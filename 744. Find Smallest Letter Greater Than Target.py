class Solution(object):
    def nextGreatestLetter(self, letters, target):
        s = 0
        e = len(letters)-1
        first = letters[0]
        while s<=e:
            m = (s+e)//2
            if ord(letters[m]) == ord(target):
                s = m+1
            elif ord(letters[m]) > ord(target):
                first = letters[m]
                e = m-1
            else:
                s = m+1
        if ord(letters[e]) <= ord(target):
            return first
        return letters[s]

        