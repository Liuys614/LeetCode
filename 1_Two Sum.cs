public class Solution {
    // solution 1
    /*
    public int[] TwoSum(int[] nums, int target) {
        int[] ans = new int[2];
        for( int i = 0; i < nums.Length; i++ ){
            for( int j = i + 1; j < nums.Length; j++ ){
                if( nums[i] + nums[j] == target ){
                    ans[1] = j;
                    break;
                }
            }
        }
        return ans;
    }
    */
    
    // solution 2
    public int[] TwoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Dictionary<int,int> dic = new Dictionary<int,int>();
        for( int i = 0; i < nums.Length; i++ ){
            if( dic.ContainsKey( nums[i] )){
                ans[0] = dic[nums[i]];
                ans[1] = i;
            }
            if( dic.ContainsKey( target - nums[i] )){
                continue;
            }
            dic.Add( target - nums[i], i );
        }
        return ans;
    }
}
