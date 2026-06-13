class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # maintain dict of num and index
       seen = {} # key -> num, val -> index

       for i,num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i