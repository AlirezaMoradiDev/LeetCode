class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        lst = list(str(n))
        for digit in lst:
            if int(digit) != 0:
                x += digit
            
        if x != '': 
            new_lst = [int(i) for i in x]
            answer = int(x) * sum(new_lst)
            return answer
        
        return 0
        
