class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        answer = []
        cost.sort(reverse=True)
        while True:
            if len(cost) <= 2:
                for i in cost:
                    answer.append(i)
                return sum(answer)
                # return sum(cost)
                break
            else:
                tup = cost[0], cost[1]
                if min(tup) >= cost[2]:
                    answer.append(cost[0])
                    answer.append(cost[1])
                    cost.remove(answer[len(answer) - 2])
                    cost.remove(answer[len(answer) - 1])
                    cost.pop(0)
                else:
                    break

        if len(answer) != 0:
            return sum(answer)
