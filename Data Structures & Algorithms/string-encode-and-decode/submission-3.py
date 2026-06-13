class Solution:

    # Initial idea: Concatenate all strings with a special character in between
        # Problem: the special char could initially be in the word



    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1: j+1 +length])
            i = j + 1 + length
        return result       



        #O(m) time for each and O(m+n) space
        # m sum of length of strings and n is # of strings
