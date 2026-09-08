class Solution(object):
    class TrieNode:
        def __init__(self):
                self.childern = [None]*26
                self.suggestion = []
    def suggestedProducts(self, products, searchWord):
        root = self.TrieNode()
        products.sort()

        for product in products:
            node = root

            for ch in product:
                index = ord(ch) - ord('a')

                if node.childern[index] is None:
                    node.childern[index] = self.TrieNode()
                node = node.childern[index]
                if len(node.suggestion)<3:
                    node.suggestion.append(product)
        node = root
        result = []

        for ch in searchWord:

            if node is None:
                result.append([])
                continue

            index = ord(ch) - ord('a')

            if node.childern[index] is None:
                result.append([])
                node = None
            else:
                node = node.childern[index]
                result.append(node.suggestion)
        return result