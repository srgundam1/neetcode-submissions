class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapify doesnt have maxheap, only minheap
        # can enforce maxheap by turning each in neg value, then take abs() value
        stones = [-s for s in stones] # turn weights into negative
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second  == first:
                continue
            else:
                new = first - second
                heapq.heappush(stones, new)
        stones.append(0)
        return abs(stones[0])
        # if stones:
        #     return abs(heapq.heappop(stones))
        # else:
        #     return 0




        # sort
        # stones.sort() # O(nlogn)

        # while len(stones) >= 2:
        #     x, y = stones[-1], stones[-2]
        #     if x == y:
        #         stones.pop()
        #         stones.pop()
        #     else:
        #         z = abs(x - y)
        #         stones.pop()
        #         stones.pop()
        #         stones.append(z)
        #        stones.sort()
        # if stones:
        #     return stones[0]
        # else:
        #     return 0
        