public class Solution {
    public int FindSubstringInWraproundString(string p) {
        for( int i=0 ;i< p.Length; i++ ){
            for(int l =1 ; l <= p.Length-i;l++){
                string szSubstr = p.Substring(i,l);
                
                if( m_StringList.Contains(szSubstr) ){
                    continue;
                }
                
                if( isWhatWeWant(szSubstr) ){
                    m_StringList.Add(szSubstr);
                }
                
            } 
        }
        return m_StringList.Count;
    }
    
    
    bool isWhatWeWant(string szInput ){
        for(int i=0;i<szInput.Length-1;i++){
            char curChar = Convert.ToChar(szInput[i]);
            char nextChar = Convert.ToChar(szInput[i+1]);
            
            if( curChar == 'z'){
                if( nextChar != 'a'){
                    return false;
                }
                continue;
            }
            
            if( nextChar - curChar != 1  ){
                return false;
            }
        }
        
        return true;
    }
    
    List<string> m_StringList = new List<string>();
}

// Time Limit Exceeded
