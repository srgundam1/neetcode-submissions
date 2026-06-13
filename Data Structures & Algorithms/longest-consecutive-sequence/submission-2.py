class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort() # O(nlogn)

        seen = {}
        
        for i in range(len(nums)):
            if i == 0:
                seen[nums[i]] = 1
                continue
            if (nums[i] -1) in seen:
                seen[nums[i]] = seen.get(nums[i] - 1) + 1
            else:
                seen[nums[i]] = 1
        if seen:
                return max(seen.values())
        return 0


        