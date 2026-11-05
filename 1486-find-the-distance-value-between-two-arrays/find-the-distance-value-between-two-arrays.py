class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        answer = 0

        for num in arr1:
            i = bisect_left(arr2, num)

            left = i - 1
            right = i

            if left >= 0 and abs(num - arr2[left]) <= d:
                continue

            if right < len(arr2) and abs(num - arr2[right]) <= d:
                continue

            answer += 1

        return answer