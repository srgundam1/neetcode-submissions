class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # sort
        stones.sort() # O(nlogn)

        while len(stones) >= 2:
            x, y = stones[-1], stones[-2]
            if x == y:
                stones.pop()
                stones.pop()
            else:
                z = abs(x - y)
                stones.pop()
                stones.pop()
                stones.append(z)
                stones.sort()
        if stones:
            return stones[0]
        else:
            return 0
        