class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = []
        temp = []
        for num in nums:
            if len(answer) == 0:
                if num > 0:
                    answer.append(num)
                    if len(temp) >= 0:
                        for data in temp:
                            if data < 0:
                                answer.append(data)
                                temp.remove(data)
                                break
                else:
                    temp.append(num)
            else:
                if num > 0:
                    if answer[len(answer) - 1] < 0:
                        answer.append(num)
                        for data in temp:
                            if data < 0:
                                answer.append(data)
                                temp.remove(data)
                                break
                    else:
                        temp.append(num)
                else:
                    if answer[len(answer) - 1] > 0:
                        answer.append(num)
                        for data in temp:
                            if data > 0:
                                answer.append(data)
                                temp.remove(data)
                                break
                    else:
                        temp.append(num)
        return answer