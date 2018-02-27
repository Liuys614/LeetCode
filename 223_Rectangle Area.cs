public class Solution {
    public int ComputeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int nRec1Area = ( C - A ) * ( D - B );
        int nRec2Area = ( G - E ) * ( H - F );

        bool NotOverlay = ( A > G ) || ( E > C ) || ( F > D ) || ( B > H );
        
        if( NotOverlay ){
            return nRec1Area + nRec2Area;
        }
        else{
            int[] xArray = { A, C, E, G };
            int[] yArray = { B, D, F, H };
            Array.Sort( xArray );
            Array.Sort( yArray );
            int nRecOverlap = ( xArray[2] - xArray[1] ) * ( yArray[2] - yArray[1] );
            
            return nRec1Area + nRec2Area - nRecOverlap;
        }
    }
}
