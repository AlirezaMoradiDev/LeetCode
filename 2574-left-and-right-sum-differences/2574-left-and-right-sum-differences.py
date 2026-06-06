class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        rightSum = [0]
        i = 0
        while i < len(nums) - 1:
            leftSum.append(leftSum[len(leftSum) - 1] + nums[i])
            i += 1

        j = len(nums) - 1
        while j > 0:
            rightSum.append(rightSum[len(rightSum) - 1] + nums[j])
            j -= 1

        rightSum.reverse()

        answer = []
        k = 0
        while k < len(leftSum):
            answer.append(abs(leftSum[k] - rightSum[k]))
            k += 1

        return answer