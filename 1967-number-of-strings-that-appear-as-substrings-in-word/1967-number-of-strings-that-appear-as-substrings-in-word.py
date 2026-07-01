class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0
        for item in patterns:
            if item in word:
                counter += 1

        return counter