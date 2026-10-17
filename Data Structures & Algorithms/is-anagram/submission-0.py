class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        schars = {}
        tchars = {}
        for ch in s:
            schars[ch] = schars.get(ch, 0) + 1
        for ch in t:
            tchars[ch] = tchars.get(ch, 0) + 1

        return schars == tchars
