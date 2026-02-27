class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        answer = 0
        left_subarray = []
        right_subarray = []

        if len(nums) == 2:
            if (nums[0] - nums[1]) % 2 == 0:
                answer += 1 
        elif len(nums) == 3:
            if (nums[0] - sum(nums[1:])) % 2 == 0:
                answer += 1
            if (sum(nums[0:2]) - nums[2]) % 2 == 0:
                answer += 1 
        else:
            while i <= len(nums) - 2 :
                left_subarray = [nums[x] for x in range(0, i+1)]
                right_subarray = [nums[y] for y in range(i + 1, len(nums))]
                
                if (sum(left_subarray) - sum(right_subarray)) % 2 == 0:
                    answer += 1

                i += 1

        return answer 