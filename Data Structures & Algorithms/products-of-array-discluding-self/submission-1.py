class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive: for each element, multiply all other elements
        #result = []
        #for i in range(len(nums)):
        #    prod = 1
        #    for j in range(len(nums)):
        #        if i == j:
        #            continue
        #        else:
        #            prod *= nums[j]
        #    result.append(prod)
        #return result

        # optimal solution uses array traversal and cumulative

        #compute prefixes
        prefixes = [1] * len(nums)
        for i in range(1, len(nums), 1):
            prefixes[i] = prefixes[i-1] * nums[i-1]


        #compute suffixes
        suffixes = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]

        # multiple prefix and suffix
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefixes[i] * suffixes[i]

        return result
