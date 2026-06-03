class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        if len(arr) < 3:
            return True
        else:
            constant = arr[1] -arr[0]
            i = 1
            j = 2
            while j < len(arr):
                if arr[j] - arr[i] == constant:
                    i += 1
                    j += 1
                    continue
                else:
                    return False
            return True
