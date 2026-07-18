import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = [((2*x) + 1) for x in range(0, n)]
        even = [2*x for x in range(1, n + 1)]
        sumOdd = sum(odd)
        sumEven = sum(even)
        return math.gcd(sumOdd, sumEven)