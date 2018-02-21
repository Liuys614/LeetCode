public class Solution {
    public int MaxProfit(int[] prices) {
        if( prices.Length < 2 ){
            return 0;
        }
        
        int[] HoldStock = new int[ prices.Length ];
        int[] NotHoldStock = new int[ prices.Length ];
        
        HoldStock[0] = -prices[0];
        NotHoldStock[0] = 0;
        HoldStock[1] = Math.Max( HoldStock[0], - prices[ 1 ] );
        NotHoldStock[1] = Math.Max( NotHoldStock[0], HoldStock[0] + prices[1] );    // first two day can not sell stock
        
        for( int i = 2; i < prices.Length; i++ ){
            HoldStock[i] = Math.Max( HoldStock[i-1], NotHoldStock[i-2] - prices[i] );
            NotHoldStock[i] = Math.Max( NotHoldStock[i-1], HoldStock[i-1] + prices[i] );
        }
        
        return NotHoldStock[ prices.Length - 1 ];
    }
}
