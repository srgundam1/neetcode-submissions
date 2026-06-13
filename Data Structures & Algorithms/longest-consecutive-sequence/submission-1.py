class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        #result = [1] * len(nums)
        seen = {} # key is num, value is longest subsequence
        for i in range(len(nums)):
            if i == 0:
                seen[nums[i]] = 1
                continue
            if (nums[i] - 1) in seen:
                seen[nums[i]] = seen.get(nums[i] - 1) + 1
            else:
                seen[nums[i]] = 1
        print(seen)
        if seen:
            return max(seen.values())
        return 0