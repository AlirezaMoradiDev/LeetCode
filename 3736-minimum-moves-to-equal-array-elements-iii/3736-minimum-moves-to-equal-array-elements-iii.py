class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        s = 0
        for data in nums:
            s += mx - data

        return s 