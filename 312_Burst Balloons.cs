public class Solution {
    public int MaxCoins(int[] nums) {
        int nMaxValue = 0;
        int[] newNums = new int[ nums.Count() + 2 ];
        int n = 1;  // ballons without 0, and plus 2 ballons with value 1 in head and tail
        
        // Create new array without 0 and concact 1 on head,tail of array.
        foreach( int Value in nums ){
            if( Value > 0 ){
                newNums[ n++ ] = Value;
            }
        }
        newNums[0] = 1;
        newNums[n++] = 1;
        
        // data[left,right] => all coins after bursted all ballon between left and right.
        // (left and rigth ballon would not be bursted)
        int[,] data = new int[n,n];

        return recursive( data, newNums, 0, n-1 );
    }

    int recursive( int[,] data, int[] nums, int left, int right ){
        int nMaxValue = 0;
        
        // optimal performance avoiding druplicate calculate
        if( data[left,right] != 0 ){
            return data[left,right];
        }
        
        // iterator all case of i-th ballon is the last busted case
        for( int i = left + 1; i < right; i++ ){
            nMaxValue = Math.Max( nMaxValue, 
                                 recursive( data, nums, left, i ) + 
                                 nums[left] * nums[i] * nums[right] + 
                                 recursive( data, nums, i, right ) );
        }
        
        data[left,right] = nMaxValue;
        return data[left,right];
    }
}
