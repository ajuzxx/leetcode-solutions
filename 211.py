class WordDictionary(object):
    class Treenode:
        def __init__(self):
            self.children = [None]*26
            self.eof = False

    def __init__(self):
        self.root = self.Treenode()
            

    def addWord(self, word):
        temp = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if temp.children[idx] is None:
                temp.children[idx] = self.Treenode()
            temp= temp.children[idx]
        temp.eof = True
        
        

    def search(self, word):
        def dfs(node,i):
            if i == len(word):
                return node.eof
            
            ch = word[i]
            if ch != '.':
                idx= ord(ch) - ord('a')
                if node.children[idx] is None :
                    return False
                return dfs(node.children[idx],i+1)
            else:
                for child in node.children:
                    if child is not None:
                        if dfs(child,i+1):
                            return True
                return False


        return dfs(self.root, 0)
                



        

        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)