public class Solution {
    public bool JudgeSquareSum(int c) {
        Dictionary<long, long> dic = new Dictionary<long, long>();  // ( c - a^2 , a )
        for( long i = 0; i <= c; i++ ){
            if( i * i > c ){
                break;
            }
            
            if( 2 * i * i == c ){
                return true;
            }
            
            if( dic.ContainsKey( i * i ) ){
                return true;
            }
            
            dic.Add( c - i * i, i );
        }
        
        return false;
    }
}
