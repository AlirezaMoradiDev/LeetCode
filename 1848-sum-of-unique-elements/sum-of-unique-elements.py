class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count_dict = {}

        for num in nums:
            count_dict[num] = nums.count(num)
        answer = []    
        for key in count_dict.keys():
            if count_dict.get(key) == 1:
                answer.append(key)

        return sum(answer)