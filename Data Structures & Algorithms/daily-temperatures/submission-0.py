class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # brute force
        res = []
        for i in range(len(temperatures)):
            found = False
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    found = True
                    break
                else:
                    j += 1
            if not found:
                res.append(0)
            
        return res
