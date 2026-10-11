class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        indx = 0
        while indx < len(nums):
            if len(nums) % (indx + 1) == 0:
                answer += nums[indx] ** 2
            indx += 1 

        return answer