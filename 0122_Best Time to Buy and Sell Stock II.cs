public class Solution {
    public int MaxProfit(int[] prices) {
        int nProfit = 0;
        for( int i = 1; i < prices.Length; i++ ){
            int nDiff = prices[i] - prices[i-1];
            if( nDiff > 0 ){
                nProfit += nDiff;
            }
        }
        return nProfit;
    }
}
