class Bank(object):

    def __init__(self, balance):
        self.balance = {}
        for i in range(len(balance)):
            self.balance[i+1] = balance[i]
        

    def transfer(self, account1, account2, money):
        if account1 not in self.balance or account2 not in self.balance:
            return False
        if self.balance[account1] - money >=0:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        
        return False


    def deposit(self, account, money):
        if account not in self.balance :
            return False
        self.balance[account]+=money
        return True
        

    def withdraw(self, account, money):
        if account not in self.balance :
            return False
        if self.balance[account] - money >=0:
            self.balance[account] -= money
            return True
        return False
        
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)