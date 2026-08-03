class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checker1 = True
        checker2 = True
        d1 = {}
        for char in t:
            d1[char] = t.count(char)
            if char not in s:
                checker1 = False

        for char2 in s: 
            try:
                if s.count(char2) != d1[char2]:
                    return False
            except: 
                return False

            else:
                if char2 not in t:
                    checker2 = False
        
        
        return checker1 and checker2
