from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)
        for ch in strs:
            sorted_key = "".join(sorted(ch))

            anagram_groups[sorted_key].append(ch)
        return list(anagram_groups.values())
        

        