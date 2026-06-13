class Solution {
    public int missingNumber(int[] nums) {
        // the missing number is not in it's index
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.length;
    }
}
