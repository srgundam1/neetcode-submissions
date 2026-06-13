class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap
        # if in hashmap, return true
        # if not, add to hashmap
        num_set = set()
        for i in nums:
            if (i in num_set):
                return True
            else:
                num_set.add(i)
        return False