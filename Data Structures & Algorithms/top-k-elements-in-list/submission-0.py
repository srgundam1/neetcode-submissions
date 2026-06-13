class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # intial solution
        # use a dict to store int and frequency
        # use a max heap and then pop the first k elements
        # popping takes k*logn

        # O(n) solution (linear time), uses dict bucket sort idea

        count = {} # dict for int and frequency
        freq = [[] for i in range(len(nums) + 1)] # index = frequency, value is a list of ints that have that frequency
        # max frequency is the length of nums

        for n in nums:
            count[n] = 1 + count.get(n, 0) # increase count for each int
        for n, c in count.items():
            freq[c].append(n) # n occurs c times  

        res = []

        # start from descending frequency, and print out top k numbers

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
