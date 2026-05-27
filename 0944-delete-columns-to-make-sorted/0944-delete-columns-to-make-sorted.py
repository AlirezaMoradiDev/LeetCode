class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs[0]) == 1:
            x = 0
            while x < len(strs) - 1:
                if strs[x] <= strs[x + 1]:
                    x += 1
                    continue
                else:
                    return 1
            return 0
        new_strs = []
        o = 0
        while o < len(strs[0]):    
            answer = ''
            for i in strs:
                answer += i[o]
            else:
                new_strs.append(answer)
                o += 1 
        
        ret = 0

        x = 0
        while x < len(new_strs):
            y = 0
            answer = 0
            while y < len(new_strs[x]) - 1:
                if new_strs[x][y] <= new_strs[x][y + 1]:
                    answer += 1
                    y += 1
                else:
                    y += 1
            if answer < len(new_strs[x]) - 1:
                ret += 1 
            x += 1
        
        return ret