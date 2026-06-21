class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        answer = 0
        counter = len(s) - 1
        while s[counter] != ' ' and counter >= 0:
            answer += 1
            counter -= 1


        return answer

        