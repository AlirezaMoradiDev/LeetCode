class Solution:
    def minElement(self, nums: List[int]) -> int:
        counter = 0
        while counter < len(nums):
            num = str(nums[counter])
            answer = [int(i) for i in num]
            nums[counter] = sum(answer)
            counter += 1

        return(min(nums))