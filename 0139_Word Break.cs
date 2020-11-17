public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        bool[] dp = new bool[s.Length+1];
        // dp[i] record as true while substring s(0~i) can be compose by Dictionary
        Array.Clear( dp, 0, s.Length+1 );
        dp[0] = true;
        
        // try every length of word start from head of string s
        for( int i = 1; i < s.Length+1; i++ ){
            // try every case that cut string into 0~j and j~i
            // and judge dp[i] as cutable when dp[j] and string(j~i) both are true
            for( int j = 0; j < i; j++ ){
                string str = s.Substring( j, i - j );
                if( dp[j] && wordDict.Contains( str ) ){
                    dp[i] = true;
                    continue;
                }
            }
        }
        
        return dp[s.Length];
    }
}