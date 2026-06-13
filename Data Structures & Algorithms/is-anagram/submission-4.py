class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict, key is char, value is # of times seen
        # reduce value for every char in str t
        # if all values in dict are 0, return true
        seen = {}
        for i in s:
            if i in seen:
                seen[i] = seen.get(i) + 1
            else:
                seen[i] = 1
        for j in t:
            if j in seen:
                seen[j] = seen.get(j) - 1
            else:
                return False
        for k in seen:
            if seen[k] !=0:
                return False
        return True
        