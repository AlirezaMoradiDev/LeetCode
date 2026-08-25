class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        c = 1
        while True:
            if k * c in nums:
                c += 1
            else:
                return k * c