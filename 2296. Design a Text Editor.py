class TextEditor:

    def __init__(self):
        self.left = deque()
        self.right = deque()
        

    def addText(self, text: str) -> None:
        for ch in text:
            self.left.append(ch)
        

    def deleteText(self, k: int) -> int:
        k = min(len(self.left),k)
        for i in range(k):
            self.left.pop()
        return k
        

    def cursorLeft(self, k: int) -> str:
        k = min(len(self.left),k)
        for i in range(k):
            self.right.append(self.left.pop())
        num = min(len(self.left),10)
        result = []
        for i in range(1,num+1):
            result.append(self.left[-i])
        return "".join(result[::-1])

        
           

    def cursorRight(self, k: int) -> str:
        k = min(len(self.right),k)
        for i in range(k):
            self.left.append(self.right.pop())
        num = min(len(self.left),10)
        result = []
        for i in range(1,num+1):
            result.append(self.left[-i])
        return "".join(result[::-1])



        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)