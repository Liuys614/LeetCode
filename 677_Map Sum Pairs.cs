public class MapSum {

    /** Initialize your data structure here. */
    public MapSum() {
        m_Data = new Dictionary< string, int >();
    }
    
    public void Insert(string key, int val) {
        if( m_Data.ContainsKey( key ) ){
            m_Data.Remove( key );
        }
        m_Data.Add( key, val );
    }
    
    public int Sum(string prefix) {
        int nSum = 0;
        foreach( KeyValuePair< string, int > kvp in m_Data ){
            if( kvp.Key.StartsWith( prefix ) ){
                nSum += kvp.Value;
            }
        }
        return nSum;
    }
    
    Dictionary < string, int > m_Data;
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.Insert(key,val);
 * int param_2 = obj.Sum(prefix);
 */