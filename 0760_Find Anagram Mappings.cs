public class Solution {
    public int[] AnagramMappings(int[] A, int[] B) {
        int [] nResult = new int[ A.Length ];
        
        // enumerate array A
        for( int i=0; i<A.Length; i++ ){
            // find index in array B
            for ( int j=0; j<B.Length; j++ ){
                if( A[i] == B[j] ){
                    nResult[i] = j;
                }
            }
        }
        
        return nResult;
    }
}
