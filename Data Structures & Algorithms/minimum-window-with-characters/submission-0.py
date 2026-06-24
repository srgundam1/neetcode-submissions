class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # window minimum size would be len of t

        if t == "":
            return ""

        countT = {} # map for how many times each letter in str t appears
        window = {} # map for how many times the needed letters appear in the current window

        for c in t: # traverse t
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT) # gives count of unique letters in str t
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)): # because we need index of r
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # does count satisfy count of t
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
