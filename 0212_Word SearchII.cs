public class Solution {
    public IList<string> FindWords(char[,] board, string[] words) {
        List<string> outputList = new List<string>();
        TrieNode root = BuildTrieNode(words);
        
        for( int j = 0; j < board.GetLength(0); j++ ){
            for( int i = 0; i < board.GetLength(1); i++ ){
                dfs( board, new Point( i, j ), root, outputList );
            }
        }

        outputList.Sort();
        return outputList;
    }

    public void dfs( char[,] board, Point CurPos, TrieNode t, List<string> words)
    {
        if( CurPos.x < 0 || CurPos.x >= board.GetLength(1) || CurPos.y < 0 || CurPos.y >= board.GetLength(0) ) return;

        char c = board[ CurPos.y, CurPos.x ];
        
        if( c == '-' || t.next[c - 'a'] == null ) return;
        
        t = t.next[ c - 'a' ];
        // found one
        if ( t.word != null ) {
            words.Add( t.word );
            t.word = null;          // avoid find twice
        }
        
        // Mark current position is travered
        board[CurPos.y, CurPos.x] = '-';

        // Check adjacent letter is next letter or not
        dfs( board, new Point( CurPos.x, CurPos.y - 1 ), t, words );
        dfs( board, new Point( CurPos.x - 1, CurPos.y ), t, words );
        dfs( board, new Point( CurPos.x + 1, CurPos.y ), t, words );
        dfs( board, new Point( CurPos.x, CurPos.y + 1 ), t, words );
        board[CurPos.y, CurPos.x] = c;
    }
    
    public TrieNode BuildTrieNode( string[] wrods ){
        TrieNode root = new TrieNode();
        foreach( string word in wrods ){
            TrieNode p = root;
            foreach( char letter in word.ToCharArray() ){
                int n = letter - 'a';
                if( p.next[n] == null ){
                    p.next[n] = new TrieNode();
                }
                p = p.next[n];
            }
            p.word = word;
        }
        return root;
    }    
    
    public class TrieNode {
        public TrieNode[] next = new TrieNode[26];
        public string word = null;
    }
}
