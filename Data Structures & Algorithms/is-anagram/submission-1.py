class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first = {}
        second = {}
        for ch in s:
            first[ch] = first.get(ch, 0) + 1
        
        for ch in t:
            second[ch] = second.get(ch, 0) + 1
        
        return first == second