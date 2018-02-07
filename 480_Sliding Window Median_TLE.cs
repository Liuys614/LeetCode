public class Solution {
    public double[] MedianSlidingWindow(int[] nums, int k) {
        double[] output = new double[nums.Length - k + 1];

        // loop each window
        for( int i=0; i< nums.Length - k + 1 ; i++){
            int[] window = new int[k];
            Array.Copy(nums, i, window, 0, k );
            Array.Sort(window);
            
            // get median value
            // even case
            if( k % 2 == 0 ){
                output[i] = ( (double)window[ k/2 ] + (double)window[ k/2 - 1 ] )/2.0;
            }
            // odd case
            else{
                output[i] = window[k/2];
            }
        }
        
        return output;
    }
}