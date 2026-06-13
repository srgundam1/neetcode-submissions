class Solution{
    public boolean hasDuplicate(int[] nums){
        for (int i = 0; i < nums.length; i += 1){
            for (int j = i+1; j < nums.length; j += 1){
                if (nums[i] == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}