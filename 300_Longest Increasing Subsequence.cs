// Solution 1
public class Solution {
    public int LengthOfLIS(int[] nums) {
        if( nums.Length == 0 ){
            return 0;
        }
        
        int[] dp = Enumerable.Repeat( 1, nums.Length ).ToArray();
        int maxLength = 1;
        
        for( int i = 1; i < nums.Length; i++ ){
            for( int j = 0; j < i; j++ ){
                if( nums[i] > nums[j] ){
                    dp[i] = Math.Max( dp[i], dp[j] + 1 );
                    maxLength = Math.Max( maxLength, dp[i] );
                }
            }
        }
        
        return maxLength;
    }
}

// Solution 2
public class Solution {
    public int LengthOfLIS(int[] nums) 
    {
        if(nums == null || nums.Count() == 0){
            return 0;
        }
        
        List<int> dp = new List<int>();
        
        foreach( int num in nums ){
            if( dp.Count == 0 || dp[dp.Count()-1] < num ){
                dp.Add( num );
            }
            else{
                int index = dp.BinarySearch( num );
                // Not found case, BinarySearch funciton will return the insert index(in Complement format)
                if( index < 0 ){
                    index = ~index;
                }
                // Keep numbers of List as smaller as possiable
                dp[index] = num;
            }
        }
        
        return dp.Count();
    }
}



