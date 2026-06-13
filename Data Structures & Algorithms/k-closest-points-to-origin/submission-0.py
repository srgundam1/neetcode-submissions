class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a minheap
        # don't need to take sqrt, bc values will be same order
        # heapify is O(n)
        # popping is logn (pop then rearrange)

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res



