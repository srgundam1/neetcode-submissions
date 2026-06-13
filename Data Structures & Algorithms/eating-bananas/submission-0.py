class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # O(n) where n = # of elements in array
        result = r
        while l <= r :
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m) # rounds up

            if hours <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1
        return result


        