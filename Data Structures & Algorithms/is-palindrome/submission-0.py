class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join([char for char in s if char.isalnum()])
        first = 0
        last = len(clean) - 1

        while first <= last:
            if clean[first].lower() == clean[last].lower():
                first += 1
                last -= 1
            else:
                return False
        return True