class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        x = 2
        while x < len(nums):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[x])
            else:
                arr2.append(nums[x])

            x += 1

        return arr1+arr2
        