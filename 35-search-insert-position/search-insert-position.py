class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if len(nums) == 1:
                if target < nums[0]:
                    return 0
                else: 
                    return 1
            else:
                for i in nums:
                    index = nums.index(i)
                    gre = index + 1
                    les = index - 1
                
                    if target > i  and gre >= len(nums):
                        return len(nums)
                    elif target > i and target < nums[gre]:
                        return gre
                    elif target < i and les <= 0:
                        return 0
