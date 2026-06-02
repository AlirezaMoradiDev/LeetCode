class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        i = 0
        answer = []
        while i < len(landStartTime):
            time1 = landStartTime[i] + landDuration[i]
            j = 0
            while j < len(waterStartTime):
                if time1 < waterStartTime[j]:
                    final1 = waterStartTime[j] + waterDuration[j]
                else:
                    final1 = time1 + waterDuration[j]
                answer.append(final1)
                j += 1
            i += 1

        m = 0
        while m < len(waterStartTime):
            time2 = waterStartTime[m] + waterDuration[m]
            n = 0
            while n < len(landStartTime):
                if time2 < landStartTime[n]:
                    final2 = landStartTime[n] + landDuration[n]
                else:
                    final2 = time2 + landDuration[n]
                answer.append(final2)
                n += 1
            m += 1

        return min(answer)