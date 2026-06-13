class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search = cutting into half repeatedly

        high = len(nums) - 1
        low = 0

        while (low <= high):
            middle= (high + low) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                high = middle - 1
            else: # target > nums[middle]
                low = middle + 1
        return -1

        
