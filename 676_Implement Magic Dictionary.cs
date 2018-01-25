public class MagicDictionary {

    /** Initialize your data structure here. */
    public MagicDictionary() {
        
    }
    
    /** Build a dictionary through a list of words */
    public void BuildDict(string[] dict) {
        m_dict = new List<string>( dict );
        foreach( string str in dict ){
            //m_dict.add( str );
            
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    public bool Search(string word) {
        foreach(string str in m_dict){
            if( word.Length != str.Length ){
                continue;
            }
            
            int nCount=0;
            for( int i=0; i<word.Length; i++ ){
                if( word[i] != str[i] ){
                    nCount++;
                }
            }
            
            if( nCount == 1 ){
                return true;
            }
        }
        
        return false;
    }
    
    List<string> m_dict = new List<string>();
    
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.BuildDict(dict);
 * bool param_2 = obj.Search(word);
 */