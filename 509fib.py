class Solution(object):
    def fib(self, n):
        
        if n <=1:
            return n
        re1 = self.fib(n-1)
        re2 = self.fib(n-2)
        mes = re1+re2
        return mes