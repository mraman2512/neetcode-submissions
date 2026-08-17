class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = dict()
        for each in s:
            if each not in hs:
                hs[each] = 1
            else:
                hs[each] += 1
        ht = dict()
        for each in t:
            if each not in ht:
                ht[each] = 1
            else:
                ht[each] += 1

        for key in set(s+t):
            if ht.get(key, 0) != hs.get(key, 0):
                return False
        return True 
        