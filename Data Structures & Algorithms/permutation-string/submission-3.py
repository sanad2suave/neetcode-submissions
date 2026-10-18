class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        k = len(s1)
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1           
            if r >= k:
                window[ord(s2[r - k]) - ord('a')] -= 1   
            if window == need:
                return True
        return False

        
        
            
        