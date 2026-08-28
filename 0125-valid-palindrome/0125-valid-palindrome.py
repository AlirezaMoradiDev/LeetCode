class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalpha() and not char.isdigit():
                s = s.replace(char, '')
        s = s.lower()

        if len(s) == 1:
            return True
        if s == s[::-1]:
            return True
        return False