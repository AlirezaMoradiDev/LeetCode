class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0, ]
        sum = 0
        for num in gain:
            sum += num
            lst.append(sum)
        
        return max(lst)