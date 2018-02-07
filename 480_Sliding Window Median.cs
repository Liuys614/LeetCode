public class Solution {
    public double[] MedianSlidingWindow(int[] nums, int k) {
        List<int> window;
        double[] output = new double[nums.Length - k + 1];
        bool windowIsEven = ( k % 2 == 0 );

        // Init first window
        int[] tmp = new int[k];
        Array.Copy(nums, 0, tmp, 0, k );
        window = new List<int>(tmp);
        window.Sort();
        
        // loop each window
        for( int i = 0; i <= nums.Length - k ; i++){
            // get median value
            output[i] = windowIsEven ? ( (double)window[k/2]+(double)window[k/2-1] )/2.0 : window[k/2];
            
            // fininsh window move
            if( ( i + k ) >= nums.Length ){
                break;
            } 
            
            // adjust window
            int nIndex = window.BinarySearch( nums[i+k] );
            if( nIndex < 0 ){
                nIndex = ~nIndex;
            }
            window.Insert( nIndex, nums[i+k] );
            window.Remove( nums[i] );
        }
        
        return output;
    }
}