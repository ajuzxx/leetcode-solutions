class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digit = list(str(n))
        for i in range(len(digit)-2,-1,-1):
            if digit[i] < digit[i+1]:
                for j in range(len(digit)-1,i,-1):
                    if digit[i] < digit[j]:
                        digit[i],digit[j] = digit[j],digit[i]
                        break
                digit[i + 1:] = digit[i + 1:][::-1]
                res = int("".join(digit))
                return res if res <= 2**31 - 1 else -1

                        
                
        return -1
        

    
        