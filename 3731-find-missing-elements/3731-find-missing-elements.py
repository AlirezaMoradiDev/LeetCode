class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s1 = set(nums)
        mx = max(nums)
        mn = min(nums)

        s2 = set([x for x in range(mn, mx + 1)])
        answer = sorted(list(s2.difference(s1)))
        return answer