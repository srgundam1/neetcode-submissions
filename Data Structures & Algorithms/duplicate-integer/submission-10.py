class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap
        # if in hashmap, return true
        # if not, add to hashmap
        num_set = set()
        for i in nums: # O(n) where n is length of nums
            if (i in num_set): # O(1)
                return True
            else:
                num_set.add(i)
        return False

        # Time Complexity: O(n)
        # Space Complexity: O(n)