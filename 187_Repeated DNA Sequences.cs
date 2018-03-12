public class Solution {
    public IList<string> FindRepeatedDnaSequences(string s) {
        TrieNode root = new TrieNode();
        TrieNode[] ptrList = new TrieNode[10];
        int[] LengthCnt = new int[10];
        IList<string> output = new List<string>();
        
        for( int i = 0 ; i < 10; i++ ){
            LengthCnt[i] = -i;
            ptrList[i] = root;
        }

        foreach( char c in s )
        {
            int ID = -1;
            if( c == 'A' ) ID = 0;
            else if( c == 'C' ) ID = 1;
            else if( c == 'G' ) ID = 2;
            else if( c == 'T' ) ID = 3;
            
            for( int i = 0; i < 10; i++ )
            {
                if( LengthCnt[i] < 0 ){
                    LengthCnt[i]++;
                    continue;
                }
                
                if( LengthCnt[i] == 9 ){
                    if( ptrList[i].next[ID] != null ){
                        if( output.Contains( ptrList[i].next[ID].word ) == false ){
                            output.Add( ptrList[i].next[ID].word );
                        }
                    }
                }
                
                if( ptrList[i].next[ID] == null ){
                    ptrList[i].next[ID] = new TrieNode();
                    ptrList[i].next[ID].word = ptrList[i].word + c;
                }
                
                ptrList[i] = ptrList[i].next[ID];
                LengthCnt[i]++;
                
                if( LengthCnt[i] == 10 ){
                    LengthCnt[i] = 0;
                    ptrList[i] = root;
                }
            }        
        }
        
        return output;
    }
    
    public class TrieNode{
        public string word;
        public TrieNode[] next = new TrieNode[4];
    }
}
