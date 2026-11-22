class Solution:
    def checkString(self, s: str) -> bool:
        checker = False
        counter = 0
        while counter < len(s):
            if s[counter] == 'a' and checker == True:
                return False
            elif s[counter] == 'b':
                checker = True
            
            counter += 1

        return True