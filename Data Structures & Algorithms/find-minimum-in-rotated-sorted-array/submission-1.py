class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        # return min(nums) # O(n) time complexity

        # use binary search (middle pointer)
        # idea: a rotated array has 2 sorted halfs, left and right
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r) //2
            if nums[m] > nums[r]: # middle is in the left-sorted portion
                # so min has to be right sorted portion, lets look at right portion
                l = m + 1
            else: # middle is in left sorted portion, min can be the middle or before
                r = m
        # when l == r, that means it is the min
        return nums[l]
