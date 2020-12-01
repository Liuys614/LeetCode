class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        
        vector<int> nResult;
        
        // enumerate array A
        for( int i=0; i<A.size(); i++ ){
            // find index in array B
            for ( int j=0; j<B.size(); j++ ){
                if( A[i] == B[j] ){
                    nResult.push_back(j);
                    break;
                }
            }
        }
        
        return nResult;
        
    }
};
