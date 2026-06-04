class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        answer = 0
        for number in range(num1, num2 + 1):
            number = str(number)
            i = 0
            while True:
                if i+2 >= len(number):
                    break
                n = number[(i):(i+2)+1]
                checker = int(n[1])
                if (checker > int(n[0]) and checker > int(n[2])) or (checker < int(n[0]) and checker < int(n[2])):
                    answer += 1
                i += 1
        
        return answer