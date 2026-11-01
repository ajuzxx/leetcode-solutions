class BrowserHistory(object):

    def __init__(self, homepage):
        self.leftstack = []
        self.rightstack = []
        self.leftstack.append(homepage)
        
    def visit(self, url):
        self.leftstack.append(url)
        self.rightstack = []
        

    def back(self, steps):
        possible = min(steps,len(self.leftstack)-1)
        for i in range(possible):
            current = self.leftstack.pop()
            self.rightstack.append(current)
        return self.leftstack[-1]
        
        

    def forward(self, steps):
        possible = min(steps,len(self.rightstack))
        for i in range(possible):
            current = self.rightstack.pop()
            self.leftstack.append(current)
        return self.leftstack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)