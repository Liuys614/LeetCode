public class Solution {
    public int MaximalRectangle(char[,] matrix) {
        int nY = matrix.GetLength( 0 );
        int nX = matrix.GetLength( 1 );
        int nMaxArea = 0;
        
        int[] height = new int[nX];     // current row consist how many 1 above (include this row)
        int[] left = new int[nX];       // left closest bondary value of above rectangle which own height of height[x]
        int[] right = new int[nX];      // right closest bondary value of above rectangle which own height of height[x]

        initIntArray( ref height, 0 );
        initIntArray( ref left, 0 );
        initIntArray( ref right, nX );
        
        for( int y = 0; y < nY; y++ ){
            int cur_left = 0;               // temporary record the left bondary of contious 1's in current row
            int cur_right = nX;             // temporary record the right bondary of contious 1's in current row
            
            for( int x = 0; x < nX; x++ ){
                if( matrix[y,x] == '1' ){
                    height[x]++;
                }
                else{
                    height[x] = 0;
                }    
            }
            
            for( int x = 0; x < nX; x++ ){
                if( matrix[y,x] == '1' ){
                    left[x] = Math.Max( left[x], cur_left );
                }
                else{
                    left[x] = 0;
                    cur_left = x + 1;
                }  
            }
            
            for( int x = nX - 1; x >= 0; x-- ){
                if( matrix[y,x] == '1' ){
                    right[x] = Math.Min( right[x], cur_right );
                }
                else{
                    right[x] = nX;
                    cur_right = x;
                }  
            }
            
            for( int x = 0; x < nX; x++ ){
                nMaxArea = Math.Max( nMaxArea, ( right[x] - left[x] ) * height[x] );
            }
        }
        
        return nMaxArea;
    }
    
    void initIntArray( ref int[] Array, int nValue ){
        for( int i = 0; i < Array.Length; i++ ){
            Array[i] = nValue;
        }
    }
}
