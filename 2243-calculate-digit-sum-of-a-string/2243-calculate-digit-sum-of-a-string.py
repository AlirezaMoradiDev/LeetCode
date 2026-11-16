class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            answer = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = sum(map(int, group))
                answer += str(total)

            s = answer

        return s