class Solution(object):
    def findAnagrams(self, s, p):
        
        result = []
        collection = {}
        check = {}

        for ch in p:
            collection[ch] = collection.get(ch, 0) + 1

        left = 0

        for right in range(len(s)):
            check[s[right]] = check.get(s[right], 0) + 1


            if right - left + 1 > len(p):
                check[s[left]] -= 1
                if check[s[left]] == 0:
                    del check[s[left]]
                left += 1

            if right - left + 1 == len(p):
                if check == collection:
                    result.append(left)

        return result