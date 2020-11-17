public class Solution {
    // wrong anser
    /*
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> ansList = new List<IList<int>>();
        for( int i = 0; i < nums.Length; i++ ){
            for( int j = i + 1; j < nums.Length; j++ ){
                for( int k = j + 1; k < nums.Length; k++ ){
                    if( nums[i] + nums[j] + nums[k] == 0){
                        List<int> ans = new List<int>();
                        ans.Add( nums[i] );
                        ans.Add( nums[j] );
                        ans.Add( nums[k] );
                        ans.Sort();
                        ansList.Add( ans );
                    }
                }
            }
        }
        return ansList;
    }
    */
    
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> ansList = new List<IList<int>>();
        Array.Sort( nums );
        for( int num1 = 0; num1 < nums.Length - 2; num1++ ){
            int num2 = num1 + 1;
            int num3 = nums.Length - 1;
            
            // num1 is smallest number should not be postive integer
            if( nums[num1] > 0 ){
                continue;
            }
            
            // num1 run once each unique number
            if( num1 != 0 && nums[num1] == nums[num1 - 1] ){
                continue;
            }
            
            // fix num1 find all case of num2 and num3 pair
            while( num2 < num3 ){
                int nSum = nums[num1] + nums[num2] + nums[num3];
                if( nSum == 0 ){
                    List<int> ans = new List<int>();
                    ans.Add( nums[num1] );
                    ans.Add( nums[num2] );
                    ans.Add( nums[num3] );
                    ansList.Add( ans );
                    
                    // move to next different value index
                    while( num2 < num3 && nums[ num2 ] == nums[ num2 + 1 ] ){
                        num2++;
                    }
                    num2++;

                    // move to previous different value index
                    while( num2 < num3 && nums[ num3 ] == nums[ num3 - 1 ] ){
                        num3--;
                    }
                    num3--;
                    continue;
                }
                
                if( nSum < 0 ){
                    // move to next different value index
                    while( num2 < num3 && nums[ num2 ] == nums[ num2 + 1 ] ){
                        num2++;
                    }
                    num2++;
                    continue;
                }
                
                if( nSum > 0 ){
                    // move to previous different value index
                    while( num2 < num3 && nums[ num3 ] == nums[ num3 - 1 ] ){
                        num3--;
                    }
                    num3--;
                    continue;
                }
            }
        }
        
        return ansList;
    }
}
