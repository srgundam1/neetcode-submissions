class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of max frequency of a letter in that window
        # if length of window minus max frequency of a letter in that
        # window is <= k, valid.
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res