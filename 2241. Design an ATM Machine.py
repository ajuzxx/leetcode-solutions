class ATM:

    def __init__(self):
        self.money = [0]*5
        self.coin = [20,50,100,200,500]
        

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(5):
            self.money[i] +=banknotesCount[i]
        

    def withdraw(self, amount: int) -> list[int]:
        result = [0]*5

        for i in range(4,-1,-1):
            used = min(self.money[i],amount//self.coin[i])
            result[i] = used
            amount -= (used*self.coin[i])

        if amount != 0:
            return [-1]
        for i in range(5):
            self.money[i] -=result[i]
        return result

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)